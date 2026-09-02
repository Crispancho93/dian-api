from .dian_catalogos import get_department_name, get_municipality_name

class Customer:
    def __init__(self, invoice):
        self.invoice = invoice
        self.names = invoice.names
        self.set_value = invoice.set_value
        self.set_scheme = invoice.set_scheme

        # El vendedor (persona natural) va en AccountingSupplierParty
        self._AddressLocation = '//cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:Address'
        self._TaxScheme = '//cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme'
        self._PartyLegalEntity = '//cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity'
        self._Party = '//cac:AccountingSupplierParty/cac:Party'

    @property
    def AdditionalAccountID(self):
        return self._AdditionalAccountID

    @AdditionalAccountID.setter
    def AdditionalAccountID(self, value):
        self.set_value({'cac': self.names['cac'], 'cbc': self.names['cbc']}, '//cac:AccountingSupplierParty/cbc:AdditionalAccountID', value)
        self._AdditionalAccountID = value

    @property
    def PartyName(self):
        return self._PartyName

    @PartyName.setter
    def PartyName(self, value):
        self.set_value({'cac': self.names['cac'], 'cbc': self.names['cbc']}, '//cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name', value)
        self._PartyName = value

    @property
    def CompanyID(self):
        return self._CompanyID

    @CompanyID.setter
    def CompanyID(self, value):
        self.set_value({'cac': self.names['cac'], 'cbc': self.names['cbc']}, f'{self._TaxScheme}/cbc:CompanyID', value)
        self.set_value({'cac': self.names['cac'], 'cbc': self.names['cbc']}, f'{self._PartyLegalEntity}/cbc:CompanyID', value)
        self._CompanyID = value

    @property
    def DocumentType(self):
        return self._DocumentType

    @DocumentType.setter
    def DocumentType(self, value):
        self.set_scheme({'cac': self.names['cac'], 'cbc': self.names['cbc']}, f'{self._TaxScheme}/cbc:CompanyID', 'schemeName', value)
        self.set_scheme({'cac': self.names['cac'], 'cbc': self.names['cbc']}, f'{self._PartyLegalEntity}/cbc:CompanyID', 'schemeName', value)
        self._DocumentType = value

    @property
    def VerificationDigit(self):
        return self._VerificationDigit

    @VerificationDigit.setter
    def VerificationDigit(self, value):
        self.set_scheme({'cac': self.names['cac'], 'cbc': self.names['cbc']}, f'{self._TaxScheme}/cbc:CompanyID', 'schemeID', value)
        self.set_scheme({'cac': self.names['cac'], 'cbc': self.names['cbc']}, f'{self._PartyLegalEntity}/cbc:CompanyID', 'schemeID', value)
        self._VerificationDigit = value

    @property
    def RegistrationName(self):
        return self._RegistrationName

    @RegistrationName.setter
    def RegistrationName(self, value):
        self.set_value({'cac': self.names['cac'], 'cbc': self.names['cbc']}, f'{self._TaxScheme}/cbc:RegistrationName', value)
        self.set_value({'cac': self.names['cac'], 'cbc': self.names['cbc']}, f'{self._PartyLegalEntity}/cbc:RegistrationName', value)
        self._RegistrationName = value

    @property
    def TaxLevelCode(self):
        return self._TaxLevelCode

    @TaxLevelCode.setter
    def TaxLevelCode(self, value):
        self.set_value({'cac': self.names['cac'], 'cbc': self.names['cbc']}, f'{self._TaxScheme}/cbc:TaxLevelCode', value)
        self._TaxLevelCode = value

    @property
    def AddressID(self):
        return self._AddressID

    #@AddressID.setter
    #def AddressID(self, value):
    #    self.set_value({'cac': self.names['cac'], 'cbc': self.names['cbc']}, f'{self._AddressLocation}/cbc:ID', value)
    #    self._AddressID = value

    @AddressID.setter
    def AddressID(self, value):

    # Guardamos el código del municipio
        self._AddressID = value

    # Obtenemos el nombre oficial del municipio
    # directamente desde el catálogo DIAN.
        municipality_name = get_municipality_name(value)

    # Escribimos el código del municipio
        self.set_value(
        {'cac': self.names['cac'], 'cbc': self.names['cbc']},
        f'{self._AddressLocation}/cbc:ID',
        value
    )

    # Escribimos el nombre oficial del municipio
        self.set_value(
        {'cac': self.names['cac'], 'cbc': self.names['cbc']},
        f'{self._AddressLocation}/cbc:CityName',
        municipality_name
    )


    @property
    def AddressPostalZone(self):
        return self._AddressPostalZone

    @AddressPostalZone.setter
    def AddressPostalZone(self, value):
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']},
            f'{self._AddressLocation}/cbc:PostalZone',
            value
        )
        self._AddressPostalZone = value

    @property
    def AddressCityName(self):
        return self._AddressCityName

    @AddressCityName.setter
    def AddressCityName(self, value):
        self.set_value({'cac': self.names['cac'], 'cbc': self.names['cbc']}, f'{self._AddressLocation}/cbc:CityName', value)
        self._AddressCityName = value

    @property
    def AddressCountrySubentity(self):
        return self._AddressCountrySubentity

    @AddressCountrySubentity.setter
    def AddressCountrySubentity(self, value):
        self.set_value({'cac': self.names['cac'], 'cbc': self.names['cbc']}, f'{self._AddressLocation}/cbc:CountrySubentity', value)
        self._AddressCountrySubentity = value

  #   @property
   #  def AddressCountrySubentity(self):
  #       return self._AddressCountrySubentity

  #   @AddressCountrySubentity.setter
 #    def AddressCountrySubentity(self, value):

        # Normalizar el nombre del departamento para el XML
     #    normalized_value = str(value).strip().lower()

        # self.set_value(
       #      {'cac': self.names['cac'], 'cbc': self.names['cbc']},
      #       f'{self._AddressLocation}/cbc:CountrySubentity',
      #       normalized_value
     #    )

      #  self._AddressCountrySubentity = normalized_value

    @property
    def AddressCountrySubentityCode(self):
        return self._AddressCountrySubentityCode

    #@AddressCountrySubentityCode.setter
    #def AddressCountrySubentityCode(self, value):
    #    self.set_value({'cac': self.names['cac'], 'cbc': self.names['cbc']}, f'{self._AddressLocation}/cbc:CountrySubentityCode', value)
    #    self._AddressCountrySubentityCode = value

    @AddressCountrySubentityCode.setter
    def AddressCountrySubentityCode(self, value):

    # Guardamos el código
        self._AddressCountrySubentityCode = value

    # Obtenemos el nombre oficial desde el catálogo DIAN
        department_name = get_department_name(value)

    # Escribimos el nombre oficial en el XML
        self.set_value(
        {'cac': self.names['cac'], 'cbc': self.names['cbc']},
        f'{self._AddressLocation}/cbc:CountrySubentity',
        department_name
        )

    # Escribimos también el código
        self.set_value(
        {'cac': self.names['cac'], 'cbc': self.names['cbc']},
        f'{self._AddressLocation}/cbc:CountrySubentityCode',
        value
        )

    @property
    def AddressLine(self):
        return self._AddressLine

    @AddressLine.setter
    def AddressLine(self, value):
        self.set_value({'cac': self.names['cac'], 'cbc': self.names['cbc']}, f'{self._AddressLocation}/cac:AddressLine/cbc:Line', value)
        self._AddressLine = value

    @property
    def ContactTelephone(self):
        return self._ContactTelephone

    @ContactTelephone.setter
    def ContactTelephone(self, value):
        self.set_value({'cac': self.names['cac'], 'cbc': self.names['cbc']}, f'{self._Party}/cac:Contact/cbc:Telephone', value)
        self._ContactTelephone = value

    @property
    def ContactElectronicMail(self):
        return self._ContactElectronicMail

    @ContactElectronicMail.setter
    def ContactElectronicMail(self, value):
        self.set_value({'cac': self.names['cac'], 'cbc': self.names['cbc']}, f'{self._Party}/cac:Contact/cbc:ElectronicMail', value)
        self._ContactElectronicMail = value