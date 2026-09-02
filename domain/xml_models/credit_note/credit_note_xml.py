from .credit_note_base import CreditNoteBase
from .control import Control
from .company import Company
from .customer import Customer
from .payment import Payment
from .amount import Amount

class CreditNoteXml(CreditNoteBase):
    def __init__(self):
        super().__init__()
        self.Company = Company(self)
        self.Control = Control(self)
        self.Customer = Customer(self)
        self.Payment = Payment(self)
        self.Amounts = Amount(self)

    @property
    def UUID(self):
        return self._UUID

    # CUFE
    @UUID.setter
    def UUID(self, value):
        self.set_value({'cbc': self.names['cbc']}, '//cbc:UUID', value)
        self._UUID = value

    @property
    def ID(self):
        return self._ID

    # Consecutivo, Numero del documento
    @ID.setter
    def ID(self, value):
        self.set_value({'cbc': self.names['cbc']}, '//cbc:ID', value)
        self._ID = value

    # Fecha de la factura 2019-06-20
    @property
    def IssueDate(self):
        return self._IssueDate

    @IssueDate.setter
    def IssueDate(self, value):
        self.set_value({'cbc': self.names['cbc']}, '//cbc:IssueDate', value)
        self._IssueDate = value

    # Hora de la factura 09:15:23-05:00
    @property
    def IssueTime(self):
        return self._IssueTime

    @IssueTime.setter
    def IssueTime(self, value):
        self.set_value({'cbc': self.names['cbc']}, '//cbc:IssueTime', value)
        self._IssueTime = value

    # tabla 13.1.5.2, 20 - Nota Crédito que referencia una factura electrónica.
    @property
    def CustomizationID(self):
        return self._CustomizationID

    @CustomizationID.setter
    def CustomizationID(self, value):
        self.set_value({'cbc': self.names['cbc']}, '//cbc:CustomizationID', value)
        self._CustomizationID = value

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, value):
        self.set_value({'cbc': self.names['cbc']}, '//cbc:Note', value)
        self._Note = value

    # Numero de lineas
    @property
    def LineCountNumeric(self):
        return self._LineCountNumeric

    @LineCountNumeric.setter
    def LineCountNumeric(self, value):
        self.set_value({'cbc': self.names['cbc']}, '//cbc:LineCountNumeric', value)
        self._LineCountNumeric = value

    @property
    def PartyIdentification(self):
        return self._PartyIdentification

    @PartyIdentification.setter
    def PartyIdentification(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            '//cac:TaxRepresentativeParty/cac:PartyIdentification/cbc:ID', 
            value,
        )
        self._PartyIdentification = value

    # Factura a la que se aplica la NOTA
    @property
    def ReferenceID(self):
        return self._ReferenceID

    @ReferenceID.setter
    def ReferenceID(self, value):
        self.set_value({'cbc': self.names['cbc']}, '//cbc:ReferenceID', value)
        self._ReferenceID = value

    # Factura a la que se aplica la NOTA
    @property
    def BillingID(self):
        return self._BillingID

    @BillingID.setter
    def BillingID(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            '//cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID', value
        )
        self._BillingID = value

    # CUFE de la Factura a la que se aplica la NOTA
    @property
    def BillingUUID(self):
        return self._BillingUUID

    @BillingUUID.setter
    def BillingUUID(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            '//cac:BillingReference/cac:InvoiceDocumentReference/cbc:UUID', value
        )
        self._BillingUUID = value

    # IssueDate de la Factura a la que se aplica la NOTA
    @property
    def BillingIssueDate(self):
        return self._BillingIssueDate

    @BillingIssueDate.setter
    def BillingIssueDate(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            '//cac:BillingReference/cac:InvoiceDocumentReference/cbc:IssueDate', value
        )
        self._BillingIssueDate = value