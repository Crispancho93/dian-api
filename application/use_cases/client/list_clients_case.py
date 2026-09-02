from sqlalchemy import select

from domain.dtos.client_dto import ClientAdminDto
from domain.entities.client import client
from domain.entities.db import get_connection

# Columnas expuestas al panel: nunca se lee pfx_password.
_COLUMNS = [
    client.c.id,
    client.c.nit,
    client.c.digito,
    client.c.resolucion,
    client.c.full_name,
    client.c.pfx_path,
    client.c.is_active,
]


class ListClientsCase:
    """Caso de uso para listar los clientes del panel administrativo."""

    def __init__(self, buscar: str = None):
        """
        :param buscar: Texto libre: busca por NIT, razón social o resolución.
        """
        self.buscar = (buscar or "").strip()

    def execute(self):
        """
        :returns: Lista de :class:`ClientAdminDto`, ordenada por razón social.
        """
        query = select(*_COLUMNS)

        if self.buscar:
            like = f"%{self.buscar}%"
            query = query.where(
                client.c.nit.ilike(like)
                | client.c.full_name.ilike(like)
                | client.c.resolucion.ilike(like)
            )

        query = query.order_by(client.c.full_name)

        with get_connection() as conn:
            rows = conn.execute(query).mappings().all()

        return [ClientAdminDto(**dict(row)) for row in rows]


class GetClientCase:
    """Caso de uso para obtener un cliente por su id, para el panel."""

    def __init__(self, client_id: int):
        """
        :param client_id: Identificador del cliente.
        """
        self.client_id = client_id

    def execute(self) -> ClientAdminDto:
        """
        :returns: :class:`ClientAdminDto` del cliente.
        :raises LookupError: ``CLIENT_NOT_FOUND`` si no existe.
        """
        with get_connection() as conn:
            row = (
                conn.execute(select(*_COLUMNS).where(client.c.id == self.client_id))
                .mappings()
                .first()
            )

        if not row:
            raise LookupError("CLIENT_NOT_FOUND")

        return ClientAdminDto(**dict(row))
