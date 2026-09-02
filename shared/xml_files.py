import os
from typing import NamedTuple
from shared import Config

_config = Config()
class XmlTemplatesData(NamedTuple):
    xml_request: str
    xml_invoice: str
    xml_credit_note: str
    xml_test: str
    xml_range: str
    xml_documentosoporte: str
    xml_nota_ajuste_ds: str
    xml_payroll: str
    xml_payroll_request: str
    xml_payroll_test_request: str
    xml_status_zip_request: str
    xml_payroll_adjustment: str

class XmlLoader:
    def __init__(self):
        self._template = None

    def load(self):
        data = {
            'xml_request': self.template_request,
            'xml_invoice': self.invoice_template,
            'xml_credit_note': self.credit_note_template,
            'xml_test': self.template_test,
            'xml_range': self.template_range,
            'xml_documentosoporte': self.documento_soporte_template,
            'xml_nota_ajuste_ds': self.nota_ajuste_ds_template,
            'xml_payroll': self.payroll_template,
            'xml_payroll_request': self.template_payroll_request,
            'xml_payroll_test_request': self.template_payroll_test_request,
            'xml_status_zip_request': self.template_status_zip_request,
            'xml_payroll_adjustment': self.payroll_adjustment_template
        }
    
        self._template = XmlTemplatesData(**data)

    @property
    def template(self):
        if not self._template:
            raise ValueError("Templates data has not been loaded.")
        return self._template
    
    @property
    def template_request(self):
        xml_request = '''
        <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
            xmlns:wcf="http://wcf.dian.colombia">
            <soap:Header xmlns:wsa="http://www.w3.org/2005/08/addressing">
                <wsse:Security
                    xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
                    xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
                    <wsu:Timestamp wsu:Id="TS-C35717809C92836BA3173565889316046">
                        <wsu:Created />
                        <wsu:Expires />
                    </wsu:Timestamp>
                    <wsse:BinarySecurityToken
                        EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary"
                        ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3"
                        wsu:Id="X509-C35717809C92836BA3173565889308341" />
                    <ds:Signature Id="SIG-C35717809C92836BA3173565889315445"
                        xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
                        <ds:SignedInfo>
                            <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
                                <ec:InclusiveNamespaces PrefixList="wsa soap wcf"
                                    xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#" />
                            </ds:CanonicalizationMethod>
                            <ds:SignatureMethod
                                Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256" />
                            <ds:Reference URI="#id-C35717809C92836BA3173565889308344">
                                <ds:Transforms>
                                    <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
                                        <ec:InclusiveNamespaces PrefixList="soap wcf"
                                            xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#" />
                                    </ds:Transform>
                                </ds:Transforms>
                                <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256" />
                                <ds:DigestValue />
                            </ds:Reference>
                        </ds:SignedInfo>
                        <ds:SignatureValue />
                        <ds:KeyInfo Id="KI-C35717809C92836BA3173565889308342">
                            <wsse:SecurityTokenReference wsu:Id="STR-C35717809C92836BA3173565889308343">
                                <wsse:Reference URI="#X509-C35717809C92836BA3173565889308341"
                                    ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3" />
                            </wsse:SecurityTokenReference>
                        </ds:KeyInfo>
                    </ds:Signature>
                </wsse:Security>
                <wsa:Action>http://wcf.dian.colombia/IWcfDianCustomerServices/SendBillSync</wsa:Action>
                <wsa:To wsu:Id="id-C35717809C92836BA3173565889308344"
                    xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">{WEB_SERVICE}</wsa:To>
            </soap:Header>
            <soap:Body>
                <wcf:SendBillSync>
                    <wcf:contentFile>{contentFile}</wcf:contentFile>
                </wcf:SendBillSync>
            </soap:Body>
        </soap:Envelope>
        '''
        return xml_request
    
    @property
    def template_range(self):
        xml_request = '''
        <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
            xmlns:wcf="http://wcf.dian.colombia"
            xmlns:wsa="http://www.w3.org/2005/08/addressing"
            xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
            xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"
            xmlns:ds="http://www.w3.org/2000/09/xmldsig#"
            xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#">

            <soap:Header>
                <wsse:Security>
                    <wsu:Timestamp wsu:Id="TS-CUSTOM">
                        <wsu:Created></wsu:Created>
                        <wsu:Expires></wsu:Expires>
                    </wsu:Timestamp>

                    <wsse:BinarySecurityToken
                        EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary"
                        ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3"
                        wsu:Id="X509-CUSTOM"></wsse:BinarySecurityToken>

                    <ds:Signature Id="SIG-CUSTOM">
                        <ds:SignedInfo>
                            <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
                                <ec:InclusiveNamespaces PrefixList="wsa soap wcf" />
                            </ds:CanonicalizationMethod>
                            <ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256" />
                            <ds:Reference URI="#id-CUSTOM">
                                <ds:Transforms>
                                    <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
                                        <ec:InclusiveNamespaces PrefixList="soap wcf" />
                                    </ds:Transform>
                                </ds:Transforms>
                                <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256" />
                                <ds:DigestValue></ds:DigestValue>
                            </ds:Reference>
                        </ds:SignedInfo>
                        <ds:SignatureValue></ds:SignatureValue>
                        <ds:KeyInfo Id="KI-CUSTOM">
                            <wsse:SecurityTokenReference wsu:Id="STR-CUSTOM">
                                <wsse:Reference URI="#X509-CUSTOM"
                                    ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3" />
                            </wsse:SecurityTokenReference>
                        </ds:KeyInfo>
                    </ds:Signature>
                </wsse:Security>

                <wsa:Action>http://wcf.dian.colombia/IWcfDianCustomerServices/GetNumberingRange</wsa:Action>
                <wsa:To wsu:Id="id-CUSTOM">{WEB_SERVICE}</wsa:To>
            </soap:Header>

            <soap:Body>
                <wcf:GetNumberingRange>
                    <wcf:accountCode>{account_code}</wcf:accountCode>
                    <wcf:accountCodeT>{account_code_t}</wcf:accountCodeT>
                    <wcf:softwareCode>{software_code}</wcf:softwareCode>
                </wcf:GetNumberingRange>
            </soap:Body>
        </soap:Envelope>
        '''
        return xml_request
    
    @property
    def template_test(self):
        xml_request = '''
        <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
            xmlns:wcf="http://wcf.dian.colombia">
            <soap:Header xmlns:wsa="http://www.w3.org/2005/08/addressing">
                <wsse:Security
                    xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
                    xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
                    <wsu:Timestamp wsu:Id="TS-C35717809C92836BA3173565889316046">
                        <wsu:Created />
                        <wsu:Expires />
                    </wsu:Timestamp>
                    <wsse:BinarySecurityToken
                        EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary"
                        ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3"
                        wsu:Id="X509-C35717809C92836BA3173565889308341" />
                    <ds:Signature Id="SIG-C35717809C92836BA3173565889315445"
                        xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
                        <ds:SignedInfo>
                            <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
                                <ec:InclusiveNamespaces PrefixList="wsa soap wcf"
                                    xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#" />
                            </ds:CanonicalizationMethod>
                            <ds:SignatureMethod
                                Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256" />
                            <ds:Reference URI="#id-C35717809C92836BA3173565889308344">
                                <ds:Transforms>
                                    <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
                                        <ec:InclusiveNamespaces PrefixList="soap wcf"
                                            xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#" />
                                    </ds:Transform>
                                </ds:Transforms>
                                <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256" />
                                <ds:DigestValue />
                            </ds:Reference>
                        </ds:SignedInfo>
                        <ds:SignatureValue />
                        <ds:KeyInfo Id="KI-C35717809C92836BA3173565889308342">
                            <wsse:SecurityTokenReference wsu:Id="STR-C35717809C92836BA3173565889308343">
                                <wsse:Reference URI="#X509-C35717809C92836BA3173565889308341"
                                    ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3" />
                            </wsse:SecurityTokenReference>
                        </ds:KeyInfo>
                    </ds:Signature>
                </wsse:Security>
                <wsa:Action>http://wcf.dian.colombia/IWcfDianCustomerServices/SendTestSetAsync</wsa:Action>
                <wsa:To wsu:Id="id-C35717809C92836BA3173565889308344"
                    xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
                    https://vpfe-hab.dian.gov.co/WcfDianCustomerServices.svc</wsa:To>
            </soap:Header>
            <soap:Body>
                <wcf:SendTestSetAsync>
                    <wcf:contentFile />
                    <wcf:testSetId />
                </wcf:SendTestSetAsync>
            </soap:Body> 
        </soap:Envelope>
        '''
        return xml_request
    
    @property
    def invoice_template(self):
        # Template para la factura
        root_dir = os.path.abspath(os.curdir)
        xml_invoice_path = os.path.join(root_dir, 'shared','xml_models', 'Generica.xml')
        with open(xml_invoice_path, 'r', encoding='utf-8') as file:
            xml_invoice = file.read()
        return xml_invoice
    
    @property
    def credit_note_template(self):
        # Template para la Nota crédito
        root_dir = os.path.abspath(os.curdir)
        xml_invoice_path = os.path.join(root_dir, 'shared','xml_models', 'CreditNote.xml')
        with open(xml_invoice_path, 'r', encoding='utf-8') as file:
            xml_invoice = file.read()
        return xml_invoice

    @property
    def documento_soporte_template(self):
        # Template para el Documento Soporte en adquisiciones a no obligados a facturar
        root_dir = os.path.abspath(os.curdir)
        xml_path = os.path.join(root_dir, 'shared','xml_models', 'DocumentoSoporte.xml')
        with open(xml_path, 'r', encoding='utf-8') as file:
            return file.read()

    @property
    def nota_ajuste_ds_template(self):
        # Template para la Nota de Ajuste al Documento Soporte (CreditNote tipo 95)
        root_dir = os.path.abspath(os.curdir)
        xml_path = os.path.join(root_dir, 'shared','xml_models', 'NotaAjusteDocumentoSoporte.xml')
        with open(xml_path, 'r', encoding='utf-8') as file:
            return file.read()

    @property
    def payroll_template(self):
        # Template para la Nómina Electrónica (NominaIndividual)
        root_dir = os.path.abspath(os.curdir)
        xml_payroll_path = os.path.join(root_dir, 'shared','xml_models', 'NominaIndividual.xml')
        with open(xml_payroll_path, 'r', encoding='utf-8') as file:
            xml_payroll = file.read()
        return xml_payroll

    @property
    def payroll_adjustment_template(self):
        # Template para la Nota de Ajuste de Nómina (NominaIndividualDeAjuste)
        root_dir = os.path.abspath(os.curdir)
        xml_path = os.path.join(root_dir, 'shared','xml_models', 'NominaIndividualDeAjuste.xml')
        with open(xml_path, 'r', encoding='utf-8') as file:
            return file.read()

    @property
    def template_payroll_request(self):
        xml_request = '''
        <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
            xmlns:wcf="http://wcf.dian.colombia">
            <soap:Header xmlns:wsa="http://www.w3.org/2005/08/addressing">
                <wsse:Security
                    xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
                    xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
                    <wsu:Timestamp wsu:Id="TS-C35717809C92836BA3173565889316046">
                        <wsu:Created />
                        <wsu:Expires />
                    </wsu:Timestamp>
                    <wsse:BinarySecurityToken
                        EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary"
                        ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3"
                        wsu:Id="X509-C35717809C92836BA3173565889308341" />
                    <ds:Signature Id="SIG-C35717809C92836BA3173565889315445"
                        xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
                        <ds:SignedInfo>
                            <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
                                <ec:InclusiveNamespaces PrefixList="wsa soap wcf"
                                    xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#" />
                            </ds:CanonicalizationMethod>
                            <ds:SignatureMethod
                                Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256" />
                            <ds:Reference URI="#id-C35717809C92836BA3173565889308344">
                                <ds:Transforms>
                                    <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
                                        <ec:InclusiveNamespaces PrefixList="soap wcf"
                                            xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#" />
                                    </ds:Transform>
                                </ds:Transforms>
                                <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256" />
                                <ds:DigestValue />
                            </ds:Reference>
                        </ds:SignedInfo>
                        <ds:SignatureValue />
                        <ds:KeyInfo Id="KI-C35717809C92836BA3173565889308342">
                            <wsse:SecurityTokenReference wsu:Id="STR-C35717809C92836BA3173565889308343">
                                <wsse:Reference URI="#X509-C35717809C92836BA3173565889308341"
                                    ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3" />
                            </wsse:SecurityTokenReference>
                        </ds:KeyInfo>
                    </ds:Signature>
                </wsse:Security>
                <wsa:Action>http://wcf.dian.colombia/IWcfDianCustomerServices/SendNominaSync</wsa:Action>
                <wsa:To wsu:Id="id-C35717809C92836BA3173565889308344"
                    xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">{WEB_SERVICE}</wsa:To>
            </soap:Header>
            <soap:Body>
                <wcf:SendNominaSync>
                    <wcf:contentFile>{contentFile}</wcf:contentFile>
                </wcf:SendNominaSync>
            </soap:Body>
        </soap:Envelope>
        '''
        return xml_request

    @property
    def template_payroll_test_request(self):
        """
        Envío del SET DE PRUEBAS de nómina (proceso de habilitación).

        Según el WSDL de la DIAN, SendNominaSync solo acepta <contentFile>;
        el identificador del set de pruebas (testSetId) únicamente lo acepta
        SendTestSetAsync (fileName, contentFile, testSetId) -- el mismo método
        que se usa para el set de pruebas de factura. Este es el método que
        exige el portal de habilitación cuando dice "debe proporcionar el
        TestSetId en el web service para el envío de su set de pruebas".

        Es ASÍNCRONO: responde un ZipKey, y el resultado de validación se
        consulta después con GetStatusZip (ver template_status_zip_request).
        """
        xml_request = '''
        <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
            xmlns:wcf="http://wcf.dian.colombia">
            <soap:Header xmlns:wsa="http://www.w3.org/2005/08/addressing">
                <wsse:Security
                    xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
                    xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
                    <wsu:Timestamp wsu:Id="TS-C35717809C92836BA3173565889316046">
                        <wsu:Created />
                        <wsu:Expires />
                    </wsu:Timestamp>
                    <wsse:BinarySecurityToken
                        EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary"
                        ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3"
                        wsu:Id="X509-C35717809C92836BA3173565889308341" />
                    <ds:Signature Id="SIG-C35717809C92836BA3173565889315445"
                        xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
                        <ds:SignedInfo>
                            <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
                                <ec:InclusiveNamespaces PrefixList="wsa soap wcf"
                                    xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#" />
                            </ds:CanonicalizationMethod>
                            <ds:SignatureMethod
                                Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256" />
                            <ds:Reference URI="#id-C35717809C92836BA3173565889308344">
                                <ds:Transforms>
                                    <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
                                        <ec:InclusiveNamespaces PrefixList="soap wcf"
                                            xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#" />
                                    </ds:Transform>
                                </ds:Transforms>
                                <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256" />
                                <ds:DigestValue />
                            </ds:Reference>
                        </ds:SignedInfo>
                        <ds:SignatureValue />
                        <ds:KeyInfo Id="KI-C35717809C92836BA3173565889308342">
                            <wsse:SecurityTokenReference wsu:Id="STR-C35717809C92836BA3173565889308343">
                                <wsse:Reference URI="#X509-C35717809C92836BA3173565889308341"
                                    ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3" />
                            </wsse:SecurityTokenReference>
                        </ds:KeyInfo>
                    </ds:Signature>
                </wsse:Security>
                <wsa:Action>http://wcf.dian.colombia/IWcfDianCustomerServices/SendTestSetAsync</wsa:Action>
                <wsa:To wsu:Id="id-C35717809C92836BA3173565889308344"
                    xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">{WEB_SERVICE}</wsa:To>
            </soap:Header>
            <soap:Body>
                <wcf:SendTestSetAsync>
                    <wcf:fileName>{fileName}</wcf:fileName>
                    <wcf:contentFile>{contentFile}</wcf:contentFile>
                    <wcf:testSetId>{testSetId}</wcf:testSetId>
                </wcf:SendTestSetAsync>
            </soap:Body>
        </soap:Envelope>
        '''
        return xml_request

    @property
    def template_status_zip_request(self):
        """
        Consulta del resultado de un envío asíncrono (SendTestSetAsync),
        usando el ZipKey/trackId devuelto por ese método.
        """
        xml_request = '''
        <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
            xmlns:wcf="http://wcf.dian.colombia">
            <soap:Header xmlns:wsa="http://www.w3.org/2005/08/addressing">
                <wsse:Security
                    xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
                    xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
                    <wsu:Timestamp wsu:Id="TS-C35717809C92836BA3173565889316046">
                        <wsu:Created />
                        <wsu:Expires />
                    </wsu:Timestamp>
                    <wsse:BinarySecurityToken
                        EncodingType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-soap-message-security-1.0#Base64Binary"
                        ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3"
                        wsu:Id="X509-C35717809C92836BA3173565889308341" />
                    <ds:Signature Id="SIG-C35717809C92836BA3173565889315445"
                        xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
                        <ds:SignedInfo>
                            <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
                                <ec:InclusiveNamespaces PrefixList="wsa soap wcf"
                                    xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#" />
                            </ds:CanonicalizationMethod>
                            <ds:SignatureMethod
                                Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256" />
                            <ds:Reference URI="#id-C35717809C92836BA3173565889308344">
                                <ds:Transforms>
                                    <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#">
                                        <ec:InclusiveNamespaces PrefixList="soap wcf"
                                            xmlns:ec="http://www.w3.org/2001/10/xml-exc-c14n#" />
                                    </ds:Transform>
                                </ds:Transforms>
                                <ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256" />
                                <ds:DigestValue />
                            </ds:Reference>
                        </ds:SignedInfo>
                        <ds:SignatureValue />
                        <ds:KeyInfo Id="KI-C35717809C92836BA3173565889308342">
                            <wsse:SecurityTokenReference wsu:Id="STR-C35717809C92836BA3173565889308343">
                                <wsse:Reference URI="#X509-C35717809C92836BA3173565889308341"
                                    ValueType="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-x509-token-profile-1.0#X509v3" />
                            </wsse:SecurityTokenReference>
                        </ds:KeyInfo>
                    </ds:Signature>
                </wsse:Security>
                <wsa:Action>http://wcf.dian.colombia/IWcfDianCustomerServices/GetStatusZip</wsa:Action>
                <wsa:To wsu:Id="id-C35717809C92836BA3173565889308344"
                    xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">{WEB_SERVICE}</wsa:To>
            </soap:Header>
            <soap:Body>
                <wcf:GetStatusZip>
                    <wcf:trackId>{trackId}</wcf:trackId>
                </wcf:GetStatusZip>
            </soap:Body>
        </soap:Envelope>
        '''
        return xml_request

templates_loader = XmlLoader()