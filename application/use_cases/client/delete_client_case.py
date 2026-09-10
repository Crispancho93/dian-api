import os

from sqlalchemy import delete, select
from sqlalchemy.exc import IntegrityError

from domain.entities.client import client
from domain.entities.db import get_connection
from domain.entities.document import document


class DeleteClientCase:
    """Elimina un cliente que no tenga documentos asociados."""

    def __init__(self, client_id: int):
        self.client_id = client_id

    def execute(self):
        with get_connection() as conn:
            client_row = conn.execute(
                select(client.c.nit, client.c.pfx_path).where(client.c.id == self.client_id)
            ).mappings().first()

            if not client_row:
                raise LookupError("CLIENT_NOT_FOUND")

            has_documents = conn.execute(
                select(document.c.id)
                .where(document.c.cliente_nit == client_row["nit"])
                .limit(1)
            ).first()
            if has_documents:
                raise ValueError(
                    "No se puede eliminar el cliente porque tiene documentos asociados"
                )

            try:
                conn.execute(delete(client).where(client.c.id == self.client_id))
                conn.commit()
            except IntegrityError as error:
                conn.rollback()
                raise ValueError(
                    "No se puede eliminar el cliente porque tiene documentos asociados"
                ) from error

        pfx_path = client_row["pfx_path"]
        if pfx_path and os.path.isfile(pfx_path):
            os.remove(pfx_path)