from sqlalchemy import select, func, or_

from domain.dtos.document_dto import DocumentDto
from domain.entities.document import document
from domain.entities.db import get_connection


class ListDocumentsCase:
    """Caso de uso para listar documentos enviados, con filtros y paginación."""

    # Columnas livianas: el listado no trae el XML crudo de la respuesta, que
    # puede pesar bastante y solo se usa en el detalle.
    _COLUMNS = [
        document.c.id,
        document.c.tipo,
        document.c.numero,
        document.c.cliente_nit,
        document.c.resolucion,
        document.c.identificador,
        document.c.ambiente,
        document.c.estado,
        document.c.mensajes,
        document.c.zip_path,
        document.c.zip_key,
        document.c.created_at,
    ]

    def __init__(
        self,
        cliente_nit: str = None,
        tipo: str = None,
        estado: str = None,
        desde: str = None,
        hasta: str = None,
        buscar: str = None,
        page: int = 1,
        page_size: int = 50,
    ):
        """
        :param cliente_nit: Filtra por NIT del emisor.
        :param tipo: Filtra por tipo de documento (FV, NC, DS, NAS, NI, NIA).
        :param estado: Filtra por estado (ACEPTADO, RECHAZADO, ENVIADO, ERROR).
        :param desde: Fecha inicial (YYYY-MM-DD), inclusive.
        :param hasta: Fecha final (YYYY-MM-DD), inclusive.
        :param buscar: Texto libre: busca en número e identificador (CUFE/CUDS/CUNE).
        :param page: Página, base 1.
        :param page_size: Tamaño de página.
        """
        self.cliente_nit = (cliente_nit or "").strip()
        self.tipo = (tipo or "").strip()
        self.estado = (estado or "").strip()
        self.desde = (desde or "").strip()
        self.hasta = (hasta or "").strip()
        self.buscar = (buscar or "").strip()
        self.page = max(1, int(page or 1))
        self.page_size = max(1, min(int(page_size or 50), 200))

    def _conditions(self):
        conditions = []

        if self.cliente_nit:
            conditions.append(document.c.cliente_nit == self.cliente_nit)
        if self.tipo:
            conditions.append(document.c.tipo == self.tipo)
        if self.estado:
            conditions.append(document.c.estado == self.estado)
        if self.desde:
            conditions.append(func.date(document.c.created_at) >= self.desde)
        if self.hasta:
            conditions.append(func.date(document.c.created_at) <= self.hasta)
        if self.buscar:
            like = f"%{self.buscar}%"
            conditions.append(
                or_(
                    document.c.numero.ilike(like),
                    document.c.identificador.ilike(like),
                )
            )

        return conditions

    def execute(self):
        """
        Ejecuta la consulta.

        :returns: Tupla ``(documentos, total)`` donde ``documentos`` es una
            lista de :class:`DocumentDto` y ``total`` el conteo sin paginar.
        """
        conditions = self._conditions()
        offset = (self.page - 1) * self.page_size

        query = select(*self._COLUMNS)
        count_query = select(func.count()).select_from(document)

        for condition in conditions:
            query = query.where(condition)
            count_query = count_query.where(condition)

        query = (
            query.order_by(document.c.created_at.desc(), document.c.id.desc())
            .limit(self.page_size)
            .offset(offset)
        )

        with get_connection() as conn:
            rows = conn.execute(query).mappings().all()
            total = conn.execute(count_query).scalar() or 0

        return [DocumentDto(**dict(row)) for row in rows], total


class CountDocumentsByStatusCase:
    """Caso de uso para el resumen del tablero: conteo de documentos por estado."""

    def execute(self) -> dict:
        """
        :returns: Diccionario ``{estado: cantidad}``.
        """
        with get_connection() as conn:
            rows = conn.execute(
                select(document.c.estado, func.count().label("total"))
                .group_by(document.c.estado)
            ).mappings().all()

        return {row["estado"]: row["total"] for row in rows}
