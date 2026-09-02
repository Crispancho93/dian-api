from sqlalchemy import select

from domain.dtos.document_dto import DocumentDto
from domain.entities.document import document
from domain.entities.db import get_connection


class GetDocumentCase:
    """Caso de uso para obtener un documento enviado por su id."""

    def __init__(self, document_id: int):
        """
        :param document_id: Identificador del registro.
        """
        self.document_id = document_id

    def execute(self) -> DocumentDto:
        """
        :returns: :class:`DocumentDto` con el detalle completo, incluida la
            respuesta cruda de la DIAN.
        :raises LookupError: ``DOCUMENT_NOT_FOUND`` si no existe.
        """
        with get_connection() as conn:
            row = (
                conn.execute(select(document).where(document.c.id == self.document_id))
                .mappings()
                .first()
            )

        if not row:
            raise LookupError("DOCUMENT_NOT_FOUND")

        return DocumentDto(**dict(row))
