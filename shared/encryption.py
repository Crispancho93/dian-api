from cryptography.fernet import Fernet

from .config import Config


class EncryptionService:
    """
    Servicio de encriptación y desencriptación de valores.

    Utiliza el algoritmo Fernet para garantizar confidencialidad
    y seguridad en los datos.
    """

    def __init__(self, encryption_key: str):
        """
        :param encryption_key: Clave utilizada para encriptar y desencriptar valores.
        """
        self._fernet = Fernet(encryption_key)

    def encrypt(self, value: str) -> str:
        """
        Encripta un valor en texto plano.

        :param value: Texto plano a encriptar.
        :returns: Cadena encriptada.
        """
        return self._fernet.encrypt(value.encode("utf-8")).decode("utf-8")

    def decrypt(self, token: str) -> str:
        """
        Desencripta un valor previamente encriptado.

        :param token: Cadena encriptada.
        :returns: Texto plano desencriptado.
        """
        return self._fernet.decrypt(token.encode("utf-8")).decode("utf-8")


def get_encryption_service() -> EncryptionService:
    """
    Obtiene una nueva instancia de :class:`EncryptionService`.

    :returns: :class:`EncryptionService` configurado con la clave de encriptación.
    :raises ValueError: Si la clave de encriptación no está configurada.
    """
    config = Config()

    if not config.ENCRYPTION_KEY:
        raise ValueError("ENCRYPTION_KEY no está configurada")

    return EncryptionService(config.ENCRYPTION_KEY)