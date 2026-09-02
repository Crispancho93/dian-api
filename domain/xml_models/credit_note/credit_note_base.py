import hashlib
from lxml import etree
from typing import List

from domain.dtos.credit_note_dto import TaxSubTotalDto
from shared import templates_loader

class CreditNoteBase:
    def __init__(self):
        self.root = etree.fromstring(templates_loader.template.xml_credit_note.encode('utf-8'))

        self.names = {
            'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2',
            'sts': 'http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures',
            'cac': 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2'
        }

    @property
    def get_root(self):
        return self.root

    def set_value(self, namespaces, xpath, value, index = 0):
        item = self.root.xpath(xpath, namespaces=namespaces)
        if item:
            item[index].text = value

    def set_scheme(self, namespaces, xpath, key, value):
        item = self.root.xpath(xpath, namespaces=namespaces)
        if item:
            item[0].set(key, value)

    def write_xml(self, output_path):
        xml_file = etree.tostring(
            self.root, 
            xml_declaration=True, 
            encoding='utf-8', 
        ).decode('utf-8')

        xml_file = xml_file.replace(
            '<ext:ExtensionContent/>', 
            '<ext:ExtensionContent></ext:ExtensionContent>'
        )

        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(xml_file)

    def get_cude(self, values):
        cufe_string = (
            values["NumFac"] + values["FecFac"] + values["HorFac"] + values["ValFac"] +
            values["CodImp1"] + values["ValImp1"] + values["CodImp2"] + values["ValImp2"] +
            values["CodImp3"] + values["ValImp3"] + values["ValTot"] + values["NitOFE"] +
            values["NumAdq"] + values["ClTec"] + values["TipoAmbiente"]
        )
        cufe_hash = hashlib.sha384(cufe_string.encode('utf-8')).hexdigest()
        return cufe_hash
    
    def add_tax_total(self, tax_amount, lines: List[TaxSubTotalDto]):
        parent = self.root.xpath('//cac:PaymentMeans', namespaces=self.names)
        cac = '{' + self.names["cac"] + '}'
        cbc = '{' + self.names["cbc"] + '}'

        tax_total = etree.Element(f'{cac}TaxTotal')

        tax_amount_elem = etree.SubElement(tax_total, f'{cbc}TaxAmount', currencyID="COP")
        tax_amount_elem.text = str(tax_amount)

        for line in lines:
            tax_subtotal = etree.SubElement(tax_total, f'{cac}TaxSubtotal')
            taxable_amount_elem = etree.SubElement(tax_subtotal, f'{cbc}TaxableAmount', currencyID="COP")
            taxable_amount_elem.text = str(line.TaxableAmount)
            tax_amount_elem = etree.SubElement(tax_subtotal, f'{cbc}TaxAmount', currencyID="COP")
            tax_amount_elem.text = str(line.TaxAmount)

            tax_category = etree.SubElement(tax_subtotal, f'{cac}TaxCategory')
            tax_percent_elem = etree.SubElement(tax_category, f'{cbc}Percent')
            tax_percent_elem.text = str(line.TaxPercent)
            tax_scheme = etree.SubElement(tax_category, f'{cac}TaxScheme')
            tax_id_elem = etree.SubElement(tax_scheme, f'{cbc}ID')
            tax_id_elem.text = line.TaxSchemeID 
            tax_name_elem = etree.SubElement(tax_scheme, f'{cbc}Name')
            tax_name_elem.text = line.TaxSchemeName

            tax_total[0].addnext(tax_subtotal)

        if parent:
            #parent[0].addprevious(tax_total)
            parent[0].addnext(tax_total)
        else:
            self.root.append(tax_total)

    def add_credit_note_line(self, line: dict):
        parent = self.root.xpath('//cac:CreditNote', namespaces=self.names)
        cac = '{' + self.names["cac"] + '}'
        cbc = '{' + self.names["cbc"] + '}'

        parent = self.root.xpath('//ns:CreditNote', namespaces={'ns': 'urn:oasis:names:specification:ubl:schema:xsd:CreditNote-2'})
        line_xml = etree.Element(f'{cac}CreditNoteLine')

        # Add child elements
        etree.SubElement(line_xml, f'{cbc}ID').text = str(line["ID"])
        etree.SubElement(line_xml, f'{cbc}CreditedQuantity', unitCode="EA").text = str(line["Quantity"])
        etree.SubElement(line_xml, f'{cbc}LineExtensionAmount', currencyID="COP").text = str(line["LineExtensionAmount"])
        # etree.SubElement(line_xml, f'{cbc}FreeOfChargeIndicator').text = str(line["FreeOfChargeIndicator"])

        # Add Delivery element
        # delivery = etree.SubElement(line_xml, f'{cac}Delivery')
        # delivery_location = etree.SubElement(delivery, f'{cac}DeliveryLocation')
        # etree.SubElement(delivery_location, f'{cbc}ID', schemeID="999", schemeName="EAN").text = str(line["DeliveryLocationID"])

        # Add AllowanceCharge element, Descuentos
        # allowance_charge = etree.SubElement(line_xml, f'{cac}AllowanceCharge')
        # etree.SubElement(allowance_charge, f'{cbc}ID').text = str(line["AllowanceChargeID"])
        # etree.SubElement(allowance_charge, f'{cbc}ChargeIndicator').text = str(line["ChargeIndicator"])
        # etree.SubElement(allowance_charge, f'{cbc}AllowanceChargeReason').text = str(line["AllowanceChargeReason"])
        # etree.SubElement(allowance_charge, f'{cbc}MultiplierFactorNumeric').text = str(line["MultiplierFactorNumeric"])
        # etree.SubElement(allowance_charge, f'{cbc}Amount', currencyID="COP").text = str(line["AllowanceChargeAmount"])
        # etree.SubElement(allowance_charge, f'{cbc}BaseAmount', currencyID="COP").text = str(line["BaseAmount"]) # Valor del producto antes del descuento x cantidad

        # Add TaxTotal element
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

        # Add Item element
        item = etree.SubElement(line_xml, f'{cac}Item')
        etree.SubElement(item, f'{cbc}Description').text = str(line["Description"])
        sellers_item_identification = etree.SubElement(item, f'{cac}SellersItemIdentification')
        etree.SubElement(sellers_item_identification, f'{cbc}ID').text = str(line["SellersItemID"])
        standard_item_identification = etree.SubElement(item, f'{cac}StandardItemIdentification') 
        etree.SubElement(standard_item_identification, f'{cbc}ID', schemeAgencyID="10", schemeID="001", schemeName="UNSPSC").text = "18937100-7"
        additional_item_identification = etree.SubElement(item, f'{cac}AdditionalItemIdentification')
        etree.SubElement(additional_item_identification, f'{cbc}ID', schemeID="999", schemeName="EAN13").text = str(line["AdditionalItemID"])

        # Add Price element
        price = etree.SubElement(line_xml, f'{cac}Price')
        etree.SubElement(price, f'{cbc}PriceAmount', currencyID="COP").text = str(line["PriceAmount"])
        etree.SubElement(price, f'{cbc}BaseQuantity', unitCode="EA").text = str(line["BaseQuantity"])

        # Append the new InvoiceLine to the parent
        parent[0].append(line_xml)
