from sqlalchemy import Table, Column, Integer, String, Text, DateTime, func

from .db import meta

"""
Definición de la tabla 'document' en la base de datos.

Registra cada documento enviado a la DIAN con su veredicto, para poder
consultarlo después desde el panel web. Se registran tanto los envíos
aceptados como los rechazados y los que fallaron antes de llegar a la DIAN.

:table document: Tabla de documentos enviados.
"""

# Tipos de documento registrados.
TIPO_FACTURA = 'FV'
TIPO_NOTA_CREDITO = 'NC'
TIPO_DOCUMENTO_SOPORTE = 'DS'
TIPO_NOTA_AJUSTE_DS = 'NAS'
TIPO_NOMINA = 'NI'
TIPO_NOMINA_AJUSTE = 'NIA'

TIPOS = {
    TIPO_FACTURA: 'Factura de venta',
    TIPO_NOTA_CREDITO: 'Nota crédito',
    TIPO_DOCUMENTO_SOPORTE: 'Documento soporte',
    TIPO_NOTA_AJUSTE_DS: 'Nota de ajuste al DS',
    TIPO_NOMINA: 'Nómina individual',
    TIPO_NOMINA_AJUSTE: 'Nómina de ajuste',
}

# Estados posibles de un envío.
ESTADO_ACEPTADO = 'ACEPTADO'
ESTADO_RECHAZADO = 'RECHAZADO'
ESTADO_ENVIADO = 'ENVIADO'      # asíncrono: hay ZipKey pero todavía no hay veredicto
ESTADO_ERROR = 'ERROR'          # falló antes de obtener respuesta de la DIAN

ESTADOS = [ESTADO_ACEPTADO, ESTADO_RECHAZADO, ESTADO_ENVIADO, ESTADO_ERROR]

document = Table(
    "document",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True, doc="Identificador único del registro."),
    Column("tipo", String(10), nullable=False, doc="Tipo de documento (FV, NC, DS, NAS, NI, NIA)."),
    Column("numero", String(100), nullable=False, doc="Número del documento (prefijo + consecutivo)."),
    Column("cliente_nit", String(50), nullable=False, doc="NIT del emisor."),
    Column("resolucion", String(50), nullable=True, doc="Resolución del emisor. Nulo en nómina."),
    Column("identificador", String(200), nullable=True, doc="CUFE / CUDE / CUDS / CUNE del documento."),
    Column("ambiente", String(1), nullable=False, doc="Ambiente DIAN: 1 producción, 2 habilitación."),
    Column("estado", String(20), nullable=False, doc="ACEPTADO, RECHAZADO, ENVIADO o ERROR."),
    Column("mensajes", Text, nullable=True, doc="Mensajes devueltos por la DIAN."),
    Column("respuesta_dian", Text, nullable=True, doc="XML crudo de la respuesta de la DIAN."),
    Column("zip_path", String(500), nullable=True, doc="Ruta del .zip enviado, dentro de PATH_BASE."),
    Column("zip_key", String(200), nullable=True, doc="ZipKey devuelto por envíos asíncronos."),
    Column("created_at", DateTime, nullable=False, server_default=func.now(), doc="Fecha del envío."),
)
