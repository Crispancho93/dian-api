from sqlalchemy import update

from shared import generic
from shared.certificate import CertificateLoader
from domain.dtos.document_dto import DocumentDto
from domain.entities.db import get_connection
from domain.entities.document import (
    document,
    ESTADO_ACEPTADO,
    ESTADO_RECHAZADO,
    ESTADO_ENVIADO,
)
from application.use_cases.client.get_client_by_nit_only_case import GetClientByNitOnlyCase
from application.use_cases.soap.soap_payroll import SoapStatusZipRequest

from .get_document_case import GetDocumentCase


class RefreshDocumentStatusCase:
    """
    Reconsulta en la DIAN el estado de un envío asíncrono, usando su ZipKey.

    Aplica a los envíos al set de pruebas (SendTestSetAsync), que responden un
    ZipKey en vez del veredicto. Reutiliza :class:`SoapStatusZipRequest`
    (GetStatusZip) y actualiza la fila con el resultado.
    """

    def __init__(self, document_id: int):
        """
        :param document_id: Identificador del documento a reconsultar.
        """
        self.document_id = document_id

    def execute(self) -> DocumentDto:
        """
        :returns: :class:`DocumentDto` actualizado.
        :raises LookupError: ``DOCUMENT_NOT_FOUND`` si el documento no existe.
        :raises ValueError: ``NO_ZIP_KEY`` si el documento no tiene ZipKey, es
            decir, no fue un envío asíncrono y no hay nada que reconsultar.
        """
        doc = GetDocumentCase(self.document_id).execute()

        if not doc.zip_key:
            raise ValueError("NO_ZIP_KEY")

        # El certificado se resuelve por NIT, igual que en el envío de nómina.
        certificate_loader = CertificateLoader(GetClientByNitOnlyCase)
        certificate_loader.load(doc.cliente_nit)

        response = SoapStatusZipRequest(certificate_loader.security).get_status(doc.zip_key)

        estado, mensajes = self._interpret(response.text)

        with get_connection() as conn:
            conn.execute(
                update(document)
                .where(document.c.id == self.document_id)
                .values(
                    estado=estado,
                    mensajes=mensajes,
                    respuesta_dian=response.text,
                )
            )
            conn.commit()

        return GetDocumentCase(self.document_id).execute()

    @staticmethod
    def _interpret(response_text: str):
        """
        Interpreta la respuesta de GetStatusZip.

        Si la DIAN todavía no procesó el lote, la respuesta puede no traer
        IsValid; en ese caso el documento se deja como ENVIADO para poder
        reconsultarlo más tarde.

        :returns: Tupla ``(estado, mensajes)``.
        """
        try:
            is_valid, messages = generic.extract_errors_invoice(response_text)
        except Exception:
            return ESTADO_ENVIADO, "La DIAN todavía no devuelve un veredicto para este ZipKey."

        estado = ESTADO_ACEPTADO if str(is_valid).lower() == 'true' else ESTADO_RECHAZADO
        return estado, "\n".join(str(m) for m in (messages or []) if m)
