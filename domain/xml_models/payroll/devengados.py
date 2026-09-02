class Devengados:
    """Construye el bloque <Devengados> a partir de un DevengadosDto."""

    def __init__(self, base):
        self.base = base

    def build(self, parent, d):
        dev = self.base.add(parent, 'Devengados')

        self.base.add(dev, 'Basico', {
            'DiasTrabajados': d.Basico.DiasTrabajados,
            'SueldoTrabajado': d.Basico.SueldoTrabajado,
        })

        # Transporte: 0-N elementos hermanos directos (sin wrapper)
        for t in (d.Transporte or []):
            self.base.add(dev, 'Transporte', {
                'AuxilioTransporte': t.AuxilioTransporte,
                'ViaticoManuAlojS': t.ViaticoManuAlojS,
                'ViaticoManuAlojNS': t.ViaticoManuAlojNS,
            })

        hour_attrs = lambda h: {
            'HoraInicio': h.HoraInicio, 'HoraFin': h.HoraFin,
            'Cantidad': h.Cantidad, 'Porcentaje': h.Porcentaje, 'Pago': h.Pago,
        }
        for wrap, item in (
            ('HEDs', 'HED'), ('HENs', 'HEN'), ('HRNs', 'HRN'),
            ('HEDDFs', 'HEDDF'), ('HRDDFs', 'HRDDF'),
            ('HENDFs', 'HENDF'), ('HRNDFs', 'HRNDF'),
        ):
            self.base.add_group(dev, wrap, getattr(d, wrap), item, hour_attrs)

        # Vacaciones: un solo wrapper con dos listas de hijos directos
        v = d.Vacaciones
        if v and (v.VacacionesComunes or v.VacacionesCompensadas):
            vac = self.base.add(dev, 'Vacaciones')
            for c in (v.VacacionesComunes or []):
                self.base.add(vac, 'VacacionesComunes', {
                    'FechaInicio': c.FechaInicio, 'FechaFin': c.FechaFin,
                    'Cantidad': c.Cantidad, 'Pago': c.Pago,
                })
            for c in (v.VacacionesCompensadas or []):
                self.base.add(vac, 'VacacionesCompensadas', {
                    'Cantidad': c.Cantidad, 'Pago': c.Pago,
                })

        if d.Primas is not None:
            self.base.add(dev, 'Primas', {
                'Cantidad': d.Primas.Cantidad, 'Pago': d.Primas.Pago,
                'PagoNS': d.Primas.PagoNS,
            })

        if d.Cesantias is not None:
            self.base.add(dev, 'Cesantias', {
                'Pago': d.Cesantias.Pago, 'Porcentaje': d.Cesantias.Porcentaje,
                'PagoIntereses': d.Cesantias.PagoIntereses,
            })

        self.base.add_group(dev, 'Incapacidades', d.Incapacidades, 'Incapacidad', lambda i: {
            'FechaInicio': i.FechaInicio, 'FechaFin': i.FechaFin,
            'Cantidad': i.Cantidad, 'Tipo': i.Tipo, 'Pago': i.Pago,
        })

        # Licencias: un solo wrapper con tres listas de hijos directos
        lic = d.Licencias
        if lic and (lic.LicenciaMP or lic.LicenciaR or lic.LicenciaNR):
            lic_el = self.base.add(dev, 'Licencias')
            for l in (lic.LicenciaMP or []):
                self.base.add(lic_el, 'LicenciaMP', {
                    'FechaInicio': l.FechaInicio, 'FechaFin': l.FechaFin,
                    'Cantidad': l.Cantidad, 'Pago': l.Pago,
                })
            for l in (lic.LicenciaR or []):
                self.base.add(lic_el, 'LicenciaR', {
                    'FechaInicio': l.FechaInicio, 'FechaFin': l.FechaFin,
                    'Cantidad': l.Cantidad, 'Pago': l.Pago,
                })
            for l in (lic.LicenciaNR or []):
                self.base.add(lic_el, 'LicenciaNR', {
                    'FechaInicio': l.FechaInicio, 'FechaFin': l.FechaFin,
                    'Cantidad': l.Cantidad,
                })

        self.base.add_group(dev, 'Bonificaciones', d.Bonificaciones, 'Bonificacion', lambda b: {
            'BonificacionS': b.BonificacionS, 'BonificacionNS': b.BonificacionNS,
        })

        self.base.add_group(dev, 'Auxilios', d.Auxilios, 'Auxilio', lambda a: {
            'AuxilioS': a.AuxilioS, 'AuxilioNS': a.AuxilioNS,
        })

        self.base.add_group(dev, 'HuelgasLegales', d.HuelgasLegales, 'HuelgaLegal', lambda h: {
            'FechaInicio': h.FechaInicio, 'FechaFin': h.FechaFin, 'Cantidad': h.Cantidad,
        })

        self.base.add_group(dev, 'OtrosConceptos', d.OtrosConceptos, 'OtroConcepto', lambda o: {
            'DescripcionConcepto': o.DescripcionConcepto,
            'ConceptoS': o.ConceptoS, 'ConceptoNS': o.ConceptoNS,
        })

        self.base.add_group(dev, 'Compensaciones', d.Compensaciones, 'Compensacion', lambda c: {
            'CompensacionO': c.CompensacionO, 'CompensacionE': c.CompensacionE,
        })

        self.base.add_group(dev, 'BonoEPCTVs', d.BonoEPCTVs, 'BonoEPCTV', lambda b: {
            'PagoS': b.PagoS, 'PagoNS': b.PagoNS,
            'PagoAlimentacionS': b.PagoAlimentacionS, 'PagoAlimentacionNS': b.PagoAlimentacionNS,
        })

        self.base.add_text_list(dev, 'Comisiones', 'Comision', d.Comisiones)
        self.base.add_text_list(dev, 'PagosTerceros', 'PagoTercero', d.PagosTerceros)
        self.base.add_text_list(dev, 'Anticipos', 'Anticipo', d.Anticipos)

        for tag in ('Dotacion', 'ApoyoSost', 'Teletrabajo', 'BonifRetiro', 'Indemnizacion', 'Reintegro'):
            v = getattr(d, tag, None)
            if v is not None:
                self.base.add(dev, tag, text=v)

        return dev
