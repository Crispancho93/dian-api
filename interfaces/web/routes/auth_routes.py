from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse

from application.use_cases.auth.authenticate_user_case import AuthenticateUserCase
from ..deps import login_user, logout_user
from ..templating import render

router = APIRouter(tags=["web"])


@router.get("/login")
def login_form(request: Request, next: str = "/"):
    """Muestra el formulario de inicio de sesión."""
    if request.session.get("user"):
        return RedirectResponse(url=next or "/", status_code=303)

    return render(request, "login.html", {"next_url": next or "/"})


@router.post("/login")
def login_submit(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    next: str = Form("/"),
):
    """Valida las credenciales e inicia la sesión."""
    try:
        user = AuthenticateUserCase(email=email, password=password).execute()
    except LookupError:
        return render(
            request,
            "login.html",
            {
                "error": "Correo o contraseña incorrectos.",
                "email": email,
                "next_url": next or "/",
            },
            status_code=401,
        )
    except Exception as e:
        return render(
            request,
            "login.html",
            {
                "error": f"No se pudo validar el ingreso: {e}",
                "email": email,
                "next_url": next or "/",
            },
            status_code=500,
        )

    login_user(request, user)
    return RedirectResponse(url=next or "/", status_code=303)


@router.get("/logout")
def logout(request: Request):
    """Cierra la sesión y vuelve al login."""
    logout_user(request)
    return RedirectResponse(url="/login", status_code=303)
