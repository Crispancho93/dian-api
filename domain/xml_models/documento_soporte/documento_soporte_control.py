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
        self.set_value(
            {
                'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2',
                'sts': 'dian:gov:co:facturaelectronica:Structures-2-1',
                'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2'
            }, 
            '//ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:InvoiceControl/sts:AuthorizationPeriod/cbc:StartDate', 
            value
        )
        self._StartDate = value

    # Fecha de vencimiento de la resolucion
    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, value):
        self.set_value(
            {
                'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2',
                'sts': 'dian:gov:co:facturaelectronica:Structures-2-1',
                'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2'
            }, 
            '//ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:InvoiceControl/sts:AuthorizationPeriod/cbc:EndDate', 
            value
        )
        self._EndDate = value

    # Numero de la resolucion
    @property
    def InvoiceAuthorization(self):
        return self._InvoiceAuthorization

    @InvoiceAuthorization.setter
    def InvoiceAuthorization(self, value):
        self.set_value(
            {
                'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2',
                'sts': 'dian:gov:co:facturaelectronica:Structures-2-1'
            }, 
            '//ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:InvoiceControl/sts:InvoiceAuthorization', 
            value
        )
        self._InvoiceAuthorization = value

    @property
    def Prefix(self):
        return self._Prefix

    @Prefix.setter
    def Prefix(self, value):
        self.set_value(
            {
                'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2',
                'sts': 'dian:gov:co:facturaelectronica:Structures-2-1'
            }, 
            '//ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:InvoiceControl/sts:AuthorizedInvoices/sts:Prefix', 
            value
        )
        self._Prefix = value
    
    # Numero inicial para el documento
    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, value):
        self.set_value(
            {
                'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2',
                'sts': 'dian:gov:co:facturaelectronica:Structures-2-1'
            }, 
            '//ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:InvoiceControl/sts:AuthorizedInvoices/sts:From', 
            value
        )
        self._From = value
    
    # Numero final para el documento
    @property
    def To(self):
        return self._To

    @To.setter
    def To(self, value):
        self.set_value(
            {
                'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2',
                'sts': 'dian:gov:co:facturaelectronica:Structures-2-1'
            }, 
            '//ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:InvoiceControl/sts:AuthorizedInvoices/sts:To', 
            value
        )
        self._To = value

    # Nit de la empresa
    @property
    def ProviderID(self):
        return self._ProviderID

    @ProviderID.setter
    def ProviderID(self, value):
        self.set_value(
            {
                'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2',
                'sts': 'dian:gov:co:facturaelectronica:Structures-2-1'
            }, 
            '//ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:SoftwareProvider/sts:ProviderID', 
            value
        )
        self._ProviderID = value

    @property
    def SoftwareID(self):
        return self._SoftwareID

    @SoftwareID.setter
    def SoftwareID(self, value):
        self.set_value(
            {
                'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2',
                'sts': 'dian:gov:co:facturaelectronica:Structures-2-1'
            }, 
            '//ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:SoftwareProvider/sts:SoftwareID', 
            value
        )
        self._SoftwareID = value

    # SoftwareSecurityCode:= SHA-384 (Id Software + Pin + NroDocumentos - Consecutivo)
    @property
    def SoftwareSecurityCode(self):
        return self._SoftwareSecurityCode

    @SoftwareSecurityCode.setter
    def SoftwareSecurityCode(self, value):
        hash_obj = hashlib.sha384(value.encode())
        result = hash_obj.hexdigest()
        
        self.set_value(
            {
                'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2',
                'sts': 'dian:gov:co:facturaelectronica:Structures-2-1'
            }, 
            '//ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:SoftwareSecurityCode', 
            result
        )
        self._SoftwareSecurityCode = value

    @property
    def QRCode(self):
        return self._QRCode

    @QRCode.setter
    def QRCode(self, value):
        self.set_value(
            {
                'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2',
                'sts': 'dian:gov:co:facturaelectronica:Structures-2-1'
            }, 
            '//ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:QRCode', 
            value
        )
        self._QRCode = value

    # Ambiente de destino (1 - PRD, 2 - Pruebas)
   # Ambiente de destino (1 - PRD, 2 - Pruebas)
    @property
    def ProfileExecutionID(self):
        return self._ProfileExecutionID

    @ProfileExecutionID.setter
    def ProfileExecutionID(self, value):
        # 1. Asigna el valor al nodo <cbc:ProfileExecutionID>
        self.set_value(
            {
                'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2'
            }, 
            '//cbc:ProfileExecutionID', 
            value
        )
        
        # 2. NUEVO: Actualiza dinámicamente el atributo schemeID del CUDS (UUID)
        self.set_scheme(
            {
                'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2'
            },
            '//cbc:UUID',
            'schemeID',
            str(value)
        )
        
        self._ProfileExecutionID = value

    @property
    def VerificationDigit(self):
        return self._VerificationDigit

    @VerificationDigit.setter
    def VerificationDigit(self, value):
        self.set_scheme(
            {
                'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2',
                'sts': 'dian:gov:co:facturaelectronica:Structures-2-1'
            },
            '//ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:SoftwareProvider/sts:ProviderID',
            'schemeID',
            value
        )
        self._VerificationDigit = value

    @property
    def Pin(self):
        return self._Pin

    @Pin.setter
    def Pin(self, value):
        self._Pin = value

    @property
    def TechnicalKey(self):
        return self._TechnicalKey

    @TechnicalKey.setter
    def TechnicalKey(self, value):
        self._TechnicalKey = value