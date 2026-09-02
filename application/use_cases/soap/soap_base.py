import base64
import hashlib
from lxml import etree
from datetime import datetime, timedelta, timezone

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

from shared.certificate import CertificateData



class SoapBase:
    """
    Clase base para la construcción y firma de mensajes SOAP con WS-Security.
    """

    def __init__(self, certificate_data: CertificateData):
        """
        :param certificate_data: :class:`CertificateData`
        """
        self.certificate = certificate_data.firmante
        self.private_key = certificate_data.private_key

    def _get_binary_security_token(self):
        # Extrae el certificado en formato DER y lo codifica en Base64
        cert_der = self.certificate.public_bytes(serialization.Encoding.DER)
        cert_base64 = base64.b64encode(cert_der).decode('utf-8')
        return cert_base64
    
    def _calculate_digest_value(self):
        # Encuentra el elemento ds:Reference
        reference_element = self.root.find(".//{http://www.w3.org/2000/09/xmldsig#}Reference")

        # Busca el elemento al que apunta el URI
        uri = reference_element.get("URI").lstrip("#")  # Elimina el prefijo '#'
        referenced_node = self.root.find(f".//*[@wsu:Id='{uri}']", namespaces={
            "wsu": "http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
        })
        
        # Canonicaliza el XML
        canonical_xml = etree.tostring(
            referenced_node, 
            method="c14n", 
            exclusive=True, 
            with_comments=False, 
            inclusive_ns_prefixes=["soap", "wcf"]
        )
        
        # Calcula el hash SHA-256 del XML canonicalizado
        digest = hashlib.sha256(canonical_xml).digest()
        
        # Codifica el hash en Base64
        digest_value = base64.b64encode(digest).decode('utf-8')
        
        # Añadir el DigestValue al XML
        digest_value_element = reference_element.find(".//{http://www.w3.org/2000/09/xmldsig#}DigestValue")
        digest_value_element.text = digest_value
    
    def _calculate_signature_value(self):
       # Encuentra el nodo SignedInfo
        signed_info_element = self.root.find(".//{http://www.w3.org/2000/09/xmldsig#}SignedInfo")

        # Canonicaliza el nodo SignedInfo
        canonical_signed_info = etree.tostring(
            signed_info_element,
            method="c14n", 
            exclusive=True, 
            with_comments=False, 
            inclusive_ns_prefixes=["wsa", "soap", "wcf"]
        )

        # Firma el nodo canonicalizado con la clave privada
        signature = self.private_key.sign(
            canonical_signed_info,
            padding.PKCS1v15(),
            hashes.SHA256()
        )

        # Codifica la firma en Base64
        signature_value = base64.b64encode(signature).decode('utf-8')

        # Añade el SignatureValue al XML
        signature_value_element = self.root.find(".//{http://www.w3.org/2000/09/xmldsig#}SignatureValue")
        signature_value_element.text = signature_value
    
    def _create_timestamp(self):
        created_time = datetime.now(timezone.utc)
        expires_time = created_time + timedelta(minutes=1)  # El mensaje expira en 5 minutos

        created_str = created_time.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        expires_str = expires_time.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

        created_element = self.root.find(".//{http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd}Created")
        expires_element = self.root.find(".//{http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd}Expires")
        created_element.text = created_str
        expires_element.text = expires_str

    def prepare_xml(self, xml_template):
        # Parsear el XML y preparar WS-Security ===
        self.root = etree.fromstring(xml_template.encode("utf-8"))

        # Reemplazar el token binario (certificado en base64)
        binary_security_token = self._get_binary_security_token()
        token_element = self.root.find(
            ".//{http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd}BinarySecurityToken"
        )
        token_element.text = binary_security_token

        # Generar Timestamp
        self._create_timestamp()

        # Calcular Digest y Firma
        self._calculate_digest_value()
        self._calculate_signature_value()

        # === 3️⃣ Canonizar y devolver el XML final firmado ===
        xml_request = etree.tostring(self.root, pretty_print=True, encoding="utf-8").decode("utf-8")
        return xml_request