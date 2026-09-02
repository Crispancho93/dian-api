from lxml import etree
from .documento_soporte_base import InvoiceBase


class Amount(InvoiceBase):
    def __init__(self, invoice):
        self.invoice = invoice
        self.names = invoice.names
        self.set_value = invoice.set_value
        
    def _format_amount(self, value):
        """Asegura que cualquier valor numérico se convierta a string con 2 decimales exactos."""
        try:
            return f"{float(value):.2f}"
        except (ValueError, TypeError):
            return str(value)

    # Total Valor Bruto antes de tributos
    @property
    def LineExtensionAmount(self):
        return self._LineExtensionAmount

    @LineExtensionAmount.setter
    def LineExtensionAmount(self, value):
        formatted_value = self._format_amount(value)
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            '//cac:LegalMonetaryTotal/cbc:LineExtensionAmount', 
            formatted_value,
        )
        self._LineExtensionAmount = value

    # Base imponible para el cálculo de los tributos 
    @property
    def TaxExclusiveAmount(self):
        return self._TaxExclusiveAmount

    @TaxExclusiveAmount.setter
    def TaxExclusiveAmount(self, value):
        formatted_value = self._format_amount(value)
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            '//cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount', 
            formatted_value,
        )
        self._TaxExclusiveAmount = value

    # Total de Valor Bruto más tributos
    @property
    def TaxInclusiveAmount(self):
        return self._TaxInclusiveAmount

    @TaxInclusiveAmount.setter
    def TaxInclusiveAmount(self, value):
        formatted_value = self._format_amount(value)
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            '//cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount', 
            formatted_value,
        )
        self._TaxInclusiveAmount = value
    
    # Anticipo Total: Suma de todos los pagos anticipados
    @property
    def PrepaidAmount(self):
        return self._PrepaidAmount

    @PrepaidAmount.setter
    def PrepaidAmount(self, value):
        formatted_value = self._format_amount(value)
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            '//cac:LegalMonetaryTotal/cbc:PrepaidAmount', 
            formatted_value,
        )
        self._PrepaidAmount = value

    # Este valor representa el monto pendiente por pagar.
    @property
    def PayableAmount(self):
        return self._PayableAmount

    @PayableAmount.setter
    def PayableAmount(self, value):
        formatted_value = self._format_amount(value)
        self.set_value(
            {'cac': self.names['cac'], 'cbc': self.names['cbc']}, 
            '//cac:LegalMonetaryTotal/cbc:PayableAmount', 
            formatted_value,
        )
        self._PayableAmount = value

    # @property
    # def TaxTotals(self):
    #    return self._TaxTotals

    # @TaxTotals.setter
    # def TaxTotals(self, value):
    #    self._TaxTotals = value
        # Si tu generador base soporta agregar los nodos de impuestos mediante un método o estructura, 
        # asegúrate de pasarlos aquí para que no queden en blanco en el XML.

    @property
    def TaxTotals(self):
            return self._TaxTotals

    @TaxTotals.setter
    def TaxTotals(self, value):
        self._TaxTotals = value

        if not value:
            return

        for tax in value:
            self.invoice.add_tax_total(
            tax.TaxAmount,
            tax.TaxSubtotal
        )   

    @property
    def WithholdingTaxTotals(self):
            return self._WithholdingTaxTotals


    @WithholdingTaxTotals.setter
    def WithholdingTaxTotals(self, value):

            self._WithholdingTaxTotals = value

        # ============================================================
        # SI NO HAY RETENCIONES
        # NO CREAMOS ABSOLUTAMENTE NADA EN EL XML
        # ============================================================

            if not value:
                return

        # ============================================================
        # OBTENEMOS EL ROOT DEL DOCUMENTO PRINCIPAL
        # ============================================================

            root = self.invoice.root

        # ============================================================
        # NAMESPACES UBL
        # ============================================================

            ns = {
                'cac': self.names['cac'],
                'cbc': self.names['cbc']
            }

        # ============================================================
        # UBICAMOS LegalMonetaryTotal
        #
        # El WithholdingTaxTotal debe quedar antes de este nodo.
        # ============================================================

            legal_monetary_total = root.xpath(
                '//cac:LegalMonetaryTotal',
                namespaces=ns
            )

            if not legal_monetary_total:
                raise ValueError(
                    "No se encontró cac:LegalMonetaryTotal en el XML."
                )

            legal_monetary_total = legal_monetary_total[0]

            # ============================================================
            # POR SEGURIDAD:
            # SI YA EXISTE UN WithholdingTaxTotal, LO ELIMINAMOS
            # ANTES DE CREAR EL NUEVO.
            # ============================================================

            existing = root.xpath(
                '//cac:WithholdingTaxTotal',
                namespaces=ns
            )

            for node in existing:
                parent = node.getparent()
                parent.remove(node)

            # ============================================================
            # CREAMOS EL NODO PRINCIPAL
            # ============================================================

            withholding_total = etree.Element(
                f"{{{self.names['cac']}}}WithholdingTaxTotal"
            )

            # ============================================================
            # RECORREMOS LAS RETENCIONES
            # ============================================================

            for tax in value:

                # --------------------------------------------------------
                # TaxAmount
                # --------------------------------------------------------

                tax_amount = etree.SubElement(
                    withholding_total,
                    f"{{{self.names['cbc']}}}TaxAmount"
                )

                tax_amount.set("currencyID", "COP")
                tax_amount.text = self._format_amount(tax.TaxAmount)

                # --------------------------------------------------------
                # TaxSubtotal
                # --------------------------------------------------------

                for sub in tax.TaxSubtotal:

                    tax_subtotal = etree.SubElement(
                        withholding_total,
                        f"{{{self.names['cac']}}}TaxSubtotal"
                    )

                    # ----------------------------------------------------
                    # TaxableAmount
                    # ----------------------------------------------------

                    taxable_amount = etree.SubElement(
                        tax_subtotal,
                        f"{{{self.names['cbc']}}}TaxableAmount"
                    )

                    taxable_amount.set("currencyID", "COP")
                    taxable_amount.text = self._format_amount(
                        sub.TaxableAmount
                    )

                    # ----------------------------------------------------
                    # TaxAmount
                    # ----------------------------------------------------

                    subtotal_tax_amount = etree.SubElement(
                        tax_subtotal,
                        f"{{{self.names['cbc']}}}TaxAmount"
                    )

                    subtotal_tax_amount.set("currencyID", "COP")
                    subtotal_tax_amount.text = self._format_amount(
                        sub.TaxAmount
                    )

                    # ----------------------------------------------------
                    # TaxCategory
                    # ----------------------------------------------------

                    tax_category = etree.SubElement(
                        tax_subtotal,
                        f"{{{self.names['cac']}}}TaxCategory"
                    )

                    # ----------------------------------------------------
                    # Percent
                    # ----------------------------------------------------

                    percent = etree.SubElement(
                        tax_category,
                        f"{{{self.names['cbc']}}}Percent"
                    )

                    percent.text = self._format_amount(
                        sub.TaxPercent
                    )

                    # ----------------------------------------------------
                    # TaxScheme
                    # ----------------------------------------------------

                    tax_scheme = etree.SubElement(
                        tax_category,
                        f"{{{self.names['cac']}}}TaxScheme"
                    )

                    # ----------------------------------------------------
                    # TaxScheme ID
                    # ----------------------------------------------------

                    scheme_id = etree.SubElement(
                        tax_scheme,
                        f"{{{self.names['cbc']}}}ID"
                    )

                    scheme_id.text = str(sub.TaxSchemeID)

                    # ----------------------------------------------------
                    # TaxScheme Name
                    # ----------------------------------------------------

                    scheme_name = etree.SubElement(
                        tax_scheme,
                        f"{{{self.names['cbc']}}}Name"
                    )

                    scheme_name.text = str(sub.TaxSchemeName)

            # ============================================================
            # INSERTAMOS EL SEGMENTO JUSTO ANTES DE LegalMonetaryTotal
            # ============================================================

            parent = legal_monetary_total.getparent()

            position = parent.index(legal_monetary_total)

            parent.insert(
                position,
                withholding_total
            )


    @property
    def WithholdingTaxTotalsICA(self):
        return self._WithholdingTaxTotalsICA


    @WithholdingTaxTotalsICA.setter
    def WithholdingTaxTotalsICA(self, value):

        self._WithholdingTaxTotalsICA = value

    # ============================================================
    # SI NO HAY RETENCIONES ICA
    # NO CREAMOS NADA EN EL XML
    # ============================================================

        if not value:
            return

        # ============================================================
        # OBTENEMOS EL ROOT DEL DOCUMENTO PRINCIPAL
        # ============================================================

        root = self.invoice.root

        # ============================================================
        # NAMESPACES UBL
        # ============================================================

        ns = {
            'cac': self.names['cac'],
            'cbc': self.names['cbc']
        }

        # ============================================================
        # UBICAMOS LegalMonetaryTotal
        #
        # El WithholdingTaxTotal ICA debe quedar antes de este nodo.
        # ============================================================

        legal_monetary_total = root.xpath(
            '//cac:LegalMonetaryTotal',
            namespaces=ns
        )

        if not legal_monetary_total:
            raise ValueError(
                "No se encontró cac:LegalMonetaryTotal en el XML."
            )

        legal_monetary_total = legal_monetary_total[0]

        # ============================================================
        # CREAMOS EL NODO PRINCIPAL PARA RETEICA
        # ============================================================

        withholding_total_ica = etree.Element(
            f"{{{self.names['cac']}}}WithholdingTaxTotal"
        )

        # ============================================================
        # RECORREMOS LAS RETENCIONES ICA
        # ============================================================

        for tax in value:

            # --------------------------------------------------------
            # TaxAmount
            # --------------------------------------------------------

            tax_amount = etree.SubElement(
                withholding_total_ica,
                f"{{{self.names['cbc']}}}TaxAmount"
            )

            tax_amount.set("currencyID", "COP")
            tax_amount.text = self._format_amount(tax.TaxAmount)

            # --------------------------------------------------------
            # TaxSubtotal
            # --------------------------------------------------------

            for sub in tax.TaxSubtotal:

                tax_subtotal = etree.SubElement(
                    withholding_total_ica,
                    f"{{{self.names['cac']}}}TaxSubtotal"
                )

                # ----------------------------------------------------
                # TaxableAmount
                # ----------------------------------------------------

                taxable_amount = etree.SubElement(
                    tax_subtotal,
                    f"{{{self.names['cbc']}}}TaxableAmount"
                )

                taxable_amount.set("currencyID", "COP")
                taxable_amount.text = self._format_amount(
                    sub.TaxableAmount
                )

                # ----------------------------------------------------
                # TaxAmount
                # ----------------------------------------------------

                subtotal_tax_amount = etree.SubElement(
                    tax_subtotal,
                    f"{{{self.names['cbc']}}}TaxAmount"
                )

                subtotal_tax_amount.set("currencyID", "COP")
                subtotal_tax_amount.text = self._format_amount(
                    sub.TaxAmount
                )

                # ----------------------------------------------------
                # TaxCategory
                # ----------------------------------------------------

                tax_category = etree.SubElement(
                    tax_subtotal,
                    f"{{{self.names['cac']}}}TaxCategory"
                )

                # ----------------------------------------------------
                # Percent
                # ----------------------------------------------------

                percent = etree.SubElement(
                    tax_category,
                    f"{{{self.names['cbc']}}}Percent"
                )

                percent.text = self._format_amount(
                    sub.TaxPercent
                )

                # ----------------------------------------------------
                # TaxScheme
                # ----------------------------------------------------

                tax_scheme = etree.SubElement(
                    tax_category,
                    f"{{{self.names['cac']}}}TaxScheme"
                )

                # ----------------------------------------------------
                # TaxScheme ID
                # ----------------------------------------------------

                scheme_id = etree.SubElement(
                    tax_scheme,
                    f"{{{self.names['cbc']}}}ID"
                )

                scheme_id.text = str(sub.TaxSchemeID)

                # ----------------------------------------------------
                # TaxScheme Name
                # ----------------------------------------------------

                scheme_name = etree.SubElement(
                    tax_scheme,
                    f"{{{self.names['cbc']}}}Name"
                )

                scheme_name.text = str(sub.TaxSchemeName)

        # ============================================================
        # INSERTAMOS EL SEGMENTO ICA JUSTO ANTES DE LegalMonetaryTotal
        # ============================================================

        parent = legal_monetary_total.getparent()

        position = parent.index(legal_monetary_total)

        parent.insert(
            position,
            withholding_total_ica
        )            

    