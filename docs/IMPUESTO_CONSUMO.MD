## Cambios recientes (2026-08-10)

Resumen de lo trabajado en la branch `feature/certificado-multi-empresa` (nada de esto está commiteado, queda en el working tree para revisión):

### Deploy a Kubernetes (Contabo)

Se armó el deploy de esta API en k8s (antes solo existía `docker-compose.yml`), siguiendo el mismo patrón que ya usaba el repo para Odoo (Gateway API + cert-manager + `envsubst`), pero limpiado para que sea solo de esta API:

- Nuevos: `k8s/invoice-api.yaml` (Namespace + Deployment + Service), `k8s/invoice-api-routes.yaml` (HTTPRoute + redirect HTTP→HTTPS), `k8s/invoice-api.env` (variables para `envsubst`), `k8s/apply-invoice-api.sh` (script de deploy).
- Reusado tal cual: `k8s/tls.yaml` (Certificate de cert-manager).
- Borrados (eran de Odoo/burgerdog, cliente de ejemplo, no aplicaban acá): `k8s/odoo.yaml`, `k8s/routes.yaml`, `k8s/client.env`, `k8s/apply.sh`.
- Dominio `invoice-api.atechcol.com`, namespace `invoice-api`, acceso directo por `HOST_PORT=10480` (igual al `docker-compose.yml`) además del HTTPS del gateway.
- El volumen `/srv/files` (antes volumen externo Docker `store-invoice`) pasa a `hostPath` en `${DATA_PATH}` (`/var/lib/invoice-api-data`) — **crear ese directorio en el server antes del primer deploy**.
- `.github/workflows/invoice-deploy.yml` estaba desactualizado (copia del pipeline de Odoo: `Dockerfile.odoo`, tag `odoo17-base`, `client.env`/`apply.sh` ya borrados). Se reescribió para build con el `Dockerfile` real, tag `ghcr.io/crispancho93/invoice.api:latest`, y deploy vía `apply-invoice-api.sh`.

### Variables de entorno: de `.env` a k8s

`shared/config.py` usa `pydantic-settings` leyendo `.env`, pero las variables de entorno reales tienen prioridad sobre el archivo. Se movieron todas las variables de la app (`PATH_BASE`, `SIGN_NAME`, `SIGN_PASSWORD`, `POLITICA_NAME`, `WEB_SERVICE`, `ENCRYPTION_KEY`, `DATABASE_URL`) a `k8s/invoice-api.env`, y el Deployment las inyecta como `env` del contenedor. `PATH_BASE` se ajustó a `/srv/files` (ruta del contenedor), ya no `C:\FE`.

### Higiene de secretos

`.env` (con secretos reales) estaba commiteado en git y se horneaba en la imagen Docker. Se agregó `.dockerignore` (excluye `.env`, `.git`, `k8s`, etc.) y se sacó `.env` del tracking de git (`git rm --cached` + entrada en `.gitignore`); sigue existiendo local para desarrollo. `k8s/invoice-api.env` se dejó trackeado a propósito (decisión del usuario) porque el workflow de CI necesita subirlo al server vía `scp`.

### Bug DIAN: `schemeID` del CUFE/CUDE no reflejaba el ambiente (rechazo FAD07 / CAD07)

Al facturar en ambiente de pruebas (`ProfileExecutionID="2"`), DIAN rechazaba con `@schemeID no indica un valor válido para ambiente de destino`. Causa: el setter de `ProfileExecutionID` actualizaba el texto de `<cbc:ProfileExecutionID>` pero nunca el atributo `schemeID` de `<cbc:UUID>` (hardcodeado en la plantilla). Bug presente desde el primer commit del repo. Fix aplicado en `domain/xml_models/invoice/invoice_control.py` y `domain/xml_models/credit_note/control.py`: el setter ahora también actualiza `schemeID` de `//cbc:UUID` con el valor del ambiente.

### Bug DIAN: Impoconsumo (INC) no se reflejaba en el CUFE/CUDE

El cliente es un restaurante que factura con Impoconsumo (INC, código DIAN `04`, 8%) en vez de IVA (mutuamente excluyentes). Los DTOs y el builder de XML ya eran genéricos (soportan cualquier `TaxSchemeID` por línea/`TaxTotal`), pero el cálculo del CUFE/CUDE tenía `ValImp2` (slot de INC) hardcodeado en `'0.00'` y `ValImp1` (IVA) tomado ciegamente de `TaxTotals[0]`, sin importar el impuesto real. Fix: nueva función `get_cufe_tax_amounts()` en `shared/generic.py` que mapea cada `TaxTotal` a su slot (`01`=IVA, `04`=INC, `03`=ICA) según el `TaxSchemeID` real; usada ahora en `create_invoice_case.py` (`cufe`) y `create_note_case.py` (`cude`).

Para que esto tenga efecto, quien arma el JSON del request (probablemente el módulo de Odoo) debe mandar, en las líneas de comida, `TaxSchemeID="04"`, `TaxSchemeName="INC"`, `TaxPercent="8.00"` (en vez de IVA), tanto en `Amounts.TaxTotals[].TaxSubtotal[]` como en cada `Lines[]`, sin mandar además un `TaxTotal` de IVA para esas líneas.

**Pendiente**: nada de lo anterior se probó en vivo contra DIAN (habilitación ni producción) desde esta sesión — son fixes verificados por lectura/trazabilidad del código, no end-to-end.