# Nómina Electrónica — Reporte funcional

Estado al 2026-08-13. Branch `nomina`. Complementa a [NOMINA_ELECTRONICA.md](NOMINA_ELECTRONICA.md) (el plan de implementación).

---

## 1. Qué hace hoy

Dos endpoints:

```
POST /api/payroll/create_payroll              → Nómina Electrónica (TipoXML 102)
POST /api/payroll/create_payroll_adjustment   → Nota de Ajuste  (TipoXML 103)
```

Ambos reciben un JSON y hacen **todo el proceso completo** contra la DIAN. Paso a paso, lo que ocurre por dentro:

| # | Paso | Dónde |
|---|---|---|
| 1 | Busca el certificado del empleador **por NIT** en la tabla `client` y desencripta la contraseña del `.pfx` | `GetClientByNitOnlyCase` |
| 2 | Abre el `.pfx` y arma la cadena de certificados (firmante + emisor + raíz) | `CertificateLoader` |
| 3 | Calcula el **CUNE** (SHA-384 de 11 campos concatenados) y el **SoftwareSC** (SHA-384 de SoftwareID+Pin+Numero) | `CreatePayrollCase` |
| 4 | Construye el XML `NominaIndividual` completo, omitiendo todo grupo opcional que no venga en el JSON | `PayrollXml` |
| 5 | Firma el XML con XAdES-EPES (firma enveloped dentro de `ext:UBLExtensions`) | `XmlSignerV3` (rama `'NI'`) |
| 6 | Comprime el XML firmado en `.zip` y lo pasa a base64 | `generic.zip_document` |
| 7 | Guarda una copia del `.zip` en `PATH_BASE/<NIT>/XMLNomina/` (en segundo plano) | `generic.write_file_from_base64` |
| 8 | **Envía a la DIAN** por SOAP | ver abajo |

### El paso 8 tiene dos caminos (esto es lo importante)

El código elige solo, según venga o no el campo `TestID` en el JSON:

| Si mandás… | Usa la operación | Para qué sirve |
|---|---|---|
| `TestID` con el TestSetId | **`SendTestSetAsync`** | Set de pruebas del proceso de **habilitación** ← es el que estás usando ahora |
| sin `TestID` | `SendNominaSync` | Producción/operación, una vez habilitado |

`SendTestSetAsync` es **asíncrono**: no responde si el documento fue aceptado, solo devuelve un `ZipKey`. El resultado real se consulta después con `GetStatusZip` usando ese ZipKey.

Respuesta típica del endpoint en modo pruebas:

```json
{
  "messages": [],
  "payroll": {
    "Cune": "74067f57d2dd53ec...",
    "ZipKey": "1f895c72-d5d0-4571-b2a4-ca502cdcb765",
    "FileName": "z09016166172400000005.zip"
  }
}
```

---

## 2. Estado de tu habilitación en la DIAN

Datos del portal (software "orbis", NIT `901616617`, TestSetId `2909e1cc-f6ce-4a0f-9f3f-a0376007af27`):

| Tipo de documento | **Aceptados requeridos** | Estado del código | Aceptadas verificadas |
|---|---|---|---|
| Nómina Electrónica (TipoXML 102) | 4 | ✅ Funcionando | NE5, NE6, NE77 |
| Nómina Electrónica de Ajuste (TipoXML 103) | 4 | ✅ Funcionando | NA-1 |

**Los dos tipos de documento están implementados y aceptados por la DIAN.** Solo queda repetir envíos hasta llegar a 4 aceptados de cada uno.

Historial relevante de la depuración:

| Documento | Resultado |
|---|---|
| NE1, NE2, NE3 | Rechazados — se enviaron por `SendNominaSync` (producción) antes de descubrir que el set de pruebas usa `SendTestSetAsync` |
| NE4 | Rechazado — errores `NIE901` y `NIE021` (ya corregidos) |
| NE5, NE6 | ✅ Autorizadas |
| NE7 | Rechazado — el `@Numero` ya estaba usado. **No repetir consecutivos** |
| NE77 | ✅ Autorizada |
| NA-1 | ✅ Autorizada (nota de ajuste, primera al primer intento) |

---

## 3. Qué falta

Solo **enviar más documentos** hasta completar los 4 aceptados de cada tipo. No falta código.

Regla clave: **el `@Numero` no se puede repetir**. Si mandás uno ya usado, la DIAN lo rechaza sin mensaje descriptivo (así falló NE7). Usá consecutivos nuevos en cada envío.

### Nota de Ajuste — cómo se usa

Tiene dos variantes, controladas por `TipoNota`:

| TipoNota | Qué hace | Qué mandar |
|---|---|---|
| `"1"` Reemplazar | Corrige una nómina previa | Cuerpo **completo** de nómina (igual que `create_payroll`) + `Predecesor` |
| `"2"` Eliminar | Anula una nómina previa | Solo `NumeroSecuenciaXML`, `LugarGeneracionXML`, `ProveedorXML`, `InformacionGeneral`, `Empleador` + `Predecesor` |

El bloque `Predecesor` identifica la nómina que se ajusta:

```json
"TipoNota": "1",
"Predecesor": {
  "NumeroPred": "NE5",
  "CUNEPred": "74067f57d2dd53ec...",
  "FechaGenPred": "2024-02-01"
}
```

El `CUNEPred` es el CUNE que devolvió el endpoint al crear esa nómina. En la variante Eliminar, el CUNE del ajuste se calcula con `0.00` en los totales y `0` en el documento del empleado (lo exige el anexo); el código ya lo hace solo.

---

## 4. Errores que se encontraron y corrigieron

Vale la pena dejarlos escritos porque ninguno era obvio:

| Error DIAN | Causa real | Corrección |
|---|---|---|
| `Regla 92: El Emisor no se encuentra Habilitado` | Se estaba usando `SendNominaSync` (producción) para el set de pruebas. El `testSetId` se había metido **dentro** de `SendNominaSync`, pero según el WSDL esa operación **solo acepta `contentFile`** — la DIAN lo ignoraba. | Usar `SendTestSetAsync`, que sí acepta `testSetId`. Verificado contra el WSDL real, no contra el anexo (el anexo no documenta el set de pruebas de nómina). |
| `ZB01: Attribute 'SchemaLocation' must appear` | Se había omitido el atributo `SchemaLocation=""` del root por considerarlo redundante con `xsi:schemaLocation`. El ejemplo oficial de la DIAN sí lo trae. | Agregado al template. |
| `NIE901: debe poseer Todos los Namespace` | Faltaba `xmlns:xs` en el root (también se había omitido por "redundante"). | Agregado al template **y** a la cadena de namespaces del firmador (el orden importa: C14N los ordena alfabéticamente). |
| `NIE021: información detallada del documento` | El QR apuntaba a `catalogo-vpfe.dian.gov.co` (producción) estando en ambiente de pruebas. | El QR ahora depende de `Ambiente`: `catalogo-vpfe-hab...` si es `2`, `catalogo-vpfe...` si es `1`. |
| `Invalid certificate chain in PFX` | El `.pfx` de GSE trae **solo** el certificado del firmante, sin la cadena. | `CertificateLoader` ahora arma la cadena buscando los `.crt`/`.cer`/`.pem` junto al `.pfx` y en `PATH_BASE/certificados/` (ahí están `CA_SUB01.crt` y `CA_ROOT.crt` de GSE). |
| `FileNotFoundError` al guardar el `.zip` | `write_file_from_base64` no creaba las carpetas. Como corre en un hilo aparte, el error no rompía la petición pero el archivo se perdía en silencio. | Ahora crea la carpeta destino. Aplica también a factura y nota crédito. |

**Sobre el ejemplo de CUNE del anexo:** el hash publicado en la sección 8.1.1.3 no se reproduce con la fórmula que el mismo anexo documenta (se probaron variantes de formato y las 40320 permutaciones de orden de campos). Es errata del documento. La fórmula implementada es la del texto normativo, y quedó validada en la práctica: la DIAN aceptó los documentos.

---

## 5. Cómo enviar la próxima nómina

Levantá el servidor (`uvicorn app:app --reload`) y usá el curl de [test_payroll_cune.py](../test_payroll_cune.py) (constante `CURL_HABILITACION_EJEMPLO`), **subiendo el consecutivo**:

```json
"NumeroSecuenciaXML": { "Prefijo": "NE", "Consecutivo": "7", "Numero": "NE7" }
```

Como la respuesta solo trae el `ZipKey`, para saber si fue aceptada hay que consultar el estado:

```python
case.get_status("<ZipKey>")   # devuelve el XML de GetStatusZip
```

Buscá en esa respuesta `IsValid: true` y `StatusMessage: La Nomina Individual NE-7, ha sido autorizada.`

---

## 6. Archivos del sistema

**Nuevos:**
```
domain/dtos/payroll_dto.py                          DTOs (~30 sub-modelos) + PayrollAdjustmentDto
domain/xml_models/payroll/                          Constructor del XML
  ├─ payroll_base.py                                Helpers (omite lo ausente)
  ├─ payroll_xml.py                                 Orden de elementos + CUNE/QR
  ├─ payroll_adjustment_xml.py                      Nota de ajuste (hereda de PayrollXml)
  ├─ devengados.py                                  Bloque <Devengados>
  └─ deducciones.py                                 Bloque <Deducciones>
application/use_cases/payroll/
  ├─ create_payroll_case.py                         Orquestación (nómina)
  └─ create_payroll_adjustment_case.py              Nota de ajuste (hereda del anterior)
application/use_cases/soap/soap_payroll.py          3 clases SOAP
application/use_cases/client/get_client_by_nit_only_case.py  Certificado por NIT
interfaces/api/routes/payroll_routes.py             2 endpoints
shared/xml_models/NominaIndividual.xml              Template esqueleto nómina
shared/xml_models/NominaIndividualDeAjuste.xml      Template esqueleto ajuste
test_payroll_cune.py                                Tests + curl de referencia
```

**Modificados (aditivos, sin romper factura ni nota crédito):**
```
shared/xml_files.py          + 5 templates (nómina, ajuste, set pruebas, GetStatusZip)
shared/generic.py            + get_cune, get_payroll_file_names, extract_zip_key
shared/certificate.py        + resolución de cadena de certificados
application/use_cases/sign_docs/xml_signerv3.py    + ramas 'NI' y 'NA'
application/use_cases/sign_docs/template_xades.py  política parametrizable
app.py, interfaces/api/__init__.py, domain/dtos/__init__.py, ...  wiring
```

Se verificó tras cada cambio que **factura (`FV`) y nota crédito (`NC`) siguen firmando igual** que antes.

### Pendiente menor

- La política de firma para nómina usa el digest de la política de factura (v1) como valor provisional. Está marcado con un `TODO` en `xml_signerv3.py`. La DIAN aceptó los documentos igual, pero convendría calcular el digest real del PDF de la política v2.
- `shared/generic.py` tiene el fix de `makedirs` sin commitear.
