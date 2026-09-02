from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class DocumentDto(BaseModel):
    """
    DTO que representa un documento enviado a la DIAN.

    :param id: Identificador único del registro.
    :param tipo: Tipo de documento (FV, NC, DS, NAS, NI, NIA).
    :param numero: Número del documento.
    :param cliente_nit: NIT del emisor.
    :param resolucion: Resolución del emisor (nulo en nómina).
    :param identificador: CUFE / CUDE / CUDS / CUNE.
    :param ambiente: Ambiente DIAN (1 producción, 2 habilitación).
    :param estado: ACEPTADO, RECHAZADO, ENVIADO o ERROR.
    :param mensajes: Mensajes devueltos por la DIAN.
    :param respuesta_dian: XML crudo de la respuesta.
    :param zip_path: Ruta del .zip enviado.
    :param zip_key: ZipKey de envíos asíncronos.
    :param created_at: Fecha del envío.
    """

    id: int
    tipo: str
    numero: str
    cliente_nit: str
    resolucion: Optional[str] = None
    identificador: Optional[str] = None
    ambiente: str
    estado: str
    mensajes: Optional[str] = None
    respuesta_dian: Optional[str] = None
    zip_path: Optional[str] = None
    zip_key: Optional[str] = None
    created_at: Optional[datetime] = None

    @property
    def ambiente_nombre(self) -> str:
        """Nombre legible del ambiente DIAN."""
        return "Habilitación" if self.ambiente == "2" else "Producción"
