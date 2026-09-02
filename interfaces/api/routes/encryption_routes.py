from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel

from shared.encryption import EncryptionService, get_encryption_service

"""
Controlador de seguridad.

Contiene endpoints relacionados con operaciones de encriptación.
"""

router = APIRouter(
    prefix="/api/security",
    tags=["security"]
)


class EncryptRequest(BaseModel):
    """
    DTO de solicitud para encriptar un valor.

    :param value: Valor en texto plano a encriptar.
    """
    value: str


class EncryptResponse(BaseModel):
    """
    DTO de respuesta para el valor encriptado.

    :param encrypted: Valor encriptado.
    """
    encrypted: str


@router.post("/encrypt", response_model=EncryptResponse)
def encrypt_value(
    request: EncryptRequest,
    encryption_service: EncryptionService = Depends(get_encryption_service)
):
    """
    Encripta un valor proporcionado por el cliente.

    """
    try:
        encrypted = encryption_service.encrypt(request.value)
        return {"encrypted": encrypted}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al encriptar: " + str(e)
        )