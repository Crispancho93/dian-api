import os

from pydantic_settings import BaseSettings

# Ruta absoluta al .env de la raíz del proyecto. Si se dejara relativa (".env"),
# pydantic la resolvería contra el directorio actual y la config fallaría al
# ejecutar algo desde otra carpeta (por ejemplo `python create_user.py` parado
# dentro de scripts/).
_ENV_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env"
)

WEB_SERVICE_PRODUCCION = "https://vpfe.dian.gov.co/WcfDianCustomerServices.svc"
WEB_SERVICE_HABILITACION = "https://vpfe-hab.dian.gov.co/WcfDianCustomerServices.svc"


def resolve_web_service(habilitacion: bool = False) -> str:
    """Modo por defecto: producción. Habilitación solo si el request lo pide explícitamente."""
    return WEB_SERVICE_HABILITACION if habilitacion else WEB_SERVICE_PRODUCCION


class Config(BaseSettings):
    PATH_BASE: str
    SIGN_PASSWORD: str
    SIGN_NAME: str
    POLITICA_NAME: str
    ENCRYPTION_KEY: str | None = None
    DATABASE_URL: str | None = None
    # Clave con la que se firma la cookie de sesión del panel web. Si no se
    # configura, se genera una aleatoria al arrancar y las sesiones abiertas se
    # invalidan en cada reinicio.
    SECRET_KEY: str | None = None
    class Config:
        env_file = _ENV_FILE
        env_file_encoding = 'utf-8'
        secrets_dir = None # Desactiva cualquier caché de secretos
