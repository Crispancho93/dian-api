from lxml import etree

from shared import templates_loader
from domain.xml_models.documento_soporte.documento_soporte_base import InvoiceBase


class NotaAjusteBase(InvoiceBase):
    """Base de la Nota de Ajuste al Documento Soporte (CreditNote tipo 95).

    Hereda de la base del documento soporte para reutilizar get_cuds(),
    add_invoice_line() y add_tax_total() —el cálculo del CUDS y la estructura de
    líneas y tributos son los mismos—, y solo cambia el esqueleto que carga.
    """

    def __init__(self):
        # No se llama a super().__init__(): esa cargaría el esqueleto del
        # documento soporte (Invoice tipo 05).
        self.root = etree.fromstring(
            templates_loader.template.xml_nota_ajuste_ds.encode('utf-8')
        )

        self.names = {
            'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2',
            # Structures-2-1, el mismo del esqueleto DocumentoSoporte. NO es el
            # de CreditNote.xml (.../contratos/facturaelectronica/v1/Structures):
            # con el namespace equivocado los xpath de sts: no encuentran nada y
            # set_value() falla en silencio.
            'sts': 'dian:gov:co:facturaelectronica:Structures-2-1',
            'cac': 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2',
            'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2',
        }

    def add_credit_note_line(self, line: dict):
        """Línea de la nota de ajuste.

        Misma estructura de Item, Price y TaxTotal que la línea del documento
        soporte (que la DIAN ya acepta), pero con las etiquetas del CreditNote:
        cac:CreditNoteLine y cbc:CreditedQuantity. Usar add_invoice_line() aquí
        produce cac:InvoiceLine y la DIAN rechaza con ZB01 y otras seis reglas
        en cascada, porque no encuentra ninguna línea.

        Sin cac:InvoicePeriod: el anexo lo exige dentro de la línea del
        documento soporte, pero el grupo CreditNoteLine (§8.2, NSAV01-NSAV05)
        no lo contempla.
        """
        cac = '{' + self.names["cac"] + '}'
        cbc = '{' + self.names["cbc"] + '}'

        line_xml = etree.Element(f'{cac}CreditNoteLine')

        etree.SubElement(line_xml, f'{cbc}ID').text = str(line["ID"])
        etree.SubElement(line_xml, f'{cbc}CreditedQuantity', unitCode="EA").text = str(line["Quantity"])
        etree.SubElement(line_xml, f'{cbc}LineExtensionAmount', currencyID="COP").text = str(line["LineExtensionAmount"])

        # Descuento por línea, solo si lo hay
        discount_amount = float(line.get("DiscountAmount", "0.00"))
        if discount_amount > 0:
            allowance_charge = etree.SubElement(line_xml, f'{cac}AllowanceCharge')
            etree.SubElement(allowance_charge, f'{cbc}ID').text = "1"
            etree.SubElement(allowance_charge, f'{cbc}ChargeIndicator').text = "false"
            etree.SubElement(allowance_charge, f'{cbc}AllowanceChargeReason').text = "Descuento por item"
            etree.SubElement(allowance_charge, f'{cbc}MultiplierFactorNumeric').text = str(line.get("DiscountPercent", "0.00"))
            etree.SubElement(allowance_charge, f'{cbc}Amount', currencyID="COP").text = str(line["DiscountAmount"])

            base_amount_val = float(line["PriceAmount"]) * float(line["Quantity"])
            etree.SubElement(allowance_charge, f'{cbc}BaseAmount', currencyID="COP").text = f"{base_amount_val:.2f}"

        # TaxTotal de la línea
        tax_total = etree.SubElement(line_xml, f'{cac}TaxTotal')
        etree.SubElement(tax_total, f'{cbc}TaxAmount', currencyID="COP").text = str(line["TaxAmount"])
        tax_subtotal = etree.SubElement(tax_total, f'{cac}TaxSubtotal')
        etree.SubElement(tax_subtotal, f'{cbc}TaxableAmount', currencyID="COP").text = str(line["TaxableAmount"])
        etree.SubElement(tax_subtotal, f'{cbc}TaxAmount', currencyID="COP").text = str(line["TaxSubtotalAmount"])
        tax_category = etree.SubElement(tax_subtotal, f'{cac}TaxCategory')
        etree.SubElement(tax_category, f'{cbc}Percent').text = str(line["TaxPercent"])
        tax_scheme = etree.SubElement(tax_category, f'{cac}TaxScheme')
        etree.SubElement(tax_scheme, f'{cbc}ID').text = str(line["TaxSchemeID"])
        etree.SubElement(tax_scheme, f'{cbc}Name').text = str(line["TaxSchemeName"])

        # Item
        item = etree.SubElement(line_xml, f'{cac}Item')
        etree.SubElement(item, f'{cbc}Description').text = str(line["Description"])
        sellers_item_identification = etree.SubElement(item, f'{cac}SellersItemIdentification')

        # cbc:ID va SIEMPRE, aunque venga vacío: el esquema UBL lo exige dentro
        # de SellersItemIdentification y omitirlo rompe con ZB01
        # ("The content of element 'cac:SellersItemIdentification' is not
        # complete"). Si el producto no tiene referencia interna, la DIAN
        # devuelve la notificación NSAZ07, que no bloquea: se quita poniéndole
        # referencia al producto en Odoo, no tocando el XML.
        etree.SubElement(sellers_item_identification, f'{cbc}ID').text = str(line["SellersItemID"])

        seller_extended_id = line.get("SellersItemExtendedID")
        if seller_extended_id:
            etree.SubElement(sellers_item_identification, f'{cbc}ExtendedID').text = str(seller_extended_id)

        standard_item_identification = etree.SubElement(item, f'{cac}StandardItemIdentification')
        etree.SubElement(standard_item_identification, f'{cbc}ID', schemeAgencyID="10", schemeID="001", schemeName="UNSPSC").text = "18937100-7"
        additional_item_identification = etree.SubElement(item, f'{cac}AdditionalItemIdentification')
        etree.SubElement(additional_item_identification, f'{cbc}ID', schemeID="999", schemeName="EAN13").text = str(line["AdditionalItemID"])

        # Price
        price = etree.SubElement(line_xml, f'{cac}Price')
        etree.SubElement(price, f'{cbc}PriceAmount', currencyID="COP").text = str(line["PriceAmount"])
        etree.SubElement(price, f'{cbc}BaseQuantity', unitCode="EA").text = str(line["BaseQuantity"])

        self.root.append(line_xml)
