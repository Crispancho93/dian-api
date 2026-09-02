import traceback
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.exc import SQLAlchemyError
from application.use_cases.client.get_client_by_nit_case import GetClientByNitCase
from application.use_cases.soap.soap_clave import SoapClave
from domain.dtos import InvoiceDto, CreditNoteDto, DocumentoSoporteDTO, NotaAjusteDocumentoSoporteDTO
from application.use_cases import (
    CreateInvoiceCase,
    CreateNoteCase,
    CreateDocumentoSoporteCase,
    CreateNotaAjusteDocumentoSoporteCase,
)
from shared.certificate import CertificateLoader

router = APIRouter(
    prefix="/api/invoice",
    tags=["invoice"]
)

@router.post("/create_invoice")
def create(
    request: InvoiceDto,
    certificate_loader: CertificateLoader = Depends(lambda: CertificateLoader(GetClientByNitCase))
):
    """
    Crea una factura.

    """
    try:
        create_invoice = CreateInvoiceCase(request, certificate_loader)
        return create_invoice.send()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear la factura: " + str(e))
    
@router.post("/send_test")
def create(
    request: InvoiceDto,
    certificate_loader: CertificateLoader = Depends(lambda: CertificateLoader(GetClientByNitCase))
):
    try:
        create_invoice = CreateInvoiceCase(request, certificate_loader)
        return create_invoice.send_test()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear la factura: " + str(e))

@router.post("/create_credit_note")
def create(
    request: CreditNoteDto,
    certificate_loader: CertificateLoader = Depends(lambda: CertificateLoader(GetClientByNitCase))
):
    """
    Crea una nota crédito.

    """
    try:
        create_note = CreateNoteCase(request, certificate_loader)
        return create_note.start()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear la factura: " + str(e))

@router.post("/create_documento_soporte")
def create_documento_soporte(
    request: DocumentoSoporteDTO,
    certificate_loader: CertificateLoader = Depends(lambda: CertificateLoader(GetClientByNitCase))
):
    """
    Crea un Documento Soporte en adquisiciones a no obligados a facturar.

    """
    try:
        create_doc_soporte = CreateDocumentoSoporteCase(request, certificate_loader)
        return create_doc_soporte.start()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear el documento soporte: " + str(e))

@router.post("/create_nota_ajuste_documento_soporte")
def create_nota_ajuste_documento_soporte(
    request: NotaAjusteDocumentoSoporteDTO,
    certificate_loader: CertificateLoader = Depends(lambda: CertificateLoader(GetClientByNitCase))
):
    """
    Crea una Nota de Ajuste al Documento Soporte (CreditNote tipo 95).

    Corrige o anula un documento soporte ya emitido. El concepto va en
    Discrepancy.ResponseCode (2 = anulación) y el documento corregido se
    referencia en Billing con su número y su CUDS.
    """
    try:
        create_nota_ajuste = CreateNotaAjusteDocumentoSoporteCase(request, certificate_loader)
        return create_nota_ajuste.start()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear la nota de ajuste: " + str(e))

@router.get("/get_clave_tecnica")
def get_clave_tecnica(
        invoice_authorization: str = Query(..., description="Número de la resolución (InvoiceAuthorization)"),
        account_code: str = Query(..., description="Número de identificación tributaria del obligado a Facturar - (NIT) Sin Dígito"),
        account_code_t: str = Query(..., description="Número de identificación tributaria del dueño del Software - (NIT) Sin Dígito"),
        software_code: str = Query(..., description="Número de identificación del software (SoftwareID)"),
        habilitacion: bool = Query(False, description="Si es true, consulta contra el ambiente de habilitación de la DIAN en vez de producción"),
        certificate_loader: CertificateLoader = Depends(lambda: CertificateLoader(GetClientByNitCase))
    ):
    """
    Obtiene la clave técnica (TechnicalKey) del servicio DIAN GetNumberingRange
    utilizando los códigos de cuenta y software proporcionados como query parameters.
    """
    try:
        certificate_loader.load(invoice_authorization)

        soap_client = SoapClave(
            certificate_data=certificate_loader.security,
            account_code=account_code,
            account_code_t=account_code_t,
            software_code=software_code,
            habilitacion=habilitacion
        )
        
        clave_tecnica = soap_client.get_numbering_range()

        return {
            "success": True,
            "clave_tecnica": clave_tecnica
        }

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener la clave técnica: " + str(e))
