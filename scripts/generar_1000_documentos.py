"""Genera 1000 documentos de prueba para probar la paginación del panel web."""

import os
import sys
from datetime import timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importar primero la capa de casos de uso evita el ciclo circular con
# shared -> certificate -> application.use_cases -> ...
from application.use_cases.user.create_user_case import CreateUserCase  # noqa: F401
from sqlalchemy import insert, select, func

from domain.entities.db import get_connection
from domain.entities.document import (
    document,
    TIPO_FACTURA,
    TIPO_NOTA_CREDITO,
    TIPO_DOCUMENTO_SOPORTE,
    TIPO_NOTA_AJUSTE_DS,
    TIPO_NOMINA,
    TIPO_NOMINA_AJUSTE,
    ESTADO_ACEPTADO,
    ESTADO_RECHAZADO,
    ESTADO_ENVIADO,
    ESTADO_ERROR,
)
from shared.generic import now_colombia


def generar_documentos(cantidad: int = 1000):
    with get_connection() as conn:
        total_actual = conn.execute(select(func.count()).select_from(document)).scalar() or 0

        if total_actual >= cantidad:
            print(f"Ya existen {total_actual} documentos. No se insertan más.")
            return total_actual

        faltan = cantidad - total_actual
        ahora = now_colombia()
        tipos = [
            TIPO_FACTURA,
            TIPO_NOTA_CREDITO,
            TIPO_DOCUMENTO_SOPORTE,
            TIPO_NOTA_AJUSTE_DS,
            TIPO_NOMINA,
            TIPO_NOMINA_AJUSTE,
        ]
        estados = [ESTADO_ACEPTADO, ESTADO_RECHAZADO, ESTADO_ENVIADO, ESTADO_ERROR]

        rows = []
        for i in range(1, faltan + 1):
            tipo = tipos[(i - 1) % len(tipos)]
            if tipo == TIPO_FACTURA:
                numero = f"FAC-{1000 + i:06d}"
            elif tipo == TIPO_NOTA_CREDITO:
                numero = f"NC-{1000 + i:06d}"
            elif tipo == TIPO_DOCUMENTO_SOPORTE:
                numero = f"DS-{1000 + i:06d}"
            elif tipo == TIPO_NOTA_AJUSTE_DS:
                numero = f"NAS-{1000 + i:06d}"
            elif tipo == TIPO_NOMINA:
                numero = f"NI-{1000 + i:06d}"
            else:
                numero = f"NIA-{1000 + i:06d}"

            nit = "901111111" if i % 2 == 0 else "901222222"
            resolucion = "18760000010" if nit == "901111111" else "18760000011"
            estado = estados[(i - 1) % len(estados)]

            rows.append(
                {
                    "tipo": tipo,
                    "numero": numero,
                    "cliente_nit": nit,
                    "resolucion": resolucion,
                    "identificador": f"ID-{i:06d}-{tipo}",
                    "ambiente": "2" if i % 3 != 0 else "1",
                    "estado": estado,
                    "mensajes": "Prueba de paginación",
                    "respuesta_dian": "<?xml version='1.0' encoding='utf-8'?><ok />",
                    "zip_path": None,
                    "zip_key": f"zip-{i:06d}" if estado in (ESTADO_ENVIADO, ESTADO_ACEPTADO) else None,
                    "created_at": ahora - timedelta(minutes=i, seconds=i % 60),
                }
            )

        if rows:
            conn.execute(insert(document), rows)
            conn.commit()

        total_final = conn.execute(select(func.count()).select_from(document)).scalar() or 0
        print(f"Insertados {faltan} documentos. Total actual: {total_final}")
        return total_final


if __name__ == "__main__":
    generar_documentos(1000)
