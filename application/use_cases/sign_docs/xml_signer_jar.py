import os
import subprocess
from shared import Config
from domain.dtos import InvoiceDto

_config = Config()

class XMLSignerJar:
    def __init__(self, invoice: InvoiceDto, xml_input: str):
        self.invoice = invoice
        self.xml_input = xml_input
        self.jar_path = os.path.join(_config.PATH_BASE, 'jar', 'FirmaDianv2.jar')
        self.pfx_path = os.path.join(_config.PATH_BASE, 'certificados', _config.SIGN_NAME)
        self.pfx_password = _config.SIGN_PASSWORD

        xml_file_name = f'FV{self.invoice.ID}-dian.xml'
        self.xml_output = os.path.join(_config.PATH_BASE, invoice.Control.InvoiceAuthorization, 'XMLFirmados', xml_file_name)
        self.pdf_policies = os.path.join(_config.PATH_BASE, 'certificados', 'politicadefirmav2.pdf')
        
    def sign(self):
        command = [
            'java', '-jar', self.jar_path, 
            self.xml_input, 
            self.pfx_path, 
            self.pfx_password, 
            self.xml_output, 
            self.pdf_policies
        ]
        
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.stderr:
            raise Exception(result.stderr)
        
        if 'Firmado' not in result.stdout:
            raise Exception(result.stdout)
        
        return self.xml_output
