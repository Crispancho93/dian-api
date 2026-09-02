from .payroll_xml import PayrollXml


class PayrollAdjustmentXml(PayrollXml):
    """
    Modelo XML de NominaIndividualDeAjuste (Nota de Ajuste, TipoXML 103).

    Reusa todo el builder de PayrollXml: solo cambian el namespace, el
    template esqueleto y la envoltura. El cuerpo de la nómina se cuelga del
    elemento <Reemplazar> en vez de colgarlo directo del root.

    Dos variantes (TipoNota):
      1 = Reemplazar -> cuerpo completo de nómina + <ReemplazandoPredecesor>
      2 = Eliminar   -> conjunto reducido + <EliminandoPredecesor>
    """

    NS = 'dian:gov:co:facturaelectronica:NominaIndividualDeAjuste'
    TEMPLATE_ATTR = 'xml_payroll_adjustment'
    TIPO_XML = '103'

    TIPO_NOTA_REEMPLAZAR = '1'
    TIPO_NOTA_ELIMINAR = '2'

    def build(self, dto, cune: str, software_sc: str):
        root = self.root

        self.add(root, 'TipoNota', text=dto.TipoNota)

        if dto.TipoNota == self.TIPO_NOTA_ELIMINAR:
            eliminar = self.add(root, 'Eliminar')
            self._add_predecesor(eliminar, 'EliminandoPredecesor', dto.Predecesor)
            self._build_eliminar_body(eliminar, dto, cune, software_sc)
        else:
            reemplazar = self.add(root, 'Reemplazar')
            self._add_predecesor(reemplazar, 'ReemplazandoPredecesor', dto.Predecesor)
            # El cuerpo de Reemplazar es idéntico al de NominaIndividual
            self._build_body(reemplazar, dto, cune, software_sc)

        return root

    def _add_predecesor(self, parent, tag, pred):
        self.add(parent, tag, {
            'NumeroPred': pred.NumeroPred,
            'CUNEPred': pred.CUNEPred,
            'FechaGenPred': pred.FechaGenPred,
        })

    def _build_eliminar_body(self, parent, dto, cune: str, software_sc: str):
        """
        La opción Eliminar solo lleva: NumeroSecuenciaXML, LugarGeneracionXML,
        ProveedorXML, CodigoQR, InformacionGeneral (reducido), Notas y
        Empleador. No lleva Trabajador, Pago, FechasPagos, Devengados,
        Deducciones ni totales.
        """
        n = dto.NumeroSecuenciaXML
        self.add(parent, 'NumeroSecuenciaXML', {
            'Prefijo': n.Prefijo, 'Consecutivo': n.Consecutivo, 'Numero': n.Numero,
        })

        l = dto.LugarGeneracionXML
        self.add(parent, 'LugarGeneracionXML', {
            'Pais': l.Pais, 'DepartamentoEstado': l.DepartamentoEstado,
            'MunicipioCiudad': l.MunicipioCiudad, 'Idioma': l.Idioma,
        })

        pv = dto.ProveedorXML
        self.add(parent, 'ProveedorXML', {
            'RazonSocial': pv.RazonSocial, 'PrimerApellido': pv.PrimerApellido,
            'SegundoApellido': pv.SegundoApellido, 'PrimerNombre': pv.PrimerNombre,
            'OtrosNombres': pv.OtrosNombres, 'NIT': pv.NIT, 'DV': pv.DV,
            'SoftwareID': pv.SoftwareID, 'SoftwareSC': software_sc,
        })

        self.add(parent, 'CodigoQR', text=f'{self._qr_base(dto)}{cune}')

        ig = dto.InformacionGeneral
        self.add(parent, 'InformacionGeneral', {
            'Version': ig.Version, 'Ambiente': ig.Ambiente, 'TipoXML': self.TIPO_XML,
            'CUNE': cune, 'EncripCUNE': 'CUNE-SHA384', 'FechaGen': ig.FechaGen,
            'HoraGen': ig.HoraGen,
        })

        for nota in (dto.Notas or []):
            self.add(parent, 'Notas', text=nota)

        e = dto.Empleador
        self.add(parent, 'Empleador', {
            'RazonSocial': e.RazonSocial, 'PrimerApellido': e.PrimerApellido,
            'SegundoApellido': e.SegundoApellido, 'PrimerNombre': e.PrimerNombre,
            'OtrosNombres': e.OtrosNombres, 'NIT': e.NIT, 'DV': e.DV,
            'Pais': e.Pais, 'DepartamentoEstado': e.DepartamentoEstado,
            'MunicipioCiudad': e.MunicipioCiudad, 'Direccion': e.Direccion,
        })
