import logging
import asyncio
import secrets
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

from interfaces.api import invoice_routes, encryption_routes, payroll_routes
from interfaces.web import auth_routes, dashboard_routes, document_routes, client_routes
from interfaces.web.deps import RedirectToLogin
from interfaces.web.templating import static_dir
from shared import templates_loader
from shared.config import Config

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger("fastapi_app")

_config = Config()


async def load_templates():
    templates_loader.load()
    _logger.info("Plantillas cargadas.")

async def loads():
    """Ejecuta las cargas en paralelo."""
    await asyncio.gather(load_templates())
    _logger.info("Todas las tareas de carga completadas.")

@asynccontextmanager
async def lifespan(app: FastAPI):
    _logger.info("Iniciando carga de archivos en segundo plano...")
    # Ejecutar cargas en segundo plano sin bloquear
    asyncio.create_task(loads())
    yield

app = FastAPI(lifespan=lifespan)

# Sesión del panel web (cookie firmada). Si no hay SECRET_KEY configurada se usa
# una aleatoria: la app arranca igual, pero las sesiones se pierden al reiniciar.
_secret_key = _config.SECRET_KEY
if not _secret_key:
    _secret_key = secrets.token_urlsafe(48)
    _logger.warning(
        "SECRET_KEY no está configurada: se generó una temporal. "
        "Las sesiones del panel se cerrarán en cada reinicio."
    )

app.add_middleware(SessionMiddleware, secret_key=_secret_key, same_site="lax")

app.mount("/static", StaticFiles(directory=static_dir()), name="static")

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    missing_fields = []

    for error in exc.errors():
        loc = error.get("loc", [])
        if loc:
            # Convertimos la ubicación a un formato padre.hijo.hijo
            field_path = ".".join(str(part) for part in loc if isinstance(part, str))
            missing_fields.append(field_path)

    return JSONResponse(
        status_code=400,
        content={"missing_fields": missing_fields},
    )

@app.exception_handler(RedirectToLogin)
async def redirect_to_login_handler(request: Request, exc: RedirectToLogin):
    """Manda al login en vez de devolver un 401 crudo al navegador."""
    return RedirectResponse(url=f"/login?next={exc.next_url}", status_code=303)

# API JSON. Sin autenticación: la consume la integración con Odoo.
app.include_router(invoice_routes.router)
app.include_router(encryption_routes.router)
app.include_router(payroll_routes.router)

# Panel web. Protegido por sesión (ver interfaces/web/deps.py).
app.include_router(auth_routes.router)
app.include_router(dashboard_routes.router)
app.include_router(document_routes.router)
app.include_router(client_routes.router)
