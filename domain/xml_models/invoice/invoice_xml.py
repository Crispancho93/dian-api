from .invoice_base import InvoiceBase
from .invoice_control import Control
from .company import Company
from .customer import Customer
from .payment import Payment
from .amount import Amount

class InvoiceXml(InvoiceBase):
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

    # tabla 13.1.5.1 Tipos de operación, 10 - Estandar
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

    # El periodo que estoy facturando, si es contado la misma fecha
    @property
    def PeriodStartDate(self):
        return self._PeriodStartDate

    @PeriodStartDate.setter
    def PeriodStartDate(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            '//cac:InvoicePeriod/cbc:StartDate', 
            value
        )
        self._PeriodStartDate = value

    # El periodo que estoy facturando, si es contado la misma fecha
    @property
    def PeriodEndDate(self):
        return self._PeriodEndDate

    @PeriodEndDate.setter
    def PeriodEndDate(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            '//cac:InvoicePeriod/cbc:EndDate', 
            value,
        )
        self._PeriodEndDate = value

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
