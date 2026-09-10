from urllib.parse import quote_plus

from fastapi import APIRouter, Request, Depends, Form, File, UploadFile, Query
from fastapi.responses import RedirectResponse

from application.use_cases.client.list_clients_case import ListClientsCase, GetClientCase
from application.use_cases.client.save_client_case import SaveClientCase
from application.use_cases.client.save_certificate_case import SaveCertificateCase
from application.use_cases.client.delete_client_case import DeleteClientCase
from ..deps import require_login
from ..templating import render

router = APIRouter(prefix="/clientes", tags=["web"])


@router.get("")
def list_clients(
    request: Request,
    buscar: str = Query(""),
    mensaje: str = Query(""),
    error: str = Query(""),
    user=Depends(require_login),
):
    """Listado de clientes con el estado de su certificado."""
    try:
        clientes = ListClientsCase(buscar=buscar).execute()
    except Exception as e:
        clientes, error = [], f"No se pudo consultar los clientes: {e}"

    return render(
        request,
        "clients/list.html",
        {
            "clientes": clientes,
            "buscar": buscar,
            "mensaje": mensaje,
            "error": None,
            "error_modal": error,
        },
    )


@router.get("/nuevo")
def new_client_form(request: Request, user=Depends(require_login)):
    """Formulario de alta de cliente."""
    return render(request, "clients/form.html", {"cliente": None})


@router.get("/{client_id}/editar")
def edit_client_form(
    request: Request,
    client_id: int,
    mensaje: str = Query(""),
    error: str = Query(""),
    user=Depends(require_login),
):
    """Formulario de edición de cliente y carga de su certificado."""
    try:
        cliente = GetClientCase(client_id).execute()
    except LookupError:
        return RedirectResponse(url="/clientes", status_code=303)

    return render(
        request,
        "clients/form.html",
        {"cliente": cliente, "mensaje": mensaje, "error": error},
    )


@router.post("/guardar")
def save_client(
    request: Request,
    nit: str = Form(...),
    digito: str = Form(""),
    resolucion: str = Form(...),
    full_name: str = Form(...),
    is_active: str = Form(""),
    client_id: str = Form(""),
    user=Depends(require_login),
):
    """Crea o actualiza un cliente."""
    parsed_id = int(client_id) if client_id else None

    try:
        cliente = SaveClientCase(
            nit=nit,
            digito=digito,
            resolucion=resolucion,
            full_name=full_name,
            is_active=bool(is_active),
            client_id=parsed_id,
        ).execute()
    except (ValueError, LookupError) as e:
        return render(
            request,
            "clients/form.html",
            {
                "cliente": None,
                "error": str(e),
                # Devuelve lo que el usuario había escrito, para no perderlo.
                "form": {
                    "id": parsed_id,
                    "nit": nit,
                    "digito": digito,
                    "resolucion": resolucion,
                    "full_name": full_name,
                    "is_active": bool(is_active),
                },
            },
            status_code=400,
        )

    return RedirectResponse(
        url=f"/clientes/{cliente.id}/editar?mensaje=Cliente+guardado", status_code=303
    )


@router.post("/{client_id}/eliminar")
def delete_client(client_id: int, user=Depends(require_login)):
    """Elimina un cliente sin documentos asociados."""
    try:
        DeleteClientCase(client_id).execute()
    except LookupError:
        return RedirectResponse(
            url="/clientes?error=El+cliente+no+existe", status_code=303
        )
    except ValueError as e:
        return RedirectResponse(
            url=f"/clientes?error={quote_plus(str(e))}", status_code=303
        )

    return RedirectResponse(
        url="/clientes?mensaje=Cliente+eliminado", status_code=303
    )


@router.post("/{client_id}/certificado")
async def upload_certificate(
    request: Request,
    client_id: int,
    certificado: UploadFile = File(...),
    pfx_password: str = Form(...),
    user=Depends(require_login),
):
    """
    Carga el .pfx de un cliente junto con su clave.

    El certificado se valida antes de guardarse: si la clave no corresponde, no
    se escribe nada.
    """
    content = await certificado.read()

    try:
        SaveCertificateCase(
            client_id=client_id,
            file_name=certificado.filename,
            file_content=content,
            password=pfx_password,
        ).execute()
    except LookupError:
        return RedirectResponse(url="/clientes", status_code=303)
    except ValueError as e:
        return RedirectResponse(
            url=f"/clientes/{client_id}/editar?error={e}", status_code=303
        )
    except Exception as e:
        return RedirectResponse(
            url=f"/clientes/{client_id}/editar?error=No+se+pudo+guardar+el+certificado:+{e}",
            status_code=303,
        )

    return RedirectResponse(
        url=f"/clientes/{client_id}/editar?mensaje=Certificado+cargado+y+validado+correctamente",
        status_code=303,
    )
