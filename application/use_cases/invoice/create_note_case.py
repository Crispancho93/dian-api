import os
import threading
from shared import Config, generic, certificate_loader
from domain.xml_models import CreditNoteXml
from domain.dtos import ControlNotaDto, CreditNoteDto
from shared.certificate import CertificateLoader
from ..sign_docs.xml_signerv3 import XmlSignerV3
from ..soap.soap_invoice import SoapRequest
from ..document.record_document_case import DocumentRecorder
from domain.entities.document import TIPO_NOTA_CREDITO

_config = Config()

class CreateNoteCase:
    """
    Caso de uso para la creación de una nota crédito.
    """

    def __init__(
        self,
        credit_note: CreditNoteDto,
        certificate_loader: CertificateLoader
    ):
        """
        :param credit_note: :class:`CreditNoteDto`
        :param certificate_loader: :class:`CertificateLoader`
        """
        self._certificate_loader = certificate_loader

        # 🔐 Load del certificado
        self._certificate_loader.load(credit_note.Control.InvoiceAuthorization)
        self._security = self._certificate_loader.security


        self.credit_note = credit_note
        self.xml = CreditNoteXml()
        self.xml_name = f'{self.credit_note.ID}'
        self.xml_full_path = os.path.join(_config.PATH_BASE, self.credit_note.Control.InvoiceAuthorization, 'XMLNotas', self.xml_name)
        habilitacion = credit_note.Control.ProfileExecutionID == "2"
        self.soap = SoapRequest(self._security, habilitacion=habilitacion)
    
    @property
    def cude(self):
        tax_amounts = generic.get_cufe_tax_amounts(self.credit_note.Amounts.TaxTotals)

        data = {
            "NumFac": self.credit_note.ID,
            "FecFac": self.credit_note.IssueDate,
            "HorFac": self.credit_note.IssueTime,
            "ValFac": self.credit_note.Amounts.LineExtensionAmount,
            # IVA
            "CodImp1": '01',
            "ValImp1": tax_amounts['01'],
            # Impuesto Nacional al Consumo
            "CodImp2": '04',
            "ValImp2": tax_amounts['04'],
            # ICA
            "CodImp3": '03',
            "ValImp3": tax_amounts['03'],
            "ValTot": self.credit_note.Amounts.TaxInclusiveAmount,
            "NitOFE": self.credit_note.Company.CompanyID,
            "NumAdq": self.credit_note.Customer.ID,
            "ClTec": self.credit_note.Control.Pin,
            "TipoAmbiente": self.credit_note.Control.ProfileExecutionID
        }
        return self.xml.get_cude(data)

    def start(self):
        # Llenar el xml de la factura con todos los datos
        self._set_control(self.credit_note.Control)
        self._set_invoice()
        self._set_company()
        self._set_customer()
        self._set_payment()
        self._set_amounts()
        self._set_lines()
        
        # Firmar Factura
        self.signer = XmlSignerV3(self.xml.get_root, self.credit_note, 'NC', self._security)
        signed_invoice = self.signer.sign()

        # Comprimir Factura
        zip_invoice = generic.zip_document(signed_invoice, f'{self.xml_name}.xml')

        # Guardar .zip en un segundo plano
        args = (zip_invoice, f'{self.xml_full_path}.zip')
        thread = threading.Thread(target=generic.write_file_from_base64, args=args)
        thread.start()

        recorder = DocumentRecorder(
            tipo=TIPO_NOTA_CREDITO,
            numero=self.credit_note.ID,
            cliente_nit=self.credit_note.Company.CompanyID,
            resolucion=self.credit_note.Control.InvoiceAuthorization,
            identificador=self.cude,
            ambiente=self.credit_note.Control.ProfileExecutionID,
            zip_path=f'{self.xml_full_path}.zip',
        )

        # Enviar la Factura
        try:
            response = self.soap.send_xml(zip_invoice)
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
            'credit_note': {
                'Cude': self.cude
            },
        }
    
    def _set_customer(self):
        self.xml.Customer.AdditionalAccountID = self.credit_note.Customer.AdditionalAccountID
        self.xml.Customer.PartyName = self.credit_note.Customer.PartyName
        self.xml.Customer.CompanyID = self.credit_note.Customer.ID
        self.xml.Customer.DocumentType = self.credit_note.Customer.DocumentType
        self.xml.Customer.PartyIdentificationID = self.credit_note.Customer.ID
        self.xml.Customer.TaxLevelCode = self.credit_note.Customer.TaxLevelCode
        self.xml.Customer.ContactElectronicMail = self.credit_note.Customer.Email
        self.xml.Customer.ContactTelephone = self.credit_note.Customer.Telephone
        
        self.xml.Customer.AddressID = self.credit_note.Customer.Address.AddressID
        self.xml.Customer.AddressCountrySubentityCode = self.credit_note.Customer.Address.CountrySubentityCode
        self.xml.Customer.AddressCityName = self.credit_note.Customer.Address.CityName
        self.xml.Customer.AddressCountrySubentity = self.credit_note.Customer.Address.CountrySubentity
        self.xml.Customer.AddressLine = self.credit_note.Customer.Address.AddressLine

        self.xml.Customer.RegistrationName = self.credit_note.Customer.PartyName
        self.xml.Customer.RegistrationID = self.credit_note.Customer.ID
        self.xml.Customer.RegistrationCountrySubentityCode = self.credit_note.Customer.Address.CountrySubentityCode
        self.xml.Customer.RegistrationCityName = self.credit_note.Customer.Address.CityName
        self.xml.Customer.RegistrationCountrySubentity = self.credit_note.Customer.Address.CountrySubentity
        self.xml.Customer.RegistrationAddressLine = self.credit_note.Customer.Address.AddressLine

        self.xml.Customer.LegalRegistrationName = self.credit_note.Customer.PartyName
        self.xml.Customer.LegalCompanyID = self.credit_note.Customer.ID
        self.xml.Customer.LegalDocumentType = self.credit_note.Customer.DocumentType
        self.xml.Customer.Email = self.credit_note.Customer.Email
    
    def _set_company(self):
        self.xml.Company.AdditionalAccountID = self.credit_note.Company.AdditionalAccountID
        self.xml.Company.PartyName = self.credit_note.Company.PartyName
        self.xml.Company.CompanyID = self.credit_note.Company.CompanyID
        self.xml.Company.DocumentType = self.credit_note.Company.DocumentType
        self.xml.Company.VerificationDigit = self.credit_note.Company.VerificationDigit
        self.xml.Company.TaxLevelCode = self.credit_note.Company.TaxLevelCode
        self.xml.Company.ContactElectronicMail = self.credit_note.Company.Email
        self.xml.Company.ContactTelephone = self.credit_note.Company.Telephone
        
        self.xml.Company.AddressID = self.credit_note.Company.Address.AddressID
        self.xml.Company.AddressCityName = self.credit_note.Company.Address.CityName
        self.xml.Company.AddressCountrySubentityCode = self.credit_note.Company.Address.CountrySubentityCode
        self.xml.Company.AddressCountrySubentity = self.credit_note.Company.Address.CountrySubentity
        self.xml.Company.AddressLine = self.credit_note.Company.Address.AddressLine

        self.xml.Company.RegistrationName = self.credit_note.Company.PartyName
        self.xml.Company.RegistrationID = self.credit_note.Company.Address.AddressID
        self.xml.Company.RegistrationCityName = self.credit_note.Company.Address.CityName
        self.xml.Company.RegistrationCountrySubentityCode = self.credit_note.Company.Address.CountrySubentityCode
        self.xml.Company.RegistrationCountrySubentity = self.credit_note.Company.Address.CountrySubentity
        self.xml.Company.RegistrationAddressLine = self.credit_note.Company.Address.AddressLine

        self.xml.Company.LegalRegistrationName = self.credit_note.Company.PartyName
        self.xml.Company.LegalCompanyID = self.credit_note.Company.CompanyID
        self.xml.Company.Email = self.credit_note.Company.Email
    
    def _set_lines(self):
        for index, line in enumerate(self.credit_note.Lines):
            line.ID = index  + 1
            self.xml.add_credit_note_line(line.__dict__)
    
    def _set_amounts(self):
        self.xml.Amounts.LineExtensionAmount = self.credit_note.Amounts.LineExtensionAmount #  Subtotal - Total Valor Bruto antes de tributos
        self.xml.Amounts.TaxExclusiveAmount = self.credit_note.Amounts.TaxExclusiveAmount #  Subtotal - Total Valor Bruto antes de tributos
        self.xml.Amounts.TaxInclusiveAmount = self.credit_note.Amounts.TaxInclusiveAmount # Total de Valor Bruto mas tributos
        self.xml.Amounts.PrepaidAmount = self.credit_note.Amounts.PrepaidAmount # 
        self.xml.Amounts.PayableAmount = self.credit_note.Amounts.PayableAmount # Total que paga el cliente - Total de Valor Bruto mas tributos

        # 13.2.2 Tributos, Lista de tributos que general la factura
        for item in self.credit_note.Amounts.TaxTotals:
            tax_data = {
                "tax_amount": item.TaxAmount, # Total del impuesto generado (IVA/IC/ICA)
                "lines": item.TaxSubtotal
            }
            self.xml.add_tax_total(**tax_data)
    
    def _set_payment(self):
        self.xml.Payment.PaymentID = self.credit_note.Payment.PaymentID
        self.xml.Payment.PaymentCode = self.credit_note.Payment.PaymentCode

    def _set_invoice(self):
        self.xml.ID = self.credit_note.ID
        self.xml.IssueDate = self.credit_note.IssueDate
        self.xml.IssueTime = self.credit_note.IssueTime
        self.xml.LineCountNumeric = str(len(self.credit_note.Lines))
        self.xml.UUID = self.cude
        self.xml.ReferenceID = self.credit_note.Billing.ID

        self.xml.BillingID = self.credit_note.Billing.ID
        self.xml.BillingUUID = self.credit_note.Billing.UUID
        self.xml.BillingIssueDate = self.credit_note.Billing.IssueDate

    def _set_control(self, control: ControlNotaDto):
        self.xml.Control.ProviderID = control.ProviderID
        self.xml.Control.SoftwareID = control.SoftwareID
        self.xml.Control.SoftwareSecurityCode = f"{control.SoftwareID}{control.Pin}{self.credit_note.ID}"
        self.xml.Control.QRCode = f'https://catalogovpfe.dian.gov.co/document/searchqr?documentkey={self.cude}'
        self.xml.Control.ProfileExecutionID = control.ProfileExecutionID

        self.xml.Control.VerificationDigit = self.credit_note.Company.VerificationDigit