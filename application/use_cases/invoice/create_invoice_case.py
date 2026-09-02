import os
import threading
from shared import Config, generic
from domain.xml_models import InvoiceXml
from domain.dtos import ControlDto, InvoiceDto
from shared.certificate import CertificateLoader
from ..sign_docs.xml_signerv3 import XmlSignerV3
from ..soap.soap_invoice import SoapRequest
from ..soap.soap_test import SoapRequestTest
from ..document.record_document_case import DocumentRecorder
from domain.entities.document import TIPO_FACTURA

_config = Config()

class CreateInvoiceCase:
    """
    Caso de uso para la creación de facturas.
    """

    def __init__(
        self,
        invoice: InvoiceDto,
        certificate_loader: CertificateLoader
    ):
        """
        :param invoice: :class:`InvoiceDto`
        :param certificate_loader: :class:`CertificateLoader`
        """
        self._certificate_loader = certificate_loader

        # 🔐 Load del certificado
        self._certificate_loader.load(invoice.Control.InvoiceAuthorization)
        self._security = self._certificate_loader.security

        self.invoice = invoice
        self.xml = InvoiceXml()

        # ✅ Inyección del certificado
        habilitacion = invoice.Control.ProfileExecutionID == "2"
        self.soap_invoice = SoapRequest(self._security, habilitacion=habilitacion)
        self.soap_test = SoapRequestTest(self._security, invoice.Control.TestID)

        self.xml_name = f'FV{self.invoice.ID}.xml'
        self.zip_name = f'FV{self.invoice.ID}.zip'

        self.zip_full_path = os.path.join(_config.PATH_BASE, self.invoice.Control.InvoiceAuthorization, 'XMLFacturas', self.zip_name)
    
    @property
    def cufe(self):
        tax_amounts = generic.get_cufe_tax_amounts(self.invoice.Amounts.TaxTotals)

        data = {
            "NumFac": self.invoice.ID,
            "FecFac": self.invoice.IssueDate,
            "HorFac": self.invoice.IssueTime,
            "ValFac": self.invoice.Amounts.LineExtensionAmount,
            # IVA
            "CodImp1": '01',
            "ValImp1": tax_amounts['01'],
            # Impuesto Nacional al Consumo
            "CodImp2": '04',
            "ValImp2": tax_amounts['04'],
            # ICA
            "CodImp3": '03',
            "ValImp3": tax_amounts['03'],
            "ValTot": self.invoice.Amounts.TaxInclusiveAmount,
            "NitOFE": self.invoice.Company.CompanyID,
            "NumAdq": self.invoice.Customer.ID,
            "ClTec": self.invoice.Control.TechnicalKey,
            "TipoAmbiente": self.invoice.Control.ProfileExecutionID
        }
        return self.xml.get_cufe(data)

    def _recorder(self) -> DocumentRecorder:
        """Recorder para dejar traza del envío en la tabla `document`."""
        return DocumentRecorder(
            tipo=TIPO_FACTURA,
            numero=self.invoice.ID,
            cliente_nit=self.invoice.Company.CompanyID,
            resolucion=self.invoice.Control.InvoiceAuthorization,
            identificador=self.cufe,
            ambiente=self.invoice.Control.ProfileExecutionID,
            zip_path=self.zip_full_path,
        )

    def _create(self):
        # Llenar el xml de la factura con todos los datos
        self._set_control(self.invoice.Control)
        self._set_company()
        self._set_customer()
        self._set_invoice()
        self._set_amounts()
        self._set_payment()
        self._set_lines()

        # Firmar Factura
        self.signer = XmlSignerV3(self.xml.get_root, self.invoice, 'FV', self._security)
        signed_invoice = self.signer.sign()
        
        return signed_invoice
 
    def send(self):
        signed_invoice = self._create()

        # Comprimir Factura
        zip_invoice = generic.zip_document(signed_invoice, self.xml_name)

        # Guardar .zip en un segundo plano
        args = (zip_invoice, self.zip_full_path)
        thread = threading.Thread(target=generic.write_file_from_base64, args=args)
        thread.start()

        recorder = self._recorder()

        # Enviar la Factura
        try:
            response = self.soap_invoice.send_xml(zip_invoice)
            is_valid, messages = generic.extract_errors_invoice(response.text)
            recorder.finish(is_valid, messages, response.text)

            if is_valid == 'false':
                print(f"Error al enviar la factura. XML enviado: {self.xml_name}")
                print(f"Error al enviar la factura. Respuesta XML: {response.text}")
                raise Exception(messages)

        except Exception as e:
            recorder.fail(str(e))
            print(f"Error al enviar la factura. XML enviado: {self.xml_name}")
            print(f"Error al enviar la factura. Respuesta XML: {e}")
            raise Exception(e)
        
        return {
            'messages': messages,
            'invoice': {
                'Cufe': self.cufe
            },
        }

    def send_test(self):
        signed_invoice = self._create()

        # Comprimir Factura
        zip_invoice = generic.zip_document(signed_invoice, self.xml_name)

        # Guardar .zip en un segundo plano
        args = (zip_invoice, self.zip_full_path)
        thread = threading.Thread(target=generic.write_file_from_base64, args=args)
        thread.start()

        # Enviar la Factura
        try:
            response = self.soap_test.send_xml(zip_invoice)
            return { "status": response.status_code, "text": response.text }
        except Exception as e:
            print(f"Error al enviar la factura. XML enviado: {self.xml_name}")
            print(f"Error al enviar la factura. Respuesta XML: {e}")
            raise Exception(e)

    def _set_customer(self):
        self.xml.Customer.AdditionalAccountID = self.invoice.Customer.AdditionalAccountID
        self.xml.Customer.PartyName = self.invoice.Customer.PartyName
        self.xml.Customer.CompanyID = self.invoice.Customer.ID
        self.xml.Customer.DocumentType = self.invoice.Customer.DocumentType
        self.xml.Customer.PartyIdentificationID = self.invoice.Customer.ID
        self.xml.Customer.TaxLevelCode = self.invoice.Customer.TaxLevelCode
        self.xml.Customer.ContactElectronicMail = self.invoice.Customer.Email
        self.xml.Customer.ContactTelephone = self.invoice.Customer.Telephone
        
        self.xml.Customer.AddressID = self.invoice.Customer.Address.AddressID
        self.xml.Customer.AddressCountrySubentityCode = self.invoice.Customer.Address.CountrySubentityCode
        self.xml.Customer.AddressCityName = self.invoice.Customer.Address.CityName
        self.xml.Customer.AddressCountrySubentity = self.invoice.Customer.Address.CountrySubentity
        self.xml.Customer.AddressLine = self.invoice.Customer.Address.AddressLine

        self.xml.Customer.RegistrationName = self.invoice.Customer.PartyName
        self.xml.Customer.RegistrationID = self.invoice.Customer.ID
        self.xml.Customer.RegistrationCountrySubentityCode = self.invoice.Customer.Address.CountrySubentityCode
        self.xml.Customer.RegistrationCityName = self.invoice.Customer.Address.CityName
        self.xml.Customer.RegistrationCountrySubentity = self.invoice.Customer.Address.CountrySubentity
        self.xml.Customer.RegistrationAddressLine = self.invoice.Customer.Address.AddressLine

        self.xml.Customer.LegalRegistrationName = self.invoice.Customer.PartyName
        self.xml.Customer.LegalCompanyID = self.invoice.Customer.ID
        self.xml.Customer.LegalDocumentType = self.invoice.Customer.DocumentType
    
    def _set_company(self):
        self.xml.Company.AdditionalAccountID = self.invoice.Company.AdditionalAccountID
        self.xml.Company.PartyName = self.invoice.Company.PartyName
        self.xml.Company.CompanyID = self.invoice.Company.CompanyID
        self.xml.Company.DocumentType = self.invoice.Company.DocumentType
        self.xml.Company.VerificationDigit = self.invoice.Company.VerificationDigit
        self.xml.Company.TaxLevelCode = self.invoice.Company.TaxLevelCode
        self.xml.Company.ContactElectronicMail = self.invoice.Company.Email
        self.xml.Company.ContactTelephone = self.invoice.Company.Telephone
        
        self.xml.Company.AddressID = self.invoice.Company.Address.AddressID
        self.xml.Company.AddressCityName = self.invoice.Company.Address.CityName
        self.xml.Company.AddressCountrySubentityCode = self.invoice.Company.Address.CountrySubentityCode
        self.xml.Company.AddressCountrySubentity = self.invoice.Company.Address.CountrySubentity
        self.xml.Company.AddressLine = self.invoice.Company.Address.AddressLine

        self.xml.Company.RegistrationName = self.invoice.Company.PartyName
        self.xml.Company.RegistrationID = self.invoice.Company.Address.AddressID
        self.xml.Company.RegistrationCityName = self.invoice.Company.Address.CityName
        self.xml.Company.RegistrationCountrySubentityCode = self.invoice.Company.Address.CountrySubentityCode
        self.xml.Company.RegistrationCountrySubentity = self.invoice.Company.Address.CountrySubentity
        self.xml.Company.RegistrationAddressLine = self.invoice.Company.Address.AddressLine

        self.xml.Company.LegalRegistrationName = self.invoice.Company.PartyName
        self.xml.Company.LegalCompanyID = self.invoice.Company.CompanyID
        self.xml.Company.LegalDocumentType = self.invoice.Company.DocumentType
        self.xml.Company.LegalVerificationDigit = self.invoice.Company.VerificationDigit

        self.xml.Company.CorporateRegistrationID = self.invoice.Control.Prefix
    
    def _set_lines(self):
        for index, line in enumerate(self.invoice.Lines):
            line.ID = index  + 1
            self.xml.add_invoice_line(line.__dict__)
    
    def _set_amounts(self):
        self.xml.Amounts.LineExtensionAmount = self.invoice.Amounts.LineExtensionAmount #  Subtotal - Total Valor Bruto antes de tributos
        self.xml.Amounts.TaxExclusiveAmount = self.invoice.Amounts.TaxExclusiveAmount #  Subtotal - Total Valor Bruto antes de tributos
        self.xml.Amounts.TaxInclusiveAmount = self.invoice.Amounts.TaxInclusiveAmount # Total de Valor Bruto mas tributos
        self.xml.Amounts.PrepaidAmount = self.invoice.Amounts.PrepaidAmount # 
        self.xml.Amounts.PayableAmount = self.invoice.Amounts.PayableAmount # Total que paga el cliente - Total de Valor Bruto mas tributos

        
        # ✅ DEFINIR tax_data ANTES DEL IF
        tax_data = {
            "tax_amount": "0.00",
            "lines": []
        }

        
        if self.invoice.Amounts.TaxTotals:
            for item in self.invoice.Amounts.TaxTotals:
                tax_data = {
                    "tax_amount": item.TaxAmount,
                    "lines": item.TaxSubtotal
                }
                self.xml.add_tax_total(**tax_data)
        else:
            self.xml.add_tax_total(**tax_data)

    def _set_payment(self):
        self.xml.Payment.PaymentID = self.invoice.Payment.PaymentID
        self.xml.Payment.PaymentCode = self.invoice.Payment.PaymentCode

    def _set_invoice(self):
        firt_day, last_day = generic.get_period(self.invoice.IssueDate)

        self.xml.ID = self.invoice.ID
        self.xml.IssueDate = self.invoice.IssueDate
        self.xml.IssueTime = self.invoice.IssueTime
        self.xml.LineCountNumeric = str(len(self.invoice.Lines))
        self.xml.PeriodStartDate = firt_day
        self.xml.PeriodEndDate = last_day
        self.xml.UUID = self.cufe

    def _set_control(self, control: ControlDto):
        self.xml.Control.StartDate = control.StartDate
        self.xml.Control.EndDate = control.EndDate
        self.xml.Control.InvoiceAuthorization = control.InvoiceAuthorization
        self.xml.Control.Prefix = control.Prefix
        self.xml.Control.From = control.From
        self.xml.Control.To = control.To
        self.xml.Control.ProviderID = control.ProviderID
        self.xml.Control.SoftwareID = control.SoftwareID
        self.xml.Control.SoftwareSecurityCode = f"{control.SoftwareID}{control.Pin}{self.invoice.ID}"
        self.xml.Control.QRCode = f'https://catalogovpfe.dian.gov.co/document/searchqr?documentkey={self.cufe}'
        self.xml.Control.ProfileExecutionID = control.ProfileExecutionID

        self.xml.Control.VerificationDigit = self.invoice.Company.VerificationDigit

