import os
import threading

from shared import Config, generic
from domain.xml_models.nota_ajuste_ds.nota_ajuste_xml import NotaAjusteDocumentoSoporteXml
from domain.dtos.nota_ajuste_ds_dto import NotaAjusteDocumentoSoporteDTO, ControlNotaAjusteDto
from shared.certificate import CertificateLoader
from ..sign_docs.xml_signerv3 import XmlSignerV3
from ..soap.soap_invoice import SoapRequest
from ..document.record_document_case import DocumentRecorder
from domain.entities.document import TIPO_NOTA_AJUSTE_DS

_config = Config()


class CreateNotaAjusteDocumentoSoporteCase:
    """
    Caso de uso para la Nota de Ajuste al Documento Soporte (NAS, CreditNote
    tipo 95): corrige o anula un documento soporte ya emitido.
    """

    def __init__(
        self,
        nota_ajuste: NotaAjusteDocumentoSoporteDTO,
        certificate_loader: CertificateLoader
    ):
        """
        :param nota_ajuste: :class:`NotaAjusteDocumentoSoporteDTO`
        :param certificate_loader: :class:`CertificateLoader`
        """
        self._certificate_loader = certificate_loader

        # 🔐 Load del certificado (por resolución, igual que factura/nota/DS)
        self._certificate_loader.load(nota_ajuste.Control.InvoiceAuthorization)
        self._security = self._certificate_loader.security

        self.nota_ajuste = nota_ajuste
        self.xml = NotaAjusteDocumentoSoporteXml()

        self.xml_name = f'NotaAjusteDS_{self.nota_ajuste.ID}.xml'
        self.zip_name = f'NotaAjusteDS_{self.nota_ajuste.ID}.zip'
        self.zip_full_path = os.path.join(
            _config.PATH_BASE,
            self.nota_ajuste.Control.InvoiceAuthorization,
            'XMLNotasDocSoporte',
            self.zip_name
        )

        habilitacion = nota_ajuste.Control.ProfileExecutionID == "2"
        self.soap = SoapRequest(self._security, habilitacion=habilitacion)

    @property
    def cuds(self):
        """CUDS de la nota de ajuste.

        Misma fórmula que el documento soporte (§14.1: el CUDS aplica a los dos
        instrumentos), calculada sobre los datos de ESTA nota, no del documento
        corregido. Y con los roles invertidos igual que allá:
        NitOFE = el proveedor (SNO), NumAdq = mi empresa (ABS).
        """
        total_base = sum(float(item.LineExtensionAmount) for item in self.nota_ajuste.Lines)
        total_tax = sum(float(item.TaxAmount) for item in self.nota_ajuste.Lines)
        total_iv = (
            float(self.nota_ajuste.Amounts.TaxInclusiveAmount)
            if self.nota_ajuste.Amounts else total_base + total_tax
        )

        data = {
            "NumDS": self.nota_ajuste.ID,
            "FecDS": self.nota_ajuste.IssueDate,
            "HorDS": self.nota_ajuste.IssueTime,
            "ValDS": f"{total_base:.2f}",
            "CodImp": "01",
            "ValImp": f"{total_tax:.2f}" if total_tax > 0 else "0.00",
            "ValTot": f"{total_iv:.2f}",
            "NitOFE": self.nota_ajuste.Customer.ID,
            "NumAdq": self.nota_ajuste.Company.CompanyID,
            "SoftwarePIN": self.nota_ajuste.Control.Pin,
            "TipoAmbiente": self.nota_ajuste.Control.ProfileExecutionID
        }

        return self.xml.get_cuds(data)

    def _create(self):
        self._set_control(self.nota_ajuste.Control)
        self._set_company()
        self._set_customer()
        self._set_nota_ajuste()
        self._set_discrepancy()
        self._set_billing()
        self._set_amounts()
        self._set_payment()
        self._set_lines()

        # Firmar la nota de ajuste
        self.signer = XmlSignerV3(self.xml.get_root, self.nota_ajuste, 'NAS', self._security)
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
            tipo=TIPO_NOTA_AJUSTE_DS,
            numero=self.nota_ajuste.ID,
            cliente_nit=self.nota_ajuste.Company.CompanyID,
            resolucion=self.nota_ajuste.Control.InvoiceAuthorization,
            identificador=self.cuds,
            ambiente=self.nota_ajuste.Control.ProfileExecutionID,
            zip_path=self.zip_full_path,
        )

        # Enviar la nota de ajuste
        try:
            response = self.soap.send_xml(zip_document)
            is_valid, messages = generic.extract_errors_invoice(response.text)
            recorder.finish(is_valid, messages, response.text)

            if is_valid == 'false':
                print(f"Error al enviar la nota de ajuste. XML enviado: {self.xml_name}")
                print(f"Error al enviar la nota de ajuste. Respuesta XML: {response.text}")
                raise Exception(messages)

        except Exception as e:
            recorder.fail(str(e))
            print(f"Error al enviar la nota de ajuste. XML enviado: {self.xml_name}")
            print(f"Error al enviar la nota de ajuste. Respuesta XML: {e}")
            raise Exception(e)

        return {
            'messages': messages,
            'nota_ajuste': {
                'Cuds': self.cuds
            },
        }

    def _set_company(self):
        self.xml.Company.AdditionalAccountID = self.nota_ajuste.Company.AdditionalAccountID
        self.xml.Company.PartyName = self.nota_ajuste.Company.PartyName
        self.xml.Company.RegistrationName = self.nota_ajuste.Company.PartyName
        self.xml.Company.LegalRegistrationName = self.nota_ajuste.Company.PartyName
        self.xml.Company.CompanyID = self.nota_ajuste.Company.CompanyID
        self.xml.Company.DocumentType = self.nota_ajuste.Company.DocumentType
        self.xml.Company.VerificationDigit = self.nota_ajuste.Company.VerificationDigit
        self.xml.Company.TaxLevelCode = self.nota_ajuste.Company.TaxLevelCode

        addr = self.nota_ajuste.Company.Address
        self.xml.Company.AddressID = addr.AddressID
        self.xml.Company.AddressPostalZone = addr.AddressID
        self.xml.Company.AddressCountrySubentity = addr.CountrySubentity
        self.xml.Company.AddressCountrySubentityCode = addr.CountrySubentityCode
        self.xml.Company.AddressLine = addr.AddressLine

    def _set_customer(self):
        self.xml.Customer.AdditionalAccountID = self.nota_ajuste.Customer.AdditionalAccountID
        self.xml.Customer.PartyName = self.nota_ajuste.Customer.PartyName
        self.xml.Customer.RegistrationName = self.nota_ajuste.Customer.PartyName
        self.xml.Customer.VerificationDigit = self.nota_ajuste.Customer.VerificationDigit
        self.xml.Customer.CompanyID = self.nota_ajuste.Customer.ID
        self.xml.Customer.DocumentType = self.nota_ajuste.Customer.DocumentType
        self.xml.Customer.TaxLevelCode = self.nota_ajuste.Customer.TaxLevelCode

        self.xml.Customer.ContactTelephone = self.nota_ajuste.Customer.Telephone
        self.xml.Customer.ContactElectronicMail = self.nota_ajuste.Customer.Email

        addr = self.nota_ajuste.Customer.Address
        self.xml.Customer.AddressID = addr.AddressID
        self.xml.Customer.AddressPostalZone = addr.AddressID
        self.xml.Customer.AddressCountrySubentity = addr.CountrySubentity
        self.xml.Customer.AddressCountrySubentityCode = addr.CountrySubentityCode
        self.xml.Customer.AddressLine = addr.AddressLine

    def _set_lines(self):
        for line in self.nota_ajuste.Lines:
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
            }
            # add_credit_note_line, NO add_invoice_line: el CreditNote exige
            # cac:CreditNoteLine y la DIAN rechaza con ZB01 si llega InvoiceLine.
            self.xml.add_credit_note_line(line_data)

    def _set_amounts(self):
        self.xml.Amounts.LineExtensionAmount = self.nota_ajuste.Amounts.LineExtensionAmount
        self.xml.Amounts.TaxExclusiveAmount = self.nota_ajuste.Amounts.TaxExclusiveAmount
        self.xml.Amounts.TaxInclusiveAmount = self.nota_ajuste.Amounts.TaxInclusiveAmount
        self.xml.Amounts.PrepaidAmount = self.nota_ajuste.Amounts.PrepaidAmount
        self.xml.Amounts.PayableAmount = self.nota_ajuste.Amounts.PayableAmount
        self.xml.Amounts.TaxTotals = self.nota_ajuste.Amounts.TaxTotals

        if getattr(self.nota_ajuste.Amounts, 'WithholdingTaxTotals', None):
            self.xml.Amounts.WithholdingTaxTotals = self.nota_ajuste.Amounts.WithholdingTaxTotals

    def _set_payment(self):
        self.xml.Payment.PaymentID = self.nota_ajuste.Payment.PaymentID
        self.xml.Payment.PaymentCode = self.nota_ajuste.Payment.PaymentCode

    def _set_nota_ajuste(self):
        self.xml.ID = self.nota_ajuste.ID
        self.xml.IssueDate = self.nota_ajuste.IssueDate
        self.xml.IssueTime = self.nota_ajuste.IssueTime

        self.xml.LineCountNumeric = str(len(self.nota_ajuste.Lines))
        self.xml.UUID = self.cuds

        # Siempre se escribe algo: el setter Note de InvoiceBase retorna sin
        # hacer nada si el valor es None, y entonces quedaría en el XML el
        # contenido de ejemplo del esqueleto.
        self.xml.Note = self.nota_ajuste.Note or self.nota_ajuste.Discrepancy.Description

    def _set_discrepancy(self):
        """Naturaleza de la corrección. ResponseCode 2 = anulación."""
        discrepancy = self.nota_ajuste.Discrepancy

        # ReferenceID es opcional; si no viene se referencia el documento soporte
        # corregido, que es lo más útil para quien lea el XML.
        self.xml.DiscrepancyReferenceID = discrepancy.ReferenceID or self.nota_ajuste.Billing.ID
        self.xml.DiscrepancyResponseCode = discrepancy.ResponseCode
        self.xml.DiscrepancyDescription = discrepancy.Description

    def _set_billing(self):
        """Documento soporte corregido: su número, su CUDS y su fecha."""
        self.xml.BillingID = self.nota_ajuste.Billing.ID
        self.xml.BillingUUID = self.nota_ajuste.Billing.UUID
        self.xml.BillingIssueDate = self.nota_ajuste.Billing.IssueDate

    def _set_control(self, control: ControlNotaAjusteDto):
        self.xml.Control.ProviderID = control.ProviderID
        self.xml.Control.SoftwareID = control.SoftwareID
        self.xml.Control.Pin = control.Pin
        self.xml.Control.TechnicalKey = control.TechnicalKey

        self.xml.Control.SoftwareSecurityCode = (
            f"{control.SoftwareID}{control.Pin}{self.nota_ajuste.ID}"
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
            self.nota_ajuste.Company.VerificationDigit
        )
