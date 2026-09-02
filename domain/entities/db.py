import os
from contextlib import contextmanager
from sqlalchemy import create_engine, MetaData

from shared.config import Config as AppConfig

"""
Configuración de conexión a la base de datos.

Se obtiene la cadena de conexión desde:
1. Variable de entorno DATABASE_URL
2. Configuración de la aplicación
3. Valor por defecto (fallback)
"""

_default_database_url = "mysql+pymysql://root:password@localhost:3306/database_name"
_env_database_url = os.getenv("DATABASE_URL")

if _env_database_url:
    DATABASE_URL = _env_database_url
else:
    DATABASE_URL = AppConfig().DATABASE_URL or _default_database_url

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

"""
Objeto metadata de SQLAlchemy.

Se utiliza para registrar las tablas del modelo y gestionar su creación.
"""
meta = MetaData()


@contextmanager
def get_connection():
    """
    Proporciona una conexión a la base de datos.

    Utiliza un context manager para garantizar la correcta apertura
    y cierre de la conexión.

    :yields: Conexión activa de SQLAlchemy.
    """
    with engine.connect() as conn:
        yield conn