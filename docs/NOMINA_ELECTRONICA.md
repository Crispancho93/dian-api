# Nómina Electrónica DIAN (NominaIndividual) — Plan de implementación

## Contexto

La API hoy emite **Factura** (`FV`) y **Nota Crédito** (`NC`) a la DIAN. Se necesita agregar el **Documento Soporte de Pago de Nómina Electrónica** (Resolución 000013 de 2021, Anexo Técnico V1.0).

Fuentes de verdad en el repo (leerlas, no asumir):
- `Anexo Tecnico Documento Soporte de Pago de Nómina Electrónica - V1.0.md` — la norma (9067 líneas).
- `Nomina Individual Electronica V1.0.2.xml` — **ejemplo oficial de la DIAN con todos los campos poblados**. Esta es la referencia estructural definitiva: el orden de los elementos sale de acá, no del anexo.
- `Nomina Individual De Ajuste Electronica V1.0.2.xml` — ejemplo de la nota de ajuste (fase 2).

**Alcance de esta fase:** solo `NominaIndividual` (TipoXML=`102`). La `NominaIndividualDeAjuste` (TipoXML=`103`) queda para fase 2 — al final se indican las costuras.

## Decisiones ya tomadas (no re-preguntar)

| Tema | Decisión |
|---|---|
| Alcance | Solo `NominaIndividual`. Ajuste diferido. |
| Certificado | Nuevo caso de uso que busca por **NIT** (`GetClientByNitOnlyCase`). No tocar `GetClientByNitCase`, que busca por `resolucion` y del que dependen las facturas. |
| SoftwareID / PIN | Vienen en el **payload del request**, igual que hoy en factura. Sin cambios de BD. |

## Lo que hace a nómina DISTINTA de factura (leer antes de copiar nada)

Es el punto donde más fácil se rompe todo:

1. **No es UBL.** No hay namespaces `cbc:`, `cac:` ni `sts:`. No existe `sts:DianExtensions`. Todos los helpers de factura que hacen xpath contra `//cbc:...` o `//sts:...` son **inservibles** acá.
2. **Casi todo son atributos sobre elementos vacíos**, no texto de elementos. El workhorse es escribir atributos, no `.text`.
3. **La estructura es mayormente opcional/repetible** (grupos 0-1 y 0-N). La factura tiene forma fija; nómina no.
4. **No hay resolución ni rango de numeración.** El consecutivo lo lleva quien llama.
5. El QR usa `catalogo-vpfe.dian.gov.co` (**con guión**); el código de factura usa `catalogovpfe` (sin guión). No copiar la cadena de factura.

## ⚠️ Riesgos verificados (no perder tiempo acá)

### El ejemplo de CUNE del anexo NO reproduce

El anexo (sección 8.1.1.3) publica un ejemplo resuelto: con los datos `N00001`, `2020-01-16`, `10:53:10-05:00`, `3500000.00`, `1000000.00`, `2500000.00`, `700085371`, `800199436`, `102`, `693`, `1` dice que el CUNE es `16560dc8956122e84ffb743c...`.

**Ese hash no se reproduce.** Ya lo verifiqué: probé la concatenación documentada, 5 variantes de formato de hora, y las 40320 permutaciones del orden de los últimos 8 campos, con SHA-384/512/256. Ninguna da ese resultado. Es errata del documento (le pasa lo mismo a los anexos de CUFE).

**Implicación para vos:** implementá la fórmula **tal como la define el texto normativo** y seguí adelante. **No** escribas un test que afirme contra ese hash publicado — te vas a trabar en algo inalcanzable. La validación real es la respuesta de DIAN en habilitación.

Fórmula normativa a implementar:
```
CUNE = SHA-384( NumNE + FecNE + HorNE + ValDev + ValDed + ValTolNE
                + NitNE + DocEmp + TipoXML + SoftwarePin + TipAmb )
```
(`+` = concatenación de strings, sin separadores; resultado en hex minúscula.)

### Otros puntos que fallan en silencio

- **`XmlSignerV3._get_with_schemas` tiene un `else` que atrapa todo** y le mete namespaces de CreditNote. Si le pasás un `document_type` nuevo sin agregar su rama, firma con los namespaces equivocados y DIAN rechaza con un error de firma que no dice nada útil.
- **El orden de los namespaces en esa cadena no es estético.** C14N los emite con el default (`xmlns=`) primero y luego los prefijos en orden alfabético. Cualquier otro orden produce un digest válido en apariencia pero incorrecto.
- **`<ext:ExtensionContent/>` debe quedar auto-cerrado y vacío** en el template: el firmador inserta la firma con un `str.replace("<ext:ExtensionContent/>", ...)` literal. Un espacio adentro y la firma nunca se inserta (DIAN responde "documento no firmado").
- **`XmlTemplatesData` es un `NamedTuple`**: agregá campos nuevos **al final**, nunca en el medio.
- **Los paths de templates son relativos a `os.path.abspath(os.curdir)`**: la app solo funciona lanzada desde la raíz del repo. Mantené la convención, no la "arregles" en este trabajo.
- **Nunca emitas un elemento contenedor sin hijos, ni un atributo con valor `None`.** Ambos son rechazo duro del XSD. Si un grupo opcional no viene, se omite entero.

## Estructura del documento (del XML de ejemplo oficial)

Orden exacto de los hijos de `/NominaIndividual` — **el XSD es una `sequence`, el orden es obligatorio**:

```
ext:UBLExtensions        ← ya viene del template, nunca recrearlo ni moverlo
Novedad?                 ← @CUNENov + texto "true"/"false"
Periodo                  @FechaIngreso @FechaRetiro? @FechaLiquidacionInicio
                         @FechaLiquidacionFin @TiempoLaborado @FechaGen
NumeroSecuenciaXML       @CodigoTrabajador? @Prefijo? @Consecutivo @Numero
LugarGeneracionXML       @Pais @DepartamentoEstado @MunicipioCiudad @Idioma
ProveedorXML             @RazonSocial @PrimerApellido @SegundoApellido @PrimerNombre
                         @OtrosNombres @NIT @DV @SoftwareID @SoftwareSC
CodigoQR                 ← elemento con TEXTO
InformacionGeneral       @Version @Ambiente @TipoXML @CUNE @EncripCUNE @FechaGen
                         @HoraGen @PeriodoNomina @TipoMoneda @TRM?
Notas*                   ← elemento con texto, 0-N
Empleador                @RazonSocial @PrimerApellido @SegundoApellido @PrimerNombre
                         @OtrosNombres @NIT @DV @Pais @DepartamentoEstado
                         @MunicipioCiudad @Direccion
Trabajador               @TipoTrabajador @SubTipoTrabajador @AltoRiesgoPension
                         @TipoDocumento @NumeroDocumento @PrimerApellido
                         @SegundoApellido @PrimerNombre @OtrosNombres
                         @LugarTrabajoPais @LugarTrabajoDepartamentoEstado
                         @LugarTrabajoMunicipioCiudad @LugarTrabajoDireccion
                         @SalarioIntegral @TipoContrato @Sueldo @CodigoTrabajador?
Pago                     @Forma @Metodo @Banco? @TipoCuenta? @NumeroCuenta?
FechasPagos              → FechaPago+ (elementos con texto)
Devengados
Deducciones
Redondeo?                ← ⚠️ VA ACÁ, ANTES de los totales
DevengadosTotal          ← elementos con TEXTO, no atributos
DeduccionesTotal
ComprobanteTotal
```

`Devengados` y `Deducciones`: copiá la lista completa de grupos, elementos e items directamente del archivo `Nomina Individual Electronica V1.0.2.xml` (líneas 87-259). Tiene absolutamente todos los casos poblados; es más confiable que transcribir las tablas del anexo.

Patrón de los grupos: hay tres formas y hay que respetarlas:
- **Item con atributos**: `<Basico DiasTrabajados="" SueldoTrabajado=""/>`
- **Wrapper + items repetibles**: `<HEDs><HED .../></HEDs>`, `<Incapacidades><Incapacidad .../></Incapacidades>`
- **Elemento simple con texto**: `<Dotacion>0.00</Dotacion>`, y también dentro de wrappers: `<Comisiones><Comision>0.00</Comision></Comisiones>`

Obligatorios: `Devengados/Basico`, `Deducciones/Salud`, `Deducciones/FondoPension`. **Todo lo demás es opcional** y se omite si no viene.

## Pasos de implementación

Ordenados para que la app quede importable/ejecutable después de cada paso.

### 1. Lookup de certificado por NIT (nuevo)

**Nuevo:** `application/use_cases/client/get_client_by_nit_only_case.py`

Copiá `get_client_by_nit_case.py` tal cual; renombrá la clase a `GetClientByNitOnlyCase`, el parámetro `resolucion` → `nit`, y cambiá el where a `(client.c.nit == self.nit) & (client.c.is_active.is_(True))`. Agregá `.order_by(client.c.id)` para que sea determinista si un NIT tiene varias filas. Mantené el `raise LookupError("CLIENT_NOT_FOUND")`.

**No toques `GetClientByNitCase`** — las facturas dependen de su semántica por resolución.

### 2. Template esqueleto (nuevo)

**Nuevo:** `shared/xml_models/NominaIndividual.xml`

```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<NominaIndividual xmlns="dian:gov:co:facturaelectronica:NominaIndividual"
   xmlns:ds="http://www.w3.org/2000/09/xmldsig#"
   xmlns:ext="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"
   xmlns:xades="http://uri.etsi.org/01903/v1.3.2#"
   xmlns:xades141="http://uri.etsi.org/01903/v1.4.1#"
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="dian:gov:co:facturaelectronica:NominaIndividual NominaIndividualElectronicaXSD.xsd">
   <ext:UBLExtensions>
      <ext:UBLExtension>
         <ext:ExtensionContent/>
      </ext:UBLExtension>
   </ext:UBLExtensions>
</NominaIndividual>
```

Notas:
- El ejemplo oficial de la DIAN trae además `xmlns:xs` (duplicado de `xsi`) y un atributo `SchemaLocation=""` espurio. **No los copies** — cada namespace declarado tiene que aparecer después en la cadena del firmador, y de más solo agregan riesgo.
- El ejemplo oficial trae `<ext:UBLExtensions>` **vacío**. Nosotros sí necesitamos el `ext:UBLExtension`/`ext:ExtensionContent` adentro, porque ahí va la firma.
- Solo hay **un** `ext:UBLExtension` (a diferencia de `Generica.xml`, que tiene dos porque el primero lleva `sts:DianExtensions`).

### 3. Loader de templates (modificar, aditivo)

**Modificar:** `shared/xml_files.py`

- Agregá **al final** de `XmlTemplatesData` dos campos: `xml_payroll: str` y `xml_payroll_request: str`, y las dos claves correspondientes al dict `data` de `load()`.
- Nueva property `payroll_template`: copia de `credit_note_template` apuntando a `'NominaIndividual.xml'`.
- Nueva property `template_payroll_request`: copia **literal** de `template_request`, cambiando exactamente dos cosas:
  - `<wsa:Action>http://wcf.dian.colombia/IWcfDianCustomerServices/SendNominaSync</wsa:Action>`
  - el body a `<wcf:SendNominaSync><wcf:contentFile>{contentFile}</wcf:contentFile></wcf:SendNominaSync>`

  Dejá **todos los `wsu:Id` idénticos** — `SoapBase._calculate_digest_value` resuelve el `URI="#id-..."` por `wsu:Id`.

### 4. DTOs (nuevo)

**Nuevo:** `domain/dtos/payroll_dto.py`, siguiendo el estilo de `credit_note_dto.py`.

Reglas duras:
- **Todo valor numérico/monetario es `str`**, nunca `float`. El CUNE hashea strings exactos; un float introduce drift.
- Todo campo es `Optional[...] = None` salvo `Basico` (en Devengados) y `Salud`/`FondoPension` (en Deducciones).
- Grupos repetibles: `Optional[List[XDto]] = None`.

`PayrollDto` top-level: `Periodo, NumeroSecuenciaXML, LugarGeneracionXML, ProveedorXML, InformacionGeneral, Notas: Optional[List[str]], Empleador, Trabajador, Pago, FechasPagos: List[str], Devengados, Deducciones, Redondeo: Optional[str], DevengadosTotal, DeduccionesTotal, ComprobanteTotal, Pin: str`.

`Pin` es insumo del CUNE y del SoftwareSC, **nunca se serializa al XML**.

**Requisito del firmador:** `XmlSignerV3.set_properties` lee `dto.IssueDate` y `dto.IssueTime`. Agregá a `PayrollDto`:

```python
    @property
    def IssueDate(self): return self.InformacionGeneral.FechaGen
    @property
    def IssueTime(self): return self.InformacionGeneral.HoraGen
```

Exportá `PayrollDto` desde `domain/dtos/__init__.py`.

### 5. Helpers CUNE y nombres de archivo (modificar, aditivo)

**Modificar:** `shared/generic.py` — agregá `import hashlib` arriba (hoy no está) y dos funciones puras:

```python
def get_cune(values: dict) -> str:
    """CUNE = SHA-384 de la concatenación definida en el anexo, sección 8.1.1."""
    raw = (values["NumNE"] + values["FecNE"] + values["HorNE"] + values["ValDev"] +
           values["ValDed"] + values["ValTolNE"] + values["NitNE"] + values["DocEmp"] +
           values["TipoXML"] + values["SoftwarePin"] + values["TipAmb"])
    return hashlib.sha384(raw.encode('utf-8')).hexdigest()


def get_payroll_file_names(nit: str, year: str, consecutive: int):
    """nie + NIT(10, con ceros) + aa + 8 hex  →  (nombre_xml, nombre_zip)."""
    base = f"{nit.zfill(10)}{year[-2:]}{consecutive:08X}"
    return (f"nie{base}.xml", f"z{base}.zip")
```

`SoftwareSC` usa la misma forma que ya existe en factura: `SHA-384(SoftwareID + Pin + NumeroSecuenciaXML.Numero)`.

### 6. Firmador: tercera rama (modificar — MÁXIMO RIESGO)

**Modificar:** `application/use_cases/sign_docs/xml_signerv3.py`, método `_get_with_schemas`. Insertá un `elif` **antes** del `else` existente (dejá el `else` como está, para no cambiar el comportamiento de `NC`):

```python
        elif self.document_type == 'NI':
            schema = ('xmlns="dian:gov:co:facturaelectronica:NominaIndividual" '
                      'xmlns:ds="http://www.w3.org/2000/09/xmldsig#" '
                      'xmlns:ext="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2" '
                      'xmlns:xades="http://uri.etsi.org/01903/v1.3.2#" '
                      'xmlns:xades141="http://uri.etsi.org/01903/v1.4.1#" '
                      'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
```

**La cadena tiene que listar exactamente los mismos namespaces que declara el template del paso 2, en orden C14N** (default primero, después prefijos alfabéticos: `ds, ext, xades, xades141, xsi`). Si agregás o quitás un namespace del template, actualizá esta cadena en el mismo commit.

**Política de firma:** el anexo indica para nómina la política v2 con descripción *"Política de firma para nóminas electrónicas de la República de Colombia"*. `template_xades.py` la tiene hardcodeada para factura. Parametrizá `create_signature_template` con defaults iguales a los actuales (para no alterar factura) y pasá los valores de nómina cuando `document_type == 'NI'`. **El digest de la política hay que calcularlo del PDF real** (`base64(sha256(pdf))`), no inventarlo: si no lo podés verificar, dejalo anotado como pendiente y probá primero en habilitación con el valor v1.

### 7. Builders XML (nuevo paquete)

**Nuevo:** `domain/xml_models/payroll/` con `__init__.py`, `payroll_base.py`, `payroll_xml.py`, `devengados.py`, `deducciones.py`.

**Decisión de diseño: esqueleto + construcción dinámica**, NO template poblado + xpath.

Razón: `set_value`/`set_scheme` de los modelos de factura solo mutan nodos **preexistentes** (hacen `if item:` y si no está, no hacen nada en silencio). Como nómina es ~90% grupos opcionales, un template poblado obligaría a *borrar* lo que no se usa, y cada borrado que se te escape viaja como elemento vacío y DIAN lo rechaza. Construir con `etree.SubElement` hace que "ausente" sea el default seguro.

Copiá el patrón de builder de `add_credit_note_line` (en `credit_note_base.py`), **no** el patrón de property setters.

`payroll_base.py`:

```python
class PayrollBase:
    NS = 'dian:gov:co:facturaelectronica:NominaIndividual'

    def __init__(self):
        self.root = etree.fromstring(templates_loader.template.xml_payroll.encode('utf-8'))

    @property
    def get_root(self):
        return self.root

    def q(self, tag):
        return '{' + self.NS + '}' + tag

    def add(self, parent, tag, attrs=None, text=None):
        """Crea un subelemento omitiendo los atributos None/''."""
        el = etree.SubElement(parent, self.q(tag))
        for k, v in (attrs or {}).items():
            if v is not None and v != '':
                el.set(k, str(v))
        if text is not None:
            el.text = str(text)
        return el

    def add_group(self, parent, tag, items, item_tag, attr_fn):
        """Omite el wrapper por completo si items viene vacío o None."""
        if not items:
            return None
        wrapper = etree.SubElement(parent, self.q(tag))
        for it in items:
            self.add(wrapper, item_tag, attr_fn(it))
        return wrapper
```

`payroll_xml.py` — `PayrollXml(PayrollBase)` con `build(dto, cune, software_sc)` que agrega los hijos **en el orden de la sección "Estructura del documento"** de arriba. `ext:UBLExtensions` ya viene del template: no lo toques.

`devengados.py` / `deducciones.py` — una clase cada uno con `build(self, parent, dto)`. Las 7 familias de horas extra comparten firma de atributos, así que resolvelas con un loop:

```python
        hour_attrs = lambda h: {'HoraInicio': h.HoraInicio, 'HoraFin': h.HoraFin,
                                'Cantidad': h.Cantidad, 'Porcentaje': h.Porcentaje,
                                'Pago': h.Pago}
        for wrap, item in (('HEDs','HED'), ('HENs','HEN'), ('HRNs','HRN'),
                           ('HEDDFs','HEDDF'), ('HRDDFs','HRDDF'),
                           ('HENDFs','HENDF'), ('HRNDFs','HRNDF')):
            self.base.add_group(dev, wrap, getattr(d, wrap), item, hour_attrs)
```

y los elementos simples de valor también:

```python
        for tag in ('Dotacion','ApoyoSost','Teletrabajo','BonifRetiro',
                    'Indemnizacion','Reintegro'):
            v = getattr(d, tag, None)
            if v is not None:
                self.base.add(dev, tag, text=v)
```

Exportá `PayrollXml` desde `domain/xml_models/payroll/__init__.py` y desde `domain/xml_models/__init__.py`.

### 8. SOAP (nuevo)

**Nuevo:** `application/use_cases/soap/soap_payroll.py` — copia de `soap_invoice.py`; clase `SoapPayrollRequest(SoapBase)`; `self.xml_template = templates_loader.template.xml_payroll_request`; header `'SOAPAction': 'http://wcf.dian.colombia/IWcfDianCustomerServices/SendNominaSync'`.

Mismo servicio y misma URL (`_config.WEB_SERVICE`), solo cambia la operación. **No modifiques `soap_invoice.py`.**

La respuesta tiene la misma forma que la de factura (`b:IsValid` + `c:string`), así que `generic.extract_errors_invoice` se reusa tal cual.

### 9. Caso de uso (nuevo)

**Nuevo:** `application/use_cases/payroll/create_payroll_case.py` — clase `CreatePayrollCase(payroll: PayrollDto, certificate_loader: CertificateLoader)`, espejo de `create_note_case.py`.

- `__init__`: `certificate_loader.load(payroll.Empleador.NIT)` → `.security`. Calculá y **cacheá** el CUNE acá (`self._cune = ...`); no lo recalcules en cada acceso como hace `create_note_case`.
- Insumos del CUNE: `NumNE`=`NumeroSecuenciaXML.Numero`, `FecNE`=`InformacionGeneral.FechaGen`, `HorNE`=`InformacionGeneral.HoraGen`, `ValDev`=`DevengadosTotal`, `ValDed`=`DeduccionesTotal`, `ValTolNE`=`ComprobanteTotal`, `NitNE`=`Empleador.NIT`, `DocEmp`=`Trabajador.NumeroDocumento`, `TipoXML`=`'102'`, `SoftwarePin`=`Pin`, `TipAmb`=`InformacionGeneral.Ambiente`.
- `InformacionGeneral/@EncripCUNE` = `"CUNE-SHA384"` (constante).
- `CodigoQR` = `https://catalogo-vpfe.dian.gov.co/document/searchqr?documentkey={cune}` — **con guión**.
- `start()`: construir XML → `XmlSignerV3(self.xml.get_root, self.payroll, 'NI', self._security).sign()` → `generic.zip_document(...)` → hilo en background con `generic.write_file_from_base64` → `SoapPayrollRequest(security).send_xml(zip)` → `generic.extract_errors_invoice(response.text)` → si `is_valid == 'false'`, `raise`. Devolver `{'messages': messages, 'payroll': {'Cune': self._cune}}`.
- Ruta de guardado: `os.path.join(_config.PATH_BASE, payroll.Empleador.NIT, 'XMLNomina', xml_name)`. **`write_file_from_base64` no crea directorios**: creá `XMLNomina` en el deploy, o envolvé el target del hilo en try/except (si no, el archivo se pierde en silencio porque el error muere en el thread).

Exportá `CreatePayrollCase` desde `application/use_cases/__init__.py`.

### 10. Ruta y wiring

**Nuevo:** `interfaces/api/routes/payroll_routes.py` — `APIRouter(prefix="/api/payroll", tags=["payroll"])`, handler `POST /create_payroll` con la forma del handler de nota crédito pero con `Depends(lambda: CertificateLoader(GetClientByNitOnlyCase))`.

**Modificar:** `interfaces/api/__init__.py` (agregar `payroll_routes` al import) y `app.py` (import + `app.include_router(payroll_routes.router)`).

## Verificación

En este orden:

1. **CUNE — test de estabilidad, no de valor.** Escribí un test que fije la fórmula (misma entrada → mismo hash, longitud 96, hex minúscula). **No** afirmes contra el hash publicado en el anexo: ya está verificado que no reproduce (ver sección de riesgos).

2. **Forma del XML, offline.** Construí `PayrollXml` con dos fixtures: una "completa" (todos los grupos) y una **mínima** (solo `Basico` + `Salud` + `FondoPension`). Serializá con `pretty_print=True` y compará contra `Nomina Individual Electronica V1.0.2.xml`. Comprobá: (a) ningún wrapper quedó sin hijos, (b) ningún atributo quedó en `None`, (c) el orden de los hijos del root coincide, (d) `assert '<ext:ExtensionContent/>' in xml_str` — si esto falla, la firma nunca se va a insertar.

3. **Firma.** Después de `sign()`, verificá que la salida contiene `<ds:Signature` y que re-parsea bien con lxml. Si conseguís el pack de XSD de la DIAN (`NominaIndividualElectronicaXSD.xsd`), validá con `etree.XMLSchema` — es lo que más rápido caza los errores de orden y de grupos vacíos, y te ahorra viajes a DIAN.

4. **End-to-end en habilitación**, en este orden:
   1. `InformacionGeneral/@Ambiente = "2"` y `WEB_SERVICE` apuntando a `vpfe-hab` (ya está así en `k8s/invoice-api.env`).
   2. Enviá primero el documento **mínimo** — solo `Basico`, `Salud`, `FondoPension` — para aislar problemas de firma/SOAP de problemas de contenido.
   3. Con `IsValid=true`, agregá un grupo opcional por envío (Transporte → horas extra → vacaciones → deducciones opcionales).
   4. Recién ahí pasá a `@Ambiente = "1"`.

## Fase 2 diferida: NominaIndividualDeAjuste (TipoXML 103)

Costuras ya previstas — no hace falta rediseñar nada:
- El root es `NominaIndividualDeAjuste` con namespace `dian:gov:co:facturaelectronica:NominaIndividualDeAjuste`: solo cambia la URI del default. Se agrega otra rama `elif document_type == 'NA'` en `_get_with_schemas`.
- La estructura es `TipoNota` (1=Reemplazar, 2=Eliminar) + una rama `Reemplazar` o `Eliminar` que contiene `ReemplazandoPredecesor`/`EliminandoPredecesor` (`@NumeroPred @CUNEPred @FechaGenPred`) seguido de una copia completa del cuerpo de nómina.
- `Devengados` y `Deducciones` se reusan **sin cambios** (solo cuelgan de otro padre).
- Mismo `SoapPayrollRequest`: la operación `SendNominaSync` es la misma.
- `get_cune` ya recibe `TipoXML` como parámetro; para `Eliminar`, el anexo indica que `ValDev`/`ValDed`/`ValTolNE` van en `0.00` literal y `DocEmp` en `0`.
