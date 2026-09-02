import logging

from sqlalchemy import insert, update

from shared.generic import now_colombia
from domain.entities.db import get_connection
from domain.entities.document import (
    document,
    ESTADO_ACEPTADO,
    ESTADO_RECHAZADO,
    ESTADO_ENVIADO,
    ESTADO_ERROR,
)

_logger = logging.getLogger(__name__)


class DocumentRecorder:
    """
    Registra en la tabla ``document`` el resultado de un envío a la DIAN.

    Se usa desde los casos de uso de creación de documentos, que comparten la
    misma forma: firmar, comprimir, enviar, interpretar la respuesta. El
    recorder guarda tanto los envíos aceptados como los rechazados y los que
    fallaron antes de obtener respuesta.

    **Ningún método de esta clase propaga excepciones**: un fallo al registrar
    no debe tumbar un envío que la DIAN ya aceptó. Los errores se loguean y se
    siguen de largo, con el mismo criterio que el guardado del .zip en segundo
    plano.

    Uso típico::

        recorder = DocumentRecorder(tipo='FV', numero=..., cliente_nit=..., ...)
        try:
            response = self.soap.send_xml(zip_doc)
            is_valid, messages = generic.extract_errors_invoice(response.text)
            recorder.finish(is_valid, messages, response.text)
            if is_valid == 'false':
                raise Exception(messages)
        except Exception as e:
            recorder.fail(str(e))
            raise
    """

    def __init__(
        self,
        tipo: str,
        numero: str,
        cliente_nit: str,
        ambiente: str,
        resolucion: str = None,
        identificador: str = None,
        zip_path: str = None,
    ):
        """
        :param tipo: Tipo de documento (FV, NC, DS, NAS, NI, NIA).
        :param numero: Número del documento.
        :param cliente_nit: NIT del emisor.
        :param ambiente: Ambiente DIAN: "1" producción, "2" habilitación.
        :param resolucion: Resolución del emisor. Nulo en nómina.
        :param identificador: CUFE / CUDE / CUDS / CUNE.
        :param zip_path: Ruta del .zip enviado.
        """
        self.tipo = tipo
        self.numero = str(numero) if numero is not None else ''
        self.cliente_nit = cliente_nit
        self.ambiente = str(ambiente) if ambiente is not None else '1'
        self.resolucion = resolucion
        self.identificador = identificador
        self.zip_path = zip_path

        self._document_id = None

    @property
    def document_id(self):
        """Id de la fila registrada, o None si todavía no se registró nada."""
        return self._document_id

    def finish(self, is_valid, messages, respuesta_dian: str = None):
        """
        Registra el veredicto de un envío síncrono.

        :param is_valid: Valor devuelto por ``generic.extract_errors_invoice``
            ('true' / 'false'), o un booleano.
        :param messages: Mensajes devueltos por la DIAN.
        :param respuesta_dian: XML crudo de la respuesta.
        """
        aceptado = is_valid is True or str(is_valid).lower() == 'true'
        estado = ESTADO_ACEPTADO if aceptado else ESTADO_RECHAZADO

        self._save(
            estado=estado,
            mensajes=self._as_text(messages),
            respuesta_dian=respuesta_dian,
        )

    def sent_async(self, zip_key: str, messages=None, respuesta_dian: str = None):
        """
        Registra un envío asíncrono (set de pruebas) que todavía no tiene
        veredicto: la DIAN solo devolvió un ZipKey.

        :param zip_key: ZipKey devuelto por SendTestSetAsync.
        :param messages: Mensajes devueltos junto al ZipKey, si los hay.
        :param respuesta_dian: XML crudo de la respuesta.
        """
        self._save(
            estado=ESTADO_ENVIADO,
            mensajes=self._as_text(messages),
            respuesta_dian=respuesta_dian,
            zip_key=zip_key,
        )

    def fail(self, error: str):
        """
        Registra un fallo previo a obtener respuesta de la DIAN.

        Es idempotente respecto de :meth:`finish` y :meth:`sent_async`: si el
        envío ya quedó registrado con un veredicto, no lo pisa. Esto permite
        llamarlo desde el ``except`` sin condicionales, incluso cuando la
        excepción es el ``raise`` que sigue a un rechazo ya registrado.

        :param error: Descripción del error.
        """
        if self._document_id is not None:
            return

        self._save(estado=ESTADO_ERROR, mensajes=self._as_text(error))

    def _save(self, estado, mensajes=None, respuesta_dian=None, zip_key=None):
        """Inserta la fila, o la actualiza si el recorder ya registró una."""
        values = {
            'estado': estado,
            'mensajes': mensajes,
            'respuesta_dian': respuesta_dian,
            'zip_key': zip_key,
        }

        try:
            with get_connection() as conn:
                if self._document_id is None:
                    values.update({
                        'tipo': self.tipo,
                        'numero': self.numero,
                        'cliente_nit': self.cliente_nit,
                        'resolucion': self.resolucion,
                        'identificador': self.identificador,
                        'ambiente': self.ambiente,
                        'zip_path': self.zip_path,
                        # Hora colombiana explícita: el servidor corre en UTC y
                        # el panel filtra por fecha local.
                        'created_at': now_colombia(),
                    })
                    result = conn.execute(insert(document).values(**values))
                    self._document_id = result.inserted_primary_key[0]
                else:
                    conn.execute(
                        update(document)
                        .where(document.c.id == self._document_id)
                        .values(**values)
                    )

                # SQLAlchemy 2.0 usa "commit as you go".
                conn.commit()
        except Exception as e:
            # Registrar no puede romper el envío: solo se deja traza en el log.
            _logger.error(
                "No se pudo registrar el documento %s %s: %s",
                self.tipo, self.numero, e
            )

    @staticmethod
    def _as_text(value):
        """Normaliza mensajes que pueden venir como lista, None o texto."""
        if value is None:
            return None
        if isinstance(value, (list, tuple)):
            return "\n".join(str(item) for item in value)
        return str(value)
