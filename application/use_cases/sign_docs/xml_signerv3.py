import base64
import hashlib
from lxml import etree

from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.x509 import load_der_x509_certificate

from shared.certificate import CertificateData
from .template_xades import TemplateXades

class XmlSignerV3:
    def __init__(self, invoice_xml, invoice_dto, document_type,security: CertificateData):
             # 🔐 Certificados (inyectados)
            self.firmante = security.firmante.public_bytes(serialization.Encoding.DER)
            self.emisor = security.emisor.public_bytes(serialization.Encoding.DER)
            self.ca_raiz = security.ca_raiz.public_bytes(serialization.Encoding.DER)
            self.private_key = security.private_key
            self.politica_file = security.politica_file

            self.invoice_root = invoice_xml
            self.invoice_dto = invoice_dto
            self.document_type = document_type
    
    def _get_with_schemas(self, input_data):
        if isinstance(input_data, bytes):
            node = input_data.decode('utf-8')
        else:
            node = input_data

        if self.document_type == 'FV':
            schema = 'xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:ext="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2" xmlns:sts="http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures" xmlns:xades="http://uri.etsi.org/01903/v1.3.2#" xmlns:xades141="http://uri.etsi.org/01903/v1.4.1#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
        elif self.document_type == 'NI':
            schema = 'xmlns="dian:gov:co:facturaelectronica:NominaIndividual" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:ext="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2" xmlns:xades="http://uri.etsi.org/01903/v1.3.2#" xmlns:xades141="http://uri.etsi.org/01903/v1.4.1#" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
        elif self.document_type == 'NA':
            schema = 'xmlns="dian:gov:co:facturaelectronica:NominaIndividualDeAjuste" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:ext="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2" xmlns:xades="http://uri.etsi.org/01903/v1.3.2#" xmlns:xades141="http://uri.etsi.org/01903/v1.4.1#" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
        elif self.document_type == 'DS':
            # Documento Soporte en adquisiciones a no obligados a facturar.
            # Usa el namespace de Invoice-2 pero con el sts de Structures-2-1.
            schema = 'xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:ext="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2" xmlns:sts="dian:gov:co:facturaelectronica:Structures-2-1" xmlns:xades="http://uri.etsi.org/01903/v1.3.2#" xmlns:xades141="http://uri.etsi.org/01903/v1.4.1#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
        elif self.document_type == 'NAS':
            # Nota de Ajuste al Documento Soporte: es un híbrido. Raíz
            # CreditNote-2 como la nota crédito, pero el sts de Structures-2-1
            # como el documento soporte. Sin esta rama caía al else, que usa el
            # sts de la nota crédito de venta: la canonicalización no coincidía
            # con el documento real y la DIAN devolvía ZE02, firma inválida.
            schema = 'xmlns="urn:oasis:names:specification:ubl:schema:xsd:CreditNote-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:ext="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2" xmlns:sts="dian:gov:co:facturaelectronica:Structures-2-1" xmlns:xades="http://uri.etsi.org/01903/v1.3.2#" xmlns:xades141="http://uri.etsi.org/01903/v1.4.1#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
        else:
            schema = 'xmlns="urn:oasis:names:specification:ubl:schema:xsd:CreditNote-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:ext="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2" xmlns:sts="http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures" xmlns:xades="http://uri.etsi.org/01903/v1.3.2#" xmlns:xades141="http://uri.etsi.org/01903/v1.4.1#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'

        return node.replace(
            'xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:xades="http://uri.etsi.org/01903/v1.3.2#"',
            schema
        )
    
    def _get_c14n_node(self, input_data):
        if isinstance(input_data, str):
            node = etree.fromstring(input_data.encode('utf-8'))
        else:
            node = input_data

        return etree.tostring(
            node,
            method="c14n",
            exclusive=False,
            with_comments=False
        )
    
    def _generate_signature_value(self, canonical_signed_info):
        if isinstance(canonical_signed_info, str):
            canonical_signed_info = canonical_signed_info.encode('utf-8')
        elif not isinstance(canonical_signed_info, bytes):
            raise TypeError("El contenido canonicalizado debe ser una cadena o bytes.")
        
        # Firmar el contenido canonicalizado
        signature = self.private_key.sign(
            canonical_signed_info,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        
        # Codificar la firma en Base64
        signature_value = base64.b64encode(signature).decode('utf-8')
        return signature_value
    
    def _get_digest_issuer(self, certificate):
        digest = hashlib.sha256(certificate).digest()
        digest_base64 = base64.b64encode(digest).decode('utf-8')

        cert = load_der_x509_certificate(certificate)
        issuer = cert.issuer.rfc4514_string()
        serial_number = str(cert.serial_number)

        # # issuer_attributes = cert.issuer.get_attributes_for_oid
        # cert_issuer = [
        #     f"{attr.oid._name}={attr.value}" for attr in cert.issuer
        # ]
        # cert_issuer_str = ", ".join(reversed(cert_issuer))

        result = {
            'DigestValue': digest_base64,
            'X509IssuerName': issuer,
            'X509SerialNumber': serial_number
        }
        return result
    
    def _get_digest(self, data) -> str:
        if isinstance(data, str):
            data = data.encode('utf-8')
        elif not isinstance(data, bytes):
            raise TypeError("El dato debe ser una cadena o bytes.")
        
        return base64.b64encode(hashlib.sha256(data).digest()).decode('utf-8')

    def _set_key_info(self):
        x509_certificate = self.signature_xml.find(".//{http://www.w3.org/2000/09/xmldsig#}X509Certificate")
        x509_certificate.text = base64.b64encode(self.firmante).decode("utf-8")

    def _get_properties_values(self) -> dict:
        cert_firmante = self._get_digest_issuer(self.firmante)
        cert_ca_raiz = self._get_digest_issuer(self.ca_raiz)
        cert_emisor = self._get_digest_issuer(self.emisor)

        values =  [
            {
                "DigestValue": cert_firmante['DigestValue'],
                "X509IssuerName": cert_firmante['X509IssuerName'],
                "X509SerialNumber": cert_firmante['X509SerialNumber'],
            },
            {
                "DigestValue": cert_ca_raiz['DigestValue'],
                "X509IssuerName": cert_ca_raiz['X509IssuerName'],
                "X509SerialNumber": cert_ca_raiz['X509SerialNumber'],
            },
            {
                "DigestValue": cert_emisor['DigestValue'],
                "X509IssuerName": cert_emisor['X509IssuerName'],
                "X509SerialNumber": cert_emisor['X509SerialNumber'],
            }
        ]
        
        return values
            
    def set_properties(self, references):
        # formatted_date  = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "-05:00"
        formatted_date = f"{self.invoice_dto.IssueDate}T{self.invoice_dto.IssueTime}"
        # Buscar todos los elementos <xades:Cert>
        certs = self.signature_xml.findall(".//{http://uri.etsi.org/01903/v1.3.2#}Cert")

        # Recorrer las referencias y llenar los valores en cada <xades:Cert>
        # for i, cert in enumerate(certs):
        for cert, ref in zip(certs, references):
            # Llenar CertDigest
            cert.find("{http://uri.etsi.org/01903/v1.3.2#}CertDigest").find(
                "{http://www.w3.org/2000/09/xmldsig#}DigestValue"
            ).text = ref["DigestValue"]

            # Llenar IssuerSerial
            cert.find("{http://uri.etsi.org/01903/v1.3.2#}IssuerSerial").find(
                "{http://www.w3.org/2000/09/xmldsig#}X509IssuerName"
            ).text = ref.get("X509IssuerName", "")
            cert.find("{http://uri.etsi.org/01903/v1.3.2#}IssuerSerial").find(
                "{http://www.w3.org/2000/09/xmldsig#}X509SerialNumber"
            ).text = ref.get("X509SerialNumber", "")

        
        time = self.signature_xml.find(".//{http://uri.etsi.org/01903/v1.3.2#}SigningTime")
        time.text = formatted_date

    def set_signed_info(self, references):
        # Buscar todas las referencias en <ds:SignedInfo>
        reference_elements = self.signature_xml.findall(".//{http://www.w3.org/2000/09/xmldsig#}Reference")

        # Recorrer las referencias y llenar únicamente los valores .text
        for ref_element, ref_data in zip(reference_elements, references):
            # Llenar el valor del nodo <ds:DigestValue>
            digest_value = ref_element.find("{http://www.w3.org/2000/09/xmldsig#}DigestValue")
            digest_value.text = ref_data["DigestValue"]

    def sign(self):
        if self.document_type in ('NI', 'NA'):
            # TODO: verificar el digest real de esta política (base64(sha256(pdf)));
            # se deja por ahora el valor de la política de factura (v1) hasta poder
            # descargar y hashear el PDF de nómina publicado por la DIAN.
            self.signature_xml = TemplateXades.create_signature_template(
                policy_url="https://facturaelectronica.dian.gov.co/politicadefirma/v2/politicadefirmav2.pdf"
            )
        else:
            self.signature_xml = TemplateXades.create_signature_template()

        # Setear el nodo KeyInfo
        self._set_key_info()

        # Setear el nodo SignedProperties
        properties_values = self._get_properties_values()
        self.set_properties(properties_values)

        # Setear el nodo SignedInfo
        invoice_xml = etree.tostring(
            self.invoice_root, 
            xml_declaration=True, 
            encoding='utf-8', 
        ).decode('utf-8')

        invoice_c14n = self._get_c14n_node(invoice_xml)
        
        key_info_node = self._get_c14n_node(self.signature_xml.find("{http://www.w3.org/2000/09/xmldsig#}KeyInfo"))
        key_info_node = self._get_with_schemas(key_info_node)

        properties_node = self._get_c14n_node(self.signature_xml.find(".//{http://uri.etsi.org/01903/v1.3.2#}SignedProperties"))
        properties_node = self._get_with_schemas(properties_node)

        references = [
            {"DigestValue": self._get_digest(invoice_c14n)},
            {"DigestValue": self._get_digest(key_info_node)},
            {"DigestValue": self._get_digest(properties_node)}
        ]
        self.set_signed_info(references)
        
        # Firmar el nodo SignedInfo
        signed_info_node = self.signature_xml.find("{http://www.w3.org/2000/09/xmldsig#}SignedInfo")
        canonical_signed_info = self._get_c14n_node(signed_info_node)
        canonical_signed_info = self._get_with_schemas(canonical_signed_info)

        signature_value = self._generate_signature_value(canonical_signed_info)
        self.signature_xml.find("{http://www.w3.org/2000/09/xmldsig#}SignatureValue").text = signature_value

        # Agregar la firma al XML
        signature_str = etree.tostring(self.signature_xml, encoding='UTF-8').decode('utf-8')
        signed_invoice = invoice_xml.replace(
            "<ext:ExtensionContent/>", 
            f"<ext:ExtensionContent>{signature_str}</ext:ExtensionContent>"
        )

        # Guardar el resultado canonizado en un archivo
        return signed_invoice
       