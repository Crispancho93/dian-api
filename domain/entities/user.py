from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, text, func

from .db import meta

"""
Definición de la tabla 'users' en la base de datos.

Representa los usuarios del panel web administrativo. No tiene relación con
la tabla 'client': cualquier usuario activo ve todos los clientes y documentos.

:table users: Tabla de usuarios del panel.
"""

users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True, doc="Identificador único del usuario."),
    Column("name", String(75), nullable=False, doc="Nombre del usuario."),
    Column("email", String(100), nullable=False, unique=True, doc="Correo del usuario, usado para el login."),
    Column("password_hash", String(255), nullable=False, doc="Hash scrypt de la contraseña."),
    Column("is_active", Boolean, nullable=False, server_default=text("TRUE"), doc="Estado del usuario."),
    Column("created_at", DateTime, nullable=False, server_default=func.now(), doc="Fecha de creación."),
)
