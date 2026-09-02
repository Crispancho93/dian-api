"""
Test de estabilidad del CUNE (Nómina Electrónica).

IMPORTANTE: el ejemplo resuelto del Anexo Técnico (sección 8.1.1.3) NO
reproduce contra la fórmula que el mismo anexo documenta -- se verificó
probando la concatenación tal cual está escrita, variantes de formato de
hora, y las 40320 permutaciones del orden de los últimos 8 campos, sin
encontrar coincidencia. Por eso este test NO afirma contra ese hash
publicado (ver docs/NOMINA_ELECTRONICA.md, sección de riesgos). Lo que
valida es que la fórmula es estable y determinística: misma entrada,
mismo resultado, formato correcto.

Uso: python test_payroll_cune.py   (desde la raíz del repo)
"""
# NOTA: `import app` primero es necesario por un import circular preexistente
# en shared/__init__.py (shared -> certificate -> application.use_cases ->
# domain.xml_models -> "from shared import templates_loader"). Importar `app`
# resuelve el árbol de imports en el orden correcto antes de tocar `shared`
# directamente. No es un patrón a repetir fuera de tests; no se modificó
# shared/__init__.py porque está fuera del alcance de este trabajo.
import os
import sys

# El repo se importa desde su raíz y los templates se resuelven contra el CWD
# (shared/xml_files.py usa os.path.abspath(os.curdir)), así que fijamos ambos.
_RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _RAIZ)
os.chdir(_RAIZ)

import app  # noqa: F401,E402
from shared.generic import get_cune, get_payroll_file_names  # noqa: E402

CAMPOS_EJEMPLO_ANEXO = {
    "NumNE": "N00001",
    "FecNE": "2020-01-16",
    "HorNE": "10:53:10-05:00",
    "ValDev": "3500000.00",
    "ValDed": "1000000.00",
    "ValTolNE": "2500000.00",
    "NitNE": "700085371",
    "DocEmp": "800199436",
    "TipoXML": "102",
    "SoftwarePin": "693",
    "TipAmb": "1",
}


def test_get_cune_es_determinista():
    h1 = get_cune(CAMPOS_EJEMPLO_ANEXO)
    h2 = get_cune(dict(CAMPOS_EJEMPLO_ANEXO))
    assert h1 == h2


def test_get_cune_formato_sha384():
    h = get_cune(CAMPOS_EJEMPLO_ANEXO)
    assert len(h) == 96
    assert h == h.lower()
    int(h, 16)  # hex válido


def test_get_cune_cambia_si_cambia_un_campo():
    base = get_cune(CAMPOS_EJEMPLO_ANEXO)
    otros = dict(CAMPOS_EJEMPLO_ANEXO)
    otros["ValDev"] = "3500000.01"
    assert get_cune(otros) != base


def test_get_payroll_file_names():
    xml_name, zip_name = get_payroll_file_names("800197268", "24", 12)
    assert xml_name == "nie0800197268240000000C.xml"
    assert zip_name == "z0800197268240000000C.zip"


if __name__ == "__main__":
    test_get_cune_es_determinista()
    test_get_cune_formato_sha384()
    test_get_cune_cambia_si_cambia_un_campo()
    test_get_payroll_file_names()
    print("OK: todos los tests de CUNE pasaron")


# ---------------------------------------------------------------------------
# Curl de referencia para la primera prueba manual contra /api/payroll/create_payroll
# en ambiente de habilitación DIAN. No se ejecuta como parte de los tests de
# arriba -- es solo para copiar/pegar en la terminal.
#
# Estado (2026-08-13): FUNCIONANDO. Nóminas NE5, NE6 y NE77 autorizadas por
# la DIAN en habilitación, y nota de ajuste NA-1 también autorizada.
#
# Datos del portal de habilitación (ya puestos en los payloads):
#   - SoftwareID: 7a376f67-222d-480b-9b46-73413c55401a ("orbis")
#   - Pin: 202677
#   - TestID: 2909e1cc-f6ce-4a0f-9f3f-a0376007af27 (TestSetId)
#   - NIT 901616617 (ORBIS GLOBAL TECHNOLOGY), cargado en la tabla `client`
#     con su .pfx; la cadena de CA de GSE está en C:\FE\certificados\
#     (CA_SUB01.crt + CA_ROOT.crt) y shared/certificate.py la resuelve sola.
#
# IMPORTANTE - el @Numero NO se puede repetir. Si mandás uno ya usado, la
# DIAN lo rechaza SIN mensaje descriptivo (así falló NE7). Subí el
# Consecutivo/Numero en cada envío.
#
# Cómo funciona el envío (verificado contra el WSDL, no contra el anexo):
#   - Con `TestID` en el payload  -> SendTestSetAsync (set de pruebas).
#   - Sin `TestID`                -> SendNominaSync (producción).
# El anexo solo documenta SendNominaSync, que según el WSDL acepta ÚNICAMENTE
# <contentFile>; el testSetId solo lo acepta SendTestSetAsync. Por eso meter
# el testSetId dentro de SendNominaSync no funciona: la DIAN lo ignora y
# responde "Regla 92: El Emisor no se encuentra Habilitado".
#
# SendTestSetAsync es ASÍNCRONO: la respuesta trae un ZipKey, no el veredicto.
# Para saber si fue aceptada:  case.get_status("<ZipKey>")  -> buscar
# IsValid=true y "ha sido autorizada".
CURL_HABILITACION_EJEMPLO = r'''
curl -X POST http://localhost:8000/api/payroll/create_payroll \
  -H "Content-Type: application/json" \
  -d '{
  "Periodo": {
    "FechaIngreso": "2020-01-15",
    "FechaLiquidacionInicio": "2024-01-01",
    "FechaLiquidacionFin": "2024-01-31",
    "TiempoLaborado": "30",
    "FechaGen": "2024-02-01"
  },
  "NumeroSecuenciaXML": {
    "Prefijo": "NE",
    "Consecutivo": "3",
    "Numero": "NE3"
  },
  "LugarGeneracionXML": {
    "Pais": "CO",
    "DepartamentoEstado": "11",
    "MunicipioCiudad": "11001",
    "Idioma": "es"
  },
  "ProveedorXML": {
    "RazonSocial": "ORBIS GLOBAL TECHNOLOGY",
    "NIT": "901616617",
    "DV": "7",
    "SoftwareID": "7a376f67-222d-480b-9b46-73413c55401a"
  },
  "InformacionGeneral": {
    "Version": "V1.0: Documento Soporte de Pago de Nómina Electrónica",
    "Ambiente": "2",
    "FechaGen": "2024-02-01",
    "HoraGen": "10:00:00-05:00",
    "PeriodoNomina": "5",
    "TipoMoneda": "COP"
  },
  "Empleador": {
    "RazonSocial": "ORBIS GLOBAL TECHNOLOGY",
    "NIT": "901616617",
    "DV": "7",
    "Pais": "CO",
    "DepartamentoEstado": "11",
    "MunicipioCiudad": "11001",
    "Direccion": "Calle 123 # 45-67"
  },
  "Trabajador": {
    "TipoTrabajador": "01",
    "SubTipoTrabajador": "00",
    "AltoRiesgoPension": "false",
    "TipoDocumento": "13",
    "NumeroDocumento": "1015000000",
    "PrimerApellido": "Perez",
    "SegundoApellido": "Gomez",
    "PrimerNombre": "Juan",
    "OtrosNombres": "Carlos",
    "LugarTrabajoPais": "CO",
    "LugarTrabajoDepartamentoEstado": "11",
    "LugarTrabajoMunicipioCiudad": "11001",
    "LugarTrabajoDireccion": "Calle 123 # 45-67",
    "SalarioIntegral": "false",
    "TipoContrato": "2",
    "Sueldo": "2000000.00"
  },
  "Pago": {
    "Forma": "1",
    "Metodo": "42",
    "Banco": "Bancolombia",
    "TipoCuenta": "AH",
    "NumeroCuenta": "1234567890"
  },
  "FechasPagos": ["2024-01-31"],
  "Devengados": {
    "Basico": {
      "DiasTrabajados": "30",
      "SueldoTrabajado": "2000000.00"
    },
    "Transporte": [
      { "AuxilioTransporte": "162000.00" }
    ],
    "HEDs": [
      {
        "HoraInicio": "2024-01-15T18:00:00",
        "HoraFin": "2024-01-15T19:00:00",
        "Cantidad": "1",
        "Porcentaje": "25.00",
        "Pago": "10870.00"
      }
    ]
  },
  "Deducciones": {
    "Salud": { "Porcentaje": "4.00", "Deduccion": "80000.00" },
    "FondoPension": { "Porcentaje": "4.00", "Deduccion": "80000.00" }
  },
  "DevengadosTotal": "2172870.00",
  "DeduccionesTotal": "160000.00",
  "ComprobanteTotal": "2012870.00",
  "Pin": "202677",
  "TestID": "2909e1cc-f6ce-4a0f-9f3f-a0376007af27"
}'
'''


# ---------------------------------------------------------------------------
# NOTA DE AJUSTE - opción REEMPLAZAR (TipoNota "1")
#
# Corrige una nómina ya enviada. Lleva el cuerpo COMPLETO de la nómina (los
# valores corregidos) más el bloque `Predecesor`, que identifica la nómina
# original: NumeroPred + CUNEPred + FechaGenPred.
#
# El CUNEPred es el CUNE que devolvió /api/payroll/create_payroll al crear esa
# nómina. El de abajo es el real de NE5 (autorizada).
CURL_AJUSTE_REEMPLAZAR = r'''
curl -X POST http://localhost:8000/api/payroll/create_payroll_adjustment \
  -H "Content-Type: application/json" \
  -d '{
  "TipoNota": "1",
  "Predecesor": {
    "NumeroPred": "NE5",
    "CUNEPred": "74067f57d2dd53ec7a55af04c6c9e5efdaab65ebc32d18407e7d818c7c3596d968d4869d172fcc74474b5cd4b2e62a3f",
    "FechaGenPred": "2024-02-01"
  },
  "Periodo": {
    "FechaIngreso": "2020-01-15",
    "FechaLiquidacionInicio": "2024-01-01",
    "FechaLiquidacionFin": "2024-01-31",
    "TiempoLaborado": "30",
    "FechaGen": "2024-02-01"
  },
  "NumeroSecuenciaXML": {
    "Prefijo": "NA",
    "Consecutivo": "2",
    "Numero": "NA2"
  },
  "LugarGeneracionXML": {
    "Pais": "CO",
    "DepartamentoEstado": "11",
    "MunicipioCiudad": "11001",
    "Idioma": "es"
  },
  "ProveedorXML": {
    "RazonSocial": "ORBIS GLOBAL TECHNOLOGY",
    "NIT": "901616617",
    "DV": "7",
    "SoftwareID": "7a376f67-222d-480b-9b46-73413c55401a"
  },
  "InformacionGeneral": {
    "Version": "V1.0: Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica",
    "Ambiente": "2",
    "FechaGen": "2024-02-01",
    "HoraGen": "10:00:00-05:00",
    "PeriodoNomina": "5",
    "TipoMoneda": "COP"
  },
  "Empleador": {
    "RazonSocial": "ORBIS GLOBAL TECHNOLOGY",
    "NIT": "901616617",
    "DV": "7",
    "Pais": "CO",
    "DepartamentoEstado": "11",
    "MunicipioCiudad": "11001",
    "Direccion": "Calle 123 # 45-67"
  },
  "Trabajador": {
    "TipoTrabajador": "01",
    "SubTipoTrabajador": "00",
    "AltoRiesgoPension": "false",
    "TipoDocumento": "13",
    "NumeroDocumento": "1015000000",
    "PrimerApellido": "Perez",
    "SegundoApellido": "Gomez",
    "PrimerNombre": "Juan",
    "OtrosNombres": "Carlos",
    "LugarTrabajoPais": "CO",
    "LugarTrabajoDepartamentoEstado": "11",
    "LugarTrabajoMunicipioCiudad": "11001",
    "LugarTrabajoDireccion": "Calle 123 # 45-67",
    "SalarioIntegral": "false",
    "TipoContrato": "2",
    "Sueldo": "2000000.00"
  },
  "Pago": {
    "Forma": "1",
    "Metodo": "42",
    "Banco": "Bancolombia",
    "TipoCuenta": "AH",
    "NumeroCuenta": "1234567890"
  },
  "FechasPagos": ["2024-01-31"],
  "Devengados": {
    "Basico": {
      "DiasTrabajados": "30",
      "SueldoTrabajado": "2000000.00"
    },
    "Transporte": [
      { "AuxilioTransporte": "162000.00" }
    ]
  },
  "Deducciones": {
    "Salud": { "Porcentaje": "4.00", "Deduccion": "80000.00" },
    "FondoPension": { "Porcentaje": "4.00", "Deduccion": "80000.00" }
  },
  "DevengadosTotal": "2162000.00",
  "DeduccionesTotal": "160000.00",
  "ComprobanteTotal": "2002000.00",
  "Pin": "202677",
  "TestID": "2909e1cc-f6ce-4a0f-9f3f-a0376007af27"
}'
'''


# ---------------------------------------------------------------------------
# NOTA DE AJUSTE - opción ELIMINAR (TipoNota "2")
#
# Anula una nómina ya enviada. Es un documento REDUCIDO: no lleva Trabajador,
# Pago, FechasPagos, Devengados, Deducciones ni totales -- solo identifica la
# nómina a anular. El CUNE de este documento se calcula con 0.00 en los
# totales y 0 en el documento del empleado (lo exige el anexo); el código lo
# hace solo, no hay que mandar esos campos.
CURL_AJUSTE_ELIMINAR = r'''
curl -X POST http://localhost:8000/api/payroll/create_payroll_adjustment \
  -H "Content-Type: application/json" \
  -d '{
  "TipoNota": "2",
  "Predecesor": {
    "NumeroPred": "NE6",
    "CUNEPred": "PEGAR-AQUI-EL-CUNE-DE-NE6",
    "FechaGenPred": "2024-02-01"
  },
  "NumeroSecuenciaXML": {
    "Prefijo": "NA",
    "Consecutivo": "3",
    "Numero": "NA3"
  },
  "LugarGeneracionXML": {
    "Pais": "CO",
    "DepartamentoEstado": "11",
    "MunicipioCiudad": "11001",
    "Idioma": "es"
  },
  "ProveedorXML": {
    "RazonSocial": "ORBIS GLOBAL TECHNOLOGY",
    "NIT": "901616617",
    "DV": "7",
    "SoftwareID": "7a376f67-222d-480b-9b46-73413c55401a"
  },
  "InformacionGeneral": {
    "Version": "V1.0: Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica",
    "Ambiente": "2",
    "FechaGen": "2024-02-01",
    "HoraGen": "10:00:00-05:00",
    "PeriodoNomina": "5",
    "TipoMoneda": "COP"
  },
  "Empleador": {
    "RazonSocial": "ORBIS GLOBAL TECHNOLOGY",
    "NIT": "901616617",
    "DV": "7",
    "Pais": "CO",
    "DepartamentoEstado": "11",
    "MunicipioCiudad": "11001",
    "Direccion": "Calle 123 # 45-67"
  },
  "Pin": "202677",
  "TestID": "2909e1cc-f6ce-4a0f-9f3f-a0376007af27"
}'
'''

if False:  # pragma: no cover - solo documentación, no se ejecuta
    print(CURL_HABILITACION_EJEMPLO)
