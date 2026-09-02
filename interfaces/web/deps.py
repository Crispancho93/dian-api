from fastapi import Request, HTTPException, status

"""
Dependencias compartidas del panel web.

La sesión se guarda en una cookie firmada (SessionMiddleware). Estas
dependencias aplican **solo a las rutas web**: los endpoints /api/* siguen
siendo públicos, porque los consume la integración con Odoo.
"""

SESSION_USER_KEY = "user"


class RedirectToLogin(HTTPException):
    """
    Señal de que hace falta iniciar sesión.

    Se maneja con un exception handler en `app.py` que redirige a /login, en vez
    de devolver un 401 crudo que el navegador mostraría como error.
    """

    def __init__(self, next_url: str = "/"):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED)
        self.next_url = next_url


def require_login(request: Request) -> dict:
    """
    Exige una sesión activa.

    :param request: Request de FastAPI.
    :returns: Diccionario con los datos del usuario en sesión.
    :raises RedirectToLogin: Si no hay sesión iniciada.
    """
    user = request.session.get(SESSION_USER_KEY)

    if not user:
        raise RedirectToLogin(next_url=str(request.url.path))

    return user


def login_user(request: Request, user):
    """
    Guarda el usuario en la sesión.

    :param request: Request de FastAPI.
    :param user: :class:`UserDto` autenticado.
    """
    request.session[SESSION_USER_KEY] = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
    }


def logout_user(request: Request):
    """Cierra la sesión del usuario."""
    request.session.pop(SESSION_USER_KEY, None)
