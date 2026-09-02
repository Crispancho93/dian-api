import os
import threading

from shared import Config, generic
from domain.xml_models.documento_soporte.documento_soporte_xml import DocumentoSoporteXml
from domain.dtos.documento_soporte_dto import DocumentoSoporteDTO, ControlDto
from shared.certificate import CertificateLoader
from ..sign_docs.xml_signerv3 import XmlSignerV3
from ..soap.soap_invoice import SoapRequest
from ..document.record_document_case import DocumentRecorder
from domain.entities.document import TIPO_DOCUMENTO_SOPORTE

_config = Config()


class CreateDocumentoSoporteCase:
    """
    Caso de uso para el Documento Soporte en adquisiciones efectuadas a
    sujetos no obligados a expedir factura de venta (DS).
    """

    def __init__(
        self,
        documento_soporte: DocumentoSoporteDTO,
        certificate_loader: CertificateLoader
    ):
        """
        :param documento_soporte: :class:`DocumentoSoporteDTO`
        :param certificate_loader: :class:`CertificateLoader`
        """
        self._certificate_loader = certificate_loader

        # 🔐 Load del certificado (por resolución, igual que factura/nota)
        self._certificate_loader.load(documento_soporte.Control.InvoiceAuthorization)
        self._security = self._certificate_loader.security

        self.documento_soporte = documento_soporte
        self.xml = DocumentoSoporteXml()

        self.xml_name = f'DocSop_{self.documento_soporte.Control.Prefix}_{self.documento_soporte.ID}.xml'
        self.zip_name = f'DocSop_{self.documento_soporte.Control.Prefix}_{self.documento_soporte.ID}.zip'
        self.zip_full_path = os.path.join(
            _config.PATH_BASE,
            self.documento_soporte.Control.InvoiceAuthorization,
            'XMLDocSoporte',
            self.zip_name
        )

        habilitacion = documento_soporte.Control.ProfileExecutionID == "2"
        self.soap = SoapRequest(self._security, habilitacion=habilitacion)

    @property
    def cuds(self):
        total_base = sum(float(item.LineExtensionAmount) for item in self.documento_soporte.Lines)
        total_tax = sum(float(item.TaxAmount) for item in self.documento_soporte.Lines)
        total_iv = (
            float(self.documento_soporte.Amounts.TaxInclusiveAmount)
            if self.documento_soporte.Amounts else total_base + total_tax
        )

        data = {
            "NumDS": self.documento_soporte.ID,
            "FecDS": self.documento_soporte.IssueDate,
            "HorDS": self.documento_soporte.IssueTime,
            "ValDS": f"{total_base:.2f}",
            "CodImp": "01",
            "ValImp": f"{total_tax:.2f}" if total_tax > 0 else "0.00",
            "ValTot": f"{total_iv:.2f}",
            "NitOFE": self.documento_soporte.Customer.ID,
            "NumAdq": self.documento_soporte.Company.CompanyID,
            "SoftwarePIN": self.documento_soporte.Control.Pin,
            "TipoAmbiente": self.documento_soporte.Control.ProfileExecutionID
        }

        return self.xml.get_cuds(data)

    def _create(self):
        self._set_control(self.documento_soporte.Control)
        self._set_company()
        self._set_customer()
        self._set_invoice()
        self._set_amounts()
        self._set_payment()
        self._set_lines()
        self._set_invoice_period()

        # Firmar Documento Soporte
        self.signer = XmlSignerV3(self.xml.get_root, self.documento_soporte, 'DS', self._security)
        signed_document = self.signer.sign()

        return signed_document

    def start(self):
        signed_document = self._create()

        # Comprimir
        zip_document = generic.zip_document(signed_document, self.xml_name)

        # Guardar .zip en un segundo plano
        args = (zip_document, self.zip_full_path)
        thread = threading.Thread(target=generic.write_file_from_base64, args=args)
        thread.start()

        recorder = DocumentRecorder(
            tipo=TIPO_DOCUMENTO_SOPORTE,
            numero=self.documento_soporte.ID,
            cliente_nit=self.documento_soporte.Company.CompanyID,
            resolucion=self.documento_soporte.Control.InvoiceAuthorization,
            identificador=self.cuds,
            ambiente=self.documento_soporte.Control.ProfileExecutionID,
            zip_path=self.zip_full_path,
        )

        # Enviar el Documento Soporte
        try:
            response = self.soap.send_xml(zip_document)
            is_valid, messages = generic.extract_errors_invoice(response.text)
            recorder.finish(is_valid, messages, response.text)

            if is_valid == 'false':
                print(f"Error al enviar el documento soporte. XML enviado: {self.xml_name}")
                print(f"Error al enviar el documento soporte. Respuesta XML: {response.text}")
                raise Exception(messages)

        except Exception as e:
            recorder.fail(str(e))
            print(f"Error al enviar el documento soporte. XML enviado: {self.xml_name}")
            print(f"Error al enviar el documento soporte. Respuesta XML: {e}")
            raise Exception(e)

        return {
            'messages': messages,
            'documento_soporte': {
                'Cuds': self.cuds
            },
        }

    def _set_company(self):
        self.xml.Company.AdditionalAccountID = self.documento_soporte.Company.AdditionalAccountID
        self.xml.Company.PartyName = self.documento_soporte.Company.PartyName
        self.xml.Company.RegistrationName = self.documento_soporte.Company.PartyName
        self.xml.Company.LegalRegistrationName = self.documento_soporte.Company.PartyName
        self.xml.Company.CompanyID = self.documento_soporte.Company.CompanyID
        self.xml.Company.DocumentType = self.documento_soporte.Company.DocumentType
        self.xml.Company.VerificationDigit = self.documento_soporte.Company.VerificationDigit
        self.xml.Company.TaxLevelCode = self.documento_soporte.Company.TaxLevelCode

        addr = self.documento_soporte.Company.Address
        self.xml.Company.AddressID = addr.AddressID
        self.xml.Company.AddressPostalZone = addr.AddressID
        self.xml.Company.AddressCountrySubentity = addr.CountrySubentity
        self.xml.Company.AddressCountrySubentityCode = addr.CountrySubentityCode
        self.xml.Company.AddressLine = addr.AddressLine

    def _set_customer(self):
        self.xml.Customer.AdditionalAccountID = self.documento_soporte.Customer.AdditionalAccountID
        self.xml.Customer.PartyName = self.documento_soporte.Customer.PartyName
        self.xml.Customer.RegistrationName = self.documento_soporte.Customer.PartyName
        self.xml.Customer.VerificationDigit = self.documento_soporte.Customer.VerificationDigit
        self.xml.Customer.CompanyID = self.documento_soporte.Customer.ID
        self.xml.Customer.DocumentType = self.documento_soporte.Customer.DocumentType
        self.xml.Customer.TaxLevelCode = self.documento_soporte.Customer.TaxLevelCode

        self.xml.Customer.ContactTelephone = self.documento_soporte.Customer.Telephone
        self.xml.Customer.ContactElectronicMail = self.documento_soporte.Customer.Email

        addr = self.documento_soporte.Customer.Address
        self.xml.Customer.AddressID = addr.AddressID
        self.xml.Customer.AddressPostalZone = addr.AddressID
        self.xml.Customer.AddressCountrySubentity = addr.CountrySubentity
        self.xml.Customer.AddressCountrySubentityCode = addr.CountrySubentityCode
        self.xml.Customer.AddressLine = addr.AddressLine

    def _set_lines(self):
        for line in self.documento_soporte.Lines:
            raw_data = line.model_dump() if hasattr(line, 'model_dump') else line.dict()
            line_data = {
                "ID": raw_data.get("ID"),
                "Quantity": raw_data.get("Quantity"),
                "LineExtensionAmount": raw_data.get("LineExtensionAmount"),
                "TaxAmount": raw_data.get("TaxAmount"),
                "TaxableAmount": raw_data.get("TaxableAmount"),
                "TaxSubtotalAmount": raw_data.get("TaxSubtotalAmount"),
                "TaxPercent": raw_data.get("TaxPercent"),
                "TaxSchemeID": raw_data.get("TaxSchemeID"),
                "TaxSchemeName": raw_data.get("TaxSchemeName"),
                "Description": raw_data.get("Description"),
                "SellersItemID": raw_data.get("SellersItemID"),
                "SellersItemExtendedID": raw_data.get("SellersItemExtendedID"),
                "AdditionalItemID": raw_data.get("AdditionalItemID"),
                "PriceAmount": raw_data.get("PriceAmount"),
                "BaseQuantity": raw_data.get("BaseQuantity"),
                "DiscountAmount": raw_data.get("DiscountAmount", "0.00"),
                "DiscountPercent": raw_data.get("DiscountPercent", "0.00"),
                "WithholdingTax": raw_data.get("WithholdingTax"),
                "PeriodStartDate": self.documento_soporte.IssueDate,
            }
            self.xml.add_invoice_line(line_data)

    def _set_amounts(self):
        self.xml.Amounts.LineExtensionAmount = self.documento_soporte.Amounts.LineExtensionAmount
        self.xml.Amounts.TaxExclusiveAmount = self.documento_soporte.Amounts.TaxExclusiveAmount
        self.xml.Amounts.TaxInclusiveAmount = self.documento_soporte.Amounts.TaxInclusiveAmount
        self.xml.Amounts.PrepaidAmount = self.documento_soporte.Amounts.PrepaidAmount
        self.xml.Amounts.PayableAmount = self.documento_soporte.Amounts.PayableAmount
        self.xml.Amounts.TaxTotals = self.documento_soporte.Amounts.TaxTotals

        if hasattr(self.documento_soporte.Amounts, 'WithholdingTaxTotals'):
            self.xml.Amounts.WithholdingTaxTotals = self.documento_soporte.Amounts.WithholdingTaxTotals

            if hasattr(self.documento_soporte.Amounts, 'WithholdingTaxTotalsICA'):
                self.xml.Amounts.WithholdingTaxTotalsICA = (
                    self.documento_soporte.Amounts.WithholdingTaxTotalsICA
                )

    def _set_payment(self):
        self.xml.Payment.PaymentID = self.documento_soporte.Payment.PaymentID
        self.xml.Payment.PaymentCode = self.documento_soporte.Payment.PaymentCode

    def _set_invoice(self):
        self.xml.ID = self.documento_soporte.ID
        self.xml.IssueDate = self.documento_soporte.IssueDate
        self.xml.IssueTime = self.documento_soporte.IssueTime
        self.xml.DueDate = self.documento_soporte.IssueDate
        self.xml.PeriodStartDate = self.documento_soporte.IssueDate
        self.xml.PeriodEndDate = self.documento_soporte.IssueDate

        self.xml.LineCountNumeric = str(len(self.documento_soporte.Lines))
        self.xml.UUID = self.cuds
        self.xml.Note = self.documento_soporte.Note

    def _set_control(self, control: ControlDto):
        self.xml.Control.StartDate = control.StartDate
        self.xml.Control.EndDate = control.EndDate
        self.xml.Control.InvoiceAuthorization = control.InvoiceAuthorization
        self.xml.Control.Prefix = control.Prefix
        self.xml.Control.From = control.From
        self.xml.Control.To = control.To
        self.xml.Control.ProviderID = control.ProviderID
        self.xml.Control.SoftwareID = control.SoftwareID
        self.xml.Control.Pin = control.Pin
        self.xml.Control.TechnicalKey = control.TechnicalKey

        self.xml.Control.SoftwareSecurityCode = (
            f"{control.SoftwareID}{control.Pin}{self.documento_soporte.ID}"
        )

        # ============================================================
        # AMBIENTE DIAN
        # 1 = Producción
        # 2 = Habilitación / Pruebas
        # ============================================================
        ambiente = str(control.ProfileExecutionID)

        qr_urls = {
            "1": "https://catalogo-vpfe.dian.gov.co",
            "2": "https://catalogo-vpfe-hab.dian.gov.co"
        }

        if ambiente not in qr_urls:
            raise ValueError(
                f"ProfileExecutionID no válido para DIAN: {ambiente}. "
                f"Valores permitidos: 1=Producción, 2=Habilitación."
            )

        # Primero dejamos informado el ambiente
        self.xml.Control.ProfileExecutionID = ambiente

        # Luego construimos el QR según el ambiente
        self.xml.Control.QRCode = (
            f"{qr_urls[ambiente]}/document/searchqr"
            f"?documentkey={self.cuds}"
        )

        self.xml.Control.VerificationDigit = (
            self.documento_soporte.Company.VerificationDigit
        )

    def _set_invoice_period(self):
        self.xml.PeriodStartDate = self.documento_soporte.IssueDate
        self.xml.PeriodEndDate = self.documento_soporte.IssueDate
