from sqlalchemy import select

from domain.dtos import ClientDto
from domain.entities.client import client
from domain.entities.db import get_connection
from shared.encryption import get_encryption_service


class GetClientByNitCase:
    """Caso de uso para obtener un cliente por su NIT."""

    def __init__(self, resolucion: str):
        """
        :param resolucion: Resolución del cliente a consultar.
        """
        self.resolucion = resolucion

    def execute(self) -> ClientDto:
        """
        Ejecuta la búsqueda del cliente por Resolución.

        :returns: :class:`ClientDto` con la información del cliente.
        :raises LookupError: Si el cliente no existe.
        """
        with get_connection() as conn:
            row = (
                conn.execute(
                    select(client).where(
                        (client.c.resolucion == self.resolucion)
                        & (client.c.is_active.is_(True))
                    )
                )
                .mappings()
                .first()
            )

        if not row:
            raise LookupError("CLIENT_NOT_FOUND")

        decrypted_password = get_encryption_service().decrypt(row["pfx_password"])

        data = dict(row)
        data["pfx_password"] = decrypted_password

        return ClientDto(**data)