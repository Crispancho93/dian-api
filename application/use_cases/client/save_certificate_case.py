import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import pkcs12
from sqlalchemy import update

from domain.dtos.client_dto import ClientAdminDto
from domain.entities.client import client
from domain.entities.db import get_connection
from shared.config import Config
from shared.encryption import get_encryption_service

from .list_clients_case import GetClientCase

_config = Config()


class SaveCertificateCase:
    """
    Caso de uso para cargar el certificado (.pfx) de un cliente y su clave.

    El archivo se guarda dentro de ``PATH_BASE`` (el volumen que ya está
    montado en el deploy) y la clave se guarda encriptada con el mismo
    servicio Fernet que usa el resto de la aplicación, de modo que
    ``CertificateLoader`` pueda leerla sin cambios.
    """

    # Subcarpeta, dentro de PATH_BASE/<nit>/, donde se guarda el .pfx.
    CERTIFICATE_DIR = 'certificado'

    def __init__(self, client_id: int, file_name: str, file_content: bytes, password: str):
        """
        :param client_id: Identificador del cliente.
        :param file_name: Nombre original del archivo subido.
        :param file_content: Contenido binario del .pfx.
        :param password: Clave del certificado, en texto plano.
        """
        self.client_id = client_id
        self.file_name = os.path.basename(file_name or "")
        self.file_content = file_content
        self.password = password or ""

    def execute(self) -> ClientAdminDto:
        """
        Valida y guarda el certificado.

        :returns: :class:`ClientAdminDto` del cliente actualizado.
        :raises LookupError: ``CLIENT_NOT_FOUND`` si el cliente no existe.
        :raises ValueError: Si el archivo no es un PFX válido o la clave no
            corresponde. En ese caso no se escribe nada: ni el archivo ni la
            base de datos se modifican.
        """
        client_dto = GetClientCase(self.client_id).execute()

        if not self.file_content:
            raise ValueError("No se recibió ningún archivo de certificado")

        if not self.password:
            raise ValueError("La clave del certificado es obligatoria")

        self._validate(self.file_content, self.password)

        pfx_path = self._store_file(client_dto.nit)
        encrypted_password = get_encryption_service().encrypt(self.password)

        with get_connection() as conn:
            conn.execute(
                update(client)
                .where(client.c.id == self.client_id)
                .values(pfx_path=pfx_path, pfx_password=encrypted_password)
            )
            conn.commit()

        return GetClientCase(self.client_id).execute()

    @staticmethod
    def _validate(content: bytes, password: str):
        """
        Comprueba que el archivo sea un PKCS#12 legible con esa clave.

        Es la misma carga que hace :class:`CertificateLoader` al firmar, así que
        si pasa acá, va a poder firmar después.

        :raises ValueError: Si el archivo o la clave son inválidos.
        """
        try:
            _, firmante, _ = pkcs12.load_key_and_certificates(
                content, password.encode(), default_backend()
            )
        except Exception:
            raise ValueError(
                "No se pudo abrir el certificado: verifique que el archivo sea un .pfx "
                "válido y que la clave sea la correcta."
            )

        if not firmante:
            raise ValueError("El certificado no contiene un firmante válido.")

    def _store_file(self, nit: str) -> str:
        """
        Guarda el .pfx en ``PATH_BASE/<nit>/certificado/``.

        Esa ubicación es compatible con la resolución de la cadena CA que hace
        ``CertificateLoader``, que busca los .crt/.cer/.pem en la carpeta del
        .pfx y en ``PATH_BASE/certificados``.

        :returns: Ruta absoluta del archivo guardado.
        """
        file_name = self.file_name or f"{nit}.pfx"
        target_dir = os.path.join(_config.PATH_BASE, nit, self.CERTIFICATE_DIR)
        os.makedirs(target_dir, exist_ok=True)

        pfx_path = os.path.join(target_dir, file_name)
        with open(pfx_path, "wb") as pfx_file:
            pfx_file.write(self.file_content)

        return pfx_path
