from cryptography.hazmat.backends import default_backend
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives.serialization import pkcs12
from sqlalchemy import select

from domain.dtos.client_dto import ClientAdminDto
from domain.entities.client import client
from domain.entities.db import get_connection
from shared.encryption import get_encryption_service

# Columnas públicas del cliente; la clave se añade por separado solo al listado.
_COLUMNS = [
    client.c.id,
    client.c.nit,
    client.c.digito,
    client.c.resolucion,
    client.c.full_name,
    client.c.pfx_path,
    client.c.is_active,
    client.c.created_at,
]
_LIST_COLUMNS = [*_COLUMNS, client.c.pfx_password]


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
        query = select(*_LIST_COLUMNS)

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

        encryption = None
        clients = []
        for row in rows:
            data = dict(row)
            encrypted_password = data.pop("pfx_password")
            data["fecha_vencimiento_certificado"] = None
            data["nombre_certificado"] = None

            if data["pfx_path"]:
                if encryption is None:
                    encryption = get_encryption_service()
                with open(data["pfx_path"], "rb") as pfx_file:
                    _, certificate, _ = pkcs12.load_key_and_certificates(
                        pfx_file.read(),
                        encryption.decrypt(encrypted_password).encode(),
                        default_backend(),
                    )
                if certificate:
                    data["fecha_vencimiento_certificado"] = (
                        certificate.not_valid_after_utc.date()
                    )
                    common_names = certificate.subject.get_attributes_for_oid(
                        NameOID.COMMON_NAME
                    )
                    if common_names:
                        data["nombre_certificado"] = common_names[0].value

            clients.append(ClientAdminDto(**data))

        return clients


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
