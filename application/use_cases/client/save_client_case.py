from sqlalchemy import select, insert, update

from domain.dtos.client_dto import ClientAdminDto
from domain.entities.client import client
from domain.entities.db import get_connection

from .list_clients_case import GetClientCase


class SaveClientCase:
    """
    Caso de uso para crear o actualizar un cliente desde el panel.

    No toca el certificado: ``pfx_path`` y ``pfx_password`` los administra
    :class:`SaveCertificateCase`. Así, editar la razón social de un cliente no
    puede dejarlo sin certificado por accidente.
    """

    def __init__(
        self,
        nit: str,
        digito: str,
        resolucion: str,
        full_name: str,
        is_active: bool = True,
        client_id: int = None,
    ):
        """
        :param nit: NIT del cliente.
        :param digito: Dígito de verificación.
        :param resolucion: Resolución de facturación (única por cliente).
        :param full_name: Razón social.
        :param is_active: Estado del cliente.
        :param client_id: Id del cliente a actualizar. Si es None, se crea uno nuevo.
        """
        self.nit = (nit or "").strip()
        self.digito = (digito or "").strip()
        self.resolucion = (resolucion or "").strip()
        self.full_name = (full_name or "").strip()
        self.is_active = bool(is_active)
        self.client_id = client_id

    def execute(self) -> ClientAdminDto:
        """
        :returns: :class:`ClientAdminDto` del cliente creado o actualizado.
        :raises ValueError: Si faltan campos obligatorios o la resolución ya
            está usada por otro cliente.
        """
        if not self.nit or not self.resolucion or not self.full_name:
            raise ValueError("El NIT, la resolución y la razón social son obligatorios")

        values = {
            "nit": self.nit,
            "digito": self.digito,
            "resolucion": self.resolucion,
            "full_name": self.full_name,
            "is_active": self.is_active,
        }

        with get_connection() as conn:
            # La resolución tiene índice único: se valida antes para devolver un
            # mensaje claro en vez de un error de integridad de la base.
            duplicate_query = select(client.c.id).where(client.c.resolucion == self.resolucion)
            if self.client_id:
                duplicate_query = duplicate_query.where(client.c.id != self.client_id)

            if conn.execute(duplicate_query).first():
                raise ValueError(f"Ya existe otro cliente con la resolución {self.resolucion}")

            if self.client_id:
                result = conn.execute(
                    update(client).where(client.c.id == self.client_id).values(**values)
                )
                if result.rowcount == 0:
                    raise LookupError("CLIENT_NOT_FOUND")
                client_id = self.client_id
            else:
                # pfx_path y pfx_password son NOT NULL en la tabla: se crean
                # vacíos y se llenan al cargar el certificado.
                values.update({"pfx_path": "", "pfx_password": ""})
                result = conn.execute(insert(client).values(**values))
                client_id = result.inserted_primary_key[0]

            conn.commit()

        return GetClientCase(client_id).execute()
