import os
import hashlib
import threading

from shared import Config, generic
from domain.xml_models import PayrollXml
from domain.dtos import PayrollDto
from shared.certificate import CertificateLoader
from ..sign_docs.xml_signerv3 import XmlSignerV3
from ..soap.soap_payroll import SoapPayrollRequest, SoapPayrollTestRequest, SoapStatusZipRequest
from ..document.record_document_case import DocumentRecorder
from domain.entities.document import TIPO_NOMINA

_config = Config()

class CreatePayrollCase:
    """
    Caso de uso para la creación y envío de un Documento Soporte de Pago de
    Nómina Electrónica (NominaIndividual, TipoXML 102).

    CreatePayrollAdjustmentCase hereda de esta clase; los puntos que cambian
    entre nómina y nota de ajuste están en los atributos de clase de abajo.
    """

    XML_CLASS = PayrollXml
    DOCUMENT_TYPE = 'NI'
    FILE_PREFIX = 'nie'
    # Tipo con el que se registra el envío en la tabla `document`.
    DOCUMENT_RECORD_TYPE = TIPO_NOMINA

    def __init__(
        self,
        payroll: PayrollDto,
        certificate_loader: CertificateLoader
    ):
        """
        :param payroll: :class:`PayrollDto`
        :param certificate_loader: :class:`CertificateLoader`
        """
        self._certificate_loader = certificate_loader

        # Carga del certificado, por NIT del empleador
        self._certificate_loader.load(payroll.Empleador.NIT)
        self._security = self._certificate_loader.security

        self.payroll = payroll
        self.xml = self.XML_CLASS()

        year = payroll.InformacionGeneral.FechaGen.split('-')[0]
        consecutivo = int(payroll.NumeroSecuenciaXML.Consecutivo)
        self.xml_name, self.zip_name = generic.get_payroll_file_names(
            payroll.Empleador.NIT, year, consecutivo, prefix=self.FILE_PREFIX
        )

        self._software_sc = self._get_software_sc()
        self._cune = self._get_cune()

        self.zip_full_path = os.path.join(
            _config.PATH_BASE, payroll.Empleador.NIT, 'XMLNomina', self.zip_name
        )

    def _get_software_sc(self) -> str:
        raw = (
            self.payroll.ProveedorXML.SoftwareID +
            self.payroll.Pin +
            self.payroll.NumeroSecuenciaXML.Numero
        )
        return hashlib.sha384(raw.encode('utf-8')).hexdigest()

    def _get_cune(self) -> str:
        p = self.payroll
        values = {
            "NumNE": p.NumeroSecuenciaXML.Numero,
            "FecNE": p.InformacionGeneral.FechaGen,
            "HorNE": p.InformacionGeneral.HoraGen,
            "ValDev": p.DevengadosTotal,
            "ValDed": p.DeduccionesTotal,
            "ValTolNE": p.ComprobanteTotal,
            "NitNE": p.Empleador.NIT,
            "DocEmp": p.Trabajador.NumeroDocumento,
            "TipoXML": self.XML_CLASS.TIPO_XML,
            "SoftwarePin": p.Pin,
            "TipAmb": p.InformacionGeneral.Ambiente,
        }
        return generic.get_cune(values)

    @property
    def cune(self):
        return self._cune

    def start(self):
        self.xml.build(self.payroll, self._cune, self._software_sc)

        # Firmar Nómina
        signer = XmlSignerV3(self.xml.get_root, self.payroll, self.DOCUMENT_TYPE, self._security)
        signed_payroll = signer.sign()

        # Comprimir Nómina
        zip_payroll = generic.zip_document(signed_payroll, self.xml_name)

        # Guardar .zip en un segundo plano
        args = (zip_payroll, self.zip_full_path)
        thread = threading.Thread(target=generic.write_file_from_base64, args=args)
        thread.start()

        # Si viene TestID se envía al SET DE PRUEBAS (habilitación) vía
        # SendTestSetAsync; si no, va a producción vía SendNominaSync.
        if self.payroll.TestID:
            return self._send_test_set(zip_payroll)

        return self._send_production(zip_payroll)

    def _recorder(self) -> DocumentRecorder:
        """Recorder para dejar traza del envío en la tabla `document`."""
        return DocumentRecorder(
            tipo=self.DOCUMENT_RECORD_TYPE,
            numero=self.payroll.NumeroSecuenciaXML.Numero,
            cliente_nit=self.payroll.Empleador.NIT,
            # La nómina se identifica por NIT, no por resolución.
            resolucion=None,
            identificador=self._cune,
            ambiente=self.payroll.InformacionGeneral.Ambiente,
            zip_path=self.zip_full_path,
        )

    def _send_production(self, zip_payroll):
        recorder = self._recorder()

        try:
            response = SoapPayrollRequest(self._security).send_xml(zip_payroll)
            is_valid, messages = generic.extract_errors_invoice(response.text)
            recorder.finish(is_valid, messages, response.text)

            if is_valid == 'false':
                print(f"Error al enviar la nómina. XML enviado: {self.xml_name}")
                print(f"Error al enviar la nómina. Respuesta XML: {response.text}")
                raise Exception(messages)

        except Exception as e:
            recorder.fail(str(e))
            print(f"Error al enviar la nómina. XML enviado: {self.xml_name}")
            print(f"Error al enviar la nómina. Respuesta XML: {e}")
            raise Exception(e)

        return {
            'messages': messages,
            'payroll': {
                'Cune': self._cune
            },
        }

    def _send_test_set(self, zip_payroll):
        """
        Envío al set de pruebas del proceso de habilitación. Es asíncrono: la
        DIAN responde un ZipKey y el resultado de la validación se consulta
        después con GetStatusZip (ver `get_status`).
        """
        recorder = self._recorder()

        try:
            response = SoapPayrollTestRequest(self._security).send_xml(
                zip_payroll,
                test_set_id=self.payroll.TestID,
                file_name=self.zip_name
            )
            zip_key, messages = generic.extract_zip_key(response.text)

            if not zip_key:
                print(f"Error al enviar la nómina de prueba. XML enviado: {self.xml_name}")
                print(f"Error al enviar la nómina de prueba. Respuesta XML: {response.text}")
                raise Exception(messages or 'La DIAN no devolvió ZipKey')

            # Envío asíncrono: queda ENVIADO hasta que se reconsulte el ZipKey.
            recorder.sent_async(zip_key, messages, response.text)

        except Exception as e:
            recorder.fail(str(e))
            print(f"Error al enviar la nómina de prueba. XML enviado: {self.xml_name}")
            print(f"Error al enviar la nómina de prueba. Respuesta XML: {e}")
            raise Exception(e)

        return {
            'messages': messages,
            'payroll': {
                'Cune': self._cune,
                'ZipKey': zip_key,
                'FileName': self.zip_name,
            },
        }

    def get_status(self, track_id: str):
        """
        Consulta el resultado de un envío al set de pruebas usando el ZipKey.

        :param track_id: ZipKey devuelto por el envío al set de pruebas.
        """
        response = SoapStatusZipRequest(self._security).get_status(track_id)
        return response.text
