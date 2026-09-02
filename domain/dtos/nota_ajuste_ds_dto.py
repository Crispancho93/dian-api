from pydantic import BaseModel, validator
from typing import List, Optional

from .documento_soporte_dto import (
    AmountsDto,
    CompanyDto,
    CustomerDto,
    InvoiceLineDto,
    PaymentDto,
)

# §16.2.4 del anexo. La DIAN rechaza la nota si el código no está en esta tabla.
CORRECTION_CONCEPTS = {
    '1': 'Devolución parcial de los bienes y/o no aceptación parcial del servicio',
    '2': 'Anulación del documento soporte',
    '3': 'Rebaja o descuento parcial o total',
    '4': 'Ajuste de precio',
    '5': 'Otros',
}


class ControlNotaAjusteDto(BaseModel):
    """Control de la nota de ajuste.

    Sin StartDate/EndDate/Prefix/From/To: este documento no lleva resolución ni
    rango (§8.2). InvoiceAuthorization sí hace falta, pero solo para que el
    CertificateLoader ubique el certificado de la empresa.
    """
    InvoiceAuthorization: str
    Pin: str
    ProviderID: str
    SoftwareID: str
    ProfileExecutionID: str
    TechnicalKey: str

    @validator('ProfileExecutionID')
    def check_profile_execution_id(cls, value):
        if value not in {"1", "2"}:
            raise ValueError('ProfileExecutionID must be "1" or "2"')
        return value


class DiscrepancyDto(BaseModel):
    """Naturaleza de la corrección (cac:DiscrepancyResponse, NSBF01-04)."""

    ReferenceID: Optional[str] = None
    ResponseCode: str
    Description: str

    @validator('ResponseCode')
    def check_response_code(cls, value):
        if value not in CORRECTION_CONCEPTS:
            opciones = ', '.join(f'{k} ({v})' for k, v in CORRECTION_CONCEPTS.items())
            raise ValueError(f'ResponseCode debe ser uno de: {opciones}')
        return value

    @validator('Description')
    def check_description(cls, value):
        # NSBF04: de 20 a 5000 caracteres. Se valida acá para que el error sea
        # legible y no un rechazo de la DIAN después de armar y firmar el XML.
        texto = (value or '').strip()
        if not 20 <= len(texto) <= 5000:
            raise ValueError(
                'Description debe tener entre 20 y 5000 caracteres '
                f'(recibidos: {len(texto)})'
            )
        return texto


class BillingDto(BaseModel):
    """Documento soporte que se corrige (cac:BillingReference, NSBG01-05)."""

    ID: str        # prefijo + número del documento soporte corregido
    UUID: str      # CUDS del documento soporte; la DIAN rechaza si falta
    IssueDate: str


class NotaAjusteDocumentoSoporteDTO(BaseModel):
    Control: ControlNotaAjusteDto
    ID: str
    IssueDate: str
    IssueTime: str
    Note: Optional[str] = None
    Discrepancy: DiscrepancyDto
    Billing: BillingDto
    Payment: PaymentDto
    Amounts: AmountsDto
    Lines: List[InvoiceLineDto]
    # OJO, roles invertidos respecto a una venta:
    #   Company  = MI empresa, el adquirente (ABS)
    #   Customer = EL PROVEEDOR, el sujeto no obligado a facturar (SNO)
    Company: CompanyDto
    Customer: CustomerDto
