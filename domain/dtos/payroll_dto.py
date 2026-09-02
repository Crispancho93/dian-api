from pydantic import BaseModel, model_validator
from typing import List, Optional


class PeriodoDto(BaseModel):
    FechaIngreso: str
    FechaRetiro: Optional[str] = None
    FechaLiquidacionInicio: str
    FechaLiquidacionFin: str
    TiempoLaborado: str
    FechaGen: str


class NumeroSecuenciaXMLDto(BaseModel):
    CodigoTrabajador: Optional[str] = None
    Prefijo: Optional[str] = None
    Consecutivo: str
    Numero: str


class LugarGeneracionXMLDto(BaseModel):
    Pais: str
    DepartamentoEstado: str
    MunicipioCiudad: str
    Idioma: str


class ProveedorXMLDto(BaseModel):
    RazonSocial: Optional[str] = None
    PrimerApellido: Optional[str] = None
    SegundoApellido: Optional[str] = None
    PrimerNombre: Optional[str] = None
    OtrosNombres: Optional[str] = None
    NIT: str
    DV: str
    SoftwareID: str
    SoftwareSC: Optional[str] = None  # calculado por la API, no lo manda el cliente


class InformacionGeneralDto(BaseModel):
    Version: str
    Ambiente: str
    TipoXML: Optional[str] = None  # fijo "102", lo setea la API
    CUNE: Optional[str] = None  # calculado por la API
    EncripCUNE: Optional[str] = None  # calculado por la API
    FechaGen: str
    HoraGen: str
    PeriodoNomina: str
    TipoMoneda: str
    TRM: Optional[str] = None


class EmpleadorDto(BaseModel):
    RazonSocial: Optional[str] = None
    PrimerApellido: Optional[str] = None
    SegundoApellido: Optional[str] = None
    PrimerNombre: Optional[str] = None
    OtrosNombres: Optional[str] = None
    NIT: str
    DV: str
    Pais: str
    DepartamentoEstado: str
    MunicipioCiudad: str
    Direccion: str


class TrabajadorDto(BaseModel):
    TipoTrabajador: str
    SubTipoTrabajador: str
    AltoRiesgoPension: str
    TipoDocumento: str
    NumeroDocumento: str
    PrimerApellido: str
    SegundoApellido: Optional[str] = None
    PrimerNombre: str
    OtrosNombres: Optional[str] = None
    LugarTrabajoPais: str
    LugarTrabajoDepartamentoEstado: str
    LugarTrabajoMunicipioCiudad: str
    LugarTrabajoDireccion: str
    SalarioIntegral: str
    TipoContrato: str
    Sueldo: str
    CodigoTrabajador: Optional[str] = None


class PagoDto(BaseModel):
    Forma: str
    Metodo: str
    Banco: Optional[str] = None
    TipoCuenta: Optional[str] = None
    NumeroCuenta: Optional[str] = None


# ---- Devengados ----

class BasicoDto(BaseModel):
    DiasTrabajados: str
    SueldoTrabajado: str


class TransporteDto(BaseModel):
    AuxilioTransporte: Optional[str] = None
    ViaticoManuAlojS: Optional[str] = None
    ViaticoManuAlojNS: Optional[str] = None


class HoraExtraDto(BaseModel):
    HoraInicio: str
    HoraFin: str
    Cantidad: str
    Porcentaje: str
    Pago: str


class VacacionesComunesDto(BaseModel):
    FechaInicio: str
    FechaFin: str
    Cantidad: str
    Pago: str


class VacacionesCompensadasDto(BaseModel):
    Cantidad: str
    Pago: str


class VacacionesDto(BaseModel):
    VacacionesComunes: Optional[List[VacacionesComunesDto]] = None
    VacacionesCompensadas: Optional[List[VacacionesCompensadasDto]] = None


class PrimasDto(BaseModel):
    Cantidad: Optional[str] = None
    Pago: Optional[str] = None
    PagoNS: Optional[str] = None


class CesantiasDto(BaseModel):
    Pago: Optional[str] = None
    Porcentaje: Optional[str] = None
    PagoIntereses: Optional[str] = None


class IncapacidadDto(BaseModel):
    FechaInicio: str
    FechaFin: str
    Cantidad: str
    Tipo: str
    Pago: str


class LicenciaConPagoDto(BaseModel):
    FechaInicio: str
    FechaFin: str
    Cantidad: str
    Pago: str


class LicenciaNRDto(BaseModel):
    FechaInicio: str
    FechaFin: str
    Cantidad: str


class LicenciasDto(BaseModel):
    LicenciaMP: Optional[List[LicenciaConPagoDto]] = None
    LicenciaR: Optional[List[LicenciaConPagoDto]] = None
    LicenciaNR: Optional[List[LicenciaNRDto]] = None


class BonificacionDto(BaseModel):
    BonificacionS: Optional[str] = None
    BonificacionNS: Optional[str] = None


class AuxilioDto(BaseModel):
    AuxilioS: Optional[str] = None
    AuxilioNS: Optional[str] = None


class HuelgaLegalDto(BaseModel):
    FechaInicio: str
    FechaFin: str
    Cantidad: str


class OtroConceptoDto(BaseModel):
    DescripcionConcepto: str
    ConceptoS: Optional[str] = None
    ConceptoNS: Optional[str] = None


class CompensacionDto(BaseModel):
    CompensacionO: Optional[str] = None
    CompensacionE: Optional[str] = None


class BonoEPCTVDto(BaseModel):
    PagoS: Optional[str] = None
    PagoNS: Optional[str] = None
    PagoAlimentacionS: Optional[str] = None
    PagoAlimentacionNS: Optional[str] = None


class DevengadosDto(BaseModel):
    Basico: BasicoDto
    Transporte: Optional[List[TransporteDto]] = None
    HEDs: Optional[List[HoraExtraDto]] = None
    HENs: Optional[List[HoraExtraDto]] = None
    HRNs: Optional[List[HoraExtraDto]] = None
    HEDDFs: Optional[List[HoraExtraDto]] = None
    HRDDFs: Optional[List[HoraExtraDto]] = None
    HENDFs: Optional[List[HoraExtraDto]] = None
    HRNDFs: Optional[List[HoraExtraDto]] = None
    Vacaciones: Optional[VacacionesDto] = None
    Primas: Optional[PrimasDto] = None
    Cesantias: Optional[CesantiasDto] = None
    Incapacidades: Optional[List[IncapacidadDto]] = None
    Licencias: Optional[LicenciasDto] = None
    Bonificaciones: Optional[List[BonificacionDto]] = None
    Auxilios: Optional[List[AuxilioDto]] = None
    HuelgasLegales: Optional[List[HuelgaLegalDto]] = None
    OtrosConceptos: Optional[List[OtroConceptoDto]] = None
    Compensaciones: Optional[List[CompensacionDto]] = None
    BonoEPCTVs: Optional[List[BonoEPCTVDto]] = None
    Comisiones: Optional[List[str]] = None
    PagosTerceros: Optional[List[str]] = None
    Anticipos: Optional[List[str]] = None
    Dotacion: Optional[str] = None
    ApoyoSost: Optional[str] = None
    Teletrabajo: Optional[str] = None
    BonifRetiro: Optional[str] = None
    Indemnizacion: Optional[str] = None
    Reintegro: Optional[str] = None


# ---- Deducciones ----

class SaludDto(BaseModel):
    Porcentaje: str
    Deduccion: str


class FondoPensionDto(BaseModel):
    Porcentaje: str
    Deduccion: str


class FondoSPDto(BaseModel):
    Porcentaje: Optional[str] = None
    DeduccionSP: Optional[str] = None
    PorcentajeSub: Optional[str] = None
    DeduccionSub: Optional[str] = None


class SindicatoDto(BaseModel):
    Porcentaje: str
    Deduccion: str


class SancionDto(BaseModel):
    SancionPublic: Optional[str] = None
    SancionPriv: Optional[str] = None


class LibranzaDto(BaseModel):
    Descripcion: Optional[str] = None
    Deduccion: str


class DeduccionesDto(BaseModel):
    Salud: SaludDto
    FondoPension: FondoPensionDto
    FondoSP: Optional[FondoSPDto] = None
    Sindicatos: Optional[List[SindicatoDto]] = None
    Sanciones: Optional[List[SancionDto]] = None
    Libranzas: Optional[List[LibranzaDto]] = None
    PagosTerceros: Optional[List[str]] = None
    Anticipos: Optional[List[str]] = None
    OtrasDeducciones: Optional[List[str]] = None
    PensionVoluntaria: Optional[str] = None
    RetencionFuente: Optional[str] = None
    AFC: Optional[str] = None
    Cooperativa: Optional[str] = None
    EmbargoFiscal: Optional[str] = None
    PlanComplementarios: Optional[str] = None
    Educacion: Optional[str] = None
    Reintegro: Optional[str] = None
    Deuda: Optional[str] = None


class PayrollDto(BaseModel):
    Periodo: PeriodoDto
    NumeroSecuenciaXML: NumeroSecuenciaXMLDto
    LugarGeneracionXML: LugarGeneracionXMLDto
    ProveedorXML: ProveedorXMLDto
    InformacionGeneral: InformacionGeneralDto
    Notas: Optional[List[str]] = None
    Empleador: EmpleadorDto
    Trabajador: TrabajadorDto
    Pago: PagoDto
    FechasPagos: List[str]
    Devengados: DevengadosDto
    Deducciones: DeduccionesDto
    Redondeo: Optional[str] = None
    DevengadosTotal: str
    DeduccionesTotal: str
    ComprobanteTotal: str
    Pin: str  # insumo del CUNE y del SoftwareSC; nunca se serializa al XML
    TestID: Optional[str] = None  # TestSetId de habilitación DIAN; solo va en el SOAP, no en el XML

    @property
    def IssueDate(self):
        return self.InformacionGeneral.FechaGen

    @property
    def IssueTime(self):
        return self.InformacionGeneral.HoraGen


# ---- Nota de Ajuste (NominaIndividualDeAjuste, TipoXML 103) ----

class PredecesorDto(BaseModel):
    """Documento de nómina al que se le aplica el ajuste."""
    NumeroPred: str
    CUNEPred: str
    FechaGenPred: str


class PayrollAdjustmentDto(BaseModel):
    """
    Nota de Ajuste de nómina. TipoNota: "1"=Reemplazar, "2"=Eliminar.

    Para Reemplazar se requiere el cuerpo completo de la nómina (igual que
    PayrollDto); para Eliminar solo se usa un subconjunto, por eso esos
    campos van como opcionales y se validan según TipoNota.
    """
    TipoNota: str
    Predecesor: PredecesorDto

    NumeroSecuenciaXML: NumeroSecuenciaXMLDto
    LugarGeneracionXML: LugarGeneracionXMLDto
    ProveedorXML: ProveedorXMLDto
    InformacionGeneral: InformacionGeneralDto
    Notas: Optional[List[str]] = None
    Empleador: EmpleadorDto

    # Solo para Reemplazar
    Periodo: Optional[PeriodoDto] = None
    Trabajador: Optional[TrabajadorDto] = None
    Pago: Optional[PagoDto] = None
    FechasPagos: Optional[List[str]] = None
    Devengados: Optional[DevengadosDto] = None
    Deducciones: Optional[DeduccionesDto] = None
    Redondeo: Optional[str] = None
    DevengadosTotal: Optional[str] = None
    DeduccionesTotal: Optional[str] = None
    ComprobanteTotal: Optional[str] = None

    Pin: str
    TestID: Optional[str] = None

    @model_validator(mode='after')
    def check_campos_por_tipo_nota(self):
        if self.TipoNota not in {'1', '2'}:
            raise ValueError('TipoNota must be "1" (Reemplazar) or "2" (Eliminar)')

        if self.TipoNota == '1':
            requeridos = [
                'Periodo', 'Trabajador', 'Pago', 'FechasPagos', 'Devengados',
                'Deducciones', 'DevengadosTotal', 'DeduccionesTotal', 'ComprobanteTotal',
            ]
            faltantes = [c for c in requeridos if getattr(self, c) is None]
            if faltantes:
                raise ValueError(
                    f'TipoNota "1" (Reemplazar) requiere: {", ".join(faltantes)}'
                )
        return self

    @property
    def IssueDate(self):
        return self.InformacionGeneral.FechaGen

    @property
    def IssueTime(self):
        return self.InformacionGeneral.HoraGen
