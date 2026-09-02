from .payroll_base import PayrollBase
from .devengados import Devengados
from .deducciones import Deducciones


class PayrollXml(PayrollBase):
    """
    Modelo XML de NominaIndividual. A diferencia de InvoiceXml/CreditNoteXml
    (que mutan un template poblado por xpath), esta clase construye el
    documento entero dinámicamente a partir de un PayrollDto, agregando
    únicamente lo que viene poblado.
    """

    TIPO_XML = '102'

    # La URL del QR depende del ambiente (anexo, sección 8.2):
    # Ambiente 1 = Producción, Ambiente 2 = Pruebas/Habilitación.
    QR_BASE_PRODUCCION = 'https://catalogo-vpfe.dian.gov.co/document/searchqr?documentkey='
    QR_BASE_HABILITACION = 'https://catalogo-vpfe-hab.dian.gov.co/document/searchqr?documentkey='

    def __init__(self):
        super().__init__()
        self._devengados = Devengados(self)
        self._deducciones = Deducciones(self)

    def build(self, dto, cune: str, software_sc: str):
        self._build_body(self.root, dto, cune, software_sc)
        return self.root

    def _qr_base(self, dto):
        return (
            self.QR_BASE_PRODUCCION
            if dto.InformacionGeneral.Ambiente == '1'
            else self.QR_BASE_HABILITACION
        )

    def _build_body(self, root, dto, cune: str, software_sc: str):
        """
        Construye el cuerpo del documento bajo `root`. Se extrae de build()
        para que la Nota de Ajuste (NominaIndividualDeAjuste) pueda reusarlo
        colgándolo del elemento <Reemplazar> en vez del root.
        """
        # Periodo
        p = dto.Periodo
        self.add(root, 'Periodo', {
            'FechaIngreso': p.FechaIngreso, 'FechaRetiro': p.FechaRetiro,
            'FechaLiquidacionInicio': p.FechaLiquidacionInicio,
            'FechaLiquidacionFin': p.FechaLiquidacionFin,
            'TiempoLaborado': p.TiempoLaborado, 'FechaGen': p.FechaGen,
        })

        # NumeroSecuenciaXML
        n = dto.NumeroSecuenciaXML
        self.add(root, 'NumeroSecuenciaXML', {
            'CodigoTrabajador': n.CodigoTrabajador, 'Prefijo': n.Prefijo,
            'Consecutivo': n.Consecutivo, 'Numero': n.Numero,
        })

        # LugarGeneracionXML
        l = dto.LugarGeneracionXML
        self.add(root, 'LugarGeneracionXML', {
            'Pais': l.Pais, 'DepartamentoEstado': l.DepartamentoEstado,
            'MunicipioCiudad': l.MunicipioCiudad, 'Idioma': l.Idioma,
        })

        # ProveedorXML
        pv = dto.ProveedorXML
        self.add(root, 'ProveedorXML', {
            'RazonSocial': pv.RazonSocial, 'PrimerApellido': pv.PrimerApellido,
            'SegundoApellido': pv.SegundoApellido, 'PrimerNombre': pv.PrimerNombre,
            'OtrosNombres': pv.OtrosNombres, 'NIT': pv.NIT, 'DV': pv.DV,
            'SoftwareID': pv.SoftwareID, 'SoftwareSC': software_sc,
        })

        # CodigoQR (la URL cambia según el ambiente de destino)
        self.add(root, 'CodigoQR', text=f'{self._qr_base(dto)}{cune}')

        # InformacionGeneral
        ig = dto.InformacionGeneral
        self.add(root, 'InformacionGeneral', {
            'Version': ig.Version, 'Ambiente': ig.Ambiente, 'TipoXML': self.TIPO_XML,
            'CUNE': cune, 'EncripCUNE': 'CUNE-SHA384', 'FechaGen': ig.FechaGen,
            'HoraGen': ig.HoraGen, 'PeriodoNomina': ig.PeriodoNomina,
            'TipoMoneda': ig.TipoMoneda, 'TRM': ig.TRM,
        })

        # Notas
        for nota in (dto.Notas or []):
            self.add(root, 'Notas', text=nota)

        # Empleador
        e = dto.Empleador
        self.add(root, 'Empleador', {
            'RazonSocial': e.RazonSocial, 'PrimerApellido': e.PrimerApellido,
            'SegundoApellido': e.SegundoApellido, 'PrimerNombre': e.PrimerNombre,
            'OtrosNombres': e.OtrosNombres, 'NIT': e.NIT, 'DV': e.DV,
            'Pais': e.Pais, 'DepartamentoEstado': e.DepartamentoEstado,
            'MunicipioCiudad': e.MunicipioCiudad, 'Direccion': e.Direccion,
        })

        # Trabajador
        t = dto.Trabajador
        self.add(root, 'Trabajador', {
            'TipoTrabajador': t.TipoTrabajador, 'SubTipoTrabajador': t.SubTipoTrabajador,
            'AltoRiesgoPension': t.AltoRiesgoPension, 'TipoDocumento': t.TipoDocumento,
            'NumeroDocumento': t.NumeroDocumento, 'PrimerApellido': t.PrimerApellido,
            'SegundoApellido': t.SegundoApellido, 'PrimerNombre': t.PrimerNombre,
            'OtrosNombres': t.OtrosNombres, 'LugarTrabajoPais': t.LugarTrabajoPais,
            'LugarTrabajoDepartamentoEstado': t.LugarTrabajoDepartamentoEstado,
            'LugarTrabajoMunicipioCiudad': t.LugarTrabajoMunicipioCiudad,
            'LugarTrabajoDireccion': t.LugarTrabajoDireccion,
            'SalarioIntegral': t.SalarioIntegral, 'TipoContrato': t.TipoContrato,
            'Sueldo': t.Sueldo, 'CodigoTrabajador': t.CodigoTrabajador,
        })

        # Pago
        pg = dto.Pago
        self.add(root, 'Pago', {
            'Forma': pg.Forma, 'Metodo': pg.Metodo, 'Banco': pg.Banco,
            'TipoCuenta': pg.TipoCuenta, 'NumeroCuenta': pg.NumeroCuenta,
        })

        # FechasPagos
        fechas_pagos = self.add(root, 'FechasPagos')
        for fecha in dto.FechasPagos:
            self.add(fechas_pagos, 'FechaPago', text=fecha)

        # Devengados / Deducciones
        self._devengados.build(root, dto.Devengados)
        self._deducciones.build(root, dto.Deducciones)

        # Redondeo (va antes de los totales)
        if dto.Redondeo is not None:
            self.add(root, 'Redondeo', text=dto.Redondeo)

        # Totales
        self.add(root, 'DevengadosTotal', text=dto.DevengadosTotal)
        self.add(root, 'DeduccionesTotal', text=dto.DeduccionesTotal)
        self.add(root, 'ComprobanteTotal', text=dto.ComprobanteTotal)

        return root
