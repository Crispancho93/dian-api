from sqlalchemy import select

from domain.dtos.user_dto import UserDto
from domain.entities.user import users
from domain.entities.db import get_connection
from shared.security import verify_password


class AuthenticateUserCase:
    """Caso de uso para autenticar un usuario del panel web."""

    def __init__(self, email: str, password: str):
        """
        :param email: Correo del usuario.
        :param password: Contraseña en texto plano.
        """
        self.email = (email or "").strip().lower()
        self.password = password or ""

    def execute(self) -> UserDto:
        """
        Valida las credenciales del usuario.

        :returns: :class:`UserDto` del usuario autenticado.
        :raises LookupError: ``INVALID_CREDENTIALS`` si el correo no existe, el
            usuario está inactivo o la contraseña no coincide. Se usa el mismo
            error en los tres casos para no revelar cuáles correos existen.
        """
        with get_connection() as conn:
            row = (
                conn.execute(
                    select(users).where(users.c.email == self.email)
                )
                .mappings()
                .first()
            )

        if not row or not row["is_active"]:
            raise LookupError("INVALID_CREDENTIALS")

        if not verify_password(self.password, row["password_hash"]):
            raise LookupError("INVALID_CREDENTIALS")

        return UserDto(
            id=row["id"],
            name=row["name"],
            email=row["email"],
            is_active=row["is_active"],
        )
