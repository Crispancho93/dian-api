from sqlalchemy import select

from domain.dtos import ClientDto
from domain.entities.client import client
from domain.entities.db import get_connection
from shared.encryption import get_encryption_service


class GetClientByNitOnlyCase:
    """Caso de uso para obtener un cliente por su NIT (sin resolución, usado por nómina)."""

    def __init__(self, nit: str):
        """
        :param nit: NIT del cliente a consultar.
        """
        self.nit = nit

    def execute(self) -> ClientDto:
        """
        Ejecuta la búsqueda del cliente por NIT.

        :returns: :class:`ClientDto` con la información del cliente.
        :raises LookupError: Si el cliente no existe.
        """
        with get_connection() as conn:
            row = (
                conn.execute(
                    select(client)
                    .where(
                        (client.c.nit == self.nit)
                        & (client.c.is_active.is_(True))
                    )
                    .order_by(client.c.id)
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
