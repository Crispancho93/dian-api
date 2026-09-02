from domain.xml_models.documento_soporte.documento_soporte_control import Control as DocumentoSoporteControl


class Control(DocumentoSoporteControl):
    """Control de la Nota de Ajuste al Documento Soporte.

    Igual al del documento soporte salvo por la resolución: la nota de ajuste NO
    lleva sts:InvoiceControl (§8.2 del anexo, NSAB03 pasa directo a NSAB13), así
    que StartDate, EndDate, InvoiceAuthorization, Prefix, From y To se guardan en
    memoria pero no se escriben en el XML. Se sobrescriben en vez de heredarse
    para que quede explícito: los setters heredados apuntan a nodos que no
    existen aquí y set_value() no avisa, falla en silencio.

    InvoiceAuthorization sigue haciendo falta en el DTO porque el
    CertificateLoader carga el certificado por número de resolución.
    """

    @property
    def StartDate(self):
        return self._StartDate

    @StartDate.setter
    def StartDate(self, value):
        self._StartDate = value

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, value):
        self._EndDate = value

    @property
    def InvoiceAuthorization(self):
        return self._InvoiceAuthorization

    @InvoiceAuthorization.setter
    def InvoiceAuthorization(self, value):
        self._InvoiceAuthorization = value

    @property
    def Prefix(self):
        return self._Prefix

    @Prefix.setter
    def Prefix(self, value):
        self._Prefix = value

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, value):
        self._From = value

    @property
    def To(self):
        return self._To

    @To.setter
    def To(self, value):
        self._To = value
