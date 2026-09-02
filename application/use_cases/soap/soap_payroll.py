import requests
from shared import templates_loader
from shared.config import resolve_web_service
from shared.certificate import CertificateData
from .soap_base import SoapBase

_ACTION_BASE = 'http://wcf.dian.colombia/IWcfDianCustomerServices'


class SoapPayrollRequest(SoapBase):
    """
    Envío de Nómina Electrónica en PRODUCCIÓN/OPERACIÓN, vía SendNominaSync.

    Según el WSDL de la DIAN esta operación solo acepta <contentFile>; no
    admite testSetId. Para el set de pruebas del proceso de habilitación
    usar :class:`SoapPayrollTestRequest`.
    """

    def __init__(self, certificate_data: CertificateData):
        """
        :param certificate_data: :class:`CertificateData`
        """
        super().__init__(certificate_data)
        self.xml_template = templates_loader.template.xml_payroll_request
        self.web_service = resolve_web_service(habilitacion=False)

    def _send_soap_request(self, xml_request):
        url = self.web_service
        headers = {
            'Content-Type': 'application/soap+xml; charset=utf-8',
            'SOAPAction': f'{_ACTION_BASE}/SendNominaSync'
        }

        response = requests.post(url, data=xml_request, headers=headers)
        response.raise_for_status()

        return response

    def send_xml(self, base64_file):
        self.xml_template = self.xml_template.format(
            WEB_SERVICE=self.web_service,
            contentFile=base64_file
        )

        xml_request = self.prepare_xml(self.xml_template)
        return self._send_soap_request(xml_request)


class SoapPayrollTestRequest(SoapBase):
    """
    Envío del SET DE PRUEBAS de nómina (habilitación), vía SendTestSetAsync.

    Es el método que exige el portal de habilitación cuando indica que se debe
    proporcionar el TestSetId en el web service. Es asíncrono: responde un
    ZipKey y el resultado se consulta luego con :class:`SoapStatusZipRequest`.
    """

    def __init__(self, certificate_data: CertificateData):
        """
        :param certificate_data: :class:`CertificateData`
        """
        super().__init__(certificate_data)
        self.xml_template = templates_loader.template.xml_payroll_test_request
        self.web_service = resolve_web_service(habilitacion=True)

    def _send_soap_request(self, xml_request):
        url = self.web_service
        headers = {
            'Content-Type': 'application/soap+xml; charset=utf-8',
            'SOAPAction': f'{_ACTION_BASE}/SendTestSetAsync'
        }

        response = requests.post(url, data=xml_request, headers=headers)
        response.raise_for_status()

        return response

    def send_xml(self, base64_file, test_set_id: str, file_name: str):
        """
        :param base64_file: ZIP del documento firmado, en base64.
        :param test_set_id: Identificador del set de pruebas (TestSetId).
        :param file_name: Nombre del archivo .zip enviado.
        """
        self.xml_template = self.xml_template.format(
            WEB_SERVICE=self.web_service,
            fileName=file_name,
            contentFile=base64_file,
            testSetId=test_set_id
        )

        xml_request = self.prepare_xml(self.xml_template)
        return self._send_soap_request(xml_request)


class SoapStatusZipRequest(SoapBase):
    """
    Consulta del resultado de un envío asíncrono (SendTestSetAsync), usando el
    ZipKey/trackId devuelto por ese método.
    """

    def __init__(self, certificate_data: CertificateData):
        """
        :param certificate_data: :class:`CertificateData`
        """
        super().__init__(certificate_data)
        self.xml_template = templates_loader.template.xml_status_zip_request
        self.web_service = resolve_web_service(habilitacion=True)

    def _send_soap_request(self, xml_request):
        url = self.web_service
        headers = {
            'Content-Type': 'application/soap+xml; charset=utf-8',
            'SOAPAction': f'{_ACTION_BASE}/GetStatusZip'
        }

        response = requests.post(url, data=xml_request, headers=headers)
        response.raise_for_status()

        return response

    def get_status(self, track_id: str):
        """
        :param track_id: ZipKey devuelto por SendTestSetAsync.
        """
        self.xml_template = self.xml_template.format(
            WEB_SERVICE=self.web_service,
            trackId=track_id
        )

        xml_request = self.prepare_xml(self.xml_template)
        return self._send_soap_request(xml_request)
