import os
import glob

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import pkcs12
from typing import NamedTuple, Type

from application.use_cases.client.get_client_by_nit_case import GetClientByNitCase
from .config import Config

_config = Config()


class CertificateData(NamedTuple):
    """
    Estructura que representa los datos del certificado cargado.

    :param private_key: Llave privada del certificado.
    :param firmante: Certificado del firmante.
    :param emisor: Certificado del emisor.
    :param ca_raiz: Certificado de la autoridad raíz.
    :param politica_file: Archivo de política asociado (si aplica).
    """
    private_key: object
    firmante: object
    emisor: object
    ca_raiz: object
    politica_file: object


class CertificateLoader:
    """
    Servicio para cargar certificados desde un archivo PFX.
    """

    def __init__(self, client_use_case: Type[GetClientByNitCase]):
        """
        :param client_use_case: Clase :class:`GetClientByNitCase`.
        """
        self._client_use_case = client_use_case
        self._security = None

    def load(self, nit: str):
        """
        Carga el certificado asociado a un cliente.

        :param nit: NIT del cliente.
        :raises ValueError: Si el certificado es inválido.
        """
        # Transient: nueva instancia del use case
        client_dto = self._client_use_case(nit).execute()

        pfx_path = client_dto.pfx_path
        pfx_password = client_dto.pfx_password

        if not os.path.exists(pfx_path):
            raise FileNotFoundError(f"PFX no encontrado en la ruta: {pfx_path}")

        with open(pfx_path, "rb") as pfx_file:
            pfx_data = pfx_file.read()

        private_key, firmante, additional_certs = pkcs12.load_key_and_certificates(
            pfx_data,
            pfx_password.encode(),
            default_backend()
        )

        if not firmante:
            raise ValueError("Invalid certificate chain in PFX.")

        # Resuelve la cadena (emisor + raíz) a partir de los certificados
        # embebidos en el .pfx y, como respaldo, de los .crt/.cer/.pem que
        # estén junto al .pfx (misma carpeta) o en la carpeta compartida
        # PATH_BASE/certificados (donde se guardan las cadenas de CA, ya que
        # son las mismas para todos los clientes que comparten entidad
        # certificadora). Así funciona tanto para .pfx que traen la cadena
        # completa como para los que no la traen (ej. certificados GSE que
        # solo incluyen el firmante).
        certs_dirs = [os.path.dirname(pfx_path), os.path.join(_config.PATH_BASE, 'certificados')]
        emisor, ca_raiz = self._resolve_chain(firmante, additional_certs, certs_dirs)

        self._security = CertificateData(
            private_key=private_key,
            firmante=firmante,
            emisor=emisor,
            ca_raiz=ca_raiz,
            politica_file=''
        )

    def _resolve_chain(self, firmante, additional_certs, certs_dirs):
        # Junta los certificados disponibles indexados por su subject.
        pool = {}
        for cert in (additional_certs or []):
            pool[cert.subject.rfc4514_string()] = cert
        for certs_dir in certs_dirs:
            for cert in self._load_ca_files(certs_dir):
                pool.setdefault(cert.subject.rfc4514_string(), cert)

        # El emisor es el certificado cuyo subject coincide con el issuer del
        # firmante; la raíz es el emisor del emisor.
        emisor = pool.get(firmante.issuer.rfc4514_string())
        if emisor is None:
            raise ValueError(
                "No se encontró el certificado EMISOR (intermedio) de la cadena. "
                f"El firmante fue emitido por: {firmante.issuer.rfc4514_string()}. "
                "El .pfx no lo trae embebido; coloque el certificado del emisor "
                f"(.crt/.cer/.pem) en alguna de estas carpetas: {certs_dirs}"
            )

        ca_raiz = pool.get(emisor.issuer.rfc4514_string())
        if ca_raiz is None:
            raise ValueError(
                "No se encontró el certificado RAÍZ de la cadena. "
                f"El emisor fue emitido por: {emisor.issuer.rfc4514_string()}. "
                f"Coloque el certificado raíz (.crt/.cer/.pem) en alguna de estas carpetas: {certs_dirs}"
            )

        return emisor, ca_raiz

    def _load_ca_files(self, certs_dir: str):
        certs = []
        if not os.path.isdir(certs_dir):
            return certs
        for pattern in ('*.crt', '*.cer', '*.pem'):
            for file_path in glob.glob(os.path.join(certs_dir, pattern)):
                try:
                    with open(file_path, 'rb') as f:
                        raw = f.read()
                    try:
                        certs.append(x509.load_pem_x509_certificate(raw, default_backend()))
                    except ValueError:
                        certs.append(x509.load_der_x509_certificate(raw, default_backend()))
                except Exception:
                    # Ignora archivos que no sean certificados válidos.
                    continue
        return certs

    @property
    def security(self) -> CertificateData:
        """
        Obtiene la información del certificado cargado.

        :returns: :class:`CertificateData`
        :raises ValueError: Si no se ha cargado el certificado.
        """
        if not self._security:
            raise ValueError("Certificate data has not been loaded.")
        return self._security


# Instancia (inyección manual tipo transient-friendly)
certificate_loader = CertificateLoader(GetClientByNitCase)