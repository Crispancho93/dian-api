import hashlib

class Control:
    def __init__(self, invoice):
        self.invoice = invoice
        self.names = invoice.names
        self.set_value = invoice.set_value
        self.set_scheme = invoice.set_scheme

    # Fecha de inicio de la resolucion
    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, value):
        self.set_value({'sts': self.names['sts'], 'cbc': self.names['cbc']}, '//cbc:StartDate', value)
        self._StartDate = value

    # Fecha de vencimiento de la resolucion
    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, value):
        self.set_value({'sts': self.names['sts'], 'cbc': self.names['cbc']}, '//cbc:EndDate', value)
        self._EndDate = value

    # Numero de la resolucion
    @property
    def InvoiceAuthorization(self):
        return self._InvoiceAuthorization

    @InvoiceAuthorization.setter
    def InvoiceAuthorization(self, value):
        self.set_value({'sts': self.names['sts']}, '//sts:InvoiceAuthorization', value)
        self._InvoiceAuthorization = value

    @property
    def Prefix(self):
        return self._Prefix

    @Prefix.setter
    def Prefix(self, value):
        self.set_value({'sts': self.names['sts']}, '//sts:Prefix', value)
        self._Prefix = value
    
    # Numero inicial para la factura
    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, value):
        self.set_value({'sts': self.names['sts']}, '//sts:From', value)
        self._From = value
    
    # Numero final para la factura
    @property
    def To(self):
        return self._To

    @To.setter
    def To(self, value):
        self.set_value({'sts': self.names['sts']}, '//sts:To', value)
        self._To = value

    # Nit de la empresa
    @property
    def ProviderID(self):
        return self._ProviderID

    @ProviderID.setter
    def ProviderID(self, value):
        self.set_value({'sts': self.names['sts']}, '//sts:ProviderID', value)
        self._ProviderID = value

    @property
    def SoftwareID(self):
        return self._SoftwareID

    @SoftwareID.setter
    def SoftwareID(self, value):
        self.set_value({'sts': self.names['sts']}, '//sts:SoftwareID', value)
        self._SoftwareID = value

    # SoftwareSecurityCode:= SHA-384 (Id Software + Pin + NroDocumentos - Consecutivo de la factura)
    @property
    def SoftwareSecurityCode(self):
        return self._SoftwareSecurityCode

    @SoftwareSecurityCode.setter
    def SoftwareSecurityCode(self, value):
        hash_obj = hashlib.sha384(value.encode())
        result = hash_obj.hexdigest()
        
        self.set_value({'sts': self.names['sts']}, '//sts:SoftwareSecurityCode', result)
        self._SoftwareSecurityCode = value

    @property
    def QRCode(self):
        return self._QRCode

    @QRCode.setter
    def QRCode(self, value):
        self.set_value({'sts': self.names['sts']}, '//sts:QRCode', value)
        self._QRCode = value

    # Ambiente de destino (1 - PRD, 2 - Pruebas)
    @property
    def ProfileExecutionID(self):
        return self._ProfileExecutionID

    @ProfileExecutionID.setter
    def ProfileExecutionID(self, value):
        self.set_value({'cbc': self.names['cbc']}, '//cbc:ProfileExecutionID', value)
        self.set_scheme({'cbc': self.names['cbc']}, '//cbc:UUID', 'schemeID', value)
        self._ProfileExecutionID = value

    @property
    def VerificationDigit(self):
        return self._VerificationDigit

    @VerificationDigit.setter
    def VerificationDigit(self, value):
        self.set_scheme(
            {'sts': self.names['sts']},
            '//sts:ProviderID',
            'schemeID',
            value
        )
        self._VerificationDigit = value