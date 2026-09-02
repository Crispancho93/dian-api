from fastapi import APIRouter, Depends, HTTPException, status
from application.use_cases.client.get_client_by_nit_only_case import GetClientByNitOnlyCase
from domain.dtos import PayrollDto, PayrollAdjustmentDto
from application.use_cases import CreatePayrollCase, CreatePayrollAdjustmentCase
from shared.certificate import CertificateLoader

router = APIRouter(
    prefix="/api/payroll",
    tags=["payroll"]
)

@router.post("/create_payroll")
def create(
    request: PayrollDto,
    certificate_loader: CertificateLoader = Depends(lambda: CertificateLoader(GetClientByNitOnlyCase))
):
    """
    Crea y envía un Documento Soporte de Pago de Nómina Electrónica.

    """
    try:
        create_payroll = CreatePayrollCase(request, certificate_loader)
        return create_payroll.start()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear la nómina: " + str(e))


@router.post("/create_payroll_adjustment")
def create_adjustment(
    request: PayrollAdjustmentDto,
    certificate_loader: CertificateLoader = Depends(lambda: CertificateLoader(GetClientByNitOnlyCase))
):
    """
    Crea y envía una Nota de Ajuste de Nómina Electrónica.

    TipoNota: "1" = Reemplazar (cuerpo completo), "2" = Eliminar (reducido).
    """
    try:
        create_adjustment = CreatePayrollAdjustmentCase(request, certificate_loader)
        return create_adjustment.start()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al crear la nota de ajuste: " + str(e))
