import os

from fastapi import APIRouter, Request, Depends, Query
from fastapi.responses import RedirectResponse, FileResponse

from application.use_cases.document.list_documents_case import ListDocumentsCase
from application.use_cases.document.get_document_case import GetDocumentCase
from application.use_cases.document.refresh_document_status_case import RefreshDocumentStatusCase
from application.use_cases.client.list_clients_case import ListClientsCase
from domain.entities.document import TIPOS, ESTADOS
from ..deps import require_login
from ..templating import render

router = APIRouter(prefix="/documentos", tags=["web"])


@router.get("")
def list_documents(
    request: Request,
    cliente_nit: str = Query(""),
    tipo: str = Query(""),
    estado: str = Query(""),
    desde: str = Query(""),
    hasta: str = Query(""),
    buscar: str = Query(""),
    page: int = Query(1),
    page_size: int = Query(30, ge=1, le=30),
    user=Depends(require_login),
):
    """Listado de documentos enviados, con filtros y paginación."""
    page_size = max(1, min(int(page_size or 30), 30))
    filtros = {
        "cliente_nit": cliente_nit,
        "tipo": tipo,
        "estado": estado,
        "desde": desde,
        "hasta": hasta,
        "buscar": buscar,
    }

    try:
        documentos, total = ListDocumentsCase(
            page=page, page_size=page_size, **filtros
        ).execute()
        clientes = ListClientsCase().execute()
        error = None
    except Exception as e:
        documentos, total, clientes = [], 0, []
        error = f"No se pudo consultar los documentos: {e}"

    clientes_por_nit = {cliente.nit: cliente.full_name for cliente in clientes}
    total_pages = max(1, (total + page_size - 1) // page_size)

    return render(
        request,
        "documents/list.html",
        {
            "documentos": documentos,
            "clientes": clientes,
            "clientes_por_nit": clientes_por_nit,
            "filtros": filtros,
            "tipos": TIPOS,
            "estados": ESTADOS,
            "total": total,
            "page": page,
            "total_pages": total_pages,
            "error": error,
        },
    )


@router.get("/{document_id}")
def document_detail(
    request: Request,
    document_id: int,
    mensaje: str = Query(""),
    error: str = Query(""),
    user=Depends(require_login),
):
    """Detalle de un documento: datos, mensajes DIAN y respuesta cruda."""
    try:
        documento = GetDocumentCase(document_id).execute()
    except LookupError:
        return render(
            request,
            "documents/detail.html",
            {"documento": None, "error": "El documento no existe.", "tipos": TIPOS},
            status_code=404,
        )

    zip_disponible = bool(documento.zip_path and os.path.exists(documento.zip_path))

    return render(
        request,
        "documents/detail.html",
        {
            "documento": documento,
            "tipos": TIPOS,
            "zip_disponible": zip_disponible,
            "mensaje": mensaje,
            "error": error,
        },
    )


@router.get("/{document_id}/descargar")
def download_document(request: Request, document_id: int, user=Depends(require_login)):
    """Descarga el .zip que se envió a la DIAN."""
    try:
        documento = GetDocumentCase(document_id).execute()
    except LookupError:
        return RedirectResponse(url="/documentos", status_code=303)

    if not documento.zip_path or not os.path.exists(documento.zip_path):
        return RedirectResponse(
            url=f"/documentos/{document_id}?error=El+archivo+ya+no+está+disponible+en+el+servidor",
            status_code=303,
        )

    return FileResponse(
        path=documento.zip_path,
        filename=os.path.basename(documento.zip_path),
        media_type="application/zip",
    )


@router.post("/{document_id}/estado")
def refresh_status(request: Request, document_id: int, user=Depends(require_login)):
    """Reconsulta el estado en la DIAN (GetStatusZip) para envíos asíncronos."""
    try:
        documento = RefreshDocumentStatusCase(document_id).execute()
        query = f"?mensaje=Estado+actualizado:+{documento.estado}"
    except LookupError:
        return RedirectResponse(url="/documentos", status_code=303)
    except ValueError:
        query = "?error=Este+documento+no+tiene+ZipKey:+no+fue+un+envío+asíncrono"
    except Exception as e:
        query = f"?error=No+se+pudo+consultar+la+DIAN:+{e}"

    return RedirectResponse(url=f"/documentos/{document_id}{query}", status_code=303)
