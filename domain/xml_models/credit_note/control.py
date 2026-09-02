import hashlib

class Control:
    def __init__(self, credit_note):
        self.credit_note = credit_note
        self.names = credit_note.names
        self.set_value = credit_note.set_value
        self.set_scheme = credit_note.set_scheme

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