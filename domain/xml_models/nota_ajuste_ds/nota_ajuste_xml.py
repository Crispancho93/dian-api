from .nota_ajuste_base import NotaAjusteBase
from .nota_ajuste_control import Control
from domain.xml_models.documento_soporte.company import Company
from domain.xml_models.documento_soporte.customer import Customer
from domain.xml_models.documento_soporte.payment import Payment
from domain.xml_models.documento_soporte.amount import Amount


class NotaAjusteDocumentoSoporteXml(NotaAjusteBase):
    """Nota de Ajuste al Documento Soporte — CreditNote, CreditNoteTypeCode 95.

    Company, Customer, Payment y Amount se reutilizan del documento soporte: la
    estructura UBL de las partes, los medios de pago y los totales es idéntica.
    Lo propio de este documento son DiscrepancyResponse (naturaleza de la
    corrección) y BillingReference (el documento soporte que se corrige).
    """

    def __init__(self):
        super().__init__()
        self.Company = Company(self)
        self.Control = Control(self)
        self.Customer = Customer(self)
        self.Payment = Payment(self)
        self.Amounts = Amount(self)

    # ------------------------------------------------------------------
    # Cabecera
    # ------------------------------------------------------------------
    @property
    def UUID(self):
        return self._UUID

    # CUDS de esta nota de ajuste
    @UUID.setter
    def UUID(self, value):
        self.set_value({'cbc': self.names['cbc']}, '//cbc:UUID', value)
        self._UUID = value

    @property
    def ID(self):
        return self._ID

    # Consecutivo, número del documento
    @ID.setter
    def ID(self, value):
        self.set_value({'cbc': self.names['cbc']}, '//cbc:ID', value)
        self._ID = value

    @property
    def IssueDate(self):
        return self._IssueDate

    @IssueDate.setter
    def IssueDate(self, value):
        self.set_value({'cbc': self.names['cbc']}, '//cbc:IssueDate', value)
        self._IssueDate = value

    @property
    def IssueTime(self):
        return self._IssueTime

    @IssueTime.setter
    def IssueTime(self, value):
        self.set_value({'cbc': self.names['cbc']}, '//cbc:IssueTime', value)
        self._IssueTime = value

    @property
    def CustomizationID(self):
        return self._CustomizationID

    @CustomizationID.setter
    def CustomizationID(self, value):
        self.set_value({'cbc': self.names['cbc']}, '//cbc:CustomizationID', value)
        self._CustomizationID = value

    @property
    def LineCountNumeric(self):
        return self._LineCountNumeric

    @LineCountNumeric.setter
    def LineCountNumeric(self, value):
        self.set_value({'cbc': self.names['cbc']}, '//cbc:LineCountNumeric', value)
        self._LineCountNumeric = value

    # ------------------------------------------------------------------
    # DiscrepancyResponse — naturaleza de la corrección (NSBF01-04)
    # ------------------------------------------------------------------
    @property
    def DiscrepancyReferenceID(self):
        return self._DiscrepancyReferenceID

    @DiscrepancyReferenceID.setter
    def DiscrepancyReferenceID(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']},
            '//cac:DiscrepancyResponse/cbc:ReferenceID',
            value,
        )
        self._DiscrepancyReferenceID = value

    @property
    def DiscrepancyResponseCode(self):
        return self._DiscrepancyResponseCode

    # §16.2.4: 1 devolución parcial · 2 anulación · 3 rebaja o descuento ·
    # 4 ajuste de precio · 5 otros. La DIAN rechaza cualquier otro valor.
    @DiscrepancyResponseCode.setter
    def DiscrepancyResponseCode(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']},
            '//cac:DiscrepancyResponse/cbc:ResponseCode',
            value,
        )
        self._DiscrepancyResponseCode = value

    @property
    def DiscrepancyDescription(self):
        return self._DiscrepancyDescription

    # NSBF04: de 20 a 5000 caracteres, obligatorio
    @DiscrepancyDescription.setter
    def DiscrepancyDescription(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']},
            '//cac:DiscrepancyResponse/cbc:Description',
            value,
        )
        self._DiscrepancyDescription = value

    # ------------------------------------------------------------------
    # BillingReference — documento soporte corregido (NSBG01-05)
    # ------------------------------------------------------------------
    @property
    def BillingID(self):
        return self._BillingID

    @BillingID.setter
    def BillingID(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']},
            '//cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID',
            value,
        )
        self._BillingID = value

    @property
    def BillingUUID(self):
        return self._BillingUUID

    # CUDS del documento soporte afectado. Rechazo de la DIAN si no se reporta.
    @BillingUUID.setter
    def BillingUUID(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']},
            '//cac:BillingReference/cac:InvoiceDocumentReference/cbc:UUID',
            value,
        )
        self._BillingUUID = value

    @property
    def BillingIssueDate(self):
        return self._BillingIssueDate

    @BillingIssueDate.setter
    def BillingIssueDate(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']},
            '//cac:BillingReference/cac:InvoiceDocumentReference/cbc:IssueDate',
            value,
        )
        self._BillingIssueDate = value
