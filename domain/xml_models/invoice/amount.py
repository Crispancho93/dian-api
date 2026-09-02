from .invoice_base import InvoiceBase

class Amount(InvoiceBase):
    def __init__(self, invoice):
        self.invoice = invoice
        self.names = invoice.names
        self.set_value = invoice.set_value
        
    # Total Valor Bruto antes de tributos
    @property
    def LineExtensionAmount(self):
        return self._LineExtensionAmount

    @LineExtensionAmount.setter
    def LineExtensionAmount(self, value):
        value = str(value)
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            '//cac:LegalMonetaryTotal/cbc:LineExtensionAmount', 
            value,
        )
        self._LineExtensionAmount = value

    # Base imponible para el cálculo de los tributos 
    @property
    def TaxExclusiveAmount(self):
        return self._TaxExclusiveAmount

    @TaxExclusiveAmount.setter
    def TaxExclusiveAmount(self, value):
        value = str(value)
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            '//cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount', 
            value,
        )
        self._TaxExclusiveAmount = value

    # Total de Valor Bruto más tributos
    @property
    def TaxInclusiveAmount(self):
        return self._TaxInclusiveAmount

    @TaxInclusiveAmount.setter
    def TaxInclusiveAmount(self, value):
        value = str(value)
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            '//cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount', 
            value,
        )
        self._TaxInclusiveAmount = value
    
    # Anticipo Total: Suma de todos los pagos anticipados
    @property
    def PrepaidAmount(self):
        return self._PrepaidAmount

    @PrepaidAmount.setter
    def PrepaidAmount(self, value):
        value = str(value)
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            '//cac:LegalMonetaryTotal/cbc:PrepaidAmount', 
            value,
        )
        self._PrepaidAmount = value

    # Este valor representa el monto pendiente por pagar.
    @property
    def PayableAmount(self):
        return self._PayableAmount

    @PayableAmount.setter
    def PayableAmount(self, value):
        value = str(value)
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            '//cac:LegalMonetaryTotal/cbc:PayableAmount', 
            value,
        )
        self._PayableAmount = value