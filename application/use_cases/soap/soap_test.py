import base64
import hashlib
import requests 
from lxml import etree
from datetime import datetime, timedelta, timezone

from shared import templates_loader

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

from shared.certificate import CertificateData

class SoapRequestTest:
    def __init__(self, security: CertificateData, test_id: str):
        """
        :param security: :class:`CertificateData`
        :param test_id: Identificador del set de pruebas DIAN
        """
        self.certificate = security.firmante
        self.private_key = security.private_key

        self.root = etree.fromstring(templates_loader.template.xml_test)
        self.test_id = test_id
        
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

    def _prepare_xml(self, base64_file):
        binary_security_token = self._get_binary_security_token()
        
        # Encuentra el elemento wsse:BinarySecurityToken y reemplaza su valor
        binary_security_token_element = self.root.find(".//{http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd}BinarySecurityToken")
        binary_security_token_element.text = binary_security_token

        # Genera y reemplaza el Timestamp
        self._create_timestamp()

        # Calcula y reemplaza el DigestValue
        self._calculate_digest_value()

        # Calcula y reemplaza el SignatureValue
        self._calculate_signature_value()

        # Comprimir factura
        # base64_file = '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'
        content_file_element = self.root.find(".//{http://wcf.dian.colombia}contentFile")
        content_file_element.text = base64_file

        test_id_element = self.root.find(".//{http://wcf.dian.colombia}testSetId")
        test_id_element.text = self.test_id
        
        xml_request = etree.tostring(self.root, pretty_print=True).decode('utf-8')
        return xml_request
        
    def _send_soap_request(self, xml_request):
        url = 'https://vpfe-hab.dian.gov.co/WcfDianCustomerServices.svc'
        headers = {
            'Content-Type': 'application/soap+xml; charset=utf-8',
            'SOAPAction': f'http://wcf.dian.colombia/IWcfDianCustomerServices/SendTestSetAsync'
        }

        response = requests.post(url, data=xml_request, headers=headers)
        response.raise_for_status()

        return response
        
    def send_xml(self, base64_file):
        xml_request = self._prepare_xml(base64_file)
        return self._send_soap_request(xml_request)

