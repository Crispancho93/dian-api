import os

from fastapi.templating import Jinja2Templates

"""
Entorno Jinja2 del panel web.

Ojo con el nombre: `shared.xml_files.templates_loader` es el cargador de
plantillas **XML** de los documentos DIAN. Esto es otra cosa: las plantillas
HTML de la interfaz.
"""

_TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
_STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

web_templates = Jinja2Templates(directory=_TEMPLATES_DIR)


def static_dir() -> str:
    """Ruta absoluta de la carpeta de archivos estáticos del panel."""
    return _STATIC_DIR


def render(request, template_name: str, context: dict = None, status_code: int = 200):
    """
    Renderiza una plantilla inyectando los datos comunes del layout.

    :param request: Request de FastAPI.
    :param template_name: Nombre de la plantilla, relativo a `templates/`.
    :param context: Contexto propio de la vista.
    :param status_code: Código HTTP de la respuesta.
    """
    data = {
        "request": request,
        "current_user": request.session.get("user"),
    }
    data.update(context or {})

    return web_templates.TemplateResponse(template_name, data, status_code=status_code)
