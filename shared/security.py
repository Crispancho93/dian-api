import base64
import hashlib
import secrets

"""
Hash y verificación de contraseñas para el panel web.

Usa scrypt de la librería estándar (PEP 452 / RFC 7914), así no hace falta
sumar passlib ni bcrypt como dependencia. El formato almacenado es:

    scrypt$<n>$<r>$<p>$<salt_b64>$<hash_b64>

Los parámetros quedan embebidos en el hash, de modo que subirlos más adelante
no invalida las contraseñas ya guardadas.
"""

_ALGORITHM = "scrypt"
_N = 2 ** 14        # costo de CPU/memoria
_R = 8              # tamaño de bloque
_P = 1              # paralelismo
_DKLEN = 32         # longitud de la clave derivada
_SALT_BYTES = 16


def hash_password(password: str) -> str:
    """
    Genera el hash de una contraseña en texto plano.

    :param password: Contraseña en texto plano.
    :returns: Cadena con el algoritmo, los parámetros, la sal y el hash.
    """
    salt = secrets.token_bytes(_SALT_BYTES)
    derived = hashlib.scrypt(
        password.encode("utf-8"), salt=salt, n=_N, r=_R, p=_P, dklen=_DKLEN
    )

    return "${}".format("$".join([
        _ALGORITHM,
        str(_N),
        str(_R),
        str(_P),
        base64.b64encode(salt).decode("ascii"),
        base64.b64encode(derived).decode("ascii"),
    ]))


def verify_password(password: str, stored_hash: str) -> bool:
    """
    Verifica una contraseña contra el hash almacenado.

    Nunca lanza excepción ante un hash malformado: en ese caso devuelve False,
    para que un registro corrupto en la base no rompa el login.

    :param password: Contraseña en texto plano a verificar.
    :param stored_hash: Hash generado previamente por :func:`hash_password`.
    :returns: True si la contraseña coincide.
    """
    if not password or not stored_hash:
        return False

    try:
        _, algorithm, n, r, p, salt_b64, hash_b64 = stored_hash.split("$")

        if algorithm != _ALGORITHM:
            return False

        salt = base64.b64decode(salt_b64)
        expected = base64.b64decode(hash_b64)

        derived = hashlib.scrypt(
            password.encode("utf-8"),
            salt=salt,
            n=int(n),
            r=int(r),
            p=int(p),
            dklen=len(expected),
        )
    except (ValueError, TypeError):
        return False

    # Comparación en tiempo constante para no filtrar información por timing.
    return secrets.compare_digest(derived, expected)
