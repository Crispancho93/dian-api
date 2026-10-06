import smtplib
import ssl
from email.message import EmailMessage

from email_validator import EmailNotValidError, validate_email

from shared.config import Config


class SendClientEmailCase:
    """Envía un correo al destinatario indicado usando el SMTP configurado."""

    def __init__(self, recipient: str | list[str], subject: str, body: str):
        recipients = [recipient] if isinstance(recipient, str) else recipient
        self.recipients = [address.strip() for address in recipients if address.strip()]
        self.subject = (subject or "").strip()
        self.body = (body or "").strip()

    def execute(self) -> None:
        if not self.recipients or not self.subject or not self.body:
            raise ValueError("El destinatario, el asunto y el mensaje son obligatorios.")
        if len(self.subject) > 200:
            raise ValueError("El asunto no puede superar 200 caracteres.")
        if len(self.body) > 15000:
            raise ValueError("El mensaje no puede superar 15.000 caracteres.")

        config = Config()
        if not config.SMTP_HOST:
            raise ValueError("Falta configurar SMTP_HOST en el archivo .env.")
        if not config.SMTP_FROM_EMAIL:
            raise ValueError("Falta configurar SMTP_FROM_EMAIL en el archivo .env.")
        if config.SMTP_USE_SSL and config.SMTP_STARTTLS:
            raise ValueError(
                "SMTP_USE_SSL y SMTP_STARTTLS no pueden estar activos al mismo tiempo."
            )
        if bool(config.SMTP_USERNAME) != bool(config.SMTP_PASSWORD):
            raise ValueError(
                "Configure SMTP_USERNAME y SMTP_PASSWORD juntos en el archivo .env."
            )

        recipients = list(dict.fromkeys(
            self._normalize_email(address) for address in self.recipients
        ))
        if "\r" in self.subject or "\n" in self.subject:
            raise ValueError("El asunto no puede contener saltos de línea.")
        sender = self._normalize_email(config.SMTP_FROM_EMAIL)

        message = EmailMessage()
        message["From"] = sender
        message["To"] = recipients[0] if len(recipients) == 1 else "undisclosed-recipients:;"
        message["Subject"] = self.subject
        message.set_content(self.body)

        context = ssl.create_default_context()
        if config.SMTP_USE_SSL:
            smtp = smtplib.SMTP_SSL(
                config.SMTP_HOST, config.SMTP_PORT, timeout=30, context=context
            )
        else:
            smtp = smtplib.SMTP(config.SMTP_HOST, config.SMTP_PORT, timeout=30)

        with smtp as server:
            if config.SMTP_STARTTLS and not config.SMTP_USE_SSL:
                server.starttls(context=context)
                server.ehlo()
            if config.SMTP_USERNAME and config.SMTP_PASSWORD:
                server.login(config.SMTP_USERNAME, config.SMTP_PASSWORD)
            server.send_message(message, to_addrs=recipients)

    @staticmethod
    def _normalize_email(address: str) -> str:
        try:
            return validate_email(address, check_deliverability=False).normalized
        except EmailNotValidError as error:
            raise ValueError("El correo destinatario o remitente no es válido.") from error
