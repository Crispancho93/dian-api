from shared import generic
from domain.xml_models import PayrollAdjustmentXml
from domain.dtos import PayrollAdjustmentDto
from shared.certificate import CertificateLoader
from .create_payroll_case import CreatePayrollCase
from domain.entities.document import TIPO_NOMINA_AJUSTE


class CreatePayrollAdjustmentCase(CreatePayrollCase):
    """
    Caso de uso para la Nota de Ajuste de Nómina Electrónica
    (NominaIndividualDeAjuste, TipoXML 103).

    Hereda de CreatePayrollCase: el flujo de firmar -> comprimir -> guardar ->
    enviar (set de pruebas o producción) es idéntico. Solo cambian el modelo
    XML, el tipo de documento para el firmador, el prefijo del archivo y el
    cálculo del CUNE en la variante Eliminar.
    """

    XML_CLASS = PayrollAdjustmentXml
    DOCUMENT_TYPE = 'NA'
    FILE_PREFIX = 'niae'
    DOCUMENT_RECORD_TYPE = TIPO_NOMINA_AJUSTE

    def __init__(
        self,
        payroll: PayrollAdjustmentDto,
        certificate_loader: CertificateLoader
    ):
        """
        :param payroll: :class:`PayrollAdjustmentDto`
        :param certificate_loader: :class:`CertificateLoader`
        """
        super().__init__(payroll, certificate_loader)

    def _get_cune(self) -> str:
        """
        Para la opción Eliminar el anexo indica que los valores de devengados,
        deducciones y total van en '0.00' literal y el documento del empleado
        en '0' (no hay Trabajador en ese documento).
        """
        p = self.payroll

        if p.TipoNota == PayrollAdjustmentXml.TIPO_NOTA_ELIMINAR:
            val_dev = val_ded = val_tol = '0.00'
            doc_emp = '0'
        else:
            val_dev = p.DevengadosTotal
            val_ded = p.DeduccionesTotal
            val_tol = p.ComprobanteTotal
            doc_emp = p.Trabajador.NumeroDocumento

        values = {
            "NumNE": p.NumeroSecuenciaXML.Numero,
            "FecNE": p.InformacionGeneral.FechaGen,
            "HorNE": p.InformacionGeneral.HoraGen,
            "ValDev": val_dev,
            "ValDed": val_ded,
            "ValTolNE": val_tol,
            "NitNE": p.Empleador.NIT,
            "DocEmp": doc_emp,
            "TipoXML": self.XML_CLASS.TIPO_XML,
            "SoftwarePin": p.Pin,
            "TipAmb": p.InformacionGeneral.Ambiente,
        }
        return generic.get_cune(values)
