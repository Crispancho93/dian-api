import requests
from lxml import etree

from shared import templates_loader
from shared.config import resolve_web_service
from shared.certificate import CertificateData
from .soap_base import SoapBase

class SoapClave(SoapBase):
    def __init__(self, certificate_data: CertificateData, account_code, account_code_t, software_code, habilitacion: bool = False):
        super().__init__(certificate_data)
        self.account_code = account_code
        self.account_code_t = account_code_t
        self.software_code = software_code
        self.web_service = resolve_web_service(habilitacion)

        self.xml_template = templates_loader.template.xml_range.format(
            account_code=account_code,
            account_code_t=account_code_t,
            software_code=software_code,
            WEB_SERVICE=self.web_service
        )

    def get_numbering_range(self):
        xml_request = self.prepare_xml(self.xml_template)

        url = self.web_service
        headers = {
            "Content-Type": "application/soap+xml; charset=utf-8",
            "SOAPAction": "http://wcf.dian.colombia/IWcfDianCustomerServices/GetNumberingRange"
        }

        try:
            response = requests.post(url, data=xml_request.encode("utf-8"), headers=headers, timeout=25)

            if not response.ok:
                raise Exception(
                    f"❌ Error HTTP {response.status_code} - {response.reason}\n"
                    f"Respuesta DIAN:\n{response.text}"
                )
            
            clave_tecnica = self._extract_clave_tecnica(response.text)
            return clave_tecnica
        except requests.exceptions.RequestException as e:
            raise Exception(f"❌ Error de conexión con la DIAN: {str(e)}")

    def _extract_clave_tecnica(self, soap_response: str):
        """
        Extrae el listado de rangos (resoluciones) y sus claves técnicas desde la respuesta SOAP de la DIAN.
        """
        try:
            root = etree.fromstring(soap_response.encode("utf-8") if isinstance(soap_response, str) else soap_response)

            nsmap = {
                'c': 'http://schemas.datacontract.org/2004/07/NumberRangeResponse'
            }

            responses = root.findall('.//c:NumberRangeResponse', namespaces=nsmap)
            if not responses:
                raise Exception("No se encontraron rangos de numeración en la respuesta SOAP.")

            result = []
            for item in responses:
                def _get_text(tag_name: str):
                    node = item.find(f'c:{tag_name}', namespaces=nsmap)
                    if node is None or node.text is None:
                        return None
                    value = node.text.strip()
                    return value if value else None

                result.append({
                    "resolution_number": _get_text("ResolutionNumber"),
                    "resolution_date": _get_text("ResolutionDate"),
                    "prefix": _get_text("Prefix"),
                    "from_number": _get_text("FromNumber"),
                    "to_number": _get_text("ToNumber"),
                    "valid_date_from": _get_text("ValidDateFrom"),
                    "valid_date_to": _get_text("ValidDateTo"),
                    "technical_key": _get_text("TechnicalKey"),
                })

            return result
        
        except Exception as e:
            raise Exception(f"❌ Error extrayendo clave técnica: {str(e)}")


