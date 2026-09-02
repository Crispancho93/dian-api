from typing import Optional

from pydantic import BaseModel


class ClientAdminDto(BaseModel):
    """
    DTO de cliente para el panel administrativo.

    A diferencia de :class:`ClientDto`, incluye los campos de administración
    (resolución, dígito, estado) y **nunca** transporta la contraseña del
    certificado, ni encriptada ni en texto plano.

    :param id: Identificador único del cliente.
    :param nit: NIT del cliente.
    :param digito: Dígito de verificación.
    :param resolucion: Resolución de facturación.
    :param full_name: Razón social.
    :param pfx_path: Ruta del archivo PFX asociado.
    :param is_active: Estado del cliente.
    """

    id: int
    nit: str
    digito: str
    resolucion: str
    full_name: str
    pfx_path: Optional[str] = None
    is_active: bool = True

    @property
    def tiene_certificado(self) -> bool:
        """True si el cliente ya tiene un certificado cargado."""
        return bool(self.pfx_path)


class ClientDto(BaseModel):
    """
    DTO que representa la información de un cliente.

    :param id: Identificador único del cliente.
    :param nit: Número de identificación tributaria del cliente.
    :param full_name: Nombre completo del cliente.
    :param pfx_password: Contraseña del certificado (desencriptada).
    :param pfx_path: Ruta del archivo PFX asociado al cliente.
    """

    id: int
    nit: str
    full_name: str
    pfx_password: str
    pfx_path: str