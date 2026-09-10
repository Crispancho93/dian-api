from sqlalchemy import Table, Column, Integer, String, Boolean, text

from .db import meta

"""
Definición de la tabla 'client' en la base de datos.

Representa la entidad de clientes, almacenando información básica
y datos asociados al certificado digital (PFX).

:table client: Tabla de clientes.
"""

client = Table(
    "client",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True, doc="Identificador único del cliente."),
    Column("nit", String(50), nullable=False, unique=True, doc="Número de identificación tributaria del cliente."),
    Column("digito", String(2), nullable=False, doc="Digito verificador del cliente."),
    Column("resolucion", String(50), nullable=False, doc="Resolución del cliente."),
    Column("full_name", String(500), nullable=False, doc="Nombre completo del cliente."),
    Column("pfx_password", String(500), nullable=False, doc="Contraseña del certificado PFX (encriptada)."),
    Column("pfx_path", String(500), nullable=False, doc="Ruta del archivo PFX del cliente."),
    Column("is_active", Boolean, nullable=False, server_default=text("TRUE"), doc="Estado del cliente."),
)