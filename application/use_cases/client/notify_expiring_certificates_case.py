import logging
import time
from datetime import datetime, timedelta, timezone

from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.fernet import InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.x509.oid import NameOID
from sqlalchemy import select

from domain.entities.client import client
from domain.entities.db import get_connection
from shared.config import Config
from shared.encryption import get_encryption_service

from .send_client_email_case import SendClientEmailCase

logger = logging.getLogger(__name__)
COLOMBIA_TIMEZONE = timezone(timedelta(hours=-5), name="America/Bogota")
EXPIRY_WARNING_DAYS = 30
EMAIL_SEND_INTERVAL_SECONDS = 5


class NotifyExpiringCertificatesCase:
    """Envía una alerta por cada certificado vencido o próximo a vencer."""

    def execute(self) -> int:
        config = Config()
        recipients = [
            address.strip()
            for address in (config.CERTIFICATE_ALERT_RECIPIENTS or "").split(",")
            if address.strip()
        ]
        if not recipients:
            raise ValueError(
                "Configure CERTIFICATE_ALERT_RECIPIENTS con los destinatarios "
                "de las alertas de certificados."
            )

        with get_connection() as conn:
            rows = conn.execute(
                select(
                    client.c.id,
                    client.c.nit,
                    client.c.digito,
                    client.c.resolucion,
                    client.c.full_name,
                    client.c.pfx_path,
                    client.c.pfx_password,
                    client.c.is_active,
                    client.c.created_at,
                ).where(client.c.pfx_path != "")
            ).mappings().all()

        today = datetime.now(COLOMBIA_TIMEZONE).date()
        encryption = get_encryption_service()
        sent = 0

        for row in rows:
            try:
                with open(row["pfx_path"], "rb") as pfx_file:
                    _, certificate, _ = pkcs12.load_key_and_certificates(
                        pfx_file.read(),
                        encryption.decrypt(row["pfx_password"]).encode(),
                        default_backend(),
                    )
            except (OSError, ValueError, UnsupportedAlgorithm, InvalidToken) as error:
                logger.exception(
                    "No se pudo leer el certificado del cliente %s (id %s): %s",
                    row["full_name"],
                    row["id"],
                    error,
                )
                continue

            if certificate is None:
                logger.error(
                    "El PFX del cliente %s (id %s) no contiene certificado firmante",
                    row["full_name"],
                    row["id"],
                )
                continue

            expiry_date = certificate.not_valid_after_utc.date()
            days_remaining = (expiry_date - today).days
            if days_remaining > EXPIRY_WARNING_DAYS:
                continue

            if sent:
                logger.info(
                    "Esperando %s segundos antes del siguiente correo de alerta",
                    EMAIL_SEND_INTERVAL_SECONDS,
                )
                time.sleep(EMAIL_SEND_INTERVAL_SECONDS)

            common_names = certificate.subject.get_attributes_for_oid(
                NameOID.COMMON_NAME
            )
            certificate_holder = (
                common_names[0].value if common_names else "No disponible"
            )
            nit = row["nit"] + (f"-{row['digito']}" if row["digito"] else "")
            status = (
                f"VENCIDO hace {abs(days_remaining)} día(s)"
                if days_remaining < 0
                else "VENCE HOY"
                if days_remaining == 0
                else f"Vence en {days_remaining} día(s)"
            )
            created_at = (
                row["created_at"].strftime("%d/%m/%Y")
                if row["created_at"]
                else "No disponible"
            )
            subject = (
                f"Alerta certificado {status}: {row['full_name']} ({nit})"
            )
            body = (
                "Alerta automática de vencimiento de certificado\n\n"
                f"Estado: {status}\n"
                f"Razón social: {row['full_name']}\n"
                f"NIT: {nit}\n"
                f"Resolución: {row['resolucion']}\n"
                f"Titular del certificado: {certificate_holder}\n"
                f"Fecha de vencimiento: {expiry_date.strftime('%d/%m/%Y')}\n"
                f"Fecha de creación del cliente: {created_at}\n"
                f"Cliente activo: {'Sí' if row['is_active'] else 'No'}\n\n"
                "Esta revisión automática se ejecuta tres veces al día."
            )
            SendClientEmailCase(
                recipient=recipients,
                subject=subject,
                body=body,
            ).execute()
            sent += 1
            logger.info(
                "Alerta de vencimiento enviada para el cliente %s (id %s)",
                row["full_name"],
                row["id"],
            )

        logger.info(
            "Revisión de certificados terminada: %s revisados, %s alertas enviadas",
            len(rows),
            sent,
        )
        return sent
