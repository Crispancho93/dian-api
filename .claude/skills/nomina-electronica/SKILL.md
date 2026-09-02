---
name: nomina-electronica
description: Conocimiento operativo de Nómina Electrónica DIAN Colombia (NominaIndividual TipoXML 102 y NominaIndividualDeAjuste TipoXML 103) en este repo. Usar al trabajar con cualquier cosa de nómina - endpoints /api/payroll/*, CUNE, firma XAdES, envío al set de pruebas o producción, errores NIExxx/NIAExxx/ZB01/Regla 92 de la DIAN, la tabla client con certificados, o al depurar rechazos. También al agregar campos nuevos a Devengados/Deducciones.
---

# Nómina Electrónica DIAN

Conocimiento destilado de implementar y hacer aceptar documentos reales en habilitación.
Documentación de respaldo en `docs/`:

| Archivo | Qué es |
|---|---|
| `docs/NOMINA_ELECTRONICA_ESTADO.md` | Reporte funcional: qué hace el sistema y qué falta |
| `docs/NOMINA_ELECTRONICA.md` | Plan de implementación original + decisiones de diseño |
| `docs/Anexo Tecnico ... V1.0.md` | La norma (9067 líneas). **Tiene erratas — ver abajo** |
| `docs/Nomina Individual Electronica V1.0.2.xml` | **Ejemplo oficial DIAN. Referencia estructural definitiva** |
| `docs/Nomina Individual De Ajuste Electronica V1.0.2.xml` | Ídem para la nota de ajuste |

## Regla de oro

**Cuando el anexo y el XML de ejemplo oficial se contradigan, gana el XML de ejemplo.
Cuando se trate del web service, gana el WSDL.** Ambas cosas costaron rechazos reales.

```
https://vpfe-hab.dian.gov.co/WcfDianCustomerServices.svc?wsdl
```

## Endpoints

```
POST /api/payroll/create_payroll              NominaIndividual        (TipoXML 102)
POST /api/payroll/create_payroll_adjustment   NominaIndividualDeAjuste (TipoXML 103)
```

Flujo interno (`CreatePayrollCase` → `CreatePayrollAdjustmentCase` hereda de él):
certificado por NIT → CUNE + SoftwareSC → construir XML → firmar XAdES → zip → guardar → enviar.

## Envío: set de pruebas vs producción

Esto es lo que más tiempo costó descubrir. Según el **WSDL**:

| Operación | Parámetros | Uso |
|---|---|---|
| `SendNominaSync` | **solo** `contentFile` | Producción/operación |
| `SendTestSetAsync` | `fileName`, `contentFile`, **`testSetId`** | Set de pruebas (habilitación) |

El anexo solo documenta `SendNominaSync`, y **no menciona el set de pruebas de nómina**. Meter
`<wcf:testSetId>` dentro de `SendNominaSync` NO funciona: no está en el schema, la DIAN lo ignora,
trata el envío como producción y responde `Regla 92: El Emisor no se encuentra Habilitado`.

El código decide solo: si el DTO trae `TestID` → `SendTestSetAsync`; si no → `SendNominaSync`.

**`SendTestSetAsync` es asíncrono**: devuelve un `ZipKey`, no el veredicto. Para saber si fue
aceptada hay que consultar aparte:

```python
case.get_status("<ZipKey>")   # GetStatusZip
# buscar: IsValid=true, StatusCode=00, "ha sido autorizada"
```

## Errores DIAN → causa real

| Error | Causa | Solución |
|---|---|---|
| `Regla 92: Emisor no Habilitado` | Se usó `SendNominaSync` para pruebas | Mandar `TestID` para que use `SendTestSetAsync` |
| `ZB01: Attribute 'SchemaLocation' must appear` | Falta el atributo `SchemaLocation=""` en el root | Está en el template; no quitarlo aunque parezca redundante con `xsi:schemaLocation` |
| `NIE901: debe poseer Todos los Namespace` | Falta algún namespace en el root (típicamente `xmlns:xs`) | El root debe declarar los 6: default, `xs`, `ds`, `ext`, `xades`, `xades141`, `xsi` |
| `NIE021: información detallada del documento` | El `CodigoQR` apunta al ambiente equivocado | Hab: `catalogo-vpfe-hab.dian.gov.co`; Prod: `catalogo-vpfe.dian.gov.co` |
| `IsValid=false` **sin mensaje** | El `@Numero` ya fue usado | Subir el consecutivo. Nunca repetir un `@Numero` |
| `NIE017` / `NIE033` (NIT no registrado) | Suelen ser ruido que acompaña a `Regla 92` | Resolver el 92 primero |
| `Invalid certificate chain in PFX` | El `.pfx` (GSE) trae solo el firmante | Poner la cadena CA en `PATH_BASE/certificados/`; `CertificateLoader` la resuelve sola |

## Trampas que fallan en silencio

- **Orden de elementos**: el XSD es una `sequence`. Orden equivocado = rechazo.
  `Redondeo` va **antes** de los totales (el anexo lo lista al final; el ejemplo oficial manda).
- **Nunca** emitir un contenedor sin hijos ni un atributo con valor `None` → rechazo duro del XSD.
  Por eso `PayrollBase.add()` / `add_group()` omiten lo ausente; usarlos siempre.
- **`<ext:ExtensionContent/>` debe quedar vacío y auto-cerrado** en el template: el firmador
  inserta la firma con un `str.replace()` literal. Un espacio adentro y no hay firma.
- **La cadena de namespaces del firmador** (`XmlSignerV3._get_with_schemas`, ramas `'NI'` y `'NA'`)
  debe listar **exactamente** los mismos namespaces que declara el template, en **orden C14N**
  (default primero, luego prefijos alfabéticos: `ds, ext, xades, xades141, xs, xsi`). Otro orden
  produce un digest válido en apariencia pero incorrecto. Si tocás el template, tocá esta cadena
  en el mismo commit.
- El `else` de `_get_with_schemas` cae en namespaces de CreditNote: un `document_type` nuevo sin
  su rama firma mal y el error de la DIAN no lo dice.
- `XmlTemplatesData` es un `NamedTuple`: agregar campos **al final**.

## CUNE

```
CUNE = SHA-384( NumNE + FecNE + HorNE + ValDev + ValDed + ValTolNE
                + NitNE + DocEmp + TipoXML + SoftwarePin + TipAmb )
```
Concatenación sin separadores, hex minúscula. `SoftwarePin` no va en el XML.
Se guarda en `InformacionGeneral/@CUNE` con `@EncripCUNE="CUNE-SHA384"`.

**El ejemplo resuelto del anexo (8.1.1.3) NO reproduce.** Verificado probando la concatenación
documentada, variantes de formato de hora y las 40320 permutaciones de orden de campos, contra
SHA-384/512/256. Es errata. **No escribir tests contra ese hash** — la validación real es que la
DIAN acepte el documento (y acepta).

`SoftwareSC = SHA-384(SoftwareID + Pin + NumeroSecuenciaXML/@Numero)`.

En la nota de ajuste **Eliminar**, el CUNE usa `0.00` en ValDev/ValDed/ValTolNE y `0` en DocEmp.

## Nota de ajuste

`TipoNota` decide la forma del documento:

| TipoNota | Elemento | Contenido |
|---|---|---|
| `"1"` Reemplazar | `<Reemplazar>` | `ReemplazandoPredecesor` + cuerpo **completo** de nómina |
| `"2"` Eliminar | `<Eliminar>` | `EliminandoPredecesor` + solo NumeroSecuenciaXML, LugarGeneracionXML, ProveedorXML, CodigoQR, InformacionGeneral (reducido), Notas, Empleador |

El bloque predecesor (`NumeroPred`, `CUNEPred`, `FechaGenPred`) identifica la nómina original;
el `CUNEPred` es el CUNE que devolvió `create_payroll`.

`PayrollAdjustmentXml` hereda de `PayrollXml` y reusa `_build_body()` colgándolo de `<Reemplazar>`.
`Devengados` y `Deducciones` se reusan sin cambios.

## Catálogos (los que más se usan)

| Campo | Valores |
|---|---|
| `Ambiente` | 1=Producción, 2=Pruebas/Habilitación |
| `TipoXML` | 102=NominaIndividual, 103=DeAjuste |
| `TipoNota` | 1=Reemplazar, 2=Eliminar |
| `TipoDocumento` (trabajador) | 11 RC, 12 TI, 13 CC, 22 CE, 31 NIT, 41 Pasaporte, 47 PEP, 91 NUIP |
| `TipoTrabajador` | 01 Dependiente, 02 Servicio doméstico, 04 Madre comunitaria, 12/19 Aprendiz SENA, 23 Estudiante, 51 Tiempo parcial |
| `SubTipoTrabajador` | 00 No aplica, 01 Pensionado por vejez activo |
| `TipoContrato` | 1 Fijo, 2 Indefinido, 3 Obra/labor, 4 Aprendizaje, 5 Prácticas |
| `PeriodoNomina` | 1 Semanal, 2 Decenal, 3 Catorcenal, 4 Quincenal, 5 Mensual, 6 Otro |
| `Pago.Forma` | 1 Contado |
| `Pago.Metodo` | 10 Efectivo, 20 Cheque, 42 Consignación, 47 Transferencia, 48/49 Tarjeta |
| Horas extra `Porcentaje` | HED 25.00, HEN 75.00, HRN 35.00, HEDDF 100.00, HRDDF 75.00, HENDF 150.00, HRNDF 110.00 |

Obligatorios mínimos: `Devengados/Basico`, `Deducciones/Salud`, `Deducciones/FondoPension`.
Todo lo demás es opcional y se omite si no viene.

## Certificados

`GetClientByNitOnlyCase` busca en la tabla `client` por **NIT** (no por resolución — nómina no
tiene resolución; el `GetClientByNitCase` de factura sí busca por `resolucion` pese al nombre).

`CertificateLoader` arma la cadena firmante→emisor→raíz buscando: los certificados embebidos en
el `.pfx`, luego los `.crt`/`.cer`/`.pem` junto al `.pfx`, luego `PATH_BASE/certificados/`.
Los `.pfx` de GSE solo traen el firmante; la cadena (`CA_SUB01.crt`, `CA_ROOT.crt`) va en la
carpeta compartida.

## Archivos

```
domain/dtos/payroll_dto.py                  PayrollDto, PayrollAdjustmentDto
domain/xml_models/payroll/
  payroll_base.py       add()/add_group() — omiten lo ausente
  payroll_xml.py        orden de elementos, CUNE/QR, _build_body()
  payroll_adjustment_xml.py
  devengados.py / deducciones.py
application/use_cases/payroll/
  create_payroll_case.py              (XML_CLASS, DOCUMENT_TYPE, FILE_PREFIX)
  create_payroll_adjustment_case.py
application/use_cases/soap/soap_payroll.py  SoapPayrollRequest / TestRequest / StatusZipRequest
shared/xml_models/NominaIndividual*.xml     templates esqueleto
shared/generic.py                           get_cune, get_payroll_file_names, extract_zip_key
test_payroll_cune.py                        tests + curls de referencia (nómina y ajuste)
```

Nombres de archivo: `nie` + NIT(10, con ceros) + `aa` + 8 hex para nómina, `niae`… para ajuste;
zip siempre `z` + NIT(10) + `aa` + 8 hex.

## Pendiente conocido

La política de firma de nómina usa el digest de la política de factura v1 como provisional
(`TODO` en `xml_signerv3.py`). La DIAN acepta los documentos igual, pero convendría calcular
`base64(sha256(pdf))` del PDF real de la política v2.
