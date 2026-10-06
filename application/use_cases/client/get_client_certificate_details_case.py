from cryptography.hazmat.backends import default_backend
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives.serialization import pkcs12
from sqlalchemy import select

from domain.dtos.client_dto import ClientAdminDto
from domain.entities.client import client
from domain.entities.db import get_connection
from shared.encryption import get_encryption_service


class GetClientCertificateDetailsCase:
    """Obtiene los datos del cliente y el titular/vencimiento de su certificado."""

    def __init__(self, client_id: int):
        self.client_id = client_id

    def execute(self) -> ClientAdminDto:
        columns = (
            client.c.id,
            client.c.nit,
            client.c.digito,
            client.c.resolucion,
            client.c.full_name,
            client.c.pfx_path,
            client.c.pfx_password,
            client.c.is_active,
            client.c.created_at,
        )
        with get_connection() as conn:
            row = (
                conn.execute(
                    select(*columns).where(client.c.id == self.client_id)
                )
                .mappings()
                .first()
            )

        if not row:
            raise LookupError("CLIENT_NOT_FOUND")

        data = dict(row)
        encrypted_password = data.pop("pfx_password")
        data["fecha_vencimiento_certificado"] = None
        data["nombre_certificado"] = None

        if data["pfx_path"]:
            with open(data["pfx_path"], "rb") as pfx_file:
                _, certificate, _ = pkcs12.load_key_and_certificates(
                    pfx_file.read(),
                    get_encryption_service().decrypt(encrypted_password).encode(),
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

        return ClientAdminDto(**data)
