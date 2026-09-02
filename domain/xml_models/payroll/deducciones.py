class Deducciones:
    """Construye el bloque <Deducciones> a partir de un DeduccionesDto."""

    def __init__(self, base):
        self.base = base

    def build(self, parent, d):
        ded = self.base.add(parent, 'Deducciones')

        self.base.add(ded, 'Salud', {
            'Porcentaje': d.Salud.Porcentaje, 'Deduccion': d.Salud.Deduccion,
        })
        self.base.add(ded, 'FondoPension', {
            'Porcentaje': d.FondoPension.Porcentaje, 'Deduccion': d.FondoPension.Deduccion,
        })

        if d.FondoSP is not None:
            self.base.add(ded, 'FondoSP', {
                'Porcentaje': d.FondoSP.Porcentaje, 'DeduccionSP': d.FondoSP.DeduccionSP,
                'PorcentajeSub': d.FondoSP.PorcentajeSub, 'DeduccionSub': d.FondoSP.DeduccionSub,
            })

        self.base.add_group(ded, 'Sindicatos', d.Sindicatos, 'Sindicato', lambda s: {
            'Porcentaje': s.Porcentaje, 'Deduccion': s.Deduccion,
        })

        self.base.add_group(ded, 'Sanciones', d.Sanciones, 'Sancion', lambda s: {
            'SancionPublic': s.SancionPublic, 'SancionPriv': s.SancionPriv,
        })

        self.base.add_group(ded, 'Libranzas', d.Libranzas, 'Libranza', lambda l: {
            'Descripcion': l.Descripcion, 'Deduccion': l.Deduccion,
        })

        self.base.add_text_list(ded, 'PagosTerceros', 'PagoTercero', d.PagosTerceros)
        self.base.add_text_list(ded, 'Anticipos', 'Anticipo', d.Anticipos)
        self.base.add_text_list(ded, 'OtrasDeducciones', 'OtraDeduccion', d.OtrasDeducciones)

        for tag in (
            'PensionVoluntaria', 'RetencionFuente', 'AFC', 'Cooperativa',
            'EmbargoFiscal', 'PlanComplementarios', 'Educacion', 'Reintegro', 'Deuda',
        ):
            v = getattr(d, tag, None)
            if v is not None:
                self.base.add(ded, tag, text=v)

        return ded
