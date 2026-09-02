"""
Deja el panel web listo para usar: crea las tablas, el usuario del primer login
y (opcionalmente) datos de prueba para poder navegar la interfaz.

Uso típico, desde la raíz del repo:

    python scripts/create_user.py

Eso crea las tablas que falten, el usuario admin por defecto y datos de prueba.

Opciones:

    --email / --password / --name   Credenciales del usuario (ver DEFAULT_* abajo)
    --sin-datos                     No crear datos de prueba (para producción)
    --solo-datos                    No tocar el usuario, solo cargar datos de prueba
    --limpiar-datos                 Borrar los datos de prueba creados por este script

El script es idempotente: se puede correr varias veces. Las tablas que ya
existen no se tocan, el usuario se actualiza en vez de duplicarse y los datos de
prueba no se vuelven a insertar si ya están.
"""

import os
import sys
import argparse
from datetime import timedelta

# Permite ejecutarlo desde cualquier carpeta (`python scripts/create_user.py`,
# o parado dentro de scripts/).
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# OJO con el orden de imports: hay que entrar por `application.use_cases`. Si se
# importa `domain.entities.db` primero, se dispara un import circular del
# proyecto (shared -> certificate -> use_cases -> xml_models -> shared).
from application.use_cases.user.create_user_case import CreateUserCase  # noqa: E402
from sqlalchemy import select, insert, delete  # noqa: E402

from domain.entities.db import engine, meta, get_connection  # noqa: E402
from domain.entities.client import client  # noqa: E402
from domain.entities.user import users  # noqa: E402
from domain.entities.document import (  # noqa: E402
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
from shared.generic import now_colombia  # noqa: E402

DEFAULT_EMAIL = "admin@atechcol.com"
DEFAULT_PASSWORD = "admin123"
DEFAULT_NAME = "Administrador"

# NITs de los clientes de prueba. Sirven también para poder borrarlos después
# con --limpiar-datos sin tocar datos reales.
MOCK_NITS = ["901111111", "901222222"]

MOCK_CLIENTS = [
    {
        "nit": "901111111",
        "digito": "1",
        "resolucion": "18760000010",
        "full_name": "DEMO COMERCIAL S.A.S.",
    },
    {
        "nit": "901222222",
        "digito": "8",
        "resolucion": "18760000011",
        "full_name": "SERVICIOS DEMO LTDA",
    },
]

_RESPUESTA_ACEPTADA = """<?xml version="1.0" encoding="utf-8"?>
<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope">
  <s:Body>
    <SendBillSyncResponse xmlns="http://wcf.dian.colombia">
      <SendBillSyncResult xmlns:b="http://schemas.datacontract.org/2004/07/DianResponse">
        <b:IsValid>true</b:IsValid>
        <b:StatusCode>00</b:StatusCode>
        <b:StatusDescription>Procesado Correctamente.</b:StatusDescription>
      </SendBillSyncResult>
    </SendBillSyncResponse>
  </s:Body>
</s:Envelope>"""

_RESPUESTA_RECHAZADA = """<?xml version="1.0" encoding="utf-8"?>
<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope">
  <s:Body>
    <SendBillSyncResponse xmlns="http://wcf.dian.colombia">
      <SendBillSyncResult xmlns:b="http://schemas.datacontract.org/2004/07/DianResponse">
        <b:IsValid>false</b:IsValid>
        <b:StatusCode>99</b:StatusCode>
      </SendBillSyncResult>
    </SendBillSyncResponse>
  </s:Body>
</s:Envelope>"""


def crear_tablas():
    """
    Crea las tablas que falten: users, document y client.

    `create_all` no toca las tablas que ya existen, así que es seguro correrlo
    sobre una base con datos.
    """
    tablas = [users, document, client]

    from sqlalchemy import inspect
    existentes = set(inspect(engine).get_table_names())

    meta.create_all(engine, tables=tablas)

    for tabla in tablas:
        estado = "ya existía" if tabla.name in existentes else "CREADA"
        print(f"  {tabla.name:<10} {estado}")


def crear_usuario(email: str, password: str, name: str):
    """Crea el usuario del panel, o le actualiza la contraseña si ya existe."""
    user = CreateUserCase(name=name, email=email, password=password).execute()
    print(f"  Usuario #{user.id}: {user.email}")
    return user


def _mock_ya_cargado(conn) -> bool:
    return conn.execute(
        select(document.c.id).where(document.c.cliente_nit.in_(MOCK_NITS)).limit(1)
    ).first() is not None


def crear_datos_prueba():
    """
    Carga clientes y documentos de prueba para poder navegar el panel.

    Los documentos cubren los seis tipos y los cuatro estados, con fechas
    repartidas en los últimos días para poder probar los filtros.
    """
    ahora = now_colombia()

    with get_connection() as conn:
        # --- Clientes ---
        creados = 0
        for datos in MOCK_CLIENTS:
            existe = conn.execute(
                select(client.c.id).where(client.c.resolucion == datos["resolucion"])
            ).first()

            if existe:
                continue

            # pfx_path y pfx_password son NOT NULL: se dejan vacíos, igual que
            # cuando se crea un cliente desde el panel. El certificado se carga
            # después desde la pantalla del cliente.
            conn.execute(insert(client).values(
                pfx_path="", pfx_password="", is_active=True, **datos
            ))
            creados += 1

        print(f"  Clientes de prueba: {creados} creados, "
              f"{len(MOCK_CLIENTS) - creados} ya existían")

        # --- Documentos ---
        if _mock_ya_cargado(conn):
            print("  Documentos de prueba: ya estaban cargados, no se duplican")
            conn.commit()
            return

        nit_a, nit_b = MOCK_NITS
        res_a = MOCK_CLIENTS[0]["resolucion"]
        res_b = MOCK_CLIENTS[1]["resolucion"]

        documentos = [
            # (tipo, numero, nit, resolucion, identificador, ambiente, estado,
            #  mensajes, respuesta, zip_key, dias_atras)
            (TIPO_FACTURA, "SETP990000101", nit_a, res_a, "a1b2c3" + "0" * 90, "2",
             ESTADO_ACEPTADO, "Procesado Correctamente.", _RESPUESTA_ACEPTADA, None, 0),
            (TIPO_FACTURA, "SETP990000102", nit_a, res_a, "d4e5f6" + "0" * 90, "2",
             ESTADO_ACEPTADO, "Procesado Correctamente.", _RESPUESTA_ACEPTADA, None, 0),
            (TIPO_FACTURA, "SETP990000103", nit_b, res_b, "g7h8i9" + "0" * 90, "1",
             ESTADO_RECHAZADO,
             "Regla: FAJ25 - Valor del atributo del elemento cbc:PayableAmount no corresponde.",
             _RESPUESTA_RECHAZADA, None, 1),
            (TIPO_NOTA_CREDITO, "NC-000045", nit_a, res_a, "j1k2l3" + "0" * 90, "2",
             ESTADO_ACEPTADO, "Procesado Correctamente.", _RESPUESTA_ACEPTADA, None, 1),
            (TIPO_DOCUMENTO_SOPORTE, "DS-000012", nit_b, res_b, "m4n5o6" + "0" * 90, "1",
             ESTADO_ACEPTADO, "Procesado Correctamente.", _RESPUESTA_ACEPTADA, None, 2),
            (TIPO_NOTA_AJUSTE_DS, "NAS-000003", nit_b, res_b, "p7q8r9" + "0" * 90, "1",
             ESTADO_ERROR,
             "PFX no encontrado en la ruta: C:/FE/901222222/certificado/demo.pfx",
             None, None, 3),
            (TIPO_NOMINA, "NE-000210", nit_a, None, "s1t2u3" + "0" * 90, "2",
             ESTADO_ENVIADO, "Recibido para validación.", None,
             "8a7b6c5d-4e3f-2a1b-9c8d-7e6f5a4b3c2d", 4),
            (TIPO_NOMINA_AJUSTE, "NA-000007", nit_a, None, "v4w5x6" + "0" * 90, "2",
             ESTADO_ACEPTADO, "Procesado Correctamente.", _RESPUESTA_ACEPTADA, None, 5),
        ]

        for (tipo, numero, nit, resolucion, identificador, ambiente, estado,
             mensajes, respuesta, zip_key, dias) in documentos:
            conn.execute(insert(document).values(
                tipo=tipo,
                numero=numero,
                cliente_nit=nit,
                resolucion=resolucion,
                identificador=identificador,
                ambiente=ambiente,
                estado=estado,
                mensajes=mensajes,
                respuesta_dian=respuesta,
                # Sin zip_path: los .zip de prueba no existen en disco, y así el
                # panel muestra correctamente que el archivo no está disponible.
                zip_path=None,
                zip_key=zip_key,
                created_at=ahora - timedelta(days=dias, hours=dias),
            ))

        conn.commit()
        print(f"  Documentos de prueba: {len(documentos)} creados")


def limpiar_datos_prueba():
    """Borra los clientes y documentos de prueba creados por este script."""
    with get_connection() as conn:
        docs = conn.execute(
            delete(document).where(document.c.cliente_nit.in_(MOCK_NITS))
        ).rowcount
        clientes = conn.execute(
            delete(client).where(client.c.nit.in_(MOCK_NITS))
        ).rowcount
        conn.commit()

    print(f"  Borrados: {docs} documentos y {clientes} clientes de prueba")


def main():
    parser = argparse.ArgumentParser(
        description="Prepara el panel web de Invoice.API: tablas, usuario y datos de prueba."
    )
    parser.add_argument("--email", default=DEFAULT_EMAIL,
                        help=f"Correo para el login (por defecto: {DEFAULT_EMAIL})")
    parser.add_argument("--password", default=DEFAULT_PASSWORD,
                        help=f"Contraseña (por defecto: {DEFAULT_PASSWORD})")
    parser.add_argument("--name", default=DEFAULT_NAME, help="Nombre del usuario")
    parser.add_argument("--sin-datos", dest="sin_datos", action="store_true",
                        help="No crear datos de prueba (recomendado en producción)")
    parser.add_argument("--solo-datos", dest="solo_datos", action="store_true",
                        help="Solo cargar datos de prueba, sin tocar el usuario")
    parser.add_argument("--limpiar-datos", dest="limpiar_datos", action="store_true",
                        help="Borrar los datos de prueba y salir")

    args = parser.parse_args()

    print(f"\nBase de datos: {engine.url}\n")

    try:
        if args.limpiar_datos:
            print("Limpiando datos de prueba...")
            limpiar_datos_prueba()
            print("\nListo.\n")
            return 0

        print("1. Tablas")
        crear_tablas()

        user = None
        if not args.solo_datos:
            print("\n2. Usuario del panel")
            user = crear_usuario(args.email, args.password, args.name)

        if not args.sin_datos:
            print("\n3. Datos de prueba")
            crear_datos_prueba()

    except Exception as e:
        print(f"\nError: {e}\n")
        print("Si el error es de conexión, revisá DATABASE_URL en el .env.")
        return 1

    print("\n" + "=" * 58)
    print("  Listo. Levantá la API y entrá al panel:")
    print("      uvicorn app:app --reload")
    print("      http://localhost:8000/login")
    if user:
        print(f"\n  Usuario:    {args.email}")
        print(f"  Contraseña: {args.password}")
        if args.password == DEFAULT_PASSWORD:
            print("\n  OJO: es la contraseña por defecto. Cambiala antes de exponer")
            print("  el panel, corriendo este script con --password.")
    if not args.sin_datos:
        print("\n  Los datos de prueba se borran con: --limpiar-datos")
    print("=" * 58 + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
