# Contexto de sesión — para retomar en otra carpeta/clon

Este archivo es un resumen para que una sesión nueva de Claude Code (en otro subfolder u otro
clon de este repo) recupere el contexto sin tener que re-derivarlo. Pegale este archivo a Claude
al empezar, o decile que lo lea primero.

**No duplica la documentación técnica profunda** — esa ya está en el repo y sigue siendo la
fuente de verdad. Este archivo es el mapa de "qué se hizo y dónde está".

## Estado del repo (2026-08-29)

- Branch: `feature/certificado-multi-empresa`, 9 commits por delante de `origin` (sin pushear).
- La branch `nomina` (donde se desarrolló nómina por separado) ya está fusionada acá.
- Único cambio sin commitear: `.env` (credenciales locales de dev — normal, no se commitea).
- Repo hermano relacionado: `C:\Users\Crispancho\Documents\GitHub\orbis\FactuarcionElectronica`
  — fork de este proyecto, **sin multiempresa** (un solo certificado por config, no por NIT/DB).
  Nómina y Documento Soporte se migraron en ambas direcciones entre los dos repos (ver abajo).

## Líneas de trabajo de esta sesión, en orden

### 1. Deploy k8s + CI/CD para esta API
Se armó `k8s/` (Deployment, Service, HTTPRoute, Certificate, `apply-invoice-api.sh`) y se corrigió
`.github/workflows/invoice-deploy.yml` (era una copia desactualizada del pipeline de Odoo).
Se movieron las variables de entorno de `.env` a `k8s/invoice-api.env` (inyectadas como env vars
del pod, que tienen prioridad sobre `.env` en pydantic-settings). Se agregó `.dockerignore` y se
sacó `.env` del tracking de git.

### 2. Bugs de factura corregidos
- **`schemeID` de `//cbc:UUID` no reflejaba el ambiente** → rechazo DIAN `FAD07`/`CAD07`. Fix en
  `domain/xml_models/invoice/invoice_control.py` y `domain/xml_models/credit_note/control.py`.
- **Impoconsumo (INC) no se reflejaba en el CUFE** → nueva función `get_cufe_tax_amounts()` en
  `shared/generic.py`, usada en `create_invoice_case.py` y `create_note_case.py`.
- **`/send_test` sin `certificate_loader`** en `invoice_routes.py` → agregado el `Depends` que le
  faltaba.
- **`get_clave_tecnica`** devolvía 500 genérico ante `CLIENT_NOT_FOUND` → ahora 404 con mensaje.

### 3. Nómina Electrónica DIAN — completa y probada en vivo
Esto es lo más grande de la sesión. Documentación específica, **leer antes de tocar nómina**:

- **`.claude/skills/nomina-electronica/SKILL.md`** — el skill se activa solo al trabajar con
  nómina. Tiene la tabla de errores DIAN → causa real, los catálogos, las trampas silenciosas
  (orden de namespaces C14N, `SchemaLocation`, etc.) y la regla de oro: cuando el anexo y el XML
  de ejemplo oficial se contradicen, gana el ejemplo; cuando se trata del web service, gana el WSDL.
- **`docs/NOMINA_ELECTRONICA.md`** — plan de implementación original.
- Implementado: `NominaIndividual` (TipoXML 102) y `NominaIndividualDeAjuste` (TipoXML 103,
  variantes Reemplazar/Eliminar). Endpoints `/api/payroll/create_payroll` y
  `/create_payroll_adjustment`.
- **Probado end-to-end contra DIAN real** (ambiente de habilitación, empresa ORBIS GLOBAL
  TECHNOLOGY, NIT 901616617): nóminas NE5, NE6, NE77 y ajuste NA-1 **autorizadas por la DIAN**.
  El set de pruebas de esa empresa quedó **Aceptado** (habilitación completada).
- Descubrimiento clave (no está en el anexo, se verificó contra el WSDL real): el set de pruebas
  de nómina usa `SendTestSetAsync` (con `testSetId`), NO `SendNominaSync` (que según el WSDL solo
  acepta `contentFile`). Meter el testSetId en `SendNominaSync` da `Regla 92: Emisor no Habilitado`.
- Scripts/ejemplos en `test/`: `test_payroll_cune.py` (tests + curls), `enviar_nomina_lote.py`
  (N empleados = N documentos, la DIAN no tiene envío por lote), `nomina_masiva.json`,
  `nota_ajuste_reemplazar.json`, `nota_ajuste_eliminar.json`.

### 4. Documento Soporte — traído de vuelta desde orbis/FactuarcionElectronica
`POST /api/invoice/create_documento_soporte`. Adaptado a la estructura multiempresa de este repo
(certificado por `CertificateLoader(GetClientByNitCase)` en vez del singleton de config que usa
orbis). Archivos: `domain/dtos/documento_soporte_dto.py`,
`domain/xml_models/documento_soporte/`, `application/use_cases/invoice/create_documento_soporte_case.py`.

**Fragilidad heredada conocida**: `Customer.VerificationDigit` es opcional en el DTO pero el
builder de XML no valida `None` — si se omite, revienta con `TypeError` poco claro en
`domain/xml_models/documento_soporte/customer.py`. No se arregló (código heredado, fuera de
alcance en su momento).

## Migraciones cruzadas con orbis/FactuarcionElectronica

Se migró código en ambas direcciones entre este repo y `orbis/FactuarcionElectronica`:
- Nómina completa: de acá → hacia orbis (adaptada a single-tenant).
- Documento Soporte: de orbis → hacia acá (adaptada a multiempresa).

Si volvés a tocar alguno de los dos, revisá si el cambio también aplica al otro repo — no hay
sincronización automática, cada migración fue manual y verificada por separado.

## Memoria del usuario relevante

- **No correr queries directas a la base de datos** del usuario sin pedir permiso antes — prefiere
  mostrar los datos él mismo (screenshot, paste). Guardado en memoria persistente
  (`feedback_no_direct_db_queries.md`), aplica en general, no solo a este repo.

## Cómo seguir

1. Si es solo para navegar el código: no hace falta nada más, andá directo a los subfolders.
2. Si necesitás retomar trabajo activo de nómina o documento soporte: leé el skill y
   `docs/NOMINA_ELECTRONICA.md` primero, no vuelvas a derivar las decisiones desde cero.
3. Si es una sesión nueva de Claude Code en otra ruta: las sesiones de Claude Code se indexan por
   ruta absoluta de carpeta (`~/.claude/projects/`), así que no hay continuidad automática entre
   carpetas distintas aunque el código sea igual — este archivo es el puente.
