import requests
from shared import templates_loader
from shared.config import resolve_web_service
from shared.certificate import CertificateData
from .soap_base import SoapBase

class SoapRequest(SoapBase):
    """
    Servicio para el envío de facturas a través de SOAP.
    """

    def __init__(self, certificate_data: CertificateData, habilitacion: bool = False):
        """
        :param certificate_data: :class:`CertificateData`
        :param habilitacion: si es True, envía al ambiente de habilitación de la DIAN en vez de producción
        """
        super().__init__(certificate_data)
        self.xml_template = templates_loader.template.xml_request
        self.web_service = resolve_web_service(habilitacion)

    def _send_soap_request(self, xml_request):
        url = self.web_service
        headers = {
            'Content-Type': 'application/soap+xml; charset=utf-8',
            'SOAPAction': f'http://wcf.dian.colombia/IWcfDianCustomerServices/SendBillSync'
        }

        response = requests.post(url, data=xml_request, headers=headers)
        response.raise_for_status()

        return response

    def send_xml(self, base64_file):
        self.xml_template = self.xml_template.format(
            WEB_SERVICE=self.web_service,
            contentFile=base64_file
        )

        xml_request = self.prepare_xml(self.xml_template)
        return self._send_soap_request(xml_request)
