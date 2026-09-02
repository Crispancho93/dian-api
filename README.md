# Proyecto facturacion-electronica-colombia

Este proyecto facturacion-electronica-colombia es una aplicación web desarrollada en Python utilizando el framework FastAPI. Proporciona una API para enviar facturas, notas crédito y prontamente notas débito a la DIAN en Colombia.

Actualmente está operando en ambiente de habilitación. Para más detalles acerca de cómo correr y depurar el proyecto, puedes consultar este video de YouTube:

[Facturación electrónica DIAN COLOMBIA software propio - API GRATIS](https://youtu.be/EaDoYikq-DI?si=W-lIRWI1gwBewll2)

En caso tal de necesitar ayuda me pueden contactar al WhatsApp +57 300 812 0524

---

## Instalación

1. Clona el repositorio desde GitHub:

    ```bash
    git clone https://github.com/Crispancho93/facturacion-electronica-colombia.git
    ```

2. Accede al directorio del proyecto:

    ```bash
    cd facturacion-electronica-colombia
    ```

3. Crea un entorno virtual e instala las dependencias:

    ```bash
    python -m venv venv
    source venv/bin/activate    # Linux / macOS
    .\venv\Scripts\activate     # Windows
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta el servidor de desarrollo:

    ```bash
    uvicorn app:app --reload
    ```

2. Accede a la documentación de la API en tu navegador:

    ```
    http://localhost:8000/docs
    ```

3. Realiza solicitudes HTTP a la API utilizando herramientas como cURL o Postman.

## Panel web

Además de la API JSON, el proyecto expone un panel administrativo en la raíz (`/`) con tres
módulos: usuarios (login), documentos enviados a la DIAN con su estado, y clientes con carga
de certificado.

> Los endpoints `/api/*` **no** requieren autenticación: los consume la integración con Odoo.
> El login protege únicamente las pantallas del panel.

Puesta en marcha, con un solo comando:

```bash
python scripts/create_user.py
```

Eso crea las tablas que falten, el usuario del primer login
(`admin@atechcol.com` / `admin123`) y datos de prueba para poder navegar el panel.
Es idempotente: se puede correr varias veces sin duplicar nada.

Opciones útiles:

```bash
python scripts/create_user.py --email tu@correo.com --password "TuClave"   # credenciales propias
python scripts/create_user.py --sin-datos                                  # sin datos de prueba
python scripts/create_user.py --limpiar-datos                              # borra los datos de prueba
```

También conviene definir `SECRET_KEY` en el `.env` (firma la cookie de sesión). Si no se define,
la app arranca igual pero las sesiones se cierran en cada reinicio:

```bash
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

Después, levantar la API y entrar a `http://localhost:8000/login`.

> El DDL también está en `domain/tables/*.sql` por si se prefiere aplicarlo a mano con `psql`.

Los documentos se registran automáticamente en la tabla `document` cada vez que se envía uno por
la API, incluidos los rechazados y los que fallan antes de llegar a la DIAN. El historial anterior
a este cambio no está en la tabla, porque antes no se guardaba nada.

## Contribución

¡Agradecemos las contribuciones! Si deseas contribuir al proyecto, sigue estos pasos:

1. Fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y commitealos (`git commit -am 'Agrega nueva característica'`).
4. Sube los cambios a tu repositorio (`git push origin feature/nueva-caracteristica`).
5. Crea un Pull Request.

## Estructura del Proyecto

## Pendiente por validar
1. Validar campo IndustryClasificationCode - Código de actividad que registra en el RUT

---

## Licencia

Este proyecto está licenciado bajo la misma licencia de código abierto que el kernel de Linux: [Licencia GPLv2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html). Esto significa que puedes usar, modificar y distribuir el software bajo los términos de la licencia.


## Permisos
chmod -R 777 ./files/generados
chown -R www-data:www-data /srv/files
chmod -R 777 /srv/files

# Exponer el id del usuario local al contenedor
export UID=$(id -u)
export GID=$(id -g)
docker-compose up --build

# Entrar al contenedor 
docker exec -u root -w /tmp -it php-factura bash