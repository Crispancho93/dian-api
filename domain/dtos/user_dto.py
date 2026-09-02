from pydantic import BaseModel


class UserDto(BaseModel):
    """
    DTO que representa un usuario del panel web.

    Nunca transporta el hash de la contraseña: solo los datos que la interfaz
    necesita mostrar.

    :param id: Identificador único del usuario.
    :param name: Nombre del usuario.
    :param email: Correo del usuario, usado para el login.
    :param is_active: Estado del usuario.
    """

    id: int
    name: str
    email: str
    is_active: bool = True
