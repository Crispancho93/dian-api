from fastapi import APIRouter, Request, Depends

from application.use_cases.document.list_documents_case import (
    ListDocumentsCase,
    CountDocumentsByStatusCase,
)
from domain.entities.document import ESTADOS, TIPOS
from ..deps import require_login
from ..templating import render

router = APIRouter(tags=["web"])


@router.get("/")
def dashboard(request: Request, user=Depends(require_login)):
    """Tablero: conteo por estado y últimos documentos enviados."""
    try:
        conteos = CountDocumentsByStatusCase().execute()
        ultimos, _ = ListDocumentsCase(page=1, page_size=10).execute()
        error = None
    except Exception as e:
        conteos, ultimos = {}, []
        error = f"No se pudo leer la información de documentos: {e}"

    return render(
        request,
        "dashboard.html",
        {
            "conteos": {estado: conteos.get(estado, 0) for estado in ESTADOS},
            "total": sum(conteos.values()) if conteos else 0,
            "ultimos": ultimos,
            "tipos": TIPOS,
            "error": error,
        },
    )
