from lxml import etree

from shared import templates_loader


class PayrollBase:
    """
    Base del modelo XML de Nómina Electrónica (NominaIndividual).

    A diferencia de Factura/Nota Crédito (UBL, forma fija, mutada por xpath),
    la nómina es mayormente opcional/repetible: se parte de un esqueleto
    (root + namespaces + ext:UBLExtensions vacío) y se construye dinámicamente
    con etree.SubElement, omitiendo cualquier grupo o atributo ausente.
    """

    NS = 'dian:gov:co:facturaelectronica:NominaIndividual'
    # Nombre del campo de XmlTemplatesData con el esqueleto a usar. La Nota de
    # Ajuste sobreescribe NS y TEMPLATE_ATTR para reusar toda esta base.
    TEMPLATE_ATTR = 'xml_payroll'

    def __init__(self):
        template = getattr(templates_loader.template, self.TEMPLATE_ATTR)
        self.root = etree.fromstring(template.encode('utf-8'))

    @property
    def get_root(self):
        return self.root

    def q(self, tag):
        return '{' + self.NS + '}' + tag

    def add(self, parent, tag, attrs=None, text=None):
        """Crea un subelemento omitiendo los atributos None/''."""
        el = etree.SubElement(parent, self.q(tag))
        for k, v in (attrs or {}).items():
            if v is not None and v != '':
                el.set(k, str(v))
        if text is not None:
            el.text = str(text)
        return el

    def add_group(self, parent, tag, items, item_tag, attr_fn):
        """Omite el wrapper por completo si items viene vacío o None."""
        if not items:
            return None
        wrapper = etree.SubElement(parent, self.q(tag))
        for it in items:
            self.add(wrapper, item_tag, attr_fn(it))
        return wrapper

    def add_text_list(self, parent, tag, item_tag, values):
        """Wrapper + N elementos hijos con texto (ej. Comisiones/Comision)."""
        if not values:
            return None
        wrapper = etree.SubElement(parent, self.q(tag))
        for v in values:
            self.add(wrapper, item_tag, text=v)
        return wrapper

    def write_xml(self, output_path):
        xml_file = etree.tostring(
            self.root,
            xml_declaration=True,
            encoding='utf-8',
        ).decode('utf-8')

        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(xml_file)
