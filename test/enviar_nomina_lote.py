"""
Envío de nómina para VARIOS empleados, leyendo test/nomina_masiva.json.

La DIAN no tiene envío por lote: /Trabajador es 1-1 y SendNominaSync transmite
"1 documento electrónico" por zip. O sea, N empleados = N documentos = N envíos,
cada uno con su propio @Numero (consecutivo único) y su propio CUNE.

Uso (desde cualquier carpeta):
    python test/enviar_nomina_lote.py            # DRY RUN: arma y firma, NO envía
    python test/enviar_nomina_lote.py --enviar   # envía de verdad a la DIAN
"""
import os
import sys
import json
import time

# El repo se importa desde su raíz y los templates se resuelven contra el CWD
# (shared/xml_files.py usa os.path.abspath(os.curdir)), así que fijamos ambos.
_RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _RAIZ)
os.chdir(_RAIZ)

import app  # noqa: F401,E402  (resuelve el import circular de shared/__init__.py)
from shared import templates_loader  # noqa: E402
from shared.certificate import CertificateLoader  # noqa: E402
from application.use_cases.client.get_client_by_nit_only_case import GetClientByNitOnlyCase  # noqa: E402
from application.use_cases import CreatePayrollCase  # noqa: E402
from application.use_cases.soap.soap_payroll import SoapStatusZipRequest  # noqa: E402
from domain.dtos import PayrollDto  # noqa: E402
from lxml import etree  # noqa: E402

ARCHIVO = os.path.join(_RAIZ, 'test', 'nomina_masiva.json')
DIAN_NS = '{http://schemas.datacontract.org/2004/07/DianResponse}'


def armar_payload(comunes, empleado, prefijo, consecutivo):
    """Expande un empleado del JSON a un payload completo de PayrollDto."""
    sueldo = float(empleado['Sueldo'])
    dias = empleado.get('DiasTrabajados', '30')
    # Si trabajó menos del mes, el sueldo devengado puede venir explícito
    sueldo_trabajado = float(empleado.get('SueldoTrabajado', sueldo))
    transporte = float(empleado.get('AuxilioTransporte', 0) or 0)

    # Deducciones: explícitas si vienen, si no 4% del sueldo devengado
    salud = float(empleado['Salud']) if 'Salud' in empleado else round(sueldo_trabajado * 0.04, 2)
    pension = float(empleado['FondoPension']) if 'FondoPension' in empleado else round(sueldo_trabajado * 0.04, 2)

    devengados = {
        'Basico': {
            'DiasTrabajados': str(dias),
            'SueldoTrabajado': f'{sueldo_trabajado:.2f}',
        }
    }
    if transporte > 0:
        devengados['Transporte'] = [{'AuxilioTransporte': f'{transporte:.2f}'}]

    horas_extra = empleado.get('HorasExtraDiurnas')
    if horas_extra:
        devengados['HEDs'] = horas_extra

    pago_extras = sum(float(h['Pago']) for h in (horas_extra or []))

    devengado_total = round(sueldo_trabajado + transporte + pago_extras, 2)
    deduccion_total = round(salud + pension, 2)
    comprobante_total = round(devengado_total - deduccion_total, 2)

    trabajador = {
        'TipoTrabajador': empleado.get('TipoTrabajador', '01'),
        'SubTipoTrabajador': empleado.get('SubTipoTrabajador', '00'),
        'AltoRiesgoPension': empleado.get('AltoRiesgoPension', 'false'),
        'TipoDocumento': empleado.get('TipoDocumento', '13'),
        'NumeroDocumento': empleado['NumeroDocumento'],
        'PrimerApellido': empleado['PrimerApellido'],
        'PrimerNombre': empleado['PrimerNombre'],
        'LugarTrabajoPais': 'CO',
        'LugarTrabajoDepartamentoEstado': comunes['Empleador']['DepartamentoEstado'],
        'LugarTrabajoMunicipioCiudad': comunes['Empleador']['MunicipioCiudad'],
        'LugarTrabajoDireccion': comunes['Empleador']['Direccion'],
        'SalarioIntegral': empleado.get('SalarioIntegral', 'false'),
        'TipoContrato': empleado.get('TipoContrato', '2'),
        'Sueldo': f'{sueldo:.2f}',
    }
    for opcional in ('SegundoApellido', 'OtrosNombres'):
        if empleado.get(opcional):
            trabajador[opcional] = empleado[opcional]

    return {
        'Periodo': comunes['Periodo'],
        'NumeroSecuenciaXML': {
            'Prefijo': prefijo,
            'Consecutivo': str(consecutivo),
            'Numero': f'{prefijo}{consecutivo}',
        },
        'LugarGeneracionXML': comunes['LugarGeneracionXML'],
        'ProveedorXML': comunes['ProveedorXML'],
        'InformacionGeneral': comunes['InformacionGeneral'],
        'Empleador': comunes['Empleador'],
        'Trabajador': trabajador,
        'Pago': comunes['Pago'],
        'FechasPagos': comunes['FechasPagos'],
        'Devengados': devengados,
        'Deducciones': {
            'Salud': {'Porcentaje': '4.00', 'Deduccion': f'{salud:.2f}'},
            'FondoPension': {'Porcentaje': '4.00', 'Deduccion': f'{pension:.2f}'},
        },
        'DevengadosTotal': f'{devengado_total:.2f}',
        'DeduccionesTotal': f'{deduccion_total:.2f}',
        'ComprobanteTotal': f'{comprobante_total:.2f}',
        'Pin': comunes['Pin'],
        'TestID': comunes.get('TestID'),
    }


def consultar_estado(loader, zip_key):
    resp = SoapStatusZipRequest(loader.security).get_status(zip_key)
    tree = etree.fromstring(resp.text.encode())
    valido = tree.find(f'.//{DIAN_NS}IsValid')
    msg = tree.find(f'.//{DIAN_NS}StatusMessage')
    errores = [e.text for e in tree.findall(
        './/{http://schemas.microsoft.com/2003/10/Serialization/Arrays}string') if e.text]
    aceptada = valido is not None and valido.text == 'true'
    detalle = (msg.text if msg is not None else '') or ''
    if not aceptada and errores:
        detalle = ' | '.join(errores)
    return aceptada, detalle


def main(enviar: bool):
    with open(ARCHIVO, encoding='utf-8') as f:
        cfg = json.load(f)

    comunes = cfg['comunes']
    empleados = cfg['empleados']
    prefijo = cfg.get('prefijo', 'NE')
    consecutivo = int(cfg.get('consecutivo_inicial', 1))

    templates_loader.load()
    loader = CertificateLoader(GetClientByNitOnlyCase)

    modo = 'ENVÍO REAL' if enviar else 'DRY RUN (no se envía nada)'
    ambiente = comunes['InformacionGeneral']['Ambiente']
    print(f'== {modo} ==')
    print(f'   {len(empleados)} empleados | consecutivo desde {consecutivo} | '
          f'Ambiente {ambiente} ({"pruebas" if ambiente == "2" else "PRODUCCIÓN"})\n')

    enviados = []
    for i, empleado in enumerate(empleados):
        numero_actual = consecutivo + i
        quien = f"{empleado['PrimerNombre']} {empleado['PrimerApellido']}"
        payload = armar_payload(comunes, empleado, prefijo, numero_actual)

        try:
            case = CreatePayrollCase(PayrollDto(**payload), loader)
        except Exception as e:
            print(f'  {prefijo}{numero_actual:<6} {quien:<22} ERROR al preparar: {str(e)[:80]}')
            continue

        if not enviar:
            case.xml.build(case.payroll, case._cune, case._software_sc)
            print(f'  {prefijo}{numero_actual:<6} {quien:<22} '
                  f'total={payload["ComprobanteTotal"]:>12}  CUNE={case.cune[:16]}...')
            continue

        try:
            res = case.start()
            zip_key = res['payroll'].get('ZipKey')
            enviados.append((f'{prefijo}{numero_actual}', quien, zip_key))
            print(f'  {prefijo}{numero_actual:<6} {quien:<22} enviado  ZipKey={zip_key}')
        except Exception as e:
            print(f'  {prefijo}{numero_actual:<6} {quien:<22} ERROR al enviar: {str(e)[:80]}')

    if not enviar:
        print('\nOK: todos los documentos se construyen y firman correctamente.')
        print('Corré con --enviar para mandarlos a la DIAN.')
        return

    if not enviados:
        print('\nNo se envió ningún documento.')
        return

    print('\nEsperando validación de la DIAN...')
    time.sleep(10)

    print('\n== RESULTADOS ==')
    aceptadas = 0
    for numero, quien, zip_key in enviados:
        if not zip_key:
            print(f'  {numero:<8} {quien:<22} (producción, sin ZipKey)')
            continue
        try:
            ok, detalle = consultar_estado(loader, zip_key)
            aceptadas += ok
            print(f'  {numero:<8} {quien:<22} {"ACEPTADA" if ok else "RECHAZADA":<10} {detalle[:70]}')
        except Exception as e:
            print(f'  {numero:<8} {quien:<22} error consultando: {str(e)[:60]}')

    print(f'\n{aceptadas}/{len(enviados)} aceptadas.')


if __name__ == '__main__':
    main(enviar='--enviar' in sys.argv)
