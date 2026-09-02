from pydantic import BaseModel, Field, EmailStr, validator
from typing import List, Optional, Literal

class ControlRequest(BaseModel):
    StartDate: str
    EndDate: str
    InvoiceAuthorization: str
    Pin: str
    Prefix: str
    From: str
    To: str
    ProviderID: str
    SoftwareID: str
    ProfileExecutionID: str

    @validator('ProfileExecutionID')
    def check_profile_execution_id(cls, value):
        if value not in {"1", "2"}:
            raise ValueError('ProfileExecutionID must be "1" or "2"')
        return value

class PaymentRequest(BaseModel):
    PaymentID: str
    PaymentCode: str

class TaxSubtotalRequest(BaseModel):
    TaxAmount: str
    TaxableAmount: str
    TaxPercent: str
    TaxSchemeID: str
    TaxSchemeName: str

class TaxTotalRequest(BaseModel):
    TaxAmount: str
    TaxSubtotal: List[TaxSubtotalRequest]

class AmountsRequest(BaseModel):
    LineExtensionAmount: str
    TaxExclusiveAmount: str
    TaxInclusiveAmount: str
    PrepaidAmount: str
    PayableAmount: str
    TaxTotals: List[TaxTotalRequest]

class InvoiceLineRequest(BaseModel):
    ID: Optional[str] = None
    InvoicedQuantity: str
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

class AddressRequest(BaseModel):
    AddressID: str
    CountrySubentityCode: str
    CityName: str
    CountrySubentity: str
    AddressLine: str

class LegalRequest(BaseModel):
    RegistrationName: str
    CompanyID: str

class PartyRequest(BaseModel):
    AdditionalAccountID: str
    PartyName: str
    CompanyID: str
    TaxLevelCode: str
    Address: AddressRequest

class CustomerRequest(BaseModel):
    ID: str
    DocumentType: str
    AdditionalAccountID: str
    PartyName: str
    Telephone: str
    Email: str
    Address: AddressRequest

class InvoiceRequest(BaseModel):
    Control: ControlRequest
    ID: str
    IssueDate: str
    IssueTime: str
    Payment: PaymentRequest
    Amounts: AmountsRequest
    Lines: List[InvoiceLineRequest]
    Company: PartyRequest
    Customer: CustomerRequest
