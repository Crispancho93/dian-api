from pydantic import BaseModel, Field, EmailStr, validator
from typing import List, Optional, Literal

class ControlNotaDto(BaseModel):
    Pin: str # Se queda si debo calcular CUFE
    InvoiceAuthorization: str
    ProviderID: str
    SoftwareID: str
    ProfileExecutionID: str
    TechnicalKey: str

    @validator('ProfileExecutionID')
    def check_profile_execution_id(cls, value):
        if value not in {"1", "2"}:
            raise ValueError('ProfileExecutionID must be "1" or "2"')
        return value

class PaymentDto(BaseModel):
    PaymentID: str
    PaymentCode: str

class TaxSubTotalDto(BaseModel):
    TaxAmount: str
    TaxableAmount: str
    TaxPercent: str
    TaxSchemeID: str
    TaxSchemeName: str

class TaxTotalDto(BaseModel):
    TaxAmount: str
    TaxSubtotal: List[TaxSubTotalDto]

class AmountsDto(BaseModel):
    LineExtensionAmount: str
    TaxExclusiveAmount: str
    TaxInclusiveAmount: str
    PrepaidAmount: str
    PayableAmount: str
    TaxTotals: List[TaxTotalDto]

class CreditNoteLineDto(BaseModel):
    ID: Optional[str] = None
    Quantity: str
    LineExtensionAmount: str
    TaxAmount: str
    TaxableAmount: str
    TaxSubtotalAmount: str
    TaxPercent: str
    TaxSchemeID: str
    TaxSchemeName: str
    Description: str
    SellersItemID: str
    AdditionalItemID: str
    PriceAmount: str
    BaseQuantity: str

class AddressDto(BaseModel):
    AddressID: str
    CountrySubentityCode: str
    CityName: str
    CountrySubentity: str
    AddressLine: str

class LegalDto(BaseModel):
    RegistrationName: str
    CompanyID: str

class CompanyDto(BaseModel):
    AdditionalAccountID: str
    PartyName: str
    CompanyID: str
    DocumentType: str
    VerificationDigit: Optional[str] = None
    TaxLevelCode: str
    Email: str
    Address: AddressDto
    Telephone: str

class CustomerDto(BaseModel):
    ID: str
    DocumentType: str
    AdditionalAccountID: str
    PartyName: str
    Telephone: str
    Email: str
    TaxLevelCode: str
    Address: AddressDto

class Billing(BaseModel):
    ID: str
    UUID: str
    IssueDate: str

class CreditNoteDto(BaseModel):
    Control: ControlNotaDto
    ID: str
    IssueDate: str
    IssueTime: str
    Billing: Billing
    Payment: PaymentDto
    Amounts: AmountsDto
    Lines: List[CreditNoteLineDto]
    Company: CompanyDto
    Customer: CustomerDto