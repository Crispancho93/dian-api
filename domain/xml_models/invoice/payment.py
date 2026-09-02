from .invoice_base import InvoiceBase

class Payment(InvoiceBase):
    def __init__(self, invoice):
        self.invoice = invoice
        self.names = invoice.names
        self.set_value = invoice.set_value

    # tabla de 13.3.4.1 (1 - Contado, 2 - Credito)
    @property
    def PaymentID(self):
        return self._PaymentID

    @PaymentID.setter
    def PaymentID(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            '//cac:PaymentMeans/cbc:ID', 
            value,
        )
        self._PaymentID = value

    # tabla 13.3.4.2, Metodo de pago (10 - Efectivo 49, Tarjeta Débito)
    @property
    def PaymentCode(self):
        return self._PaymentCode

    @PaymentCode.setter
    def PaymentCode(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            '//cac:PaymentMeans/cbc:PaymentMeansCode', 
            value,
        )
        self._PaymentCode = value
    
    # Fecha de vencimiento de la factura
    @property
    def PaymentDueDate(self):
        return self._PaymentDueDate

    @PaymentDueDate.setter
    def PaymentDueDate(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            '//cac:PaymentMeans/cbc:PaymentDueDate', 
            value,
        )
        self._PaymentDueDate = value

    # Se envia una secuencia propia x cada pago
    @property
    def PaymentSequence(self):
        return self._PaymentSequence

    @PaymentSequence.setter
    def PaymentSequence(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            '//cac:PaymentMeans/cbc:PaymentID', 
            value,
        )
        self._PaymentSequence = value
