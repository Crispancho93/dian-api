from sqlalchemy import select, insert, update

from domain.dtos.user_dto import UserDto
from domain.entities.user import users
from domain.entities.db import get_connection
from shared.security import hash_password


class CreateUserCase:
    """
    Caso de uso para crear un usuario del panel, o actualizar su contraseña si
    el correo ya existe.
    """

    def __init__(self, name: str, email: str, password: str):
        """
        :param name: Nombre del usuario.
        :param email: Correo del usuario (se normaliza a minúsculas).
        :param password: Contraseña en texto plano.
        """
        self.name = (name or "").strip()
        self.email = (email or "").strip().lower()
        self.password = password or ""

    def execute(self) -> UserDto:
        """
        Crea el usuario o actualiza el existente.

        :returns: :class:`UserDto` del usuario creado o actualizado.
        :raises ValueError: Si falta el correo o la contraseña.
        """
        if not self.email or not self.password:
            raise ValueError("El correo y la contraseña son obligatorios")

        password_hash = hash_password(self.password)

        with get_connection() as conn:
            existing = (
                conn.execute(select(users).where(users.c.email == self.email))
                .mappings()
                .first()
            )

            if existing:
                conn.execute(
                    update(users)
                    .where(users.c.id == existing["id"])
                    .values(
                        name=self.name or existing["name"],
                        password_hash=password_hash,
                        is_active=True,
                    )
                )
                user_id = existing["id"]
                name = self.name or existing["name"]
            else:
                result = conn.execute(
                    insert(users).values(
                        name=self.name or self.email,
                        email=self.email,
                        password_hash=password_hash,
                        is_active=True,
                    )
                )
                user_id = result.inserted_primary_key[0]
                name = self.name or self.email

            # SQLAlchemy 2.0 usa "commit as you go": sin esto no se persiste.
            conn.commit()

        return UserDto(id=user_id, name=name, email=self.email, is_active=True)
