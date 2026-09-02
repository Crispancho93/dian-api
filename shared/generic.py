import io
import os
import re
import base64
import hashlib
import zipfile
import requests
from datetime import datetime, timedelta, timezone
from lxml import etree

# Colombia es UTC-5 fijo (sin horario de verano desde 1993), así que un offset
# constante alcanza y evita depender de la base de datos tzdata del sistema.
COLOMBIA_TZ = timezone(timedelta(hours=-5))


def now_colombia() -> datetime:
    """
    Fecha y hora actual en Colombia, como datetime naive.

    Se usa para estampar los registros que después se filtran por fecha desde el
    panel. Si se dejara el CURRENT_TIMESTAMP de la base, el servidor (que corre
    en UTC) marcaría el día siguiente para todo lo enviado después de las 19:00
    hora local, y filtrar "hoy" perdería esos documentos.

    :returns: datetime sin tzinfo, en hora local colombiana.
    """
    return datetime.now(COLOMBIA_TZ).replace(tzinfo=None)


def read_file(path: str, mode: str = "r"):
    with open(path, mode) as file:
        file_content = file.read()
    return file_content

def write_file_from_base64(base64_content, output_file_path):
    """
    Escribe un archivo desde un contenido codificado en Base64.
    
    Args:
        base64_content (str): El contenido en Base64 a decodificar.
        output_file_path (str): Ruta donde se guardará el archivo.
    """
    # Decodificar el contenido de Base64
    file_content = base64.b64decode(base64_content)

    # Crear la carpeta destino si no existe. Esta función se ejecuta en un
    # hilo en segundo plano, así que un fallo acá no rompe la petición pero
    # sí hace perder el archivo en silencio.
    output_dir = os.path.dirname(output_file_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    # Escribir el archivo decodificado
    with open(output_file_path, 'wb') as file:
        file.write(file_content)


def make_request(method, url, headers=None, data=None, params=None):
    if method.upper() == 'GET':
        response = requests.get(url, headers=headers, params=params)
    elif method.upper() == 'POST':
        response = requests.post(url, headers=headers, json=data, params=params)
    elif method.upper() == 'PUT':
        response = requests.put(url, headers=headers, json=data, params=params)
    elif method.upper() == 'DELETE':
        response = requests.delete(url, headers=headers, params=params)
    else:
        raise ValueError(f"Invalid method: {method}")

    return response

def get_identification_digit( vat):
    clean_string = re.sub(r'\s+', ' ', vat).strip()
    parts = clean_string.split("-")
    result = parts[1] if len(parts) > 1 else '0'
    return result

def get_cufe_tax_amounts(tax_totals):
    """
    Mapea cada TaxTotal a su slot CUFE/CUDE (01=IVA, 04=Impoconsumo, 03=ICA)
    según el TaxSchemeID real de cada uno, en vez de asumir un orden fijo.
    """
    amounts = {'01': '0.00', '04': '0.00', '03': '0.00'}
    for tax_total in tax_totals:
        if tax_total.TaxSubtotal:
            scheme_id = tax_total.TaxSubtotal[0].TaxSchemeID
            if scheme_id in amounts:
                amounts[scheme_id] = tax_total.TaxAmount
    return amounts

def get_cune(values: dict) -> str:
    """
    CUNE = SHA-384 de la concatenación definida en el Anexo Técnico de Nómina
    Electrónica, sección 8.1.1: NumNE+FecNE+HorNE+ValDev+ValDed+ValTolNE+NitNE+
    DocEmp+TipoXML+SoftwarePin+TipAmb.
    """
    raw = (
        values["NumNE"] + values["FecNE"] + values["HorNE"] + values["ValDev"] +
        values["ValDed"] + values["ValTolNE"] + values["NitNE"] + values["DocEmp"] +
        values["TipoXML"] + values["SoftwarePin"] + values["TipAmb"]
    )
    return hashlib.sha384(raw.encode('utf-8')).hexdigest()

def get_payroll_file_names(nit: str, year: str, consecutive: int, prefix: str = 'nie'):
    """
    <prefix> + NIT(10, con ceros) + aa + 8 hex  ->  (nombre_xml, nombre_zip).

    :param prefix: 'nie' para NominaIndividual, 'niae' para la Nota de Ajuste.
    """
    base = f"{nit.zfill(10)}{year[-2:]}{consecutive:08X}"
    return (f"{prefix}{base}.xml", f"z{base}.zip")

def get_period(fecha_str: str):
    date = datetime.strptime(fecha_str, "%Y-%m-%d")
    firt_day = date.replace(day=1)
    
    # Obtener el último día del mes
    next_moth = firt_day.replace(day=28) + timedelta(days=4)
    last_day = next_moth - timedelta(days=next_moth.day)
    
    firt_day = firt_day.strftime("%Y-%m-%d")
    last_day = last_day.strftime("%Y-%m-%d")

    return (firt_day, last_day)

"""
    Convierte un objeto en un diccionario, manejando subobjetos de forma recursiva.
"""
def to_dict(obj):
    if hasattr(obj, "__dict__"):
        return {key: to_dict(value) for key, value in obj.__dict__.items()}
    elif isinstance(obj, list):
        return [to_dict(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: to_dict(value) for key, value in obj.items()}
    else:
        return obj  # Para tipos primitivos
    
def get_sequence(value):
    try:
        number = int(value)
        number += 1
        return str(number)
    except ValueError:
        return "Convert Error in get_id"
    
def compress_file_to_base64(file_path):
    # Crear un buffer en memoria
    buffer = io.BytesIO()
    
    # Comprimir el archivo y guardarlo en el buffer
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.write(file_path, arcname=file_path.split('/')[-1])
    
    # Obtener el contenido del buffer
    buffer.seek(0)
    zip_content = buffer.read()
    
    # Codificar el contenido en Base64
    base64_content = base64.b64encode(zip_content).decode('utf-8')
    
    return base64_content

def convert_and_compress_xml_to_base64(xml_root, xml_name):
    """
    Convierte un árbol XML de lxml en un archivo en memoria, 
    lo comprime en un archivo ZIP y lo codifica en Base64.
    
    Args:
        xml_root (etree.Element): El elemento raíz del árbol XML.
    
    Returns:
        str: El contenido del archivo comprimido en formato Base64.
    """
    # Crear un buffer en memoria para el archivo XML
    xml_buffer = io.BytesIO()
    
    # Guardar el árbol XML en el buffer
    xml_tree = etree.ElementTree(xml_root)
    xml_tree.write(xml_buffer, pretty_print=True, encoding='utf-8', xml_declaration=True)
    
    # Resetear el puntero del buffer
    xml_buffer.seek(0)
    
    # Crear un buffer en memoria para el archivo ZIP
    zip_buffer = io.BytesIO()
    
    # Comprimir el archivo XML en el buffer ZIP
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.writestr(xml_name, xml_buffer.getvalue())
    
    # Obtener el contenido del buffer ZIP
    zip_buffer.seek(0)
    zip_content = zip_buffer.read()
    
    # Codificar el contenido del ZIP en Base64
    base64_content = base64.b64encode(zip_content).decode('utf-8')
    
    return base64_content

def zip_document(invoice_xml, name_invoice):
    """
    Toma una factura en formato string, la comprime en un archivo ZIP
    y retorna su contenido codificado en Base64.

    Args:
        factura_str (str): La factura en formato texto (string).
        nombre_archivo (str): Nombre del archivo dentro del ZIP. Por defecto es "factura.xml".

    Returns:
        str: El contenido del archivo ZIP codificado en Base64.
    """
    # Crear un buffer en memoria para el archivo ZIP
    buffer_zip = io.BytesIO()
    
    # Crear un archivo ZIP en memoria y añadir la factura como un archivo
    with zipfile.ZipFile(buffer_zip, mode="w", compression=zipfile.ZIP_DEFLATED) as zip_mem:
        zip_mem.writestr(name_invoice, invoice_xml)
    
    # Obtener los bytes del ZIP
    buffer_zip.seek(0)
    zip_bytes = buffer_zip.read()
    
    # Codificar el archivo ZIP en Base64
    base64_encoded = base64.b64encode(zip_bytes).decode('utf-8')
    
    return base64_encoded

def extract_errors_invoice(xml_response):
        tree = etree.fromstring(xml_response)
        namespaces = {
            's': 'http://www.w3.org/2003/05/soap-envelope',
            'a': 'http://www.w3.org/2005/08/addressing',
            'u': 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd',
            'b': 'http://schemas.datacontract.org/2004/07/DianResponse',
            'c': 'http://schemas.microsoft.com/2003/10/Serialization/Arrays'
        }
        
        error_elements = tree.findall('.//c:string', namespaces)
        error_messages = [element.text for element in error_elements]

        namespaces = { 
            's': 'http://www.w3.org/2003/05/soap-envelope', 
            'a': 'http://www.w3.org/2005/08/addressing', 
            'u': 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd', 
            'b': 'http://schemas.datacontract.org/2004/07/DianResponse' 
        } 

        is_valid = tree.find('.//b:IsValid', namespaces).text
        
        return (is_valid, error_messages)

def extract_zip_key(xml_response):
    """
    Parsea la respuesta de SendTestSetAsync (UploadDocumentResponse).

    A diferencia de SendBillSync/SendNominaSync (que responden DianResponse con
    IsValid), este método es asíncrono y responde un ZipKey junto con una lista
    de errores de recepción. El resultado real de la validación se consulta
    luego con GetStatusZip usando ese ZipKey.

    :returns: (zip_key, [mensajes de error])
    """
    tree = etree.fromstring(xml_response)
    namespaces = {
        'u': 'http://schemas.datacontract.org/2004/07/UploadDocumentResponse',
        'x': 'http://schemas.datacontract.org/2004/07/XmlParamsResponseTrackId',
    }

    zip_key_element = tree.find('.//u:ZipKey', namespaces)
    zip_key = zip_key_element.text if zip_key_element is not None else None

    error_messages = [
        element.text
        for element in tree.findall('.//x:XmlParamsResponseTrackId//x:ProcessedMessage', namespaces)
        if element.text
    ]
    if not error_messages:
        # Fallback: cualquier string suelto de la lista de errores
        error_messages = [
            element.text
            for element in tree.findall(
                './/{http://schemas.microsoft.com/2003/10/Serialization/Arrays}string'
            )
            if element.text
        ]

    return (zip_key, error_messages)

def extract_errors_credit(xml_response):
    try:
        tree = etree.fromstring(xml_response)
    except etree.XMLSyntaxError as e:
        # Manejo de error si la respuesta no es un XML válido
        return ('false', [f"Error al parsear el XML: {e}"], f"Error al parsear el XML: {e}")
        
    namespaces = {
        's': 'http://www.w3.org/2003/05/soap-envelope',
        'a': 'http://www.w3.org/2005/08/addressing',
        'u': 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd',
        'b': 'http://schemas.datacontract.org/2004/07/DianResponse',
        'c': 'http://schemas.microsoft.com/2003/10/Serialization/Arrays'
    }
    
    # Intenta encontrar los mensajes de error en la estructura 'c:string'
    error_elements = tree.findall('.//c:string', namespaces)
    error_messages = [element.text for element in error_elements if element.text]

    # También busca el 'StatusDescription' que a veces contiene el error principal
    status_description_element = tree.find('.//b:StatusDescription', namespaces)
    if status_description_element is not None and status_description_element.text:
        error_messages.append(status_description_element.text.strip())

    # Une todos los mensajes de error en una sola cadena
    full_error_message = "\n".join(error_messages) if error_messages else ""

    is_valid_element = tree.find('.//b:IsValid', namespaces)
    is_valid = is_valid_element.text if is_valid_element is not None else 'false'
    
    return (is_valid, error_messages)