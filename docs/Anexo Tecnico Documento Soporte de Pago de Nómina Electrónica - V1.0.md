**Resolución No. 000013** 

(11 FEB 2021) 





Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

Dirección de Impuestos y Aduanas Nacionales 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica 

Versión 1.0 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 1 de 269 

**Resolución No. 000013** 

(11 FEB 2021) 





Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

# Contenido 

|1. Introducción. ............................................................................................................................................. 6|
|---|
|1.1. Calidad de la información: las Validaciones. ....................................................................................... 7|
|1.1.1. Redondeos. ................................................................................................................................... 7|
|1.1.2. Identificador de los documentos electrónicos. ............................................................................ 8|
|1.1.3. Valores Negativos. ........................................................................................................................ 9|
|2. Convenciones utilizadas en las tablas. ...................................................................................................... 9|
|2.1. Columnas de las tablas de definición. ................................................................................................. 9|
|2.2. Tipos de campos de los archivos XML. ..............................................................................................10|
|2.3. Tamaños de los elementos. ...............................................................................................................11|
|2.4. Convenciones utilizadas en las Tablas de Reglas de Validación. .......................................................13|
|3. Formato para la generación de los Documentos Electrónicos. ............................................................... 14|
|3.1. Documento Soporte de Pago de Nómina Electrónica:_NominaIndividual._.......................................14|
|_3.2._Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica:|
|_NominaIndividualDeAjuste._......................................................................................................................50|
|3.3. Estándar del nombre del documento electrónico Documento Soporte de Pago de Nómina<br>Electrónica XML. .......................................................................................................................................96|
|3.4. Estándar del nombre del documento electrónico Nota de Ajuste de Documento Soporte de Pago|
|de Nómina Electrónica XML. ....................................................................................................................96|
|3.5. Guía del nombre del archivo que contiene uno o más documentos electrónicos y que será<br>entregado a la DIAN mediante un web service de recepción. .................................................................97|
|3.6. firma digital del documento:_ds:Signature._.......................................................................................99|
|3.7. Respuesta DIAN con validaciones de documentos Nomina: ApplicationResponse. .......................107|
|3.7.1. Garantía de que el evento será registrado en el documento correcto. ...................................107|
|3.7.2. Relacionamientos mutuos entre los eventos. ..........................................................................108|
|3.7.3. Detalles de cada evento. ..........................................................................................................109|
|4. Inconvenientes tecnológicos. ................................................................................................................ 119|
|4.1. Por parte del Sujeto Obligado. ........................................................................................................119|
|4.2. Por parte de la DIAN. .......................................................................................................................119|
|5. Tablas de Contenidos de Elementos y de Atributos. ............................................................................. 119|
|5.1. Códigos Relacionados con Documentos. ........................................................................................120|
|_5.1.1._Ambiente de Destino del Documento:_Ambiente._...................................................................120|
|_5.1.2._Algoritmo:_EncripCUNE._............................................................................................................120|
|5.2. Códigos para identificación fiscal. ...................................................................................................120|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 2 de 269 

**Resolución No. 000013** 

(11 FEB 2021) 





Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_5.2.1._Documento de identificación (Tipo de Identificador Fiscal):_TipoDocumento._........................120|
|---|



|5.3. Códigos Diversos. ............................................................................................................................121|
|---|
|5.3.1. Lenguaje (ISO 639):_Idioma._.....................................................................................................121|
|5.3.2. Moneda (ISO 4217):_TipoMoneda._...........................................................................................124|
|5.3.3. Pagos. .......................................................................................................................................130|
|5.4. Códigos Geográficos. .......................................................................................................................131|
|5.4.1. Países (ISO 3166-1):_Pais._.........................................................................................................131|
|5.4.2. Departamentos (ISO 3166-2:CO):_Departamento._...................................................................143|
|5.4.3. Municipios:_Municipio._.............................................................................................................144|
|5.5. Campos Nómina. .............................................................................................................................178|
|5.5.1. Periodo de Nómina: PeriodoNomina. ......................................................................................178|
|5.5.2. Tipo de Contrato: TipoContrato. ..............................................................................................179|
|5.5.3. Tipo de Trabajador: TipoTrabajador.........................................................................................179|
|5.5.4. Subtipo de Trabajador: SubTipoTrabajador. ............................................................................179|
|5.5.5. Tipo de Hora Extra o Recargo: Porcentaje. ..............................................................................180|
|5.5.6. Tipo de Incapacidad: Tipo.........................................................................................................180|
|5.5.7. Tipo de XML: TipoXML. .............................................................................................................180|
|5.5.8. Tipo de Nota de Ajuste: TipoNota. ...........................................................................................180|
|6. Reglas y Mensajes de Validación. .......................................................................................................... 182|
|6.1. Documentos Electrónicos. ...............................................................................................................182|
|6.1.1. Documento Soporte de Pago de Nómina Electrónica: NominaIndividual. ..............................182|
|6.1.2. Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica:<br>NominaIndividualDeAjuste. ..............................................................................................198|
|_6.1.3._Firma Digital del Documento:_ds:Signature_. ............................................................................221|
|6.2. Reglas Relativas al Establecimiento de la Conexión. .......................................................................231|
|6.2.1. Mensaje del Web Service. ........................................................................................................231|
|6.2.2. Schema XML. ............................................................................................................................231|
|6.2.3. Certificado Digital de Transmisión (conexión). ........................................................................231|
|6.2.4. Certificado Digital de Firma (Firma XML). ................................................................................232|
|6.2.5. Firma. ........................................................................................................................................232|
|Abreviaturas Utilizadas. ............................................................................................................................. 232|
|7. Política de firma. .................................................................................................................................... 234|
|7.1. Observaciones. ................................................................................................................................234|
|7.2. Consideraciones Generales. ............................................................................................................234|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 3 de 269 

**Resolución No. 000013** 





### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|7.3. Especificaciones técnicas sobre la firma digital Avanzada. .............................................................234|
|---|
|7.4. Alcance de la Política de Firma. .......................................................................................................235|
|7.5. Política de Firma. .............................................................................................................................235|
|7.5.1. Actores de la Firma. ..................................................................................................................235|
|7.5.2. Formato de Firma. ....................................................................................................................235|
|7.6. Algoritmo de Firma. .........................................................................................................................236|
|7.7. Algoritmo de Organización de Datos según el Canon. ....................................................................236|
|7.8. Ubicación de la Firma. .....................................................................................................................236|
|7.9. Condiciones de la Firma. .................................................................................................................236|
|7.10. Identificador de la Política. ............................................................................................................238|
|7.11. Hora de Firma. ...............................................................................................................................239|
|7.12. Firmante. .......................................................................................................................................239|
|7.13. Mecanismo de firma digital. ..........................................................................................................239|
|7.14. Certificado digital desde la vigencia de la circular 03-2016 de la ONAC. ......................................239|
|8. Mecanismos de Control del Documento Soporte de Pago de Nómina Electrónica y Nota de Ajuste del|
|Documento Soporte de Pago de Nómina Electrónica. .............................................................................. 245|
|8.1. Especificación Técnica de Generación Del CUNE. ...........................................................................245|
|8.1.1. Consideraciones Generales del CUNE. .....................................................................................245|
|8.2. Especificacón Técnica Del Código De Seguridad Del Software. ......................................................248|
|8.3. Métodos de Calculo. ........................................................................................................................249|
|8.3.1. Cálculo de Tiempo Laborado ....................................................................................................249|
|9. Descripciónes Tecnológicas del Web Services de Método Síncrono. ................................................... 249|
|9.1. Modelo conceptual de comunicación. ............................................................................................250|
|9.2. Servicio síncrono. ............................................................................................................................250|
|9.2.1. Secuencia del servicio síncrono. ...............................................................................................250|
|9.3. Aspectos tecnológicos de las operaciones del web service. ...........................................................251|
|9.4. Estándar de comunicación. .............................................................................................................251|
|9.5. Estándar de mensajes de los servicios de La DIAN..........................................................................252|
|9.6. Descripción de los servicios web de La DIAN. .................................................................................252|
|9.7. WS recepción documento electrónico – SendNominaSync. ...........................................................252|
|9.7.1. Descripción de procesamiento. ................................................................................................252|
|9.7.2. Mensaje de petición. ................................................................................................................253|
|9.8. WS Consulta del estado de DE – GetStatus. ....................................................................................254|
|9.8.1. Descrición de procesamiento. ..................................................................................................254|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 4 de 269 

**Resolución No. 000013** 





### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|9.8.2. Mensaje de petición. ................................................................................................................255|
|---|
|10. Campos definidos en las extensiones. ................................................................................................. 257|
|10.1. Estructura para reporte de información adicional específica de cada sector. .............................257|
|11. Elemento Novedad. ............................................................................................................................. 257|
|12. Preguntas Frecuentes. ......................................................................................................................... 258|
|13. Servicio de Consulta. ........................................................................................................................... 258|
|13.1. Servicio de consulta a través de Código Bidimensional QR. .........................................................258|
|14. Anexo: Herramienta para el consumo de Web Services. .................................................................... 261|
|14.1. Introducción ..................................................................................................................................261|
|14.2. Descargar SOAP UI. .......................................................................................................................261|
|14.3. Ejecutar SOAP UI. ..........................................................................................................................261|
|14.4. Crear un nuevo proyecto tipo SOAP..............................................................................................261|
|14.5. Configuración inicial. .....................................................................................................................262|
|14.6. Configurar Keystore. ......................................................................................................................262|
|14.7. Configurar WS-Security Signature. ................................................................................................263|
|14.8. Configurar TimeStamp. .................................................................................................................264|
|14.9. Configurar GetStatus Request, Authentication y WS-A addressing. .............................................264|
|14.10. Configurar y ejecutar GetStatus Request. ...................................................................................266|
|14.11. Configurar y ejecutar SendBillAsync Request. ............................................................................267|
|14.12. SendBillAsync Response. .............................................................................................................268|
|14.13. Recomendaciones. ......................................................................................................................269|
|15. Control de cambios. ............................................................................................................................ 269|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 5 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

### 1. Introducción. 

El presente anexo técnico describe el Documento Soporte de Pago de Nómina Electrónica y la Nota de Ajuste del Documento Soporte de Pago de Nómina Electrónica, para que sean documentos soporte de costos y deducciones en el impuesto sobre la renta y complementarios, de conformidad con lo dispuesto en el parágrafo 6 del artículo 616-1. 

El formato No pertenece al Estandar _Universal Business Language_ – UBL. 

La generación del Documento Soporte de Pago de la Nómina Electrónica y la Nota de Ajuste del Documento Soporte de Pago de Nómina Electrónica poseen las siguientes características: 

- Documento Soporte de Pago de Nómina Electrónica (NominaIndividual): Debe existir al menos 1 documento de este tipo por cada empleado que tenga la empresa por mes, el cual corresponde al Comprobante de Nómina de dicho trabajador. 

- Nota de Ajuste del Documento Soporte de Pago de Nómina Electrónica (NominaIndividualDeAjuste): Debe existir 1 documento de este tipo por cada Documento Soporte de Pago de Nómina Electrónica de cada empleado que tenga la empresa el cual se deba ajustar o reemplazar por errores aritméticos contables o de contenido y que el sujeto obligado deberá ajustar o corregir. Este documento electrónico podrá hacerse tantas veces como correcciones se requieran realizar sobre un mismo Documento Soporte de Pago de Nómina Electrónica, siendo la úlima nota de ajuste del documento soporte de pago de nómina electrónica validada, la que sirva como soporte. 

Este documento también permite eliminar un Documento Soporte de Pago de Nómina Electrónica o una Nota de Ajuste del Documento Soporte de Pago de Nómina Electrónica que el sujeto obligado deba eliminar por errores contables o de procedimiento. 

El objetivo de la presente descripción es buscar, una estandarización del Documento Soporte de Pago de Nómina Electrónica y Nota de Ajuste del Documento Soporte de Pago de Nómina Electrónica, permitiendo que la información pueda ser utilizada de la manera más eficaz, eficiente y efectiva posible. 

De igual forma se deberá tener en cuenta lo referente al tratamiento de datos personales relacionado con la seguridad de la información que contienen los documentos que por medio de este anexo se implementan, de conformidad con lo previsto en los artículos 17 y 18 de la Ley 1581 de 2012 y la Circular 000001 del 25 de enero de 2019 de la Unidad Administrativa Especial Dirección de Impuestos y Aduanas Nacionales -DIAN, las cuales señalan los aspectos relacionados con el tratamiento de datos personales y la seguridad de la información, los cuales se desarrollan en el TÍTULO IX de la presente resolución. 

> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Página 6 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

Se imponen por lo tanto dos (2) requisitos: confiabilidad y calidad en las informaciones tal como se describe a continuación. 

### 1.1. Calidad de la información: las Validaciones. 

En el presente anexo técnico se aclara las limitaciones que se pueden presentar al brindar información en un determinado elemento, tanto de manera lógica, como de manera aritmética. 

La aplicación de las reglas de validación puede terminar en uno (1) de los siguientes tres (3) resultados: 

- Rechazo, si la aplicación de la regla apunta a una discrepancia grave, que indica que las informaciones del archivo no pueden ser utilizadas de manera confiable o de manera legal; 

- Notificación, si la aplicación de la regla apunta a una discrepancia menos importante, pero que asimismo merece que se advierta al emisor de un posible problema con las informaciones del archivo; 

- Aprobación, si la aplicación de la regla no apunta a ningún tipo de problema. 

Las reglas de validación serán aplicadas en los siguientes momentos: 

- Por la DIAN al recibir, del Sujeto Obligado directamente a través de Modalidad Software Propio o a través de un tercero. 

### 1.1.1. Redondeos. 

Las reglas de validación que contengan operaciones aritméticas relacionadas con valores monetarios deberán cumplir con los siguientes parámetros para su aproximación, dependiendo de la cantidad de decimales definidos para el campo respectivo en las reglas de validación que apliquen: 

|_Dígito siguiente al dígito menos significativo es_|_Redondeo_|
|---|---|
|Entre 0 y 4.|Mantener el dígito menos significativo.|
|Entre 6 y 9.|Incrementar el dígito menos significativo.|
|5, y el segundo dígito siguiente al dígito menos significativo es cero o par.|Mantener el dígito menos significativo.|
|5, y el segundo dígito siguiente al dígito menos significativo es impar.|Incrementar el dígito menos significativo.|



Esta definición se hace para que se reduzca el riesgo de problemas de suma de los valores redondeados, para valores originales con décimas conteniendo el número “5”. 

En caso que con la adopción de este procedimiento haya diferencia entre los totales calculados y la suma de los parciales para el valor total de un documento, se deberá utilizar el elemento 

> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Página 7 de 269 

**Resolución No. 000013** 





### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

_/NominaIndividual/Redondeo y /NominaIndividualDeAjuste/Reempolazar/Redondeo_ para informar la diferencia. 

#### 1.1.1.1. <u>Redondeos valores monetarios.</u> 

Redondeos para los elementos, que contienen valores monetarios. 

Nota: Los valores monetarios permitirán una tolerancia de error + - 2.00. 

Nota: La fórmula de redondeo utilizada en estos momentos es la round-half-to-even cuya definición se puede encontrar en la siguiente dirección https://www.w3.org/TR/xpath-functions-31/#funcround-half-to-even, y, corresponde a la norma técnica colombiana NTC 3711 (Norma técnica internacional JIS Z 8401). 

### 1.1.2. Identificador de los documentos electrónicos. 

El Código Único de Documento Soporte de Pago de Nómina Electrónica – CUNE utilizado para los Documentos Soporte de Pago de Nómina Electrónica, es el identificador de los diferentes documentos electrónicos. Para su cálculo debe remitirse al numeral 8.1 del presente documento. 

Para posibilitar la referencia cruzada entre los diferentes documentos electrónicos, se incluye la etiqueta _/Generales/@CUNE_ , la cual contendrá un identificador universal denominado “CUNE” y su Tipo de encriptado denominado “EncripCUNE”. Este identificador y el Tipo de Encriptado están localizados en la siguiente ruta de ambos documentos: 

Documento Soporte de Pago de Nómina Electrónica: 

- /NominaIndividual/InformacionGeneral/@CUNE 

- /NominaIndividual/InformacionGeneral/@EncripCUNE 

Nota de Ajuste del Documento Soporte de Pago de Nómina Electrónica: 

- /NominaIndividualDeAjuste/Reemplazar/InformacionGeneral/@CUNE 

- /NominaIndividualDeAjuste/Eliminar/InformacionGeneral/@CUNE 

- /NominaIndividualDeAjuste/Reemplazar/InformacionGeneral/@EncripCUNE 

- /NominaIndividualDeAjuste/Eliminar/InformacionGeneral/@EncripCUNE 

La etiqueta CUNE contendrá: 

 Como se mencionó anteriormente, el lector debe remitirse al <u>numeral 8.1, con el objeto de revisar</u> cómo se calcula o genera el CUNE para los diferentes documentos electrónicos. 

Los elementos utilizados en los cálculos se encuentran especificados en el presente documento. 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 8 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

### 1.1.3. Valores Negativos. 

#### 1.1.3.1. <u>Monetarios.</u> 

Todos los valores monetarios deberán ser expresados en valores positivos. La naturaleza del signo negativo o positivo la otorga el concepto de campo, mas no está incluido en el valor. Se informa la generación de la regla VLR01. 

#### 1.1.3.2. <u>Tarifas.</u> 

Las tarifas tributarias deben corresponder a valores iguales o superiores a 0.00, en este caso no se permiten valores negativos. 

### 2. Convenciones utilizadas en las tablas. 

Este capítulo presenta la definición de las estructuras de las tablas de definición del formato XML tanto de los Documentos Electrónicos, como de las reglas de validación. 

### 2.1. Columnas de las tablas de definición. 

Las columnas de las Tablas de Definición siguen las descripciones que se encuentran en la Tabla 1. 

_Tabla 1 – Convenciones Utilizadas en la Tablas de Definición de los Formatos XML._ 

|_Columna_|_Descripción_|
|---|---|
|ID|Identificador único del elemento atributo y que servirá de base para la codificación de notificaciones o errores de cada<br>uno de ellos.|
|NS|Identifica el NameSpace al cual pertenece el campo:<br><br>xmlns="dian:gov:co:facturaelectronica:NominaIndividual"<br><br>xmlns="dian:gov:co:facturaelectronica:NominaIndividualDeAjuste"<br><br>xmlns:xs="http://www.w3.org/2001/XMLSchema-instance"<br><br>ds - http://www.w3.org/2000/09/xmldsig#<br><br>ext - urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2<br><br>xades -http://uri.etsi.org/01903/v1.3.2#<br><br>xmlns - xades141="http://uri.etsi.org/01903/v1.4.1#"<br><br>xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"<br><br>SchemaLocation=""<br><br>xsi:schemaLocation="dian:gov:co:facturaelectronica:NominaIndividual NominaIndividualElectronicaXSD.xsd"<br><br>xsi:schemaLocation="dian:gov:co:facturaelectronica:NominaIndividualDeAjuste<br>NominaIndividualDeAjusteElectronicaXSD.xsd"|
|Campo|Nombre del elemento o grupo de elementos:<br><br>Los atributos de elementos inician con el símbolo “@”.|
|Descripción|Descripción del elemento o grupo y su significado.|
|T|Tipo de elemento (verTabla 2).|
|F|Tipo de dato (verTabla 3).|
|Tam|Tamaño del elemento (verTabla 4).|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

www.dian.gov.co 

Página 9 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_Columna_|_Descripción_|
|---|---|
|Padre|Nombre del grupo que contiene este elemento o grupo.|
|Ocu|Identifica la cantidad de posibles ocurrencias del elemento o grupo. Ejemplo:<br>1-1 – Identifica que el elemento o grupo es obligatorio, con máximo de una ocurrencia.<br>0-1 – Identifica que el elemento o grupo es facultativo (posible de no ser informado), con máximo de una ocurrencia.<br>1-N – Identifica que el elemento o grupo es obligatorio, con máximo de N ocurrencias.<br>0-N – Identifica que el elemento o grupo es facultativo (posible de no ser informado), con máximo de N ocurrencias.|
|Observaciones|Observaciones importantes sobre el campo, incluyendo listas de valores posibles, validaciones relevantes entre otras.|
|V|Versión que el campo fue introducido en el formato, o versión en que ha sido modificado por la última vez.|



Nota: La definición de los namespace utilizados en los Documentos Electrónicos deben ser mencionados a nivel de la cabecera de los documentos NominaIndividual o NominaIndividualDeAjuste. 

### 2.2. Tipos de campos de los archivos XML. 

Los tipos de campos de los archivos XML tienen su contenido descrito en la Tabla 2 y en la Tabla 3. 

_Tabla 2 – Tipos de Campo en los Archivos XML._ 

|_Tipo_|_Descripción_|
|---|---|
|G|Grupo de elementos.|
|E|Elemento.|
|A|Atributo de un elemento.|



_Tabla 3 – Tipos de Datos de los Elementos en los Archivos XML._ 

|_Tipo_|_Descripción_|
|---|---|
|A|Alfanumérico: son aceptados los caracteres UNICODE permitidos en el XML.|
|B|Booleano: acepta solamente los literales “true” y “false” (se debe usar minúsculas).|
|N|Numérico: solamente son aceptados los números “0” a “9”, el punto de separación decimal, y las señales “+” y “-“.|
|F|Fecha: elementos que deben ser informados en el formato AAAA-MM-DD, de acuerdo con la norma ISO 8601-2, en el<br>cual:<br><br>AAAA: año.<br><br>MM: mes.<br><br>DD: día.|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 10 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_Tipo_|_Descripción_|
|---|---|
|H|Hora: elementos que deben ser informados en el formato de tiempo universal coordinado HH:MM:SSdhh:mm, de<br>acuerdo con la norma ISO 8601-2, en el cual:<br><br>HH: hora UTC (número de horas contadas desde la media noche, o sea, de 00 hasta 23).<br><br>MM: minutos.<br><br>SS: segundos.<br><br>hh:mm – diferencia en horas y minutos con relación a la hora GMT.<br><br>d: señal (“+” o “-“) para la diferencia con relación a la hora GMT<sup>1</sup>.<br>Ejemplo: dos y treinta de la tarde en Bogotá debe ser informado como 14:30:00-05:00.|
|I|Intervalo de tiempo: elementos que deben ser informados en el formato <Fecha Inicial>/<Fecha Final>, siendo que<br>obedece el formato “F” para ambas las fechas.<br>Ejemplo: el período entre 01 de septiembre y 30 de septiembre de 2020 debe ser informado como 2020-09-01/2020-<br>09-30.|
|X|Documento XML.|



### 2.3. Tamaños de los elementos. 

Existen elementos con tamaño fijo, y elementos con tamaño variable. Los elementos de tamaño fijo no admiten información con otro número de posición diferente a la que se establece, es decir, la información en este tipo de configuración siempre tiene exactamente el mismo tamaño. 

Los elementos de tamaño variable admiten un rango de número de posiciones que varía de un mínimo hasta un máximo. En caso que la información no utilice el número máximo de posiciones, no se deben <u>incluir caracteres para rellenar el espacio, tales como ceros o blancos.</u> 

Los elementos de tamaño variable que tienen el valor cero (0) como tamaño mínimo admiten que sean informados sin contenido, en este caso, el emisor declara que no existe o no se encuentra disponible la información correspondiente. 

_Tabla 4 – Tamaños de Elementos._ 

|_Formato_|_Descripción_|
|---|---|
|X|Tamaño exacto del elemento.|



> 1 Atención: no es la hora “Zulu”, o sea, referenciada al meridiano zero. Debe ser informada una hora en una zona horaria específica, de libre elección del emisor: en el ejemplo fue escogido -5, que es la zona horaria oficial de Colombia. 

- La zona horaria elegida por el emisor del documento electrónico es indiferente para la aplicación de las reglas de validación: todas las operaciones de evaluación de horas se realizan tomando en cuenta la zona horaria informada en el campo específico. 

- No existe necesidad de utilizar la misma zona horaria en todos los campos del tipo “hora” a lo largo de un mismo archivo. 

Dirección de Gestión de Ingresos 

> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Página 11 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

||<br>ej.: 5.<br> Informar menos o más de cincoposiciones tendrá como resultado el rechazo del archivo.|
|---|---|
|x-y|Tamaño mínimo de “x”, máximo de “y”.<br><br>ej.: 0-10.<br> Es posible expresar ningún valor, porque se permite el tamaño “0”.<br> Informar más de diez posiciones tendrá como resultado el rechazo del archivo.|
|x p n|Tamaño exacto del elemento de “x”, con exactamente “n” casillas decimales.<br><br>ej.: 11 p 4.<br> El número debe tener once posiciones, siendo exactamente seis posiciones antes del punto<br>decimal, y exactamente cuatro (4) posiciones después del punto decimal; cualquier otro número<br>deposiciones tendrá como resultado el rechazo del archivo.|
|x p (n-m)|Tamaño exacto del elemento de “x”, con entre “n” y “m” casillas decimales.<br><br>ej.: 11 p (0-6).<br> El número debe tener exactamente once posiciones, aceptándose cualquier combinación desde<br>once posiciones sin punto decimal hasta exactamente cuatro (4) posiciones antes del punto<br>decimal, yexactamente seis(6) posiciones después delpunto decimal.|
|(x-y) p (n-m)|Tamaño mínimo de “x”, máximo de “y”, con entre “n” y “m” casillas decimales.<br><br>ej.: 1-11 p (0-6).<br> Es obligatorio expresar algún valor, porque no se permite el tamaño “0”.<br> El número debe entre una (1) y once posiciones, aceptándose cualquier combinación desde once<br>posiciones sin punto decimal hasta exactamente cuatro (4) posiciones antes del punto decimal, y<br>exactamente seis(6) posiciones después delpunto decimal, pero laparte fraccionaria es opcional.|
|Valores separados<br>por comas|El elemento deberá ser informado con tamaño de exactamente una de las opciones listadas.<br><br>ej.: 1, 3, 5, 8 significa que se debe informar el elemento con uno de estos cuatro tamaños fijos.|



Ejemplos de cómo se deben informar los valores en los elementos numéricos de acuerdo con el formato especificado pueden ser encontrados en la Tabla 5 . 

_Tabla 5 – Ejemplos de Información de Valores Utilizando los Formatos Numéricos._ 

|_Formato_<br>_Para Informar:_|_Llenar elemento con:_|
|---|---|
|1,105.13|1105.13|
|1,105.137|1105.137|
|0-11 p (0-6)<br>1,105|1105|
|0|0|
|para no informar cantidad|dejar el elemento vacío|
|1,105|1105|
|1-11<br>0|0|
|para no informar cantidad|no es posible|



> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Página 12 de 269 

**Resolución No. 000013** 





### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

### 2.4. Convenciones utilizadas en las Tablas de Reglas de Validación. 

Las columnas de las Tablas de Reglas de Validación siguen las descripciones que se encuentran en la Tabla 6. 

_Tabla 6 – Nombres de las Columnas de las Tablas de Reglas de Validación._ 

|_Columna_|_Descripción_|
|---|---|
|Tipo|Categoría de la regla de validación.|
|#|Identificador de la regla de validación.|
|Campo|Nombre del campo en las tablas de formato.|
|Regla|Descripción de la regla de validación.|
|Cod|Código de mensaje correspondiente a la regla de validación.|
|Y|Efecto de la regla de validación:<br><br>R: Rechazo, el procesamiento correspondiente ha encontrado problemas que impiden el procesamiento de la<br>solicitud.<br><br>N: Notificación, el procesamiento correspondiente ha encontrado indicios de potenciales problemas, los<br>cuales no impiden el procesamiento de la solicitud.|
|Mensaje|Mensaje regresado como resultado de un rechazo el de una notificación.|
|V|Versión de las reglas de validación.|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 13 de 269 

**Resolución No. 000013** 





### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

### 3. Formato para la generación de los Documentos Electrónicos. 

El sistema de Documento Soporte de Pago de Nómina Electrónica de Colombia utiliza dos (2) documentos XML: NominaIndividual y NominaIndividualDeAjuste. 

### 3.1. Documento Soporte de Pago de Nómina Electrónica: _NominaIndividual._ 

|_ID_|_ns_|<br>_Campo_|_Descripción_|_T_<br>_F_<br>|_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|---|
|||NominaIndividual|Documento Soporte de Pago de Nómina<br>Electrónica - NominaIndividual (raíz)||||1-1||1.0<br>/NominaIndividual|
|NIE001|Ext|UBLExtensions|Grupo correspondiente a la Firma Digital<br>del Documento (Signature)|G A||NominaIndividual|1-1|Solamente puede haber una ocurrencia de<br>un grupo UBLExtensions conteniendo el<br>grupo ds:Signature. Ver definición en<br>numeral 3.6|1.0<sup>/NominaIndividual/ext:UB</sup><br>LExtensions|
|NIE199||Novedad|Indica si existe alguna Novedad<br>Contractual en el Documento Soporte de<br>Pago de Nómina Electrónica o Nota de<br>Ajuste de Documento Soporte de Pago de<br>Nómina Electrónica del Trabajador en<br>dicho Mes.|<br>E<br>B||NominaIndividual|0-1|Se debe colocar "true" o "false".|1.0<br>/NominaIndividual/Noved<br>ad|
|NIE204||CUNENov|Debe corresponder al CUNE del<br>Documento Soporte de Pago de Nómina<br>Electrónica o Nota de Ajuste de<br>Documento Soporte de Pago de Nómina<br>Electrónica a realizar la Novedad|A A 9|6|Novedad|1-1|<sup>Debe ir el CUNE del documento al cual se le</sup><br>realizará la novedad contractual|1.0<sup>/NominaIndividual/Noved</sup><br>ad/@CUNENov|
|||Periodo|Utilizado para Atributos del Periodo<br>Generación del Documento|E<br>A||NominaIndividual|1-1|Elemento Vacio|1.0<br>/NominaIndividual/Period<br>o|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

> www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 14 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_|<br>_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|NIE002|FechaIngreso|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador o aprendiz presenta ingreso o<br>vinculación a la nómina del reportante.<br>(en caso de tener mas de un ingreso en el<br>mes, se debe reportar la primera fecha en<br>la que se presenta esta novedad en el<br>mes que se esta reportando).|<br> <br>A F|10|Periodo|1-1|Se debe indicar la Fecha de Ingreso del<br>trabajador a la empresa, en formato AAAA-<br>MM-DD|1.0<sup>/NominaIndividual/Period</sup><br>o/@FechaIngreso|
|NIE003|FechaRetiro|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador o aprendiz presenta retiro de<br>la nómina del reportante.(en caso de<br>tener mas de un retiro en el mes, se debe<br>reportar la ultima fecha en la que se<br>presenta esta novedad en el mes que se<br>esta reportando).|<br>A F|10|Periodo|0-1|Se debe indicar la Fecha de Retiro del<br>trabajador a la empresa, en formato AAAA-<br>MM-DD|1.0<sup>/NominaIndividual/Period</sup><br>o/@FechaRetiro|
|NIE004|FechaLiquidacionIni<br>cio|Fecha de inicio de Liquidación de Nómina|A F|10|Periodo|1-1|Se debe indicar la Fecha de Inicio del<br>Periodo de liquidación del documento, en<br>formato AAAA-MM-DD|1.0<br>/NominaIndividual/Period<br>o/@FechaLiquidacionInici<br>o|
|NIE005|FechaLiquidacionFin|Fecha fin de Liquidación de Nómina|A F|10|Periodo|1-1|Se debe indicar la Fecha de Fin del Periodo<br>de liquidación del documento, en formato<br>AAAA-MM-DD|1.0<sup>/NominaIndividual/Period</sup><br>o/@FechaLiquidacionFin|
|NIE006|TiempoLaborado|Cantidad de Tiempo que lleva laborando<br>el Trabajador en la empresa|A A||Periodo|1-1|<sup>Definido en elnumeral 8.4.1, debe ser</sup><br>mayor o gual a 1.|1.0<sup>/NominaIndividual/Period</sup><br>o/@TiempoLaborado|
|NIE008|FechaGen|Fecha de emisión: Fecha de emisión del<br>documento|A F|10|Periodo|1-1|Debe ir la fecha de emision del documento.<br>Considerando zona horaria de Colombia (-<br>5), en formato AAAA-MM-DD|<br>1.0<sup>/NominaIndividual/Period</sup><br>o/@FechaGen|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 15 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_|_Tam_<br>_Padre_<br>_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|
||NumeroSecuenciaX<br>ML|Utilizado para Atributos de Numero de<br>Secuencia del Documento XML|E<br>A|NominaIndividual<br>1-1|Elemento Vacio|1.0<br>/NominaIndividual/Numer<br>oSecuenciaXML|
|NIE009|CodigoTrabajador|Codigo del Trabajador|A A|<br>NumeroSecuencia<br>XML<br>0-1|<sup>Campo Opcional queda a manejo Interno</sup><br>del Empleador.|1.0<br>/NominaIndividual/Numer<br>oSecuenciaXML/@Codigo<br>Trabajador|
|NIE010|Prefijo|Prefijo del documento, depende de las<br>sucursales que posea el Empleador|A A|<br>NumeroSecuencia<br>XML<br>0-1|<sup>Debe corresponder a un Prefijo elegido por</sup><br>el Emisor del documento|1.0<sup>/NominaIndividual/Numer</sup><br>oSecuenciaXML/@Prefijo|
|NIE011|Consecutivo|Debe corresponder a un consecutivo<br>manejado por el Empleador|A N|<br>NumeroSecuencia<br>XML<br>1-1|<sup>Debe corresponder a un Consecutivo</sup><br>elegido por el Emisor del documento|1.0<br>/NominaIndividual/Numer<br>oSecuenciaXML/@Consec<br>utivo|
|NIE012|Numero|Debe corresponder al Prefijo y<br>consecutivo manejado por el Empleador|A A|<br>NumeroSecuencia<br>XML<br>1-1|No se permiten caracteres adicionales como<br>espacios o guiones. Prefijo + Número<br>consecutivo del documento|<br>1.0<br>/NominaIndividual/Numer<br>oSecuenciaXML/@Numer<br>o|
||LugarGeneracionXM<br>L|Utilizado para Atributos del Lugar de<br>Generacion del Documento XML|E<br>A|NominaIndividual<br>1-1|Elemento Vacio|1.0<br>/NominaIndividual/LugarG<br>eneracionXML|
|NIE013|Pais|Codigo del país donde se genera el<br>documento|A A|2<br>LugarGeneracionX<br>ML<br>1-1|<sup>Se debe colocar el Codigo alfa-2 de latabla</sup><br>5.4.1|1.0<sup>/NominaIndividual/LugarG</sup><br>eneracionXML/@Pais|
|NIE014|DepartamentoEstad<br>o|Código del departamento donde se<br>genera el documento|A N|2<br>LugarGeneracionX<br>ML<br>1-1|Se debe colocar el Codigo de latabla 5.4.2|1.0<br>/NominaIndividual/LugarG<br>eneracionXML/@Departa<br>mentoEstado|
|NIE015|MunicipioCiudad|Código del municipio o ciudad donde se<br>genera el documento|A N|5<br>LugarGeneracionX<br>ML<br>1-1|Se debe colocar el Codigo de latabla 5.4.3|1.0<br>/NominaIndividual/LugarG<br>eneracionXML/@Municipi<br>oCiudad|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 16 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_|_F_|<br>_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|---|
|NIE016|Idioma|Codigo del país donde se genera el<br>documento|A|A|2|LugarGeneracionX<br>ML|1-1|Se debe colocar el Codigo ISO 639-1 de la<br>tabla 5.3.1.Para Colombia se debe colocar<br>"es" (Español, Castellano)|1.0<sup>/NominaIndividual/LugarG</sup><br>eneracionXML/@Idioma|
||ProveedorXML|Utilizado para Atributos del Proveedor del<br>Documento XML|<br>E<br>|A||NominaIndividual|1-1|Elemento Vacio|1.0<br>/NominaIndividual/Provee<br>dorXML|
|NIE205|RazonSocial|Debe corresponder al Nombre de la<br>Razón Social del Proveedor de Soluciones<br>Tecnológicas|A|A||ProveedorXML|0-1|<sup>Debe ir el Nombre o Razón Social del</sup><br>Proveedor de Soluciones Tecnológicas|1.0<sup>/NominaIndividual/Provee</sup><br>dorXML/@RazonSocial|
|NIE206|PrimerApellido|Primer Apellido del Proveedor de<br>Soluciones Tecnológicas|A|A|60|ProveedorXML|0-1|<sup>Debe ir el Primer Apellido del Proveedor de</sup><br>Soluciones Tecnológicas|1.0<sup>/NominaIndividual/Provee</sup><br>dorXML/@PrimerApellido|
|NIE207|SegundoApellido|Segundo Apellido del Proveedor de<br>Soluciones Tecnológicas|A|A|60|ProveedorXML|0-1|<sup>Debe ir el Segundo Apellido del Proveedor</sup><br>de Soluciones Tecnológicas|1.0<br>/NominaIndividual/Provee<br>dorXML/@SegundoApellid<br>o|
|NIE208|PrimerNombre|Primer Nombre del Proveedor de<br>Soluciones Tecnológicas|A|A|60|ProveedorXML|0-1|<sup>Debe ir el Primer Nombre del Proveedor de</sup><br>Soluciones Tecnológicas|1.0<sup>/NominaIndividual/Provee</sup><br>dorXML/@PrimerNombre|
|NIE209|OtrosNombres|Otros Nombres del Proveedor de<br>Soluciones Tecnológicas|A|A|60|ProveedorXML|0-1|<sup>Deben ir los Otros Nombres del Proveedor</sup><br>de Soluciones Tecnológicas|1.0<sup>/NominaIndividual/Provee</sup><br>dorXML/@OtrosNombres|
|NIE017|NIT|Debe corresponder al NIT que realiza el<br>DE|A|N||ProveedorXML|1-1|Se debe colocar el NIT sin guiones ni DV de<br>la empresa dueña del Software que genera<br>el Documento, debe estar registrado en la<br>DIAN|1.0<sup>/NominaIndividual/Provee</sup><br>dorXML/@NIT|
|NIE018|DV|Debe corresponder al DV del NIT del o<br>que realiza el DE|A|N|2|ProveedorXML|1-1|Se debe colocar el DV de la empresa dueña<br>del Software que genera el Documento,<br>debe estar registrado en la DIAN|1.0<sup>/NominaIndividual/Provee</sup><br>dorXML/@DV|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 17 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_<br>|_Tam_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIE019|SoftwareID|Identificador Software: Identificador del<br>software habilitado para la emisión de<br>nóminas|A A|ProveedorXML|1-1|Identificador del software asignado cuando<br>el software se activa en el Sistema del<br>Documento Soporte de Pago de Nómina<br>Electrónica, debe corresponder a un<br>software autorizado para este Emisor|1.0<sup>/NominaIndividual/Provee</sup><br>dorXML/@SoftwareID|
|NIE020|SoftwareSC|Huella del software que autorizó la DIAN<br>al Obligado a Generar Nómina Electrónica<br>o al Proveedor de soluciones Tecnológicas|<br> <br>A A|ProveedorXML|1-1|Definido en elnumeral 8.3|1.0<sup>/NominaIndividual/Provee</sup><br>dorXML/@SoftwareSC|
|NIE021|CodigoQR|Debe poseer información detallada del<br>Documento Electronico|E<br>A|NominaIndividual|1-1|Debe corresponder a la siguiente URL<br>“https://catalogo-<br>vpfe.dian.gov.co/document/searchqr?docu<br>mentkey=CUNE”  donde la palabra CUNE<br>debe ser reemplazada por el CUNE del<br>documento electrónico|1.0<sup>/NominaIndividual/Codigo</sup><br>QR|
||InformacionGeneral|Utilizado para Atributos de Información<br>General Documento|E<br>A|NominaIndividual|1-1|Elemento Vacio|1.0<br>/NominaIndividual/Inform<br>acionGeneral|
|NIE022|Version|Versión base de Schema XML usada para<br>crear este perfil (NominaIndividual)|A A|InformacionGener<br>al|1-1|<sup>Debe ir el literal: "V1.0: Documento Soporte</sup><br>de Pago de Nómina Electrónica"|1.0<sup>/NominaIndividual/Inform</sup><br>acionGeneral/@Version|
|NIE023|Ambiente|Tipo de Ambiente de Emision del<br>Documento: Habilitacion o Produccion|A N 1|<br>InformacionGener<br>al|1-1|Se debe colocar el Codigo de latabla 5.1.1|1.0<sup>/NominaIndividual/Inform</sup><br>acionGeneral/@Ambiente|
|NIE202|TipoXML|Tipo de XML del Documento|A N 2|<br>InformacionGener<br>al|1-1|Se debe colocar el Codigo de latabla 5.5.7|1.0<sup>/NominaIndividual/Inform</sup><br>acionGeneral/@TipoXML|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 18 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_<br>|_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|NIE024|CUNE|CUNE:  Código Único de Documento<br>Soporte de Pago de Nómina Electrónica.<br>Elemento que verifica la integridad de la<br>información recibida|A A||InformacionGener<br>al|1-1|Definido en elnumeral 8.1|1.0<sup>/NominaIndividual/Inform</sup><br>acionGeneral/@CUNE|
|NIE025|EncripCUNE|Identificador del esquema de<br>identificación. Algoritmo utilizado para el<br>cáculo del CUNE, SHA-384|A A 1|1|InformacionGener<br>al|1-1|Debe ir la palabra "CUNE-SHA384"|1.0<br>/NominaIndividual/Inform<br>acionGeneral/@EncripCU<br>NE|
|NIE026|FechaGen|Fecha de emisión: Fecha de emisión del<br>documento|A F<br>1|0|InformacionGener<br>al|1-1|Debe ir la fecha de emision del documento.<br>Considerando zona horaria de Colombia (-<br>5), en formato AAAA-MM-DD|<br>1.0<sup>/NominaIndividual/Inform</sup><br>acionGeneral/@FechaGen|
|NIE027|HoraGen|Hora de emisión: hora de emisión del<br>documento|A H 1|4|InformacionGener<br>al|1-1|Debe ir la hora de emision del documento.<br>Considerando zona horaria de Colombia (-<br>5), en formato HH:MM:SSdhh:mm|1.0<sup>/NominaIndividual/Inform</sup><br>acionGeneral/@HoraGen|
|NIE029|PeriodoNomina|Corresponde al Codigo de Periodo de<br>Nómina|A N 1||InformacionGener<br>al|1-1|Se debe colocar el Codigo de latabla 5.5.1|1.0<br>/NominaIndividual/Inform<br>acionGeneral/@PeriodoN<br>omina|
|NIE030|TipoMoneda|Tipo de Moneda utilizada en el<br>documento|A A 3||InformacionGener<br>al|1-1|<sup>Se debe colocar el Codigo de latabla 5.3.2.</sup><br>Para Colombia se debe colocar "COP"|1.0<br>/NominaIndividual/Inform<br>acionGeneral/@TipoMon<br>eda|
|NIE200|TRM|Tasa Representativa del mercado.<br>Corresponde a la tasa de cambio de la<br>moneda utilizada en el documento en el<br>Campo “TipoMoneda” a Pesos<br>Colombianos.|A N||InformacionGener<br>al|0-1|Se debe colocar la tasa de cambio de la<br>moneda utilizada en el documento en el<br>Campo “TipoMoneda” a Pesos<br>Colombianos.|1.0<sup>/NominaIndividual/Inform</sup><br>acionGeneral/@TRM|
|NIE031|Notas|Campo de libre uso para Observaciones<br>en el documento|E<br>A||NominaIndividual|0-N|Información adicional: Texto libre, relativo<br>al documento, Ejemplo: Información de<br>Novedades de los trabajadores.|1.0 /NominaIndividual/Notas|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 19 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_|_F_|<br>_Tam_|<br>_Padre_|_Oc_|<br>_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|---|
||Empleador|Utilizado para Atributos del Empleador o<br>Emisor del Documento|E<br>|A||NominaIndividua|l<br>1-1|Elemento Vacio|1.0<br>/NominaIndividual/Emple<br>ador|
|NIE032|RazonSocial|Debe corresponder al Nombre de la<br>Razón Social del Empleador|A|A||Empleador|0-1|<sup>Debe ir el Nombre o Razón Social del</sup><br>Empleador|1.0<sup>/NominaIndividual/Emple</sup><br>ador/@RazonSocial|
|NIE210|PrimerApellido|Primer Apellido del Empleador|A|A|60|Empleador|0-1|Debe ir el Primer Apellido del Empleador|1.0<sup>/NominaIndividual/Emple</sup><br>ador/@PrimerApellido|
|NIE211|SegundoApellido|Segundo Apellido del Empleador|A|A|60|Empleador|0-1|Debe ir el Segundo Apellido del Empleador|1.0<sup>/NominaIndividual/Emple</sup><br>ador/@SegundoApellido|
|NIE212|PrimerNombre|Primer Nombre del Empleador|A|A|60|Empleador|0-1|Debe ir el Primer Nombre del Empleador|1.0<sup>/NominaIndividual/Emple</sup><br>ador/@PrimerNombre|
|NIE213|OtrosNombres|Otros Nombres del Empleador|A|A|60|Empleador|0-1|Deben ir los Otros Nombres del Empleador|1.0<sup>/NominaIndividual/Emple</sup><br>ador/@OtrosNombres|
|NIE033|NIT|Debe corresponder al NIT del Empleador<br>que realiza el DE|A|N||Empleador|1-1|<sup>Debe ir el NIT del Empleador sin guiones ni</sup><br>DV|1.0<sup>/NominaIndividual/Emple</sup><br>ador/@NIT|
|NIE034|DV|Debe corresponder al DV del NIT del<br>Empleador que realiza el DE|A|N|2|Empleador|1-1|Debe ir el DV del Empleador|1.0<sup>/NominaIndividual/Emple</sup><br>ador/@DV|
|NIE035|Pais|Codigo del país donde se encuentra<br>ubicada la empresa del empleador en el<br>mes que se esta reportando|A|A|2|Empleador|1-1|<sup>Se debe colocar el Codigo alfa-2 de latabla</sup><br>5.4.1|1.0<sup>/NominaIndividual/Emple</sup><br>ador/@Pais|
|NIE036|DepartamentoEstad<br>o|Código del departamento donde se<br>encuentra ubicada la empresa del<br>empleador en el mes que se esta<br>reportando|A|N|2|Empleador|1-1|Se debe colocar el Codigo de latabla 5.4.2|1.0<br>/NominaIndividual/Emple<br>ador/@DepartamentoEsta<br>do|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 20 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_|<br>_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|NIE037|MunicipioCiudad|Código del municipio o ciudad donde se<br>encuentra ubicada la empresa del<br>empleador en el mes que se esta<br>reportando|A N|5|Empleador|1-1|Se debe colocar el Codigo de latabla 5.4.3|1.0<sup>/NominaIndividual/Emple</sup><br>ador/@MunicipioCiudad|
|NIE038|Direccion|Debe corresponder a la dirección del<br>lugar físico de expedición del documento.|<sup>A A</sup>||Empleador|1-1|Debe ir la Dirección Fisica del Empleador|1.0<sup>/NominaIndividual/Emple</sup><br>ador/@Direccion|
||Trabajador|Utilizado para Atributos del Trabajador o<br>Receptor del Documento|E<br>A||NominaIndividual|1-1|Elemento Vacio|1.0<br>/NominaIndividual/Trabaj<br>ador|
|NIE041|TipoTrabajador|Código del tipo de trabajador del<br>Ministerio de salud. Aportes a Seguridad<br>Social de Activos.|A N|2|Trabajador|1-1|Corresponde a la clasificación de PILA para<br>conocer en que calidad se realizan las<br>cotizaciones a la seguridad social. Se debe<br>colocar el Codigo de latabla 5.5.3|1.0<sup>/NominaIndividual/Trabaj</sup><br>ador/@TipoTrabajador|
|NIE042|SubTipoTrabajador|Código del Sub tipo de trabajador del<br>Ministerio de salud. Aportes a Seguridad<br>Social de Activos|A N|2|Trabajador|1-1|Corresponde a una sub clasificación de PILA<br>para conocer en que calidad se realizan las<br>cotizaciones a la seguridad social. Se debe<br>colocar el Codigo de latabla 5.5.4|1.0<br>/NominaIndividual/Trabaj<br>ador/@SubTipoTrabajado<br>r|
|NIE043|AltoRiesgoPension|Si el trabajador desarrollo durante el<br>presente periodo alguna de las<br>actividades descritas en el Decreto 2090<br>de 2003, o la norma que lo modifique,<br>adicione o sustituya.|A B|4-5|Trabajador|1-1|Se debe colocar "true" o "false"|1.0<sup>/NominaIndividual/Trabaj</sup><br>ador/@AltoRiesgoPension|
|NIE044|TipoDocumento|Tipo de documento de identificación que<br>actualmente tiene el trabajador,<br>aprendiz, o pasante|A N|2|Trabajador|1-1|Se debe colocar el Codigo de latabla 5.2.1|1.0<sup>/NominaIndividual/Trabaj</sup><br>ador/@TipoDocumento|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 21 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_|_F_|<br>_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|---|
|NIE045|NumeroDocumento|<sup>Numero de identificación que</sup><br>actualmente el trabajador o aprendiz|A|N||Trabajador|1-1|<sup>Debe ir el Numero de documento del</sup><br>trabajador, sin puntos ni comas ni espacios|<sup>1.0</sup><br>/NominaIndividual/Trabaj<br>ador/@NumeroDocument<br>o|
|NIE046|PrimerApellido|Primer Apellido del trabajador o aprendiz|A|A|60|Trabajador|1-1|Debe ir el Primer Apellido del trabajador|1.0<sup>/NominaIndividual/Trabaj</sup><br>ador/@PrimerApellido|
|NIE047|SegundoApellido|Segundo Apellido del trabajador o<br>aprendiz|A|A|60|Trabajador|1-1|Debe ir el Segundo Apellido del trabajador|1.0<sup>/NominaIndividual/Trabaj</sup><br>ador/@SegundoApellido|
|NIE048|PrimerNombre|Primer Nombre del trabajador o aprendiz|A|A|60|Trabajador|1-1|Debe ir el Primer Nombre del trabajador|1.0<sup>/NominaIndividual/Trabaj</sup><br>ador/@PrimerNombre|
|NIE049|OtrosNombres|Otros Nombres del trabajador o aprendiz|A|A|60|Trabajador|0-1|Deben ir los Otros Nombres del trabajador|1.0<sup>/NominaIndividual/Trabaj</sup><br>ador/@OtrosNombres|
|NIE050|LugarTrabajoPais|Código del país actual donde se<br>encontraba ubicado el trabajador o<br>aprendiz en el mes reportado.|A|N|3|Trabajador|1-1|<sup>Se debe colocar el Codigo alfa-2 de latabla</sup><br>5.4.1|1.0<sup>/NominaIndividual/Trabaj</sup><br>ador/@LugarTrabajoPais|
|NIE051|LugarTrabajoDepart<br>amentoEstado|Código del departamento actual donde se<br>encontraba ubicado el trabajador o<br>aprendiz en el mes reportado.|<br>A|N|2|Trabajador|1-1|Se debe colocar el Codigo de latabla 5.4.2|1.0<br>/NominaIndividual/Trabaj<br>ador/@LugarTrabajoDepa<br>rtamentoEstado|
|NIE052|LugarTrabajoMunici<br>pioCiudad|Código del municipio o ciudad actual<br>donde se encontraba ubicado el<br>trabajador o aprendiz en el mes<br>reportado.|A|N|5|Trabajador|1-1|Se debe colocar el Codigo de latabla 5.4.3|1.0<br>/NominaIndividual/Trabaj<br>ador/@LugarTrabajoMuni<br>cipioCiudad|
|NIE053|LugarTrabajoDirecci<br>on|Debe corresponder a la dirección del<br>lugar físico donde vive el empleado.|A|A||Trabajador|1-1|Debe ir la Dirección Fisica del Trabajador|1.0<br>/NominaIndividual/Trabaj<br>ador/@LugarTrabajoDirec<br>cion|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 22 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_<br>|_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|NIE056|SalarioIntegral|Si el trabajador tiene un salario integral, el<br>cual es el tipo de remuneración que<br>incluye todos los conceptos que puedan<br>constituir salario en un solo monto o pago<br>(prestaciones sociales y recargos<br>nocturno, dominical y festivo, y el trabajo<br>extra) y que sea superior a 10 SMLMV<br>mas un 30% correspondiente a factor<br>prestacional.|<br> <br>A B 4|-5|Trabajador|1-1|Se debe colocar "true" o "false"|1.0<sup>/NominaIndividual/Trabaj</sup><br>ador/@SalarioIntegral|
|NIE061|TipoContrato|Tipo de Contrato que posee el empleado<br>con el Empleador|A N 1||Trabajador|1-1|Se debe colocar el Codigo de latabla 5.5.2|1.0<sup>/NominaIndividual/Trabaj</sup><br>ador/@TipoContrato|
|NIE062|Sueldo|Corresponde al valor que el empleador<br>paga de forma periódica al trabajador<br>como contraprestación por el trabajo<br>realizado, este puede ser fijo o variable de<br>acuerdo a la unidad de tiempo en que las<br>partes hayan acordado el pago, teniendo<br>como base el día o la hora trabajada.|<br>A N||Trabajador|1-1|<sup>Se debe colocar el Sueldo Base que el</sup><br>Trabajador tiene en la empresa|1.0<sup>/NominaIndividual/Trabaj</sup><br>ador/@Sueldo|
|NIE063|CodigoTrabajador|Codigo del Trabajador|A A||Trabajador|0-1|<sup>Campo Opcional queda a manejo Interno</sup><br>del Empleador.|1.0<sup>/NominaIndividual/Trabaj</sup><br>ador/@CodigoTrabajador|
||Pago|Utilizado para Atributos del Pago del<br>Documento|E<br>A||NominaIndividua|l<br>1-1|Elemento Vacio|1.0<br>/NominaIndividual/Pago|
|NIE064|Forma|Formas de Pago del Documento|A N 1||Pago|1-1|Se debe colocar el Codigo de latabla 5.3.3.1|<br>1.0<sup>/NominaIndividual/Pago/</sup><br>@Forma|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

> www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 23 de 269 





### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_|_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|NIE065|Metodo|Metodos de Pago del Documento|A N|2|Pago|1-1|Se debe colocar el Codigo de latabla 5.3.3.2|1.0<sup>/NominaIndividual/Pago/</sup><br>@Metodo|
|NIE066|Banco|Nombre de Entidad Bancaria del<br>Empleado donde se realiza la<br>consignación|A A||Pago|0-1|Si el método de pago se realiza de forma<br>bancaria. Se debe colocar el nombre de la<br>entidad bancaria donde el trabajador tiene<br>su cuenta para pago de nómina.|1.0<sup>/NominaIndividual/Pago/</sup><br>@Banco|
|NIE067|TipoCuenta|Tipo de Cuenta Bancaria del Empleado<br>donde se realiza la consignación|A A||Pago|0-1|Si el método de pago se realiza de forma<br>bancaria. Se debe colocar el tipo de cuenta<br>que el trabajador tiene para pago de<br>nómina.|1.0<sup>/NominaIndividual/Pago/</sup><br>@TipoCuenta|
|NIE068|NumeroCuenta|Numero de Cuenta Bancaria del<br>Empleado donde se realiza la<br>consignación|A A||Pago|0-1|Si el método de pago se realiza de forma<br>bancaria. Se debe colocar el número de la<br>cuenta que el trabajador tiene para pago de<br>nómina..|1.0<sup>/NominaIndividual/Pago/</sup><br>@NumeroCuenta|
||FechasPagos|Utilizado para Todos los Elementos de<br>Fechas de Pagos del Documento|G<br>A||NominaIndividual|1-1||1.0<br>/NominaIndividual/Fechas<br>Pagos|
|NIE203|FechaPago|Fecha de Pago de la Nómina|E<br>F|10|FechasPagos|1-N|Debe ir la fecha de pago del documento.<br>Considerando zona horaria de Colombia (-<br>5), en formato AAAA-MM-DD|1.0<sup>/NominaIndividual/Fechas</sup><br>Pagos/FechaPago|
||Devengados|Utilizado para Todos los Devengos del<br>Documento|G<br>A||NominaIndividual|1-1|Hace referencia al concepto de valor<br>devengado de nómina señalado en el<br>numeral 18, articulo 1 de la presente<br>resolución.|1.0<br>/NominaIndividual/Deven<br>gados|
||Basico|Utilizado para Atributos Basicos de<br>Devengos del Documento|E<br>A||Devengados|1-1|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/Basico|



> Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 24 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_<br>|_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|NIE069|DiasTrabajados|Número de días que el trabajador o<br>aprendiz efectivamente estuvo<br>ejecutando sus labores en la empresa.|A N 1|-2|Basico|1-1|<sup>Cantidad de dias laborados durante el</sup><br>Periodo de Pago|1.0<br>/NominaIndividual/Deven<br>gados/Basico/@DiasTraba<br>jados|
|NIE070|SueldoTrabajado|Corresponde al valor que el empleador<br>paga de forma periódica al trabajador<br>como contraprestación por el trabajo<br>realizado, este puede ser fijo o variable de<br>acuerdo a la unidad de tiempo en que las<br>partes hayan acordado el pago, teniendo<br>como base el día o la hora trabajada.|<br>A N||Basico|1-1|Valor Base o Sueldo del trabajador según lo<br>estipulado en su contrato. Corresponde al<br>Sueldo Trabajado por los días laborados.|1.0<br>/NominaIndividual/Deven<br>gados/Basico/@SueldoTra<br>bajado|
||Transporte|Utilizado para Atributos de Transporte de<br>Devengos del Documento|E<br>A||Devengados|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/Transporte|
|NIE071|AuxilioTransporte|Parte de los viáticos pagado al trabajador<br>correspondientes a medios de transporte<br>y/o los gastos de representación.|A N||Transporte|0-1|<sup>Valor de Auxilio de Transporte que recibe el</sup><br>trabajador por ley, según aplique|1.0<br>/NominaIndividual/Deven<br>gados/Transporte/@Auxili<br>oTransporte|
|NIE072|ViaticoManuAlojS|Parte de los viáticos pagado al trabajador<br>correspondientes a manutención y/o<br>alojamiento.|A N||Transporte|0-1|<sup>Valor de Viaticos, Manutención y</sup><br>Alojamiento de carácter Salarial|1.0<br>/NominaIndividual/Deven<br>gados/Transporte/@Viatic<br>oManuAlojS|
|NIE073|ViaticoManuAlojNS|Parte de los viáticos pagado al trabajador<br>correspondientes a manutención y/o<br>alojamiento No Salariales.|A N||Transporte|0-1|<sup>Valor de Viaticos, Manutención y</sup><br>Alojamiento de carácter No Salarial|1.0<br>/NominaIndividual/Deven<br>gados/Transporte/@Viatic<br>oManuAlojNS|
||HEDs|Utilizado para Todos los Elementos de<br>Horas Extras Diarias de Devengos del<br>Documento|G<br>A||Devengados|0-1||1.0<br>/NominaIndividual/Deven<br>gados/HEDs|
||HED|Utilizado para Atributos de Horas Extras<br>Diarias de Devengos del Documento|E<br>A||HEDs|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/HEDs/HED|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 25 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_|_F_|_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|---|
|NIE074|HoraInicio|Hora de inicio de Hora Extra Diurna|A|H|19|HED|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividual/Deven<br>gados/HEDs/HED/@HoraI<br>nicio|
|NIE075|HoraFin|Hora de fin de Hora Extra Diurna|A|H|19|HED|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividual/Deven<br>gados/HEDs/HED/@HoraF<br>in|
|NIE076|Cantidad|Cantidad de Horas Extra Diurna|A|N||HED|1-1|Cantidad de Horas|1.0<br>/NominaIndividual/Deven<br>gados/HEDs/HED/@Canti<br>dad|
|NIE077|Porcentaje|Porcentaje al cual corresponde el calculo<br>de 1 hora Extra Diurna|A|N|4-6|HED|1-1|<sup>Se debe colocar el Porcentaje que</sup><br>corresponda de latabla 5.5.5|1.0<br>/NominaIndividual/Deven<br>gados/HEDs/HED/@Porce<br>ntaje|
|NIE078|Pago|Es el valor pagado por el tiempo que se<br>trabaja adicional a la jornada legal o<br>pactada contractualmente.|A|N||HED|1-1|Valor Pagado por las Horas|1.0<sup>/NominaIndividual/Deven</sup><br>gados/HEDs/HED/@Pago|
||HENs|Utilizado para Todos los Elementos de<br>Horas Extras Nocturnas de Devengos del<br>Documento|G<br>|A||Devengados|0-1||1.0<br>/NominaIndividual/Deven<br>gados/HENs|
||HEN|Utilizado para Atributos de Horas Extras<br>Nocturnas de Devengos del Documento|E<br>|A||HENs|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/HENs/HEN|
|NIE079|HoraInicio|Hora de inicio de Hora Extra Nocturna|A|H|19|HEN|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividual/Deven<br>gados/HENs/HEN/@HoraI<br>nicio|
|NIE080|HoraFin|Hora de fin de Hora Extra Nocturna|A|H|19|HEN|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividual/Deven<br>gados/HENs/HEN/@HoraF<br>in|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 26 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_|_F_|<br>_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|---|
|NIE081|Cantidad|Cantidad de Horas Extras Nocturnas|A|N||HEN|1-1|Cantidad de Horas|1.0<br>/NominaIndividual/Deven<br>gados/HENs/HEN/@Canti<br>dad|
|NIE082|Porcentaje|Porcentaje al cual corresponde el calculo<br>de 1 hora Extra Nocturna|A|N|4-6|HEN|1-1|<sup>Se debe colocar el Porcentaje que</sup><br>corresponda de latabla 5.5.5|1.0<br>/NominaIndividual/Deven<br>gados/HENs/HEN/@Porce<br>ntaje|
|NIE083|Pago|Es el valor pagado por el tiempo que se<br>trabaja adicional a la jornada legal o<br>pactada contractualmente.|A|N||HEN|1-1|Valor Pagado por las Horas|1.0<sup>/NominaIndividual/Deven</sup><br>gados/HENs/HEN/@Pago|
||HRNs|Utilizado para Todos los Elementos de<br>Horas Recargo Nocturno de Devengos del<br>Documento|G<br>|A||Devengados|0-1||1.0<br>/NominaIndividual/Deven<br>gados/HRNs|
||HRN|Utilizado para Atributos de Horas Recargo<br>Nocturno de Devengos del Documento|<br>E<br>|A||HRNs|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/HRNs/HRN|
|NIE084|HoraInicio|Hora de inicio de Hora Recargo Nocturno|A|H|19|HRN|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividual/Deven<br>gados/HRNs/HRN/@HoraI<br>nicio|
|NIE085|HoraFin|Hora de fin de Hora Recargo Nocturno|A|H|19|HRN|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividual/Deven<br>gados/HRNs/HRN/@Hora<br>Fin|
|NIE086|Cantidad|Cantidad de Horas Recargo Nocturno|A|N||HRN|1-1|Cantidad de Horas|1.0<br>/NominaIndividual/Deven<br>gados/HRNs/HRN/@Canti<br>dad|
|NIE087|Porcentaje|Porcentaje al cual corresponde el calculo<br>de 1 hora Recargo Nocturno|A|N|4-6|HRN|1-1|<sup>Se debe colocar el Porcentaje que</sup><br>corresponda de latabla 5.5.5|1.0<br>/NominaIndividual/Deven<br>gados/HRNs/HRN/@Porce<br>ntaje|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 27 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_|_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|NIE088|Pago|Es el valor pagado por el tiempo que se<br>trabaja adicional a la jornada legal o<br>pactada contractualmente.|A N||HRN|1-1|Valor Pagado por las Horas|1.0<sup>/NominaIndividual/Deven</sup><br>gados/HRNs/HRN/@Pago|
||HEDDFs|Utilizado para Todos los Elementos de<br>Horas Extras Diarias Dominicales y<br>Festivas de Devengos del Documento|G<br>A||Devengados|0-1||1.0<br>/NominaIndividual/Deven<br>gados/HEDDFs|
||HEDDF|Utilizado para Atributos de Horas Extras<br>Diarias Dominicales y Festivas de<br>Devengos del Documento|E<br>A||HEDDFs|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/HEDDFs/HEDDF|
|NIE089|HoraInicio|Hora de inicio de Horas Extras Diurnas<br>Dominical y Festivos|A H|19|HEDDF|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividual/Deven<br>gados/HEDDFs/HEDDF/@<br>HoraInicio|
|NIE090|HoraFin|Hora de fin de Horas Extras Diurnas<br>Dominical y Festivos|A H|19|HEDDF|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividual/Deven<br>gados/HEDDFs/HEDDF/@<br>HoraFin|
|NIE091|Cantidad|Cantidad de Horas Extras Diurnas<br>Dominical y Festivos|A N||HEDDF|1-1|Cantidad de Horas|1.0<br>/NominaIndividual/Deven<br>gados/HEDDFs/HEDDF/@<br>Cantidad|
|NIE092|Porcentaje|Porcentaje al cual corresponde el calculo<br>de 1 Hora Extra Diurna Dominical y<br>Festivo|A N|4-6|HEDDF|1-1|<sup>Se debe colocar el Porcentaje que</sup><br>corresponda de latabla 5.5.5|1.0<br>/NominaIndividual/Deven<br>gados/HEDDFs/HEDDF/@<br>Porcentaje|
|NIE093|Pago|Es el valor pagado por el tiempo que se<br>trabaja adicional a la jornada legal o<br>pactada contractualmente.|A N||HEDDF|1-1|Valor Pagado por las Horas|1.0<br>/NominaIndividual/Deven<br>gados/HEDDFs/HEDDF/@<br>Pago|
||HRDDFs|Utilizado para Todos los Elementos de<br>Horas Recargo Diarias Dominicales y<br>Festivas de Devengos del Documento|G<br>A||Devengados|0-1||1.0<br>/NominaIndividual/Deven<br>gados/HRDDFs|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 28 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_|_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
||HRDDF|Utilizado para Atributos de Horas Recargo<br>Diarias Dominicales y Festivas del<br>Documento|<br>E<br>A||HRDDFs|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/HRDDFs/HRDDF|
|NIE094|HoraInicio|Hora de inicio de Horas Recargo Diurno<br>Dominical y Festivos|A H|19|HRDDF|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividual/Deven<br>gados/HRDDFs/HRDDF/@<br>HoraInicio|
|NIE095|HoraFin|Hora de fin de Horas Recargo Diurno<br>Dominical y Festivos|A H|19|HRDDF|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividual/Deven<br>gados/HRDDFs/HRDDF/@<br>HoraFin|
|NIE096|Cantidad|Cantidad de Horas Recargo Diurno<br>Dominical y Festivos|A N||HRDDF|1-1|Cantidad de Horas|1.0<br>/NominaIndividual/Deven<br>gados/HRDDFs/HRDDF/@<br>Cantidad|
|NIE097|Porcentaje|Porcentaje al cual corresponde el calculo<br>de 1 Hora Recargo Diurno Dominical y<br>Festivos|A N|4-6|HRDDF|1-1|<sup>Se debe colocar el Porcentaje que</sup><br>corresponda de latabla 5.5.5|1.0<br>/NominaIndividual/Deven<br>gados/HRDDFs/HRDDF/@<br>Porcentaje|
|NIE098|Pago|Es el valor pagado por el tiempo que se<br>trabaja adicional a la jornada legal o<br>pactada contractualmente.|A N||HRDDF|1-1|Valor Pagado por las Horas|1.0<br>/NominaIndividual/Deven<br>gados/HRDDFs/HRDDF/@<br>Pago|
||HENDFs|Utilizado para Todos los Elementos de<br>Horas Extras Nocturnas Dominicales y<br>Festivas de Devengos del Documento|G<br>A||Devengados|0-1||1.0<br>/NominaIndividual/Deven<br>gados/HENDFs|
||HENDF|Utilizado para Atributos de Horas Extras<br>Nocturnas Dominicales y Festivas del<br>Documento|E<br>A||HENDFs|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/HENDFs/HENDF|
|NIE099|HoraInicio|Hora de inicio de Horas Extras Nocturna<br>Dominical y Festivos|A H|19|HENDF|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividual/Deven<br>gados/HENDFs/HENDF/@<br>HoraInicio|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 29 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_|<br>_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|NIE100|HoraFin|Hora de fin de Horas Extras Nocturna<br>Dominical y Festivos|A H|19|HENDF|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividual/Deven<br>gados/HENDFs/HENDF/@<br>HoraFin|
|NIE101|Cantidad|Cantidad de Horas Extras Nocturna<br>Dominical y Festivos|A N||HENDF|1-1|Cantidad de Horas|1.0<br>/NominaIndividual/Deven<br>gados/HENDFs/HENDF/@<br>Cantidad|
|NIE102|Porcentaje|Porcentaje al cual corresponde el calculo<br>de 1 Hora Extra Nocturna Dominical y<br>Festivos|A N|4-6|HENDF|1-1|<sup>Se debe colocar el Porcentaje que</sup><br>corresponda de latabla 5.5.5|1.0<br>/NominaIndividual/Deven<br>gados/HENDFs/HENDF/@<br>Porcentaje|
|NIE103|Pago|Es el valor pagado por el tiempo que se<br>trabaja adicional a la jornada legal o<br>pactada contractualmente.|A N||HENDF|1-1|Valor Pagado por las Horas|1.0<br>/NominaIndividual/Deven<br>gados/HENDFs/HENDF/@<br>Pago|
||HRNDFs|Utilizado para Todos los Elementos de<br>Horas Recargo Nocturno Dominicales y<br>Festivas de Devengos del Documento|G<br>A||Devengados|0-1||1.0<br>/NominaIndividual/Deven<br>gados/HRNDFs|
||HRNDF|Utilizado para Atributos de Horas Recargo<br>Nocturno Dominicales y Festivas del<br>Documento|<br>E<br>A||HRNDFs|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/HRNDFs/HRNDF|
|NIE104|HoraInicio|Hora de inicio de Horas Recargo Nocturno<br>Dominical y Festivos|<br>A H|19|HRNDF|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividual/Deven<br>gados/HRNDFs/HRNDF/@<br>HoraInicio|
|NIE105|HoraFin|Hora de fin de Horas Recargo Nocturno<br>Dominical y Festivos|A H|19|HRNDF|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividual/Deven<br>gados/HRNDFs/HRNDF/@<br>HoraFin|
|NIE106|Cantidad|Cantidad de Horas Recargo Nocturno<br>Dominical y Festivos|A N||HRNDF|1-1|Cantidad de Horas|1.0<br>/NominaIndividual/Deven<br>gados/HRNDFs/HRNDF/@<br>Cantidad|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 30 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_|<br>_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|NIE107|Porcentaje|Porcentaje al cual corresponde el calculo<br>de 1 Hora Recargo Nocturno Dominical y<br>Festivos|A N|4-6|HRNDF|1-1|<sup>Se debe colocar el Porcentaje que</sup><br>corresponda de latabla 5.5.5|1.0<br>/NominaIndividual/Deven<br>gados/HRNDFs/HRNDF/@<br>Porcentaje|
|NIE108|Pago|Es el valor pagado por el tiempo que se<br>trabaja adicional a la jornada legal o<br>pactada contractualmente.|A N||HRNDF|1-1|Valor Pagado por las Horas|1.0<br>/NominaIndividual/Deven<br>gados/HRNDFs/HRNDF/@<br>Pago|
||Vacaciones|Utilizado para Todos los Elementos de<br>Vacaciones de Devengos del Documento|G<br>A||Devengados|0-1||1.0<br>/NominaIndividual/Deven<br>gados/Vacaciones|
||VacacionesComune|s<br>Utilizado para Atributos de Vacaciones<br>Comunes del Documento|E<br>A||Vacaciones|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/Vacaciones/Vacacio<br>nesComunes|
|NIE109|FechaInicio|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador presenta el inicio del disfrute<br>de sus vacaciones en tiempo.|A F|10|VacacionesComun<br>es|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividual/Deven<br>gados/Vacaciones/Vacacio<br>nesComunes/@FechaInici<br>o|
|NIE110|FechaFin|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador regresa o termina el disfrute<br>de sus vacaciones.|A F|10|VacacionesComun<br>es|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividual/Deven<br>gados/Vacaciones/Vacacio<br>nesComunes/@FechaFin|
|NIE111|Cantidad|Número de días que el trabajador estuvo<br>inactivo durante el mes por vacaciones.|A N||VacacionesComun<br>es|1-1|Cantidad de Dias|1.0<br>/NominaIndividual/Deven<br>gados/Vacaciones/Vacacio<br>nesComunes/@Cantidad|



Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Página 31 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_<br>|_Tam_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIE112|Pago|Corresponde al valor pagado al<br>trabajador, por el descanso remunerado<br>que tiene derecho por haber trabajado un<br>determinado tiempo. (Vacaciones SI<br>disfrutadas)|<br>A N|<br>VacacionesComun<br>es<br>|1-1|Valor Pagado por Vacaciones Si Disfrutadas|1.0<br>/NominaIndividual/Deven<br>gados/Vacaciones/Vacacio<br>nesComunes/@Pago|
||VacacionesCompe<br>adas|ns<br>Utilizado para Atributos de Vacaciones<br>Compensadas del Documento|E<br>A|Vacaciones<br>|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/Vacaciones/Vacacio<br>nesCompensadas|
|NIE115|Cantidad|Número de días que el trabajador estuvo<br>activo durante el mes sin disfrutar sus<br>vacaciones. (Vacaciones NO disfrutadas)|A N|<br>VacacionesCompe<br>nsadas<br>|1-1|Cantidad de Dias|1.0<br>/NominaIndividual/Deven<br>gados/Vacaciones/Vacacio<br>nesCompensadas/@Canti<br>dad|
|NIE116|Pago|Corresponde al valor pagado al<br>trabajador, por el descanso remunerado<br>que no disfrutó y que tiene derecho por<br>haber trabajado un determinado tiempo.<br>(Vacaciones NO disfrutadas)|A N|<br>VacacionesCompe<br>nsadas<br>|1-1|Valor Pagado por Vacaciones No Disfrutadas|1.0<br>/NominaIndividual/Deven<br>gados/Vacaciones/Vacacio<br>nesCompensadas/@Pago|
||Primas|Utilizado para Atributos de Primas de<br>Devengos del Documento|E<br>A|Devengados<br>|0-1|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/Primas|
|NIE117|Cantidad|Cantidad de dias trabajados para calculo<br>de Pago de Corte de Prima|A N|<br>Primas<br>|1-1|<sup>Cantidad de Dias a los cuales corresponde el</sup><br>pago de la Prima legal|1.0<sup>/NominaIndividual/Deven</sup><br>gados/Primas/@Cantidad|
|NIE118|Pago|Pagos por el reconocimiento del logro o<br>cumplimiento por parte del trabajador en<br>el desarrollo de sus labores, de<br>condiciones definidas expresamente<br>entre las partes.|A N|<br>Primas<br>|1-1|<sup>Valor Pagado por Prima Legal con respecto</sup><br>a Cantidad de Dias|1.0<sup>/NominaIndividual/Deven</sup><br>gados/Primas/@Pago|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 32 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_|_Tam_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIE119|PagoNS|Son valores pagados al trabajador de<br>forma ocasional y por mera liberalidad o<br>los pactados entre las partes de forma<br>expresa como pago no salarial.|A N|<br>Primas|0-1|Valor Pagado por Prima No Salarial|1.0<sup>/NominaIndividual/Deven</sup><br>gados/Primas/@PagoNS|
||Cesantias|Utilizado para Atributos de Cesantias de<br>Devengos del Documento|E<br>A|Devengados|0-1|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/Cesantias|
|NIE120|Pago|Pago de la Cesantia otorgada por Ley.|A N|<br>Cesantias|1-1|Valor Pagado por Cesantias|1.0<sup>/NominaIndividual/Deven</sup><br>gados/Cesantias/@Pago|
|NIE121|Porcentaje|Porcentaje que corresponde al Interes de<br>Cesantia de Ley|A N|<br>Cesantias|1-1|Porcentaje de Interes de Cesantias|1.0<br>/NominaIndividual/Deven<br>gados/Cesantias/@Porcen<br>taje|
|NIE122|PagoIntereses|Pago de los Intereses de Cesantia<br>otorgada por Ley.|A N|<br>Cesantias|1-1|Valor Pagado por Intereses de Cesantias|1.0<br>/NominaIndividual/Deven<br>gados/Cesantias/@PagoIn<br>tereses|
||Incapacidades|Utilizado para Todos los Elementos de<br>Incapacidades de Devengos del<br>Documento|G<br>A|Devengados|0-1||1.0<br>/NominaIndividual/Deven<br>gados/Incapacidades|
||Incapacidad|Utilizado para Atributos de Incapacidad<br>del Documento|E<br>A|Incapacidades|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/Incapacidades/Inca<br>pacidad|
|NIE123|FechaInicio|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador presenta o da por iniciada su<br>Incapacidad.|A F|10<br>Incapacidad|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividual/Deven<br>gados/Incapacidades/Inca<br>pacidad/@FechaInicio|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 33 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_<br>|_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|NIE124|FechaFin|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador presenta o da por terminada<br>su Incapacidad.|A F<br>1|0|Incapacidad|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividual/Deven<br>gados/Incapacidades/Inca<br>pacidad/@FechaFin|
|NIE125|Cantidad|Número de días que el trabajador o<br>aprendiz estuvo inactivo por incapacidad<br>(sin importar su origen).|A N||Incapacidad|1-1|Cantidad de Dias|1.0<br>/NominaIndividual/Deven<br>gados/Incapacidades/Inca<br>pacidad/@Cantidad|
|NIE126|Tipo|Se debe indicar el codigo al cual<br>corresponda el tipo de incapacidad del<br>Empleado|A N 1||Incapacidad|1-1|<sup>Se debe colocar el Codigo que corresponda</sup><br>de latabla 5.5.6|1.0<br>/NominaIndividual/Deven<br>gados/Incapacidades/Inca<br>pacidad/@Tipo|
|NIE127|Pago|Valor de la prestación económica pagada<br>al trabajador por consecuencia de la falta<br>de capacidad laboral sin importar su<br>origen.|A N||Incapacidad|1-1|<sup>Valor Pagado por Incapacidad con respecto</sup><br>a Cantidad de Dias|1.0<br>/NominaIndividual/Deven<br>gados/Incapacidades/Inca<br>pacidad/@Pago|
||Licencias|Utilizado para Todos los Elementos de<br>Licencias de Devengos del Documento|G<br>A||Devengados|0-1||1.0<br>/NominaIndividual/Deven<br>gados/Licencias|
||LicenciaMP|Utilizado para Atributos de Licencia de<br>Materinidad o Paternidad del Documento|E<br>A||Licencias|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/Licencias/Licencia<br>MP|
|NIE128|FechaInicio|Fecha donde da inicio la Licencia de<br>Maternidad o Paternidad|A F<br>1|0|LicenciaMP|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividual/Deven<br>gados/Licencias/Licencia<br>MP/@FechaInicio|
|NIE129|FechaFin|Fecha donde termina la Licencia de<br>Maternidad o Paternidad|A F<br>1|0|LicenciaMP|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividual/Deven<br>gados/Licencias/Licencia<br>MP/@FechaFin|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 34 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_<br>|_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|NIE130|Cantidad|Número de días que el trabajador o<br>aprendiz efectivamente estuvo inactivo<br>por licencia de maternidad o paternidad.|A N||LicenciaMP|1-1|Cantidad de Dias|1.0<br>/NominaIndividual/Deven<br>gados/Licencias/Licencia<br>MP/@Cantidad|
|NIE131|Pago|Valor pagado al trabajador del descanso<br>remunerado que la ley confiere por el<br>nacimiento de un hijo, y que es<br>reconocido y pagado por la EPS a la que<br>está afiliado el padre o la madre, o en su<br>defecto por el empleador.|A N||LicenciaMP|1-1|<sup>Valor Pagado por Licencia de Maternidad o</sup><br>Paternidad con respecto a Cantidad de Dias|<sup>1.0</sup><br>/NominaIndividual/Deven<br>gados/Licencias/Licencia<br>MP/@Pago|
||LicenciaR|Utilizado para Atributos de Licencia<br>Remunerada del Documento|E<br>A||Licencias|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/Licencias/LicenciaR|
|NIE132|FechaInicio|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador o aprendiz inicia algún permiso<br>o licencia remunerada.|<br>A F<br>1|0|LicenciaR|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividual/Deven<br>gados/Licencias/LicenciaR<br>/@FechaInicio|
|NIE133|FechaFin|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador o aprendiz termina el permiso<br>o licencia remunerada.|A F<br>1|0|LicenciaR|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividual/Deven<br>gados/Licencias/LicenciaR<br>/@FechaFin|
|NIE134|Cantidad|Número de días que el trabajador o<br>aprendiz efectivamente estuvo inactivo<br>por permiso o licencia pero que le fueron<br>reconocidos en su pago.|A N||LicenciaR|1-1|Cantidad de Dias|1.0<br>/NominaIndividual/Deven<br>gados/Licencias/LicenciaR<br>/@Cantidad|
|NIE135|Pago|Valor pagado al trabajador corresponde a<br>tiempo no laborado, que por ley o por<br>acuerdo con el empleador se le concede|A N||LicenciaR|1-1|<sup>Valor Pagado por Licencia Remunerada con</sup><br>respecto a Cantidad de Dias|1.0<br>/NominaIndividual/Deven<br>gados/Licencias/LicenciaR<br>/@Pago|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 35 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_<br>|_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
||LicenciaNR|Utilizado para Atributos de Licencia No<br>Remunerada del Documento|E<br>A||Licencias|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/Licencias/LicenciaN<br>R|
|NIE136|FechaInicio|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador o aprendiz inicia alguna<br>suspensión, permiso o licencia NO<br>remunerada.|A F<br>1|0|LicenciaNR|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividual/Deven<br>gados/Licencias/LicenciaN<br>R/@FechaInicio|
|NIE137|FechaFin|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador o aprendiz termina la<br>suspensión, permiso o licencia NO<br>remunerada.|A F<br>1|0|LicenciaNR|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividual/Deven<br>gados/Licencias/LicenciaN<br>R/@FechaFin|
|NIE138|Cantidad|Número de días que el trabajador o<br>aprendiz efectivamente estuvo inactivo<br>por suspensión, permiso o licencia y que<br>NO le fueron reconocidos en su pago.|A N||LicenciaNR|1-1|Cantidad de Dias|1.0<br>/NominaIndividual/Deven<br>gados/Licencias/LicenciaN<br>R/@Cantidad|
||Bonificaciones|Utilizado para Todos los Elementos de<br>Bonificaciones de Devengos del<br>Documento|G<br>A||Devengados|0-1||1.0<br>/NominaIndividual/Deven<br>gados/Bonificaciones|
||Bonificacion|Utilizado para Atributos de Bonificacion<br>del Documento|E<br>A||Bonificaciones|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/Bonificaciones/Boni<br>ficacion|
|NIE139|BonificacionS|Son valores pagados al trabajador en<br>forma de incentivo o recompensa por la<br>contraprestación directa del servicio.|A N||Bonificacion|0-1|Valor Pagado por Bonificación Salarial|1.0<br>/NominaIndividual/Deven<br>gados/Bonificaciones/Boni<br>ficacion/@BonificacionS|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

> www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 36 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_<br>|_Tam_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIE140|BonificacionNS|Son valores de incentivos pagados al<br>trabajador de forma ocasional y por mera<br>liberalidad o los pactados entre las partes<br>de forma expresa como pago no salarial.|A N|Bonificacion|0-1|Valor Pagado por Bonificación No Salarial|1.0<br>/NominaIndividual/Deven<br>gados/Bonificaciones/Boni<br>ficacion/@BonificacionNS|
||Auxilios|Utilizado para Todos los Elementos de<br>Auxilios de Devengos del Documento|G<br>A|Devengados|0-1||1.0<br>/NominaIndividual/Deven<br>gados/Auxilios|
||Auxilio|Utilizado para Atributos de Auxilio del<br>Documento|E<br>A|Auxilios|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/Auxilios/Auxilio|
|NIE141|AuxilioS|Son beneficios, ayudas o apoyos<br>económicos, pagados al trabajador de<br>forma habitual o pactados entre las<br>partes como factor salarial.|A N|Auxilio|0-1|Valor Pagado por Auxilios Salariales|1.0<br>/NominaIndividual/Deven<br>gados/Auxilios/Auxilio/@A<br>uxilioS|
|NIE142|AuxilioNS|Son beneficios, ayudas o apoyos<br>económicos, pagados al trabajador de<br>forma ocasional y por mera liberalidad o<br>los pactados entre las partes de forma<br>expresa como pago no salarial.|A N|Auxilio|0-1|Valor Pagado por Auxilios No Salariales|1.0<br>/NominaIndividual/Deven<br>gados/Auxilios/Auxilio/@A<br>uxilioNS|
||HuelgasLegales|Utilizado para Todos los Elementos de<br>Huelgas Legales de Devengos del<br>Documento|G<br>A|Devengados|0-1||1.0<br>/NominaIndividual/Deven<br>gados/HuelgasLegales|
||HuelgaLegal|Utilizado para Atributos de Huelga Legal<br>del Documento|E<br>A|HuelgasLegales|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/HuelgasLegales/Hu<br>elgaLegal|



> Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 37 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_<br>|_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|NIE143|FechaInicio|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador inicia la huelga legalmente<br>declarada.|A F<br>1|0|HuelgaLegal|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividual/Deven<br>gados/HuelgasLegales/Hu<br>elgaLegal/@FechaInicio|
|NIE144|FechaFIn|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador termina la huelga legalmente<br>declarada.|A F<br>1|0|HuelgaLegal|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividual/Deven<br>gados/HuelgasLegales/Hu<br>elgaLegal/@FechaFIn|
|NIE145|Cantidad|número de días en los que el trabajador<br>estuvo inactivo por huelga legalmente<br>declarada.|A N||HuelgaLegal|1-1|Cantidad de Dias|1.0<br>/NominaIndividual/Deven<br>gados/HuelgasLegales/Hu<br>elgaLegal/@Cantidad|
||OtrosConceptos|Utilizado para Todos los Elementos de<br>Otros Conceptos de Devengos del<br>Documento|G<br>A||Devengados|0-1||1.0<br>/NominaIndividual/Deven<br>gados/OtrosConceptos|
||OtroConcepto|Utilizado para Atributos de Otro Concepto<br>del Documento|<br>E<br>A||OtrosConceptos|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/OtrosConceptos/Ot<br>roConcepto|
|NIE146|DescripcionConcept<br>o|Nombre del Concepto que corresponde a<br>los demás pagos fijos o variables<br>realizados al trabajador que remuneren<br>en dinero o en especie como<br>contraprestación directa del servicio, sea<br>cualquiera la forma o denominación que<br>se adopte.|A A||OtroConcepto|1-1|Debe ir la Descripcion del Concepto|1.0<br>/NominaIndividual/Deven<br>gados/OtroConceptos/Otr<br>oConcepto/@Descripcion<br>Concepto|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 38 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_|_Tam_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIE147|ConceptoS|Valor de los demás pagos fijos o variables<br>realizados al trabajador que remuneren<br>en dinero o en especie como<br>contraprestación directa del servicio, sea<br>cualquiera la forma o denominación que<br>se adopte (Salarial).|A N|<br>OtroConcepto|0-1|Valor Pagado por Conceptos Salariales|1.0<br>/NominaIndividual/Deven<br>gados/OtroConceptos/Otr<br>oConcepto/@ConceptoS|
|NIE148|ConceptoNS|Valor de los demás pagos que<br>ocasionalmente y por mera liberalidad<br>recibe el trabajador del empleador, en<br>dinero o en especie no para su beneficio,<br>ni para enriquecer su patrimonio, sino<br>para desempeñar a cabalidad sus<br>funciones (No Salarial).|A N|<br>OtroConcepto|0-1|Valor Pagado por Conceptos No Salariales|1.0<br>/NominaIndividual/Deven<br>gados/OtroConceptos/Otr<br>oConcepto/@ConceptoNS|
||Compensaciones|Utilizado para Todos los Elementos de<br>Compensaciones de Devengos del<br>Documento|G<br>A|Devengados|0-1||1.0<br>/NominaIndividual/Deven<br>gados/Compensaciones|
||Compensacion|Utilizado para Atributos de Compensacion<br>del Documento|<br>E<br>A|Compensaciones|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/Compensaciones/C<br>ompensacion|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 39 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_<br>|_Tam_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIE149|CompensacionO|Suma de dinero definido en el régimen de<br>compensaciones como retribución<br>mensual recibido por el asociado por la<br>ejecución de su actividad material o<br>inmaterial, la cual se fija teniendo en<br>cuenta el tipo de labor desempeñada, el<br>rendimiento o la productividad y la<br>cantidad de trabajo aportado. El monto<br>de la compensación ordinaria podrá ser<br>una suma básica igual para todos los<br>asociados (Ordinaria).<br>|A N|Compensacion|1-1|<sup>Valor Pagado por Compensaciones</sup><br>Ordinarias|1.0<br>/NominaIndividual/Deven<br>gados/Compensaciones/C<br>ompensacion/@Compens<br>acionO|
|NIE150|CompensacionE|Los demás pagos adicionales a la<br>Compensación Ordinaria que recibe el<br>asociado como retribución por su trabajo,<br>definidos en el régimen de<br>compensaciones (Extraordinaria).<br>|A N|Compensacion|1-1|<sup>Valor Pagado por Compensaciones</sup><br>Extraordinarias|1.0<br>/NominaIndividual/Deven<br>gados/Compensaciones/C<br>ompensacion/@Compens<br>acionE|
||BonoEPCTVs|Utilizado para Todos los Elementos de<br>Bonos Electronicos o de Papel de Servicio,<br>Cheques, Tarjetas, Vales, etc de Devengos<br>del Documento<br>|G<br>A|Devengados|0-1||1.0<br>/NominaIndividual/Deven<br>gados/BonoEPCTVs|
||BonoEPCTV|Utilizado para Atributos de Bono<br>Electronico o de Papel de Servicio,<br>Cheque, Tarjeta, Vale, etc del Documento<br>|E<br>A|BonoEPCTVs|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deven<br>gados/BonoEPCTVs/Bono<br>EPCTV|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 40 de 269 



**Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_<br>|_Tam_<br>_Padre_|_Oc_|<br>_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIE151|PagoS|Valor que el trabajador recibe como<br>contraprestación por el trabajo realizado,<br>por medio de bonos electrónicos,<br>recargas, cheques, vales. es decir, todo<br>pago realizado en un medio diferente a<br>dinero en efectivo o consignación de<br>cuenta bancaria (Salarial).|A N|<br>BonoEPCTV|0-1|Concepto Salarial|1.0<br>/NominaIndividual/Deven<br>gados/BonoEPCTVs/Bono<br>EPCTV/@PagoS|
|NIE152|PagoNS|Valor que el trabajador recibe como<br>concepto no salarial, por medio de bonos<br>electrónicos, recargas, cheques, vales. es<br>decir, todo pago realizado en un medio<br>diferente a dinero en efectivo o<br>consignación de cuenta bancaria (No<br>Salarial).|A N|<br>BonoEPCTV|0-1|Concepto No Salarial|1.0<br>/NominaIndividual/Deven<br>gados/BonoEPCTVs/Bono<br>EPCTV/@PagoNS|
|NIE153|PagoAlimentacionS|Valor que el trabajador recibe como<br>concepto no salarial, por medio de bonos<br>electrónicos, recargas, cheques, vales. es<br>decir, todo pago realizado en un medio<br>diferente a dinero en efectivo o<br>consignación de cuenta bancaria (Para<br>Alimentación Salarial).|A N|<br>BonoEPCTV|0-1|Concepto Salarial|1.0<br>/NominaIndividual/Deven<br>gados/BonoEPCTVs/Bono<br>EPCTV/@PagoAlimentacio<br>nS|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 41 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_<br>|_Tam_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIE154|PagoAlimentacionN<br>S|Valor que el trabajador recibe como<br>concepto no salarial, por medio de bonos<br>electrónicos, recargas, cheques, vales. es<br>decir, todo pago realizado en un medio<br>diferente a dinero en efectivo o<br>consignación de cuenta bancaria (Para<br>Alimentación No Salarial).|A N|BonoEPCTV|0-1|Concepto No Salarial|1.0<br>/NominaIndividual/Deven<br>gados/BonoEPCTVs/Bono<br>EPCTV/@PagoAlimentacio<br>nNS|
||Comisiones|Utilizado para Todos los Elementos de<br>Comisiones de Devengos del Documento|G<br>A|Devengados|0-1||1.0<br>/NominaIndividual/Deven<br>gados/Comisiones|
|NIE155|Comision|Valor pagado al trabajador usualmente<br>del área comercial, y de forma regular se<br>liquida con un porcentaje sobre el<br>importe de una operación, también se<br>presenta como incentivo por el logro de<br>objetivos.|E<br>N|Comisiones|0-N|Valor Pagado por Comision|1.0<br>/NominaIndividual/Deven<br>gados/Comisiones/Comisi<br>on|
||PagosTerceros|Utilizado para Todos los Elementos de<br>Pagos a Tercero de Devengos del<br>Documento|G<br>A|Devengados|0-1||1.0<br>/NominaIndividual/Deven<br>gados/PagosTerceros|
|NIE193|PagoTercero|Beneficios en cabeza del Trabjador que se<br>pagan a un proveedor o tercero.|E<br>N|PagosTerceros|0-N|Valor Pagado por Pago Tercero|1.0<br>/NominaIndividual/Deven<br>gados/PagosTerceros/Pag<br>oTercero|
||Anticipos|Utilizado para Todos los Elementos de<br>Anticipos de Devengos del Documento|G<br>A|Devengados|0-1||1.0<br>/NominaIndividual/Deven<br>gados/Anticipos|
|NIE194|Anticipo|Anticipos de Nómina.|E<br>N|Anticipos|0-N|Valor Pagado por Anticipo|1.0<sup>/NominaIndividual/Deven</sup><br>gados/Anticipos/Anticipo|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 42 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_<br>|_Tam_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIE156|Dotacion|De conformidad con lo previsto en el<br>artículo 230 del Código Sustantivo del<br>Trabajo, o la norma que lo modifique,<br>adicione o sustituya, corresponde al valor<br>que el empleador dispone para<br>suministrar la dotación de sus<br>trabajadores.|E<br>N|Devengados|0-1|Valor Pagado por Dotación|1.0<sup>/NominaIndividual/Deven</sup><br>gados/Dotacion|
|NIE157|ApoyoSost|Corresponde al valor no salarial que el<br>patrocinador paga de forma mensual<br>como ayuda o apoyo economía al<br>aprendiz o practicante universitario<br>durante su etapa lectiva y fase practica.|E<br>N|Devengados|0-1|Valor Pagado por Apoyo a Sostenimiento|1.0<sup>/NominaIndividual/Deven</sup><br>gados/ApoyoSost|
|NIE158|Teletrabajo|Valor que debe ser pagado al trabajador<br>cuyo contrato indica expresamente que<br>puede laborar mediante teletrabajo|E<br>N|Devengados|0-1|Valor Pagado por trabajo en Teletrabajo|1.0<sup>/NominaIndividual/Deven</sup><br>gados/Teletrabajo|
|NIE159|BonifRetiro|Valor establecido por mutuo acuerdo por<br>retiro del Trabajador|E<br>N|Devengados|0-1|Valor Pagado por Retiro de la empresa|1.0<sup>/NominaIndividual/Deven</sup><br>gados/BonifRetiro|
|NIE160|Indemnizacion|Valor de Indemnizacion establecido por<br>ley|E<br>N|Devengados|0-1|Valor Pagado por Indemnización|1.0<sup>/NominaIndividual/Deven</sup><br>gados/Indemnizacion|
|NIE201|Reintegro|Valor que le regresa la empresa al<br>trabajador por una deducción mal<br>realizada en otro pago de nomina|E<br>N|Devengados|0-1|<sup>Valor Pagado correspondiente a Reintegro</sup><br>por parte del empleador|1.0<sup>/NominaIndividual/Deven</sup><br>gados/Reintegro|
||Deducciones|Utilizado para Todas las Deducciones del<br>Documento|G<br>A|NominaIndividua|l<br>1-1|Hace referencia al concepto de valor<br>deducido de nómina señalado en el<br>numeral 18, articulo 1 de la presente<br>resolución.|1.0<br>/NominaIndividual/Deduc<br>ciones|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 43 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_|_Tam_<br>_Padre_|_Oc_|<br>_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
||Salud|Utilizado para Atributos de Salud del<br>Documento|E<br>A|Deducciones|1-1|Elemento Vacio|1.0<br>/NominaIndividual/Deduc<br>ciones/Salud|
|NIE161|Porcentaje|Debe corresponder al porcentaje de<br>deducción de salud que paga el<br>trabajador|A N|<br>Salud|1-1|<sup>Se debe colocar el Porcentaje que</sup><br>corresponda|1.0<br>/NominaIndividual/Deduc<br>ciones/Salud/@Porcentaj<br>e|
|NIE163|Deduccion|El trabajador debe estar afiliado al<br>sistema de salud. La cotización por salud<br>que corresponde al 12.5% de la base del<br>aporte, se hace en conjunto con la<br>empresa. Ésta última aporta el 8.5%, y el<br>empleado debe aportar el 4% restante.<br>Ese 4% es el valor que se debe descontar<br>(deducir) del total devengado a cargo del<br>empleado.|A N|<br>Salud|1-1|<sup>Valor Pagado correspondiente a Salud por</sup><br>parte del trabajador|1.0<sup>/NominaIndividual/Deduc</sup><br>ciones/Salud/@Deduccion|
||FondoPension|Utilizado para Atributos de Fondos de<br>Pension del Documento|E<br>A|Deducciones|1-1|Elemento Vacio|1.0<br>/NominaIndividual/Deduc<br>ciones/FondoPension|
|NIE164|Porcentaje|Debe corresponder al porcentaje de<br>deducción de fondo de pensión que paga<br>el trabajador|A N|4-6<br>FondoPension|1-1|<sup>Se debe colocar el Porcentaje que</sup><br>corresponda|1.0<br>/NominaIndividual/Deduc<br>ciones/FondoPension/@P<br>orcentaje|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 44 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_<br>|_Tam_|<br>_Padre_|_Oc_|<br>_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|NIE166|Deduccion|El trabajador también debe estar afiliado<br>al sistema de pensiones. La cotización por<br>pensión está a cargo tanto de la empresa<br>como del empleado. Del total del aporte<br>(16%), la empresa aporta el 75% (12%) y<br>el trabajador aporta el restante 25% (4%).<br>Como el trabajador debe aportar un 4%<br>por concepto de pensión, este valor se le<br>descuenta (deduce) del valor devengado<br>en el respectivo periodo (mes o<br>quincena).|<br> <br>A N||FondoPension|1-1|<sup>Valor Pagado correspondiente a Pension</sup><br>por parte del trabajador|1.0<br>/NominaIndividual/Deduc<br>ciones/FondoPension/@D<br>educcion|
||FondoSP|Utilizado para Atributos de Fondo de<br>Seguridad Pensional del Documento|E<br>A||Deducciones|0-1|Elemento Vacio|1.0<br>/NominaIndividual/Deduc<br>ciones/FondoSP|
|NIE167|Porcentaje|Debe corresponder al porcentaje de<br>deducción de fondo de seguridad<br>pensional que paga el trabajador|A N 4|-6|FondoSP|0-1|<sup>Se debe colocar el Porcentaje que</sup><br>corresponda|1.0<br>/NominaIndividual/Deduc<br>ciones/FondoSP/@Porcen<br>taje|
|NIE168|DeduccionSP|Todo trabajador que devengue un sueldo<br>que sea igual o superior a 4 salarios<br>mininos, debe aportar un 1% al Fondo de<br>solidaridad pensional.|A N||FondoSP|0-1|Valor Pagado correspondiente a Fondo de<br>Solidaridad Pensional por parte del<br>trabajador|1.0<br>/NominaIndividual/Deduc<br>ciones/FondoSP/@Deducc<br>ionSP|
|NIE169|PorcentajeSub|Se debe colocar el Porcentaje que<br>correspondiente al Fondo de Subsistencia<br>correspondiente|<br>A N 4|-6|FondoSP|0-1|Se debe colocar el Porcentaje que<br>correspondiente al Fondo de Subsistencia<br>correspondiente|1.0<br>/NominaIndividual/Deduc<br>ciones/FondoSP/@Porcen<br>tajeSub|
|NIE170|DeduccionSub|Valor Pagado correspondiente a Fondo de<br>Subsistencia por parte del trabajador|<br>A N||FondoSP|0-1|<sup>Valor Pagado correspondiente a Fondo de</sup><br>Subsistencia por parte del trabajador|1.0<br>/NominaIndividual/Deduc<br>ciones/FondoSP/@Deducc<br>ionSub|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 45 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_<br>_T_|_am_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
||Sindicatos|Utilizado para Todos los Elementos de<br>Sindicatos de Deducciones del<br>Documento|G<br>A|Deducciones|0-1||1.0<br>/NominaIndividual/Deduc<br>ciones/Sindicatos|
||Sindicato|Utilizado para Atributos de Sindicato del<br>Documento|E<br>A|Sindicatos|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deduc<br>ciones/Sindicatos/Sindicat<br>o|
|NIE171|Porcentaje|Porcentaje establecido en la ley o por<br>estatutos del sindicato.|A N|Sindicato|1-1|Se debe colocar el Porcentaje que<br>correspondiente a Aportes del Sindicato<br>correspondiente|1.0<br>/NominaIndividual/Deduc<br>ciones/Sindicatos/Sindicat<br>o/@Porcentaje|
|NIE172|Deduccion|Las cuotas que los trabajadores<br>sindicalizados deben aportar al sindicato<br>al que estén afiliados, y siempre que<br>medie autorización del empleado.|A N|Sindicato|1-1|<sup>Valor Pagado correspondiente a Aportes del</sup><br>Sindicato por parte del trabajador|1.0<br>/NominaIndividual/Deduc<br>ciones/Sindicatos/Sindicat<br>o/@Deduccion|
||Sanciones|Utilizado para Todos los Elementos de<br>Sanciones de Deducciones del<br>Documento|G<br>A|Deducciones|0-1||1.0<br>/NominaIndividual/Deduc<br>ciones/Sanciones|
||Sancion|Utilizado para Atributos de Sancion del<br>Documento|E<br>A|Sanciones|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deduc<br>ciones/Sanciones/Sancion|
|NIE173|SancionPublic|Valor por el del incumplimiento de una<br>regla o norma de conducta obligatoria<br>(Publica)|A N|Sancion|1-1|<sup>Valor Pagado correspondiente a Sanción</sup><br>Pública por parte del trabajador|1.0<br>/NominaIndividual/Deduc<br>ciones/Sanciones/Sancion<br>/@SancionPublic|
|NIE174|SancionPriv|Valor por el del incumplimiento de una<br>regla o norma de conducta obligatoria<br>(Privada o Ordinaria)|A N|Sancion|1-1|<sup>Valor Pagado correspondiente a Sanción</sup><br>Privada por parte del trabajador|1.0<br>/NominaIndividual/Deduc<br>ciones/Sanciones/Sancion<br>/@SancionPriv|
||Libranzas|Utilizado para Todos los Elementos de<br>Libranzas de Deducciones del Documento|G<br>A|Deducciones|0-1||1.0<br>/NominaIndividual/Deduc<br>ciones/Libranzas|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 46 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_<br>_T_|_am_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
||Libranza|Utilizado para Atributos de Libranza del<br>Documento|E<br>A|Libranzas|0-N|Elemento Vacio|1.0<br>/NominaIndividual/Deduc<br>ciones/Libranzas/Libranza|
|NIE175|Descripcion|Nombre de la Libranza que corresponda a<br>las cuotas que el empleado deba pagar a<br>una entidad financiera, para la<br>amortización de un crédito que le haya<br>sido otorgado por libranza|A A|Libranza|1-1|Debe ir la Descripcion de la Libranza|1.0<br>/NominaIndividual/Deduc<br>ciones/Libranzas/Libranza<br>/@Descripcion|
|NIE176|Deduccion|Las cuotas que el empleado deba pagar a<br>una entidad financiera, para la<br>amortización de un crédito que le haya<br>sido otorgado por libranza|A N|Libranza|1-1|Valor Pagado correspondiente a Aportes a<br>Entidades Financieras por parte del<br>trabajador|1.0<br>/NominaIndividual/Deduc<br>ciones/Libranzas/Libranza<br>/@Deduccion|
||PagosTerceros|Utilizado para Todos los Elementos de<br>Pagos a Tercero de Deducciones del<br>Documento|G<br>A|Deducciones|0-1||1.0<br>/NominaIndividual/Deduc<br>ciones/PagosTerceros|
|NIE195|PagoTercero|Deducciones en cabeza del Trabjador que<br>se pagan a un proveedor o tercero.|E<br>N|PagosTerceros|0-N|Valor Pagado por Pago Tercero|1.0<br>/NominaIndividual/Deduc<br>ciones/PagosTerceros/Pag<br>oTercero|
||Anticipos|Utilizado para Todos los Elementos de<br>Anticipos de Deducciones del Documento|G<br>A|Deducciones|0-1||1.0<br>/NominaIndividual/Deduc<br>ciones/Anticipos|
|NIE196|Anticipo|Deduccion por Anticipos de Nómina.|E<br>N|Anticipos|0-N|Valor Pagado por Anticipo|1.0<br>/NominaIndividual/Deduc<br>ciones/Anticipos/Anticipo|
||OtrasDeducciones|Utilizado para Todos los Elementos de<br>Otras Deducciones del Documento|G<br>A|Deducciones|0-1||1.0<br>/NominaIndividual/Deduc<br>ciones/OtrasDeducciones|



> Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 47 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_n_|_s_<br>_Campo_|_Descripción_|_T_<br>_F_<br>|_Tam_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|NIE197||OtraDeduccion|Otro tipo de deducción dentro de la<br>Nomina.|E<br>N|OtrasDeduccion|es 0-N|Valor Pagado por Otra Deducción|1.0<br>/NominaIndividual/Deduc<br>ciones/OtrasDeducciones/<br>OtraDeduccion|
|NIE198||PensionVoluntaria|Valor correspondiente al ahorro que hace<br>el trabajador para complementar su<br>pension obligatoria o cumplir metas<br>especificas.|E<br>N|Deducciones|0-1|Valor Pagado correspondiente al ahorro que<br>hace el trabajador para complementar su<br>pension obligatoria o cumplir metas<br>especificas.|<br>1.0<sup>/NominaIndividual/Deduc</sup><br>ciones/PensionVoluntaria|
|NIE177||RetencionFuente|Si hubiere lugar, la empresa deberá<br>calcular y retener al empleado el valor<br>correspondiente a retención en la fuente<br>por ingresos laborales. Este valor será<br>declarado y consignado en la respectiva<br>declaración mensual de retención en la<br>fuente.|E<br>N|Deducciones|0-1|<sup>Valor Pagado correspondiente a Retención</sup><br>en la Fuente por parte del trabajador|1.0<sup>/NominaIndividual/Deduc</sup><br>ciones/RetencionFuente|
|NIE179||AFC|Corresponde a (Ahorro Fomento a la<br>contruccion)|E<br>N|Deducciones|0-1|<sup>Valor Pagado correspondiente a AFC por</sup><br>parte del trabajador|1.0<sup>/NominaIndividual/Deduc</sup><br>ciones/AFC|
|NIE180||Cooperativa|Las cuotas o aportes que los empleados<br>hagan a las cooperativas legalmente<br>constituidas|E<br>N|Deducciones|0-1|<sup>Valor Pagado correspondiente a</sup><br>Cooperativas por parte del trabajador|1.0<sup>/NominaIndividual/Deduc</sup><br>ciones/Cooperativa|
|NIE181||EmbargoFiscal|Los embargos ordenados por autoridad<br>judicial competente contra los empleados<br>deben ser descontados de la nómina por<br>la empresa y consignarlos en la cuenta<br>que el juez haya ordenado.|E<br>N|Deducciones|0-1|<sup>Valor Pagado correspondiente aEmbargos</sup><br>Fiscales por parte del trabajador|1.0<sup>/NominaIndividual/Deduc</sup><br>ciones/EmbargoFiscal|



Dirección de Gestión de Ingresos 

> Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 48 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_<br>_Campo_|_Descripción_|_T_<br>_F_<br>_T_|_am_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIE182|PlanComplementari<br>os|Valor de planes complementarios de<br>salud al que el trabajador se encuentran<br>afiliado, siempre que medie autorización<br>del empleado.|E<br>N|Deducciones|0-1|<sup>Valor Pagado correspondiente a Planes</sup><br>Complementarios por parte del trabajador|1.0<br>/NominaIndividual/Deduc<br>ciones/PlanComplementar<br>ios|
|NIE183|Educacion|Valor de servicios educativos  que el<br>trabajador autorice descuento.|E<br>N|Deducciones|0-1|<sup>Valor Pagado correspondiente a Conceptos</sup><br>Educativos por parte del trabajador|1.0<sup>/NominaIndividual/Deduc</sup><br>ciones/Educacion|
|NIE184|Reintegro|Valor que le regresa el trabajador a la<br>empresa por un devengo mal realizado en<br>otro pago de nómina|<br>E<br>N|Deducciones|0-1|<sup>Valor Pagado correspondiente a Reintegro</sup><br>por parte del trabajador|1.0<sup>/NominaIndividual/Deduc</sup><br>ciones/Reintegro|
|NIE185|Deuda|Valor que se deba pagar por las<br>obligaciones que el empleado tenga con<br>su empresa, como puede ser un crédito<br>que ésta le haya otorgado, o como<br>compensación por algún perjuicio o<br>detrimento económico que el empleado<br>le haya causado a la empresa.|E<br>N|Deducciones|0-1|<sup>Valor Pagado correspondiente a Deuda con</sup><br>la Empresa por parte del trabajador|1.0<sup>/NominaIndividual/Deduc</sup><br>ciones/Deuda|
|NIE186|Redondeo|Se utiliza para cuando se utilice el<br>Redondeo en el Documento|E<br>N|NominaIndividual|0-1|Definido en elnumeral 1.1.1|1.0<sup>/NominaIndividual/Redon</sup><br>deo|
|NIE187|DevengadosTotal|Valor total de la Suma de todos los<br>Devengados del Documento|E<br>N|NominaIndividual|1-1|<sup>Debe ir el valor Total de Todos los</sup><br>Devengados del Trabajador|1.0<sup>/NominaIndividual/Deven</sup><br>gadosTotal|
|NIE188|DeduccionesTotal|Valor total de la Suma de todas las<br>Deducciones del Documento|E<br>N|NominaIndividual|1-1|<sup>Debe ir el valor Total de Todos las</sup><br>Deducciones del Trabajador|1.0<sup>/NominaIndividual/Deduc</sup><br>cionesTotal|
|NIE189|ComprobanteTotal|Debe ir el total de: Devengados -<br>Deducciones|E<br>N|NominaIndividual|1-1|<sup>Debe ser la Diferencia entre</sup><br>DevengadosTotal - DeduccionesTotal|1.0<sup>/NominaIndividual/Compr</sup><br>obanteTotal|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 49 de 269 

**Resolución No. 000013** 





### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

### _3.2._ Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica: _NominaIndividualDeAjuste._ 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_T_|_am_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
||NominaIndividualDe<br>Ajuste|Nota de Ajuste de Documento Soporte de<br>Pago de Nómina Electrónica -<br>NominaIndividualDeAjuste (raíz)|||1-1||1.0<br>/NominaIndividualDeAjust<br>e|
|NIAE001 ext|UBLExtensions|Grupo correspondiente a la Firma Digital<br>del Documento (Signature)|G A|NominaIndividual<br>DeAjuste|1-1|Solamente puede haber una ocurrencia de<br>un grupo UBLExtensions conteniendo el<br>grupo ds:Signature. Ver definición en<br>numeral 3.6|1.0<sup>/NominaIndividualDeAjust</sup><br>e/ext:UBLExtensions|
|NIAE214|TipoNota|Corresponde al tipo de Nota de Ajuste de<br>Documento Soporte de Pago de Nómina<br>Electrónica que se desee implementar|E<br>N 1|<br>NominaIndividual<br>DeAjuste|1-1|Se debe colocar el Codigo de latabla 5.5.8|1.0<sup>/NominaIndividualDeAjust</sup><br>e/TipoNota|
||Reemplazar|Utilizado para todo el contenido<br>correspondiente al evento de Reemplazar<br>Documento|G<br>A|NominaIndividual<br>DeAjuste|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar|
||ReemplazandoPrede<br>cesor|Utilizado para Atributos de Documento<br>Predecesor a Reemplazar|E<br>A|Reemplazar|1-1|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Reemplaza<br>ndoPredecesor|
|NIAE190|NumeroPred|Debe corresponder al Numero de<br>Documento Soporte de Pago de Nómina<br>Electrónica a Reemplazar|A A|ReemplazandoPre<br>decesor|1-1|<sup>Debe ir el Numero de documento a</sup><br>Reemplazar|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Reemplaza<br>ndoPredecesor/@Numero<br>Pred|
|NIAE191|CUNEPred|Debe corresponder al CUNE del<br>Documento Soporte de Pago de Nómina<br>Electrónica a Reemplazar|A A|ReemplazandoPre<br>decesor|1-1|<sup>Debe ir el CUNE del documento a</sup><br>Reemplazar|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Reemplaza<br>ndoPredecesor/@CUNEPr<br>ed|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 50 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_T_|_am_|<br>_Padre_<br>|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|NIAE192|FechaGenPred|Debe corresponder a la Fecha de Emision<br>del Documento Soporte de Pago de<br>Nómina Electrónica a Reemplazar|A F<br>1|0|ReemplazandoPre<br>decesor<br>1|-1|<sup>Debe ir la fecha del documento a</sup><br>Reemplazar, en formato AAAA-MM-DD|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Reemplaza<br>ndoPredecesor/@FechaG<br>enPred|
||Periodo|Utilizado para Atributos del Periodo<br>Generación del Documento|E<br>A||Reemplazar<br>1|-1|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Periodo|
|NIAE002|FechaIngreso|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador o aprendiz presenta ingreso o<br>vinculación a la nómina del reportante.<br>(en caso de tener mas de un ingreso en el<br>mes, se debe reportar la primera fecha en<br>la que se presenta esta novedad en el<br>mes que se esta reportando).|<br> <br>A F<br>1|0|Periodo<br>1|-1|Se debe indicar la Fecha de Ingreso del<br>trabajador a la empresa, en formato AAAA-<br>MM-DD|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Periodo/@<br>FechaIngreso|
|NIAE003|FechaRetiro|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador o aprendiz presenta retiro de<br>la nómina del reportante.(en caso de<br>tener mas de un retiro en el mes, se debe<br>reportar la ultima fecha en la que se<br>presenta esta novedad en el mes que se<br>esta reportando).|<br>A F<br>1|0|Periodo<br>0|-1|Se debe indicar la Fecha de Retiro del<br>trabajador a la empresa, en formato AAAA-<br>MM-DD|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Periodo/@<br>FechaRetiro|
|NIAE004|FechaLiquidacionIni<br>cio|Fecha de inicio de Liquidación de Nómina|A F<br>1|0|Periodo<br>1|-1|Se debe indicar la Fecha de Inicio del<br>Periodo de Liquidación del documento, en<br>formato AAAA-MM-DD|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Periodo/@<br>FechaLiquidacionInicio|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

> www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 51 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_||_Tam_<br>_Padre_<br>_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIAE005|FechaLiquidacionFin|Fecha fin de Liquidación de Nómina|A F||10<br>Periodo<br>1-1|Se debe indicar la Fecha de Fin del Periodo<br>de Liquidación del documento, en formato<br>AAAA-MM-DD|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Periodo/@<br>FechaLiquidacionFin|
|NIAE006|TiempoLaborado|Cantidad de Tiempo que lleva laborando<br>el Trabajador en la empresa|A|A|<br>Periodo<br>1-1|<sup>Definido en elnumeral 8.4.1, debe ser</sup><br>mayor o gual a 1.|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Periodo/@<br>TiempoLaborado|
|NIAE008|FechaGen|Fecha de emisión: Fecha de emisión del<br>documento|A F||10<br>Periodo<br>1-1|Debe ir la fecha de emision del documento.<br>Considerando zona horaria de Colombia (-<br>5), en formato AAAA-MM-DD|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Periodo/@<br>FechaGen|
||NumeroSecuenciaX<br>ML|Utilizado para Atributos de Numero de<br>Secuencia del Documento XML|E<br>|A|Reemplazar<br>1-1|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/NumeroSec<br>uenciaXML|
|NIAE009|CodigoTrabajador|Codigo del Trabajador|A|A|<br>NumeroSecuencia<br>XML<br>0-1|<sup>Campo Opcional queda a manejo Interno</sup><br>del Empleador.|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/NumeroSec<br>uenciaXML/@CodigoTrab<br>ajador|
|NIAE010|Prefijo|Prefijo del documento, depende de las<br>sucursales que posea el Empleador|A|A|<br>NumeroSecuencia<br>XML<br>0-1|<sup>Debe corresponder a un Prefijo elegido por</sup><br>el Emisor del documento|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/NumeroSec<br>uenciaXML/@Prefijo|
|NIAE011|Consecutivo|Debe corresponder a un consecutivo<br>manejado por el Empleador|A|N|<br>NumeroSecuencia<br>XML<br>1-1|<sup>Debe corresponder a un Consecutivo</sup><br>elegido por el Emisor del documento|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/NumeroSec<br>uenciaXML/@Consecutivo|
|NIAE012|Numero|Debe corresponder al Prefijo y<br>consecutivo manejado por el Empleador|A|A|<br>NumeroSecuencia<br>XML<br>1-1|No se permiten caracteres adicionales como<br>espacios o guiones. Prefijo + Número<br>consecutivo del documento|<br>1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/NumeroSec<br>uenciaXML/@Numero|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 52 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>|_F_<br>_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
||LugarGeneracionXM<br>L|Utilizado para Atributos del Lugar de<br>Generacion del Documento XML|E<br>|A|Reemplazar|1-1|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/LugarGener<br>acionXML|
|NIAE013|Pais|Codigo del país donde se genera el<br>documento|A|A 2|LugarGeneracionX<br>ML|1-1|<sup>Se debe colocar el Codigo alfa-2 de latabla</sup><br>5.4.1|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/LugarGener<br>acionXML/@Pais|
|NIAE014|DepartamentoEstad<br>o|Código del departamento donde se<br>genera el documento|A|N 2|LugarGeneracionX<br>ML|1-1|Se debe colocar el Codigo de latabla 5.4.2|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/LugarGener<br>acionXML/@Departament<br>oEstado|
|NIAE015|MunicipioCiudad|Código del municipio o ciudad donde se<br>genera el documento|A|N 5|LugarGeneracionX<br>ML|1-1|Se debe colocar el Codigo de latabla 5.4.3|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/LugarGener<br>acionXML/@MunicipioCiu<br>dad|
|NIAE016|Idioma|Codigo del país donde se genera el<br>documento|A|A 2|LugarGeneracionX<br>ML|1-1|Se debe colocar el Codigo ISO 639-1 de la<br>tabla 5.3.1.Para Colombia se debe colocar<br>"es" (Español, Castellano)|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/LugarGener<br>acionXML/@Idioma|
||ProveedorXML|Utilizado para Atributos del Proveedor del<br>Documento XML|<br>E<br>|A|Reemplazar|1-1|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/ProveedorX<br>ML|
|NIAE205|RazonSocial|Debe corresponder al Nombre de la<br>Razón Social del Proveedor de Soluciones<br>Tecnológicas|A|A|ProveedorXML|0-1|<sup>Debe ir el Nombre o Razón Social del</sup><br>Proveedor de Soluciones Tecnológicas|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/ProveedorX<br>ML/@RazonSocial|
|NIAE206|PrimerApellido|Primer Apellido del Proveedor de<br>Soluciones Tecnológicas|A|A 60|ProveedorXML|0-1|<sup>Debe ir el Primer Apellido del Proveedor de</sup><br>Soluciones Tecnológicas|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/ProveedorX<br>ML/@PrimerApellido|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 53 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>|_F_<br>_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|NIAE207|SegundoApellido|Segundo Apellido del Proveedor de<br>Soluciones Tecnológicas|A|A 60|ProveedorXML|0-1|<sup>Debe ir el Segundo Apellido del Proveedor</sup><br>de Soluciones Tecnológicas|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/ProveedorX<br>ML/@SegundoApellido|
|NIAE208|PrimerNombre|Primer Nombre del Proveedor de<br>Soluciones Tecnológicas|A|A 60|ProveedorXML|0-1|<sup>Debe ir el Primer Nombre del Proveedor de</sup><br>Soluciones Tecnológicas|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/ProveedorX<br>ML/@PrimerNombre|
|NIAE209|OtrosNombres|Otros Nombres del Proveedor de<br>Soluciones Tecnológicas|A|A 60|ProveedorXML|0-1|<sup>Deben ir los Otros Nombres del Proveedor</sup><br>de Soluciones Tecnológicas|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/ProveedorX<br>ML/@OtrosNombres|
|NIAE017|NIT|Debe corresponder al NIT del Proveedor<br>de Soluciones Tecnologicas que realiza el<br>DE|A|N|ProveedorXML|1-1|Se debe colocar el NIT sin guiones ni DV de<br>la empresa dueña del Software que genera<br>el Documento, debe estar registrado en la<br>DIAN|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/ProveedorX<br>ML/@NIT|
|NIAE018|DV|Debe corresponder al DV del NIT del<br>Proveedor de Soluciones Tecnologicas<br>que realiza el DE|A|N 2|ProveedorXML|1-1|Se debe colocar el DV de la empresa dueña<br>del Software que genera el Documento,<br>debe estar registrado en la DIAN|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/ProveedorX<br>ML/@DV|
|NIAE019|SoftwareID|Identificador Software: Identificador del<br>software habilitado para la emisión de<br>nóminas|A|A|ProveedorXML|1-1|Identificador del software asignado cuando<br>el software se activa en el Sistema del<br>Documento Soporte de Pago de Nómina<br>Electrónica, debe corresponder a un<br>software autorizado para este Emisor|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/ProveedorX<br>ML/@SoftwareID|
|NIAE020|SoftwareSC|Huella del software que autorizó la DIAN<br>al Obligado a Generar Nómina Electrónica<br>o al Proveedor de Soluciones Tecnológicas|<br> <br>A|A|ProveedorXML|1-1|Definido en elnumeral 8.3|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/ProveedorX<br>ML/@SoftwareSC|



Dirección de Gestión de Ingresos 

> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Página 54 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_T_|_am_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIAE021|CodigoQR|Debe poseer información detallada del<br>Documento Electronico|E<br>A|NominaIndividual<br>DeAjuste|1-1|Debe  corresponder a la siguiente URL<br>“https://catalogo-<br>vpfe.dian.gov.co/document/searchqr?docu<br>mentkey=CUNE”  donde la palabra CUNE<br>debe ser reemplazada por el CUNE del<br>documento electrónico|1.0<sup>/NominaIndividualDeAjust</sup><br>e/Reemplazar/CodigoQR|
||InformacionGeneral|Utilizado para Atributos de Información<br>General Documento|E<br>A|Reemplazar|1-1|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Informacio<br>nGeneral|
|NIAE022|Version|Versión base de Schema XML usada para<br>crear este perfil<br>(NominaIndividualDeAjuste)|A A|InformacionGener<br>al|1-1|Debe ir el literal: "V1.0: Nota de Ajuste de<br>Documento Soporte de Pago de Nómina<br>Electrónica"|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Informacio<br>nGeneral/@Version|
|NIAE023|Ambiente|Tipo de Ambiente de Emision del<br>Documento: Habilitacion o Produccion|A N 1|<br>InformacionGener<br>al|1-1|Se debe colocar el Codigo de latabla 5.1.1|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Informacio<br>nGeneral/@Ambiente|
|NIAE202|TipoXML|Tipo de XML del Documento|A N 2|<br>InformacionGener<br>al|1-1|Se debe colocar el Codigo de latabla 5.5.7|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Informacio<br>nGeneral/@TipoXML|
|NIAE024|CUNE|CUNE:  Código Único de Documento<br>Soporte de Pago de Nómina Electrónica.<br>Elemento que verifica la integridad de la<br>información recibida|A A|InformacionGener<br>al|1-1|Definido en elnumeral 8.1|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Informacio<br>nGeneral/@CUNE|
|NIAE025|EncripCUNE|Identificador del esquema de<br>identificación. Algoritmo utilizado para el<br>cáculo del CUNE, SHA-384|A A 7|<br>InformacionGener<br>al|1-1|Debe ir la palabra "CUNE-SHA384"|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Informacio<br>nGeneral/@EncripCUNE|



Dirección de Gestión de Ingresos 

> Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 55 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>|_F_<br>_T_|_am_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|---|
|NIAE026|FechaGen|Fecha de emisión: Fecha de emisión del<br>documento|A|F<br>1|0|InformacionGener<br>al|1-1|Debe ir la fecha de emision del documento.<br>Considerando zona horaria de Colombia (-<br>5), en formato AAAA-MM-DD|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Informacio<br>nGeneral/@FechaGen|
|NIAE027|HoraGen|Hora de emisión: hora de emisión del<br>documento|A|H 1|4|InformacionGener<br>al|1-1|Debe ir la hora de emision del documento.<br>Considerando zona horaria de Colombia (-<br>5), en formato HH:MM:SSdhh:mm|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Informacio<br>nGeneral/@HoraGen|
|NIAE029|PeriodoNomina|Corresponde al Codigo de Periodo de<br>Nómina|A|N 1||InformacionGener<br>al|1-1|Se debe colocar el Codigo de latabla 5.5.1|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Informacio<br>nGeneral/@PeriodoNomi<br>na|
|NIAE030|TipoMoneda|Tipo de Moneda utilizada en el<br>documento|A|A 3||InformacionGener<br>al|1-1|<sup>Se debe colocar el Codigo de latabla 5.3.2.</sup><br>Para Colombia se debe colocar "COP"|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Informacio<br>nGeneral/@TipoMoneda|
|NIAE200|TRM|Tasa Representativa del mercado.<br>Corresponde a la tasa de cambio de la<br>moneda utilizada en el documento en el<br>Campo “TipoMoneda” a Pesos<br>Colombianos.|A|N||InformacionGener<br>al|0-1|Se debe colocar la tasa de cambio de la<br>moneda utilizada en el documento en el<br>Campo “TipoMoneda” a Pesos<br>Colombianos.|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Informacio<br>nGeneral/@TRM|
|NIAE031|Notas|Campo de libre uso para Observaciones<br>en el documento|E<br>|A||NominaIndividual<br>DeAjuste|0-N|<sup>Información adicional: Texto libre, relativo</sup><br>al documento|1.0<sup>/NominaIndividualDeAjust</sup><br>e/Reemplazar/Notas|
||Empleador|Utilizado para Atributos del Empleador o<br>Emisor del Documento|E<br>|A||Reemplazar|1-1|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Empleador|
|NIAE032|RazonSocial|Debe corresponder al Nombre de la<br>Razón Social del Empleador|A|A||Empleador|0-1|<sup>Debe ir el Nombre o Razón Social del</sup><br>Empleador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Empleador/<br>@RazonSocial|



Dirección de Gestión de Ingresos 

> Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

> www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 56 de 269 



**Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>|_F_|_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|---|
|NIAE210|PrimerApellido|Primer Apellido del Empleador|A|A|60|Empleador|0-1|Debe ir el Primer Apellido del Empleador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Empleador/<br>@PrimerApellido|
|NIAE211|SegundoApellido|Segundo Apellido del Empleador|A|A|60|Empleador|0-1|Debe ir el Segundo Apellido del Empleador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Empleador/<br>@SegundoApellido|
|NIAE212|PrimerNombre|Primer Nombre del Empleador|A|A|60|Empleador|0-1|Debe ir el Primer Nombre del Empleador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Empleador/<br>@PrimerNombre|
|NIAE213|OtrosNombres|Otros Nombres del Empleador|A|A|60|Empleador|0-1|Deben ir los Otros Nombres del Empleador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Empleador/<br>@OtrosNombres|
|NIAE033|NIT|Debe corresponder al NIT del Empleador<br>que realiza el DE|A|N||Empleador|1-1|<sup>Debe ir el NIT del Empleador sin guiones ni</sup><br>DV|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Empleador/<br>@NIT|
|NIAE034|DV|Debe corresponder al DV del NIT del<br>Empleador que realiza el DE|A|N|2|Empleador|1-1|Debe ir el DV del Empleador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Empleador/<br>@DV|
|NIAE035|Pais|Codigo del país donde donde se<br>encuentra ubicado el empleador el mes<br>que se esta reportando|A|A|2|Empleador|1-1|<sup>Se debe colocar el Codigo alfa-2 de latabla</sup><br>5.4.1|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Empleador/<br>@Pais|
|NIAE036|DepartamentoEstad<br>o|Código del departamento donde se<br>encuentra ubicado el empleador el mes<br>que se esta reportando|A|N|2|Empleador|1-1|Se debe colocar el Codigo de latabla 5.4.2|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Empleador/<br>@DepartamentoEstado|
|NIAE037|MunicipioCiudad|Código del municipio o ciudad donde se<br>encuentra ubicado el empleador el mes<br>que se esta reportando|A|N|5|Empleador|1-1|Se debe colocar el Codigo de latabla 5.4.3|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Empleador/<br>@MunicipioCiudad|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 57 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIAE038|Direccion|Debe corresponder a la dirección del<br>lugar físico de expedición del documento.|<sup>A A</sup>|Empleador|1-1|Debe ir la Dirección Fisica del Empleador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Empleador/<br>@Direccion|
||Trabajador|Utilizado para Atributos del Trabajador o<br>Receptor del Documento|E<br>A|Reemplazar|1-1|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador|
|NIAE041|TipoTrabajador|Código del tipo de trabajador del<br>Ministerio de salud. Aportes a Seguridad<br>Social de Activos.|A N 2|Trabajador|1-1|Corresponde a la clasificación de PILA para<br>conocer en que calidad se realizan las<br>cotizaciones a la seguridad social. Se debe<br>colocar el Codigo de latabla 5.5.3|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador<br>/@TipoTrabajador|
|NIAE042|SubTipoTrabajador|Código del Sub tipo de trabajador del<br>Ministerio de salud. Aportes a Seguridad<br>Social de Activos|A N 2|Trabajador|1-1|Corresponde a una sub clasificación de PILA<br>para conocer en que calidad se realizan las<br>cotizaciones a la seguridad social. Se debe<br>colocar el Codigo de latabla 5.5.4|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador<br>/@SubTipoTrabajador|
|NIAE043|AltoRiesgoPension|Si el trabajador desarrollo durante el<br>presente periodo alguna de las<br>actividades descritas en el Decreto 2090<br>de 2003, o la norma que lo modifique,<br>adicione o sustituya.|A B 4-5|Trabajador|1-1|Se debe colocar "true" o "false"|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador<br>/@AltoRiesgoPension|
|NIAE044|TipoDocumento|Tipo de documento de identificación que<br>actualmente tiene el trabajador, aprendiz<br>o pasante.|A N 2|Trabajador|1-1|Se debe colocar el Codigo de latabla 5.2.1|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador<br>/@TipoDocumento|
|NIAE045|NumeroDocumento|<sup>Numero de identificación que</sup><br>actualmente el trabajador o aprendiz|A N|Trabajador|1-1|<sup>Debe ir el Numero de documento del</sup><br>trabajador, sin puntos ni comas ni espacios|<sup>1.0</sup><br>/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador<br>/@NumeroDocumento|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 58 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>|_F_<br>_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|NIAE046|PrimerApellido|Primer Apellido del trabajador o aprendiz|A|A 60|Trabajador|1-1|Debe ir el Primer Apellido del trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador<br>/@PrimerApellido|
|NIAE047|SegundoApellido|Segundo Apellido del trabajador o<br>aprendiz|A|A 60|Trabajador|1-1|Debe ir el Segundo Apellido del trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador<br>/@SegundoApellido|
|NIAE048|PrimerNombre|Primer Nombre del trabajador o aprendiz|A|A 60|Trabajador|1-1|Debe ir el Primer Nombre del trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador<br>/@PrimerNombre|
|NIAE049|OtrosNombres|Otros Nombres del trabajador o aprendiz|A|A 60|Trabajador|0-1|Deben ir los Otros Nombres del trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador<br>/@OtrosNombres|
|NIAE050|LugarTrabajoPais|Código del país actual donde se<br>encontraba ubicado el trabajador o<br>aprendiz en el mes reportado.|A|N 3|Trabajador|1-1|<sup>Se debe colocar el Codigo alfa-2 de latabla</sup><br>5.4.1|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador<br>/@LugarTrabajoPais|
|NIAE051|LugarTrabajoDepart<br>amentoEstado|Código del departamento actual donde se<br>encontraba ubicado el trabajador o<br>aprendiz en el mes reportado.|<br>A|N 2|Trabajador|1-1|Se debe colocar el Codigo de latabla 5.4.2|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador<br>/@LugarTrabajoDepartam<br>entoEstado|
|NIAE052|LugarTrabajoMunici<br>pioCiudad|Código del municipio o ciudad actual<br>donde se encontraba ubicado el<br>trabajador o aprendiz en el mes<br>reportado.|A|N 5|Trabajador|1-1|Se debe colocar el Codigo de latabla 5.4.3|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador<br>/@LugarTrabajoMunicipio<br>Ciudad|
|NIAE053|LugarTrabajoDirecci<br>on|Debe corresponder a la dirección del<br>lugar físico donde vive el empleado.|A|A|Trabajador|1-1|Debe ir la Dirección Fisica del Trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador<br>/@LugarTrabajoDireccion|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 59 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIAE056|SalarioIntegral|Si el trabajador tiene un salario integral, el<br>cual es el tipo de remuneración que<br>incluye todos los conceptos que puedan<br>constituir salario en un solo monto o pago<br>(prestaciones sociales y recargos<br>nocturno, dominical y festivo, y el trabajo<br>extra) y que sea superior a 10 SMLMV<br>mas un 30% correspondiente a factor<br>prestacional.|<br> <br>A B 4-5|Trabajador|1-1|Se debe colocar "true" o "false"|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador<br>/@SalarioIntegral|
|NIAE061|TipoContrato|Tipo de Contrato que posee el empleado<br>con el Empleador|A N 1|Trabajador|1-1|Se debe colocar el Codigo de latabla 5.5.2|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador<br>/@TipoContrato|
|NIAE062|Sueldo|Corresponde al valor que el empleador<br>paga de forma periódica al trabajador<br>como contraprestación por el trabajo<br>realizado, este puede ser fijo o variable de<br>acuerdo a la unidad de tiempo en que las<br>partes hayan acordado el pago, teniendo<br>como base el día o la hora trabajada.|<br>A N|Trabajador|1-1|<sup>Se debe colocar el Sueldo Base que el</sup><br>Trabajdor tiene en la empresa|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador<br>/@Sueldo|
|NIAE063|CodigoTrabajador|Codigo del Trabajador|A A|Trabajador|0-1|<sup>Campo Opcional queda a manejo Interno</sup><br>del Empleador.|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador<br>/@CodigoTrabajador|
||Pago|Utilizado para Atributos del Pago del<br>Documento|E<br>A|Reemplazar|1-1|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Pago|
|NIAE064|Forma|Formas de Pago del Documento|A N 1|Pago|1-1|Se debe colocar el Codigo de latabla 5.3.3.1|<br>1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Pago/@For<br>ma|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 60 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_||_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|---|
|NIAE065|Metodo|Metodos de Pago del Documento|A|N|2|Pago|1-1|Se debe colocar el Codigo de latabla 5.3.3.2|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Pago/@Me<br>todo|
|NIAE066|Banco|Nombre de Entidad Bancaria del<br>Empleado donde se realiza la<br>consignación|A|A||Pago|0-1|Se debe colocar el nombre de la entidad<br>bancaria donde el trabajador tiene su<br>cuenta para pago de nómina. Si el Metodo<br>de Pago se realiza de forma Bancaria, este<br>campo es obligatorio.|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Pago/@Ba<br>nco|
|NIAE067|TipoCuenta|Tipo de Cuenta Bancaria del Empleado<br>donde se realiza la consignación|A|A||Pago|0-1|Se debe colocar el tipo de cuenta que el<br>trabajador tiene para pago de nómina. Si el<br>Metodo de Pago se realiza de forma<br>Bancaria, este campo es obligatorio.|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Pago/@Tip<br>oCuenta|
|NIAE068|NumeroCuenta|Numero de Cuenta Bancaria del<br>Empleado donde se realiza la<br>consignación|A|A||Pago|0-1|Se debe colocar el número de la cuenta que<br>el trabajador tiene para pago de nomina. Si<br>el Metodo de Pago se realiza de forma<br>Bancaria, este campo es obligatorio.|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Pago/@Nu<br>meroCuenta|
||FechasPagos|Utilizado para Todos los Elementos de<br>Fechas de Pagos del Documento|G<br>|A||Reemplazar|1-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/FechasPago<br>s|
|NIAE203|FechaPago|Fecha de Pago de la Nómina|E<br>F||10|FechasPagos|1-N|Debe ir la fecha de pago del documento.<br>Considerando zona horaria de Colombia (-<br>5), en formato AAAA-MM-DD|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/FechasPago<br>s/FechaPago|
||Devengados|Utilizado para Todos los Devengos del<br>Documento|G<br>|A||Reemplazar|1-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 61 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
||Basico|Utilizado para Atributos Basicos de<br>Devengos del Documento|E<br>A|Devengados|1-1|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Basico|
|NIAE069|DiasTrabajados|Número de días que el trabajador o<br>aprendiz efectivamente estuvo<br>ejecutando sus labores en la empresa.|A N 1-2|Basico|1-1|<sup>Cantidad de dias laborados durante el</sup><br>Periodo de Pago|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Basico/@DiasTrabajados|
|NIAE070|SueldoTrabajado|Corresponde al valor que el empleador<br>paga de forma periódica al trabajador<br>como contraprestación por el trabajo<br>realizado, este puede ser fijo o variable de<br>acuerdo a la unidad de tiempo en que las<br>partes hayan acordado el pago, teniendo<br>como base el día o la hora trabajada.|<br>A N|Basico|1-1|Valor Base o Sueldo del trabajador según lo<br>estipulado en su contrato. Corresponde al<br>Sueldo Trabajado por los días laborados.|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Basico/@SueldoTrabaja<br>do|
||Transporte|Utilizado para Atributos de Transporte de<br>Devengos del Documento|E<br>A|Devengados|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Transporte|
|NIAE071|AuxilioTransporte|Parte de los viáticos pagado al trabajador<br>correspondientes a medios de transporte<br>y/o los gastos de representación.|A N|Transporte|0-1|<sup>Valor de Auxilio de Transporte que recibe el</sup><br>trabajador por ley, según aplique|<br>1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Transporte/@AuxilioTra<br>nsporte|
|NIAE072|ViaticoManuAlojS|Parte de los viáticos pagado al trabajador<br>correspondientes a manutención y/o<br>alojamiento.|A N|Transporte|0-1|<sup>Valor de Viaticos, Manutención y</sup><br>Alojamiento de carácter Salarial|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Transporte/@ViaticoMa<br>nuAlojS|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 62 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIAE073|ViaticoManuAlojNS|Parte de los viáticos pagado al trabajador<br>correspondientes a manutención y/o<br>alojamiento No Salariales.|A N|Transporte|0-1|<sup>Valor de Viaticos, Manutención y</sup><br>Alojamiento de carácter No Salarial|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Transporte/@ViaticoMa<br>nuAlojNS|
||HEDs|Utilizado para Todos los Elementos de<br>Horas Extras Diarias de Devengos del<br>Documento|G<br>A|Devengados|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HEDs|
||HED|Utilizado para Atributos de Horas Extras<br>Diarias de Devengos del Documento|E<br>A|HEDs|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HEDs/HED|
|NIAE074|HoraInicio|Hora de inicio de Hora Extra Diurna|A H 19|HED|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HEDs/HED/@HoraInicio|
|NIAE075|HoraFin|Hora de fin de Hora Extra Diurna|A H 19|HED|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HEDs/HED/@HoraFin|
|NIAE076|Cantidad|Cantidad de Horas Extra Diurna|A N|HED|1-1|Cantidad de Horas|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HEDs/HED/@Cantidad|
|NIAE077|Porcentaje|Porcentaje al cual corresponde el calculo<br>de 1 hora Extra Diurna|A N 4-6|HED|1-1|<sup>Se debe colocar el Porcentaje que</sup><br>corresponda de latabla 5.5.5|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HEDs/HED/@Porcentaje|
|NIAE078|Pago|Es el valor pagado por el tiempo que se<br>trabaja adicional a la jornada legal o<br>pactada contractualmente.|A N|HED|1-1|Valor Pagado por las Horas|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HEDs/HED/@Pago|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 63 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
||HENs|Utilizado para Todos los Elementos de<br>Horas Extras Nocturnas de Devengos del<br>Documento|G<br>A|Devengados|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HENs|
||HEN|Utilizado para Atributos de Horas Extras<br>Nocturnas de Devengos del Documento|E<br>A|HENs|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HENs/HEN|
|NIAE079|HoraInicio|Hora de inicio de Hora Extra Nocturna|A H 19|HEN|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HENs/HEN/@HoraInicio|
|NIAE080|HoraFin|Hora de fin de Hora Extra Nocturna|A H 19|HEN|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HENs/HEN/@HoraFin|
|NIAE081|Cantidad|Cantidad de Horas Extras Nocturnas|A N|HEN|1-1|Cantidad de Horas|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HENs/HEN/@Cantidad|
|NIAE082|Porcentaje|Porcentaje al cual corresponde el calculo<br>de 1 hora Extra Nocturna|A N 4-6|HEN|1-1|<sup>Se debe colocar el Porcentaje que</sup><br>corresponda de latabla 5.5.5|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HENs/HEN/@Porcentaje|
|NIAE083|Pago|Es el valor pagado por el tiempo que se<br>trabaja adicional a la jornada legal o<br>pactada contractualmente.|A N|HEN|1-1|Valor Pagado por las Horas|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HENs/HEN/@Pago|
||HRNs|Utilizado para Todos los Elementos de<br>Horas Recargo Nocturno de Devengos del<br>Documento|G<br>A|Devengados|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRNs|
||HRN|Utilizado para Atributos de Horas Recargo<br>Nocturno de Devengos del Documento|E<br>A|HRNs|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRNs/HRN|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 64 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIAE084|HoraInicio|Hora de inicio de Hora Recargo Nocturno|A H 19|HRN|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRNs/HRN/@HoraInicio|
|NIAE085|HoraFin|Hora de fin de Hora Recargo Nocturno|A H 19|HRN|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRNs/HRN/@HoraFin|
|NIAE086|Cantidad|Cantidad de Horas Recargo Nocturno|A N|HRN|1-1|Cantidad de Horas|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRNs/HRN/@Cantidad|
|NIAE087|Porcentaje|Porcentaje al cual corresponde el calculo<br>de 1 hora Recargo Nocturno|A N 4-6|HRN|1-1|<sup>Se debe colocar el Porcentaje que</sup><br>corresponda de latabla 5.5.5|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRNs/HRN/@Porcentaje|
|NIAE088|Pago|Es el valor pagado por el tiempo que se<br>trabaja adicional a la jornada legal o<br>pactada contractualmente.|A N|HRN|1-1|Valor Pagado por las Horas|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRNs/HRN/@Pago|
||HEDDFs|Utilizado para Todos los Elementos de<br>Horas Extras Diarias Dominicales y<br>Festivas de Devengos del Documento|G<br>A|Devengados|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HEDDFs|
||HEDDF|Utilizado para Atributos de Horas Extras<br>Diarias Dominicales y Festivas de<br>Devengos del Documento|E<br>A|HEDDFs|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HEDDFs/HEDDF|
|NIAE089|HoraInicio|Hora de inicio de Horas Extras Diurnas<br>Dominical y Festivos|A H 19|HEDDF|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HEDDFs/HEDDF/@HoraI<br>nicio|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 65 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIAE090|HoraFin|Hora de fin de Horas Extras Diurnas<br>Dominical y Festivos|A H 19|HEDDF|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HEDDFs/HEDDF/@Hora<br>Fin|
|NIAE091|Cantidad|Cantidad de Horas Extras Diurnas<br>Dominical y Festivos|A N|HEDDF|1-1|Cantidad de Horas|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HEDDFs/HEDDF/@Canti<br>dad|
|NIAE092|Porcentaje|Porcentaje al cual corresponde el calculo<br>de 1 Hora Extra Diurna Dominical y<br>Festivo|A N 4-6|HEDDF|1-1|<sup>Se debe colocar el Porcentaje que</sup><br>corresponda de latabla 5.5.5|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HEDDFs/HEDDF/@Porce<br>ntaje|
|NIAE093|Pago|Es el valor pagado por el tiempo que se<br>trabaja adicional a la jornada legal o<br>pactada contractualmente.|A N|HEDDF|1-1|Valor Pagado por las Horas|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HEDDFs/HEDDF/@Pago|
||HRDDFs|Utilizado para Todos los Elementos de<br>Horas Recargo Diarias Dominicales y<br>Festivas de Devengos del Documento|G<br>A|Devengados|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRDDFs|
||HRDDF|Utilizado para Atributos de Horas Recargo<br>Diarias Dominicales y Festivas del<br>Documento|<br>E<br>A|HRDDFs|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRDDFs/HRDDF|
|NIAE094|HoraInicio|Hora de inicio de Horas Recargo Diurno<br>Dominical y Festivos|A H 19|HRDDF|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRDDFs/HRDDF/@HoraI<br>nicio|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 66 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIAE095|HoraFin|Hora de fin de Horas Recargo Diurno<br>Dominical y Festivos|A H 19|HRDDF|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRDDFs/HRDDF/@Hora<br>Fin|
|NIAE096|Cantidad|Cantidad de Horas Recargo Diurno<br>Dominical y Festivos|A N|HRDDF|1-1|Cantidad de Horas|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRDDFs/HRDDF/@Canti<br>dad|
|NIAE097|Porcentaje|Porcentaje al cual corresponde el calculo<br>de 1 Hora Recargo Diurno Dominical y<br>Festivos|A N 4-6|HRDDF|1-1|<sup>Se debe colocar el Porcentaje que</sup><br>corresponda de latabla 5.5.5|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRDDFs/HRDDF/@Porc<br>entaje|
|NIAE098|Pago|Es el valor pagado por el tiempo que se<br>trabaja adicional a la jornada legal o<br>pactada contractualmente.|A N|HRDDF|1-1|Valor Pagado por las Horas|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRDDFs/HRDDF/@Pago|
||HENDFs|Utilizado para Todos los Elementos de<br>Horas Extras Nocturnas Dominicales y<br>Festivas de Devengos del Documento|G<br>A|Devengados|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HENDFs|
||HENDF|Utilizado para Atributos de Horas Extras<br>Nocturnas Dominicales y Festivas del<br>Documento|E<br>A|HENDFs|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HENDFs/HENDF|
|NIAE099|HoraInicio|Hora de inicio de Horas Extras Nocturna<br>Dominical y Festivos|A H 19|HENDF|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HENDFs/HENDF/@HoraI<br>nicio|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 67 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIAE100|HoraFin|Hora de fin de Horas Extras Nocturna<br>Dominical y Festivos|A H 19|HENDF|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HENDFs/HENDF/@Hora<br>Fin|
|NIAE101|Cantidad|Cantidad de Horas Extras Nocturna<br>Dominical y Festivos|A N|HENDF|1-1|Cantidad de Horas|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HENDFs/HENDF/@Canti<br>dad|
|NIAE102|Porcentaje|Porcentaje al cual corresponde el calculo<br>de 1 Hora Extra Nocturna Dominical y<br>Festivos|A N 4-6|HENDF|1-1|<sup>Se debe colocar el Porcentaje que</sup><br>corresponda de latabla 5.5.5|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HENDFs/HENDF/@Porce<br>ntaje|
|NIAE103|Pago|Es el valor pagado por el tiempo que se<br>trabaja adicional a la jornada legal o<br>pactada contractualmente.|A N|HENDF|1-1|Valor Pagado por las Horas|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HENDFs/HENDF/@Pago|
||HRNDFs|Utilizado para Todos los Elementos de<br>Horas Recargo Nocturno Dominicales y<br>Festivas de Devengos del Documento|G<br>A|Devengados|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRNDFs|
||HRNDF|Utilizado para Atributos de Horas Recargo<br>Nocturno Dominicales y Festivas del<br>Documento|<br>E<br>A|HRNDFs|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRNDFs/HRNDF|
|NIAE104|HoraInicio|Hora de inicio de Horas Recargo Nocturno<br>Dominical y Festivos|<br>A H 19|HRNDF|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRNDFs/HRNDF/@HoraI<br>nicio|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 68 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_|_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|NIAE105|HoraFin|Hora de fin de Horas Recargo Nocturno<br>Dominical y Festivos|A H|19|HRNDF|0-1|En formato YYYY-MM-DDTHH:MM:SS|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRNDFs/HRNDF/@Hora<br>Fin|
|NIAE106|Cantidad|Cantidad de Horas Recargo Nocturno<br>Dominical y Festivos|A N||HRNDF|1-1|Cantidad de Horas|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRNDFs/HRNDF/@Canti<br>dad|
|NIAE107|Porcentaje|Porcentaje al cual corresponde el calculo<br>de 1 Hora Recargo Nocturno Dominical y<br>Festivos|A N|4-6|HRNDF|1-1|<sup>Se debe colocar el Porcentaje que</sup><br>corresponda de latabla 5.5.5|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRNDFs/HRNDF/@Porc<br>entaje|
|NIAE108|Pago|Es el valor pagado por el tiempo que se<br>trabaja adicional a la jornada legal o<br>pactada contractualmente.|A N||HRNDF|1-1|Valor Pagado por las Horas|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRNDFs/HRNDF/@Pago|
||Vacaciones|Utilizado para Todos los Elementos de<br>Vacaciones de Devengos del Documento|G<br>A||Devengados|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Vacaciones|
||VacacionesComu|nes<br>Utilizado para Atributos de Vacaciones<br>Comunes del Documento|E<br>A||Vacaciones|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Vacaciones/VacacionesC<br>omunes|
|NIAE109|FechaInicio|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador presenta el inicio del disfrute<br>de sus vacaciones en tiempo.|A F|10|VacacionesComun<br>es|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Vacaciones/VacacionesC<br>omunes/@FechaInicio|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 69 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_|_Tam_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIAE110|FechaFin|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador regresa o termina el disfrute<br>de sus vacaciones.|A F|10<br>VacacionesComun<br>es|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Vacaciones/VacacionesC<br>omunes/@FechaFin|
|NIAE111|Cantidad|Número de días que el trabajador estuvo<br>inactivo durante el mes por vacaciones.|A N|<br>VacacionesComun<br>es|1-1|Cantidad de Dias|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Vacaciones/VacacionesC<br>omunes/@Cantidad|
|NIAE112|Pago|Corresponde al valor pagado al<br>trabajador, por el descanso remunerado<br>que tiene derecho por haber trabajado un<br>determinado tiempo. (Vacaciones SI<br>disfrutadas)|<br>A N|<br>VacacionesComun<br>es|1-1|Valor Pagado por Vacaciones Si Disfrutadas|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Vacaciones/VacacionesC<br>omunes/@Pago|
||VacacionesCom<br>adas|pens<br>Utilizado para Atributos de Vacaciones<br>Compensadas del Documento|E<br>A|Vacaciones|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Vacaciones/VacacionesC<br>ompensadas|
|NIAE115|Cantidad|Número de días que el trabajador estuvo<br>activo durante el mes sin disfrutar sus<br>vacaciones. (Vacaciones NO disfrutadas)|A N|<br>VacacionesCompe<br>nsadas|1-1|Cantidad de Dias.|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Vacaciones/VacacionesC<br>ompensadas/@Cantidad|
|NIAE116|Pago|Corresponde al valor pagado al<br>trabajador, por el descanso remunerado<br>que no disfrutó y que tiene derecho por<br>haber trabajado un determinado tiempo.<br>(Vacaciones NO disfrutadas)|A N|<br>VacacionesCompe<br>nsadas|1-1|Valor Pagado por Vacaciones No Disfrutadas|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Vacaciones/VacacionesC<br>ompensadas/@Pago|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 70 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_T_|_am_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
||Primas|Utilizado para Atributos de Primas de<br>Devengos del Documento|E<br>A|Devengados|0-1|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Primas|
|NIAE117|Cantidad|Cantidad de dias trabajados para calculo<br>de Pago de Corte de Prima|A N|Primas|1-1|<sup>Cantidad de Dias a los cuales corresponde el</sup><br>pago de la Prima legal|<br>1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Primas/@Cantidad|
|NIAE118|Pago|Pagos por el reconocimiento del logro o<br>cumplimiento por parte del trabajador en<br>el desarrollo de sus labores, de<br>condiciones definidas expresamente<br>entre las partes.|A N|Primas|1-1|<sup>Valor Pagado por Prima Legal con respecto</sup><br>a Cantidad de Dias|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Primas/@Pago|
|NIAE119|PagoNS|Son valores pagados al trabajador de<br>forma ocasional y por mera liberalidad o<br>los pactados entre las partes de forma<br>expresa como pago no salarial.|A N|Primas|0-1|Valor Pagado por Prima No Salarial|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Primas/@PagoNS|
||Cesantias|Utilizado para Atributos de Cesantias de<br>Devengos del Documento|E<br>A|Devengados|0-1|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Cesantias|
|NIAE120|Pago|Pago de la Cesantia otorgada por Ley.|A N|Cesantias|1-1|Valor Pagado por Cesantias|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Cesantias/@Pago|
|NIAE121|Porcentaje|Porcentaje que corresponde al Interes de<br>Cesantia de Ley|A N|Cesantias|1-1|Porcentaje de Interes de Cesantias|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Cesantias/@Porcentaje|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 71 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_||_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|---|
|NIAE122|PagoIntereses|Pago de los Intereses de Cesantia<br>otorgada por Ley.|A|N||Cesantias|1-1|Valor Pagado por Intereses de Cesantias|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Cesantias/@PagoInteres<br>es|
||Incapacidades|Utilizado para Todos los Elementos de<br>Incapacidades de Devengos del<br>Documento|G<br>|A||Devengados|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Incapacidades|
||Incapacidad|Utilizado para Atributos de Incapacidad<br>del Documento|E<br>|A||Incapacidades|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Incapacidades/Incapacid<br>ad|
|NIAE123|FechaInicio|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador presenta o da por iniciada su<br>Incapacidad.|A F||10|Incapacidad|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Incapacidades/Incapacid<br>ad/@FechaInicio|
|NIAE124|FechaFin|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador presenta o da por terminada<br>su Incapacidad.|A F||10|Incapacidad|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Incapacidades/Incapacid<br>ad/@FechaFin|
|NIAE125|Cantidad|Número de días que el trabajador o<br>aprendiz estuvo inactivo por incapacidad<br>(sin importar su origen).|A|N||Incapacidad|1-1|Cantidad de Dias|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Incapacidades/Incapacid<br>ad/@Cantidad|
|NIAE126|Tipo|Se debe indicar el codigo al cual<br>corresponda el tipo de incapacidad del<br>Empleado|A|N|1|Incapacidad|1-1|<sup>Se debe colocar el Codigo que corresponda</sup><br>de latabla 5.5.6|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Incapacidades/Incapacid<br>ad/@Tipo|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 72 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_|_Ta_|_m_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|NIAE127|Pago|Valor de la prestación económica pagada<br>al trabajador por consecuencia de la falta<br>de capacidad laboral sin importar su<br>origen.|A N||Incapacidad|1-1|<sup>Valor Pagado por Incapacidad con respecto</sup><br>a Cantidad de Dias|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Incapacidades/Incapacid<br>ad/@Pago|
||Licencias|Utilizado para Todos los Elementos de<br>Licencias de Devengos del Documento|G<br>A||Devengados|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias|
||LicenciaMP|Utilizado para Atributos de Licencia de<br>Materinidad o Paternidad del Documento|E<br>A||Licencias|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaMP|
|NIAE128|FechaInicio|Fecha donde da inicio la Licencia de<br>Maternidad o Paternidad|A F|10|<br>LicenciaMP|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaMP/@<br>FechaInicio|
|NIAE129|FechaFin|Fecha donde termina la Licencia de<br>Maternidad o Paternidad|A F|10|<br>LicenciaMP|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaMP/@<br>FechaFin|
|NIAE130|Cantidad|Número de días que el trabajador o<br>aprendiz efectivamente estuvo inactivo<br>por licencia de maternidad o paternidad.|A N||LicenciaMP|1-1|Cantidad de Dias|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaMP/@<br>Cantidad|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 73 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_|<br>_T_|_am_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|---|
|NIAE131|Pago|Valor pagado al trabajador del descanso<br>remunerado que la ley confiere por el<br>nacimiento de un hijo, y que es<br>reconocido y pagado por la EPS a la que<br>está afiliado el padre o la madre, o en su<br>defecto por el empleador.|A|N||LicenciaMP|1-1|<sup>Valor Pagado por Licencia de Maternidad o</sup><br>Paternidad con respecto a Cantidad de Dias|<sup>1.0</sup><br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaMP/@<br>Pago|
||LicenciaR|Utilizado para Atributos de Licencia<br>Remunerada del Documento|E<br>|A||Licencias|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaR|
|NIAE132|FechaInicio|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador o aprendiz inicia algún permiso<br>o licencia remunerada.|<br>A F|<br>1|0|LicenciaR|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaR/@Fe<br>chaInicio|
|NIAE133|FechaFin|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador o aprendiz termina el permiso<br>o licencia remunerada.|A F|<br>1|0|LicenciaR|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaR/@Fe<br>chaFin|
|NIAE134|Cantidad|Número de días que el trabajador o<br>aprendiz efectivamente estuvo inactivo<br>por permiso o licencia pero que le fueron<br>reconocidos en su pago.|A|N||LicenciaR|1-1|Cantidad de Dias|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaR/@Ca<br>ntidad|
|NIAE135|Pago|Valor pagado al trabajador corresponde a<br>tiempo no laborado, que por ley o por<br>acuerdo con el empleador se le concede|<br>A|N||LicenciaR|1-1|<sup>Valor Pagado por Licencia Remunerada con</sup><br>respecto a Cantidad de Dias|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaR/@Pa<br>go|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

> www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 74 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_T_|_am_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
||LicenciaNR|Utilizado para Atributos de Licencia No<br>Remunerada del Documento|E<br>A||Licencias|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaNR|
|NIAE136|FechaInicio|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador o aprendiz inicia alguna<br>suspensión, permiso o licencia NO<br>remunerada.|A F<br>1|0|LicenciaNR|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaNR/@<br>FechaInicio|
|NIAE137|FechaFin|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador o aprendiz termina la<br>suspensión, permiso o licencia NO<br>remunerada.|A F<br>1|0|LicenciaNR|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaNR/@<br>FechaFin|
|NIAE138|Cantidad|Número de días que el trabajador o<br>aprendiz efectivamente estuvo inactivo<br>por suspensión, permiso o licencia y que<br>NO le fueron reconocidos en su pago.|A N||LicenciaNR|1-1|Cantidad de Dias|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaNR/@<br>Cantidad|
||Bonificaciones|Utilizado para Todos los Elementos de<br>Bonificaciones de Devengos del<br>Documento|G<br>A||Devengados|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Bonificaciones|
||Bonificacion|Utilizado para Atributos de Bonificacion<br>del Documento|E<br>A||Bonificaciones|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Bonificaciones/Bonificac<br>ion|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 75 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_T_|_am_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIAE139|BonificacionS|Son valores pagados al trabajador en<br>forma de incentivo o recompensa por la<br>contraprestación directa del servicio.|A N|Bonificacion|0-1|Valor Pagado por Bonificación Salarial|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Bonificaciones/Bonificac<br>ion/@BonificacionS|
|NIAE140|BonificacionNS|Son valores de incentivos pagados al<br>trabajador de forma ocasional y por mera<br>liberalidad o los pactados entre las partes<br>de forma expresa como pago no salarial.|A N|Bonificacion|0-1|Valor Pagado por Bonificación No Salarial|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Bonificaciones/Bonificac<br>ion/@BonificacionNS|
||Auxilios|Utilizado para Todos los Elementos de<br>Auxilios de Devengos del Documento|G<br>A|Devengados|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Auxilios|
||Auxilio|Utilizado para Atributos de Auxilio del<br>Documento|E<br>A|Auxilios|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Auxilios/Auxilio|
|NIAE141|AuxilioS|Son beneficios, ayudas o apoyos<br>económicos, pagados al trabajador de<br>forma habitual o pactados entre las<br>partes como factor salarial.|A N|Auxilio|0-1|Valor Pagado por Auxilios Salariales|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Auxilios/Auxilio/@Auxili<br>oS|
|NIAE142|AuxilioNS|Son beneficios, ayudas o apoyos<br>económicos, pagados al trabajador de<br>forma ocasional y por mera liberalidad o<br>los pactados entre las partes de forma<br>expresa como pago no salarial.|A N|Auxilio|0-1|Valor Pagado por Auxilios No Salariales|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Auxilios/Auxilio/@Auxili<br>oNS|
||HuelgasLegales|Utilizado para Todos los Elementos de<br>Huelgas Legales de Devengos del<br>Documento|G<br>A|Devengados|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HuelgasLegales|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

> www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 76 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_T_|_am_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
||HuelgaLegal|Utilizado para Atributos de Huelga Legal<br>del Documento|E<br>A||HuelgasLegales|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HuelgasLegales/HuelgaL<br>egal|
|NIAE143|FechaInicio|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador inicia la huelga legalmente<br>declarada.|A F<br>1|0|HuelgaLegal|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HuelgasLegales/HuelgaL<br>egal/@FechaInicio|
|NIAE144|FechaFIn|Este dato se debe diligenciar solamente<br>en el registro del mes en que el<br>trabajador termina la huelga legalmente<br>declarada.|A F<br>1|0|HuelgaLegal|0-1|En formato AAAA-MM-DD|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HuelgasLegales/HuelgaL<br>egal/@FechaFIn|
|NIAE145|Cantidad|número de días en los que el trabajador<br>estuvo inactivo por huelga legalmente<br>declarada.|A N||HuelgaLegal|1-1|Cantidad de Dias|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HuelgasLegales/HuelgaL<br>egal/@Cantidad|
||OtrosConceptos|Utilizado para Todos los Elementos de<br>Otros Conceptos de Devengos del<br>Documento|G<br>A||Devengados|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/OtrosConceptos|
||OtroConcepto|Utilizado para Atributos de Otro Concepto<br>del Documento|<br>E<br>A||OtrosConceptos|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/OtrosConceptos/OtroCo<br>ncepto|



> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Página 77 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>|_Tam_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIAE146|DescripcionConcept<br>o|Nombre del Concepto que corresponde a<br>los demás pagos fijos o variables<br>realizados al trabajador que remuneren<br>en dinero o en especie como<br>contraprestación directa del servicio, sea<br>cualquiera la forma o denominación que<br>se adopte.|A A|<br>OtroConcepto|1-1|Debe ir la Descripcion del Concepto|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/OtroConceptos/OtroCon<br>cepto/@DescripcionConc<br>epto|
|NIAE147|ConceptoS|Valor de los demás pagos fijos o variables<br>realizados al trabajador que remuneren<br>en dinero o en especie como<br>contraprestación directa del servicio, sea<br>cualquiera la forma o denominación que<br>se adopte (Salarial).|A N|<br>OtroConcepto|0-1|Valor Pagado por Conceptos Salariales|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/OtroConceptos/OtroCon<br>cepto/@ConceptoS|
|NIAE148|ConceptoNS|Valor de los demás pagos que<br>ocasionalmente y por mera liberalidad<br>recibe el trabajador del empleador, en<br>dinero o en especie no para su beneficio,<br>ni para enriquecer su patrimonio, sino<br>para desempeñar a cabalidad sus<br>funciones (No Salarial).|A N|<br>OtroConcepto|0-1|Valor Pagado por Conceptos No Salariales|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/OtroConceptos/OtroCon<br>cepto/@ConceptoNS|
||Compensaciones|Utilizado para Todos los Elementos de<br>Compensaciones de Devengos del<br>Documento|G<br>A|Devengados|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Compensaciones|
||Compensacion|Utilizado para Atributos de Compensacion<br>del Documento|<br>E<br>A|Compensaciones|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Compensaciones/Comp<br>ensacion|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 78 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>|_Tam_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIAE149|CompensacionO|Suma de dinero definido en el régimen de<br>compensaciones como retribución<br>mensual recibido por el asociado por la<br>ejecución de su actividad material o<br>inmaterial, la cual se fija teniendo en<br>cuenta el tipo de labor desempeñada, el<br>rendimiento o la productividad y la<br>cantidad de trabajo aportado. El monto<br>de la compensación ordinaria podrá ser<br>una suma básica igual para todos los<br>asociados (Ordinaria).|A N|<br>Compensacion|1-1|<sup>Valor Pagado por Compensaciones</sup><br>Ordinarias|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Compensaciones/Comp<br>ensacion/@Compensacio<br>nO|
|NIAE150|CompensacionE|Los demás pagos adicionales a la<br>Compensación Ordinaria que recibe el<br>asociado como retribución por su trabajo,<br>definidos en el régimen de<br>compensaciones (Extraordinaria).|A N|<br>Compensacion|1-1|<sup>Valor Pagado por Compensaciones</sup><br>Extraordinarias|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Compensaciones/Comp<br>ensacion/@Compensacio<br>nE|
||BonoEPCTVs|Utilizado para Todos los Elementos de<br>Bonos Electronicos o de Papel de Servicio,<br>Cheques, Tarjetas, Vales, etc de Devengos<br>del Documento|G<br>A|Devengados|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/BonoEPCTVs|
||BonoEPCTV|Utilizado para Atributos de Bono<br>Electronico o de Papel de Servicio,<br>Cheque, Tarjeta, Vale, etc del Documento|E<br>A|BonoEPCTVs|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/BonoEPCTVs/BonoEPCT<br>V|



> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Página 79 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_Tam_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|
|NIAE151|PagoS|Valor que el trabajador recibe como<br>contraprestación por el trabajo realizado,<br>por medio de bonos electrónicos,<br>recargas, cheques, vales. es decir, todo<br>pago realizado en un medio diferente a<br>dinero en efectivo o consignación de<br>cuenta bancaria (Salarial).|A N<br>BonoEPCTV|0-1|Concepto Salarial|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/BonoEPCTVs/BonoEPCT<br>V/@PagoS|
|NIAE152|PagoNS|Valor que el trabajador recibe como<br>concepto no salarial, por medio de bonos<br>electrónicos, recargas, cheques, vales. es<br>decir, todo pago realizado en un medio<br>diferente a dinero en efectivo o<br>consignación de cuenta bancaria (No<br>Salarial).|A N<br>BonoEPCTV|0-1|Concepto No Salarial|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/BonoEPCTVs/BonoEPCT<br>V/@PagoNS|
|NIAE153|PagoAlimentacionS|Valor que el trabajador recibe como<br>concepto no salarial, por medio de bonos<br>electrónicos, recargas, cheques, vales. es<br>decir, todo pago realizado en un medio<br>diferente a dinero en efectivo o<br>consignación de cuenta bancaria (Para<br>Alimentación Salarial).|A N<br>BonoEPCTV|0-1|Concepto Salarial|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/BonoEPCTVs/BonoEPCT<br>V/@PagoAlimentacionS|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 80 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>|_Tam_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIAE154|PagoAlimentacionN<br>S|Valor que el trabajador recibe como<br>concepto no salarial, por medio de bonos<br>electrónicos, recargas, cheques, vales. es<br>decir, todo pago realizado en un medio<br>diferente a dinero en efectivo o<br>consignación de cuenta bancaria (Para<br>Alimentación No Salarial).|A N|BonoEPCTV|0-1|Concepto No Salarial|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/BonoEPCTVs/BonoEPCT<br>V/@PagoAlimentacionNS|
||Comisiones|Utilizado para Todos los Elementos de<br>Comisiones de Devengos del Documento|G<br>A|Devengados|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Comisiones|
|NIAE155|Comision|Valor pagado al trabajador usualmente<br>del área comercial, y de forma regular se<br>liquida con un porcentaje sobre el<br>importe de una operación, también se<br>presenta como incentivo por el logro de<br>objetivos.|E<br>N|Comisiones|0-N|Valor Pagado por Comision|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Comisiones/Comision|
||PagosTerceros|Utilizado para Todos los Elementos de<br>Pagos a Tercero de Devengos del<br>Documento|G<br>A|Devengados|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/PagosTerceros|
|NIAE193|PagoTercero|Beneficios en cabeza del Trabjador que se<br>pagan a un proveedor o tercero.|E<br>N|PagosTerceros|0-N|Valor Pagado por Pago Tercero|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/PagosTerceros/PagoTerc<br>ero|
||Anticipos|Utilizado para Todos los Elementos de<br>Anticipos de Devengos del Documento|G<br>A|Devengados|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Anticipos|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

> www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 81 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_T_|_am_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIAE194|Anticipo|Anticipos de Nomina.|E<br>N|Anticipos|0-N|Valor Pagado por Anticipo|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Anticipos/Anticipo|
|NIAE156|Dotacion|De conformidad con lo previsto en el<br>artículo 230 del Código Sustantivo del<br>Trabajo, o la norma que lo modifique,<br>adicione o sustituya, corresponde al valor<br>que el empleador dispone para<br>suministrar la dotación de sus<br>trabajadores.|E<br>N|Devengados|0-1|Valor Pagado por Dotación|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Dotacion|
|NIAE157|ApoyoSost|Corresponde al valor no salarial que el<br>patrocinador paga de forma mensual<br>como ayuda o apoyo economía al<br>aprendiz o practicante universitario<br>durante su etapa lectiva y fase practica.|E<br>N|Devengados|0-1|Valor Pagado por Apoyo a Sostenimiento|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/ApoyoSost|
|NIAE158|Teletrabajo|Valor que debe ser pagado al trabajador<br>cuyo contrato indica expresamente que<br>puede laborar mediante teletrabajo|E<br>N|Devengados|0-1|Valor Pagado por trabajo en Teletrabajo|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Teletrabajo|
|NIAE159|BonifRetiro|Valor establecido por mutuo acuerdo por<br>retiro del Trabajador|E<br>N|Devengados|0-1|Valor Pagado por Retiro de la empresa|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/BonifRetiro|
|NIAE160|Indemnizacion|Valor de Indemnizacion establecido por<br>ley|E<br>N|Devengados|0-1|Valor Pagado por Indemnización|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Indemnizacion|
|NIAE201|Reintegro|Valor que le regresa la empresa al<br>trabajador por una deducción mal<br>realizada en otro pago de nomina|E<br>N|Devengados|0-1|<sup>Valor Pagado correspondiente a Reintegro</sup><br>por parte del empleador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Reintegro|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 82 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
||Deducciones|Utilizado para Todas las Deducciones del<br>Documento|G<br>A|Reemplazar|1-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es|
||Salud|Utilizado para Atributos de Salud del<br>Documento|E<br>A|Deducciones|1-1|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/Salud|
|NIAE161|Porcentaje|Debe corresponder al porcentaje de<br>deducción de salud que paga el<br>trabajador|A N 4-6|Salud|1-1|<sup>Se debe colocar el Porcentaje que</sup><br>corresponda|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/Salud/@Porcentaje|
|NIAE163|Deduccion|El trabajador debe estar afiliado al<br>sistema de salud. La cotización por salud<br>que corresponde al 12.5% de la base del<br>aporte, se hace en conjunto con la<br>empresa. Ésta última aporta el 8.5%, y el<br>empleado debe aportar el 4% restante.<br>Ese 4% es el valor que se debe descontar<br>(deducir) del total devengado a cargo del<br>empleado.|A N|Salud|1-1|<sup>Valor Pagado correspondiente a Salud por</sup><br>parte del trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/Salud/@Deduccion|
||FondoPension|Utilizado para Atributos de Fondos de<br>Pension del Documento|E<br>A|Deducciones|1-1|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/FondoPension|
|NIAE164|Porcentaje|Debe corresponder al porcentaje de<br>deducción de fondo de pension que paga<br>el trabajador|A N 4-6|FondoPension|1-1|<sup>Se debe colocar el Porcentaje que</sup><br>corresponda|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/FondoPension/@Porce<br>ntaje|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 83 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIAE166|Deduccion|El trabajador también debe estar afiliado<br>al sistema de pensiones. La cotización por<br>pensión está a cargo tanto de la empresa<br>como del empleado. Del total del aporte<br>(16%), la empresa aporta el 75% (12%) y<br>el trabajador aporta el restante 25% (4%).<br>Como el trabajador debe aportar un 4%<br>por concepto de pensión, este valor se le<br>descuenta (deduce) del valor devengado<br>en el respectivo periodo (mes o<br>quincena).|<br> <br>A N|FondoPension|1-1|<sup>Valor Pagado correspondiente a Pension</sup><br>por parte del trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/FondoPension/@Dedu<br>ccion|
||FondoSP|Utilizado para Atributos de Fondo de<br>Seguridad Pensional del Documento|E<br>A|Deducciones|0-1|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/FondoSP|
|NIAE167|Porcentaje|Debe corresponder al porcentaje de<br>deducción de fondo de seguridad<br>pensional que paga el trabajador|A N 4-6|FondoSP|0-1|<sup>Se debe colocar el Porcentaje que</sup><br>corresponda|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/FondoSP/@Porcentaje|
|NIAE168|DeduccionSP|Todo trabajador que devengue un sueldo<br>que sea igual o superior a 4 salarios<br>mininos, debe aportar un 1% al Fondo de<br>solidaridad pensional.|A N|FondoSP|0-1|Valor Pagado correspondiente a Fondo de<br>Solidaridad Pensional por parte del<br>trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/FondoSP/@Deduccion<br>SP|
|NIAE169|PorcentajeSub|Se debe colocar el Porcentaje que<br>correspondiente al Fondo de Subsistencia<br>correspondiente|<br>A N 4-6|FondoSP|0-1|Se debe colocar el Porcentaje que<br>correspondiente al Fondo de Subsistencia<br>correspondiente|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/FondoSP/@Porcentaje<br>Sub|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

> www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 84 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>|_Tam_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIAE170|DeduccionSub|Valor Pagado correspondiente a Fondo de<br>Subsistencia por parte del trabajador|A N|FondoSP|0-1|<sup>Valor Pagado correspondiente a Fondo de</sup><br>Subsistencia por parte del trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/FondoSP/@Deduccion<br>Sub|
||Sindicatos|Utilizado para Todos los Elementos de<br>Sindicatos de Deducciones del<br>Documento|G<br>A|Deducciones|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/Sindicatos|
||Sindicato|Utilizado para Atributos de Sindicato del<br>Documento|E<br>A|Sindicatos|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/Sindicatos/Sindicato|
|NIAE171|Porcentaje|Porcentaje establecido en la ley o por<br>estatutos del sindicato.|A N|Sindicato|1-1|Se debe colocar el Porcentaje que<br>correspondiente a Aportes del Sindicato<br>correspondiente|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/Sindicatos/Sindicato/@<br>Porcentaje|
|NIAE172|Deduccion|Las cuotas que los trabajadores<br>sindicalizados deben aportar al sindicato<br>al que estén afiliados, y siempre que<br>medie autorización del empleado.|A N|Sindicato|1-1|<sup>Valor Pagado correspondiente a Aportes del</sup><br>Sindicato por parte del trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/Sindicatos/Sindicato/@<br>Deduccion|
||Sanciones|Utilizado para Todos los Elementos de<br>Sanciones de Deducciones del<br>Documento|G<br>A|Deducciones|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/Sanciones|
||Sancion|Utilizado para Atributos de Sancion del<br>Documento|E<br>A|Sanciones|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/Sanciones/Sancion|



> Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 85 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_T_|_am_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIAE173|SancionPublic|Valor por el del incumplimiento de una<br>regla o norma de conducta obligatoria<br>(Publica)|A N|Sancion|1-1|<sup>Valor Pagado correspondiente a Sanción</sup><br>Pública por parte del trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/Sanciones/Sancion/@S<br>ancionPublic|
|NIAE174|SancionPriv|Valor por el del incumplimiento de una<br>regla o norma de conducta obligatoria<br>(Privada o Ordinaria)|A N|Sancion|1-1|<sup>Valor Pagado correspondiente a Sanción</sup><br>Privada por parte del trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/Sanciones/Sancion/@S<br>ancionPriv|
||Libranzas|Utilizado para Todos los Elementos de<br>Libranzas de Deducciones del Documento|G<br>A|Deducciones|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/Libranzas|
||Libranza|Utilizado para Atributos de Libranza del<br>Documento|E<br>A|Libranzas|0-N|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/Libranzas/Libranza|
|NIAE175|Descripcion|Nombre de la Libranza que corresponda a<br>las cuotas que el empleado deba pagar a<br>una entidad financiera, para la<br>amortización de un crédito que le haya<br>sido otorgado por libranza|A A|Libranza|1-1|Debe ir la Descripcion de la Libranza|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/Libranzas/Libranza/@D<br>escripcion|
|NIAE176|Deduccion|Las cuotas que el empleado deba pagar a<br>una entidad financiera, para la<br>amortización de un crédito que le haya<br>sido otorgado por libranza|A N|Libranza|1-1|Valor Pagado correspondiente a Aportes a<br>Entidades Financieras por parte del<br>trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/Libranzas/Libranza/@D<br>educcion|
||PagosTerceros|Utilizado para Todos los Elementos de<br>Pagos a Tercero de Deducciones del<br>Documento|G<br>A|Deducciones|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/PagosTerceros|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 86 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_|_Tam_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIAE195|PagoTercero|Deducciones en cabeza del Trabjador que<br>se pagan a un proveedor o tercero.|E<br>N|<br>PagosTerceros|0-N|Valor Pagado por Pago Tercero|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/PagosTerceros/PagoTe<br>rcero|
||Anticipos|Utilizado para Todos los Elementos de<br>Anticipos de Deducciones del Documento|G<br>A|Deducciones|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/Anticipos|
|NIAE196|Anticipo|Deduccion por Anticipos de Nómina.|E<br>N|<br>Anticipos|0-N|Valor Pagado por Anticipo|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/Anticipos/Anticipo|
||OtrasDeducciones|Utilizado para Todos los Elementos de<br>Otras Deducciones del Documento|G<br>A|Deducciones|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/OtrasDeducciones|
|NIAE197|OtraDeduccion|Otro tipo de deducción dentro de la<br>Nómina.|E<br>N|<br>OtrasDeduccione|s 0-N|Valor Pagado por Otra Deducción|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/OtrasDeducciones/Otr<br>aDeduccion|
|NIAE198|PensionVoluntaria|Valor correspondiente al ahorro que hace<br>el trabajador para complementar su<br>pension obligatoria o cumplir metas<br>especificas.|E<br>N|<br>Deducciones|0-1|Valor Pagado correspondiente al ahorro que<br>hace el trabajador para complementar su<br>pension obligatoria o cumplir metas<br>especificas.|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/PensionVoluntaria|



> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Página 87 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_T_|_am_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIAE177|RetencionFuente|Si hubiere lugar, la empresa deberá<br>calcular y retener al empleado el valor<br>correspondiente a retención en la fuente<br>por ingresos laborales. Este valor será<br>declarado y consignado en la respectiva<br>declaración mensual de retención en la<br>fuente.|E<br>N|Deducciones|0-1|<sup>Valor Pagado correspondiente a Retención</sup><br>en la Fuente por parte del trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/RetencionFuente|
|NIAE179|AFC|Corresponde a (Ahorro Fomento a la<br>contruccion)|E<br>N|Deducciones|0-1|<sup>Valor Pagado correspondiente a AFC por</sup><br>parte del trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/AFC|
|NIAE180|Cooperativa|Las cuotas o aportes que los empleados<br>hagan a las cooperativas legalmente<br>constituidas|E<br>N|Deducciones|0-1|<sup>Valor Pagado correspondiente a</sup><br>Cooperativas por parte del trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/Cooperativa|
|NIAE181|EmbargoFiscal|Los embargos ordenados por autoridad<br>judicial competente contra los empleados<br>deben ser descontados de la nómina por<br>la empresa y consignarlos en la cuenta<br>que el juez haya ordenado.|<br>E<br>N|Deducciones|0-1|<sup>Valor Pagado correspondiente a Embargos</sup><br>Fiscales por parte del trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/EmbargoFiscal|
|NIAE182|PlanComplementari<br>os|Valor de planes complementarios de<br>salud al que el trabajador se encuentran<br>afiliado, siempre que medie autorización<br>del empleado.|E<br>N|Deducciones|0-1|<sup>Valor Pagado correspondiente a Planes</sup><br>Complementarios por parte del trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/PlanComplementarios|
|NIAE183|Educacion|Valor de servicios educativos  que el<br>trabajador autorice descuento.|E<br>N|Deducciones|0-1|<sup>Valor Pagado correspondiente a Conceptos</sup><br>Educativos por parte del trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/Educacion|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

> www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 88 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_T_|_am_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIAE184|Reintegro|Valor que le regresa el trabajador a la<br>empresa por un devengo mal realizado en<br>otro pago de nómina|<br>E<br>N|Deducciones|0-1|<sup>Valor Pagado correspondiente a Reintegro</sup><br>por parte del trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/Reintegro|
|NIAE185|Deuda|Valor que se deba pagar por las<br>obligaciones que el empleado tenga con<br>su empresa, como puede ser un crédito<br>que ésta le haya otorgado, o como<br>compensación por algún perjuicio o<br>detrimento económico que el empleado<br>le haya causado a la empresa.|E<br>N|Deducciones|0-1|<sup>Valor Pagado correspondiente a Deuda con</sup><br>la Empresa por parte del trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>es/Deuda|
|NIAE186|Redondeo|Se utiliza para cuando se utilice el<br>Redondeo en el Documento|E<br>N|Reemplazar|0-1|Definido en elnumeral 1.1.1|1.0<sup>/NominaIndividualDeAjust</sup><br>e/Reemplazar/Redondeo|
|NIAE187|DevengadosTotal|Valor total de la Suma de todos los<br>Devengados del Documento|E<br>N|Reemplazar|1-1|<sup>Debe ir el valor Total de Todos los</sup><br>Devengados del Trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>sTotal|
|NIAE188|DeduccionesTotal|Valor total de la Suma de todas las<br>Deducciones del Documento|E<br>N|Reemplazar|1-1|<sup>Debe ir el valor Total de Todos las</sup><br>Deducciones del Trabajador|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Deduccion<br>esTotal|
|NIAE189|ComprobanteTotal|Debe ir el total de: Devengados -<br>Deducciones|E<br>N|Reemplazar|1-1|<sup>Debe ser la Diferencia entre</sup><br>DevengadosTotal - DeduccionesTotal|1.0<br>/NominaIndividualDeAjust<br>e/Reemplazar/Comproba<br>nteTotal|
||Eliminar|Utilizado para todo el contenido<br>correspondiente al evento de Eliminar<br>Documento|G<br>A|NominaIndividual<br>DeAjuste|0-1||1.0<br>/NominaIndividualDeAjust<br>e/Eliminar|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 89 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_|_Tam_<br>_Padre_<br>_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|
||EliminandoPredeces<br>or|Utilizado para Atributos de Documento<br>Predecesor a Eliminar|E<br>A|Eliminar<br>1-1|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/EliminandoPre<br>decesor|
|NIAE215|NumeroPred|Debe corresponder al Numero de<br>Documento Soporte de Pago de Nómina<br>Electrónica o Nota de Ajuste de<br>Documento Soporte de Pago de Nómina<br>Electrónica a Reemplazar|A A|<br>EliminandoPredec<br>esor<br>1-1|<sup>Debe ir el Numero de documento a</sup><br>Reemplazar|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/EliminandoPre<br>decesor/@NumeroPred|
|NIAE216|CUNEPred|Debe corresponder al CUNE del<br>Documento Soporte de Pago de Nómina<br>Electrónica o Nota de Ajuste de<br>Documento Soporte de Pago de Nómina<br>Electrónica a Reemplazar|A A|<br>EliminandoPredec<br>esor<br>1-1|<sup>Debe ir el CUNE del documento a</sup><br>Reemplazar|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/EliminandoPre<br>decesor/@CUNEPred|
|NIAE217|FechaGenPred|Debe corresponder a la Fecha de Emision<br>del Documento Soporte de Pago de<br>Nómina Electrónica o Nota de Ajuste de<br>Documento Soporte de Pago de Nómina<br>Electrónica a Reemplazar|A F|10<br>EliminandoPredec<br>esor<br>1-1|<sup>Debe ir la fecha del documento a</sup><br>Reemplazar, en formato AAAA-MM-DD|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/EliminandoPre<br>decesor/@FechaGenPred|
||NumeroSecuenciaX<br>ML|Utilizado para Atributos de Numero de<br>Secuencia del Documento XML|E<br>A|Eliminar<br>1-1|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/NumeroSecue<br>nciaXML|
|NIAE218|Prefijo|Prefijo del documento, depende de las<br>sucursales que posea el Empleador|A A|<br>NumeroSecuencia<br>XML<br>0-1|<sup>Debe corresponder a un Prefijo elegido por</sup><br>el Emisor del documento|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/NumeroSecue<br>nciaXML/@Prefijo|
|NIAE219|Consecutivo|Debe corresponder a un consecutivo<br>manejado por el Empleador|A N|<br>NumeroSecuencia<br>XML<br>1-1|<sup>Debe corresponder a un Consecutivo</sup><br>elegido por el Emisor del documento|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/NumeroSecue<br>nciaXML/@Consecutivo|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 90 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>|_F_<br>_T_|_am_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|NIAE220|Numero|Debe corresponder al Prefijo y<br>consecutivo manejado por el Empleador|A|A|NumeroSecuencia<br>XML|1-1|No se permiten caracteres adicionales como<br>espacios o guiones. Prefijo + Número<br>consecutivo del documento|<br>1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/NumeroSecue<br>nciaXML/@Numero|
||LugarGeneracionXM<br>L|Utilizado para Atributos del Lugar de<br>Generacion del Documento XML|E<br>|A|Eliminar|1-1|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/LugarGeneraci<br>onXML|
|NIAE221|Pais|Codigo del país donde se genera el<br>documento|A|A 2|<br>LugarGeneracionX<br>ML|1-1|<sup>Se debe colocar el Codigo alfa-2 de latabla</sup><br>5.4.1|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/LugarGeneraci<br>onXML/@Pais|
|NIAE222|DepartamentoEstad<br>o|Código del departamento donde se<br>genera el documento|A|N 2|<br>LugarGeneracionX<br>ML|1-1|Se debe colocar el Codigo de latabla 5.4.2|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/LugarGeneraci<br>onXML/@DepartamentoE<br>stado|
|NIAE223|MunicipioCiudad|Código del municipio o ciudad donde se<br>genera el documento|A|N 5|<br>LugarGeneracionX<br>ML|1-1|Se debe colocar el Codigo de latabla 5.4.3|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/LugarGeneraci<br>onXML/@MunicipioCiuda<br>d|
|NIAE224|Idioma|Codigo del país donde se genera el<br>documento|A|A 2|<br>LugarGeneracionX<br>ML|1-1|Se debe colocar el Codigo ISO 639-1 de la<br>tabla 5.3.1.Para Colombia se debe colocar<br>"es" (Español, Castellano)|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/LugarGeneraci<br>onXML/@Idioma|
||ProveedorXML|Utilizado para Atributos del Proveedor del<br>Documento XML|<br>E<br>|A|Eliminar|1-1|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/ProveedorXML|
|NIAE225|RazonSocial|Debe corresponder al Nombre de la<br>Razón Social del Proveedor de Soluciones<br>Tecnológicas|A|A|ProveedorXML|0-1|<sup>Debe ir el Nombre o Razón Social del</sup><br>Proveedor de Soluciones Tecnológicas|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/ProveedorXML<br>/@RazonSocial|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

> www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 91 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>|_F_<br>_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|NIAE226|PrimerApellido|Primer Apellido del Proveedor de<br>Soluciones Tecnológicas|A|A 60|ProveedorXML|0-1|<sup>Debe ir el Primer Apellido del Proveedor de</sup><br>Soluciones Tecnológicas|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/ProveedorXML<br>/@PrimerApellido|
|NIAE227|SegundoApellido|Segundo Apellido del Proveedor de<br>Soluciones Tecnológicas|A|A 60|ProveedorXML|0-1|<sup>Debe ir el Segundo Apellido del Proveedor</sup><br>de Soluciones Tecnológicas|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/ProveedorXML<br>/@SegundoApellido|
|NIAE228|PrimerNombre|Primer Nombre del Proveedor de<br>Soluciones Tecnológicas|A|A 60|ProveedorXML|0-1|<sup>Debe ir el Primer Nombre del Proveedor de</sup><br>Soluciones Tecnológicas|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/ProveedorXML<br>/@PrimerNombre|
|NIAE229|OtrosNombres|Otros Nombres del Proveedor de<br>Soluciones Tecnológicas|A|A 60|ProveedorXML|0-1|<sup>Deben ir los Otros Nombres del Proveedor</sup><br>de Soluciones Tecnológicas|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/ProveedorXML<br>/@OtrosNombres|
|NIAE230|NIT|Debe corresponder al NIT del Proveedor<br>de Soluciones Tecnologicas que realiza el<br>DE|A|N|ProveedorXML|1-1|Se debe colocar el NIT sin guiones ni DV de<br>la empresa dueña del Software que genera<br>el Documento, debe estar registrado en la<br>DIAN|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/ProveedorXML<br>/@NIT|
|NIAE231|DV|Debe corresponder al DV del NIT del<br>Proveedor de Soluciones Tecnologicas<br>que realiza el DE|A|N 2|ProveedorXML|1-1|Se debe colocar el DV de la empresa dueña<br>del Software que genera el Documento,<br>debe estar registrado en la DIAN|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/ProveedorXML<br>/@DV|
|NIAE232|SoftwareID|Identificador Software: Identificador del<br>software habilitado para la emisión de<br>nóminas|A|A|ProveedorXML|1-1|Identificador del software asignado cuando<br>el software se activa en el Sistema del<br>Documento Soporte de Pago de Nómina<br>Electrónica, debe corresponder a un<br>software autorizado para este Emisor|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/ProveedorXML<br>/@SoftwareID|
|NIAE233|SoftwareSC|Huella del software que autorizó la DIAN<br>al Obligado a Generar Nómina Electrónica<br>o al Proveedor de Soluciones Tecnológicas|<br> <br>A|A|ProveedorXML|1-1|Definido en elnumeral 8.3|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/ProveedorXML<br>/@SoftwareSC|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 92 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_T_|_am_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|NIAE234|CodigoQR|Debe poseer información detallada del<br>Documento Electronico|E<br>A|Eliminar|1-1|Debe  corresponder a la siguiente URL<br>“https://catalogo-<br>vpfe.dian.gov.co/document/searchqr?docu<br>mentkey=CUNE”  donde la palabra CUNE<br>debe ser reemplazada por el CUNE del<br>documento electrónico|1.0<sup>/NominaIndividualDeAjust</sup><br>e/Eliminar/CodigoQR|
||InformacionGeneral|Utilizado para Atributos de Información<br>General Documento|E<br>A|Eliminar|1-1|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/InformacionGe<br>neral|
|NIAE235|Version|Versión base de Schema XML usada para<br>crear este perfil<br>(NominaIndividualDeAjuste)|A A|InformacionGener<br>al|1-1|Debe ir el literal: "V1.0: Nota de Ajuste de<br>Documento Soporte de Pago de Nómina<br>Electrónica"|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/InformacionGe<br>neral/@Version|
|NIAE236|Ambiente|Tipo de Ambiente de Emision del<br>Documento: Habilitacion o Produccion|A N 1|<br>InformacionGener<br>al|1-1|Se debe colocar el Codigo de latabla 5.1.1|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/InformacionGe<br>neral/@Ambiente|
|NIAE237|TipoXML|Tipo de XML del Documento|A N 2|<br>InformacionGener<br>al|1-1|Se debe colocar el Codigo de latabla 5.5.7|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/InformacionGe<br>neral/@TipoXML|
|NIAE238|CUNE|CUNE:  Código Único de Documento<br>Soporte de Pago de Nómina Electrónica.<br>Elemento que verifica la integridad de la<br>información recibida|A A|InformacionGener<br>al|1-1|Definido en elnumeral 8.1|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/InformacionGe<br>neral/@CUNE|
|NIAE239|EncripCUNE|Identificador del esquema de<br>identificación. Algoritmo utilizado para el<br>cáculo del CUNE, SHA-384|A A 7|<br>InformacionGener<br>al|1-1|Debe ir la palabra "CUNE-SHA384"|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/InformacionGe<br>neral/@EncripCUNE|



Dirección de Gestión de Ingresos 

> Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 93 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>|_F_|_Tam_|<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|---|
|NIAE240|FechaGen|Fecha de emisión: Fecha de emisión del<br>documento|A|F|10|InformacionGener<br>al|1-1|Debe ir la fecha de emision del documento.<br>Considerando zona horaria de Colombia (-<br>5), en formato AAAA-MM-DD|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/InformacionGe<br>neral/@FechaGen|
|NIAE241|HoraGen|Hora de emisión: hora de emisión del<br>documento|A|H|14|InformacionGener<br>al|1-1|Debe ir la hora de emision del documento.<br>Considerando zona horaria de Colombia (-<br>5), en formato HH:MM:SSdhh:mm|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/InformacionGe<br>neral/@HoraGen|
|NIAE242|Notas|Campo de libre uso para Observaciones<br>en el documento|E<br>|A||Eliminar|0-N|<sup>Información adicional: Texto libre, relativo</sup><br>al documento|1.0<sup>/NominaIndividualDeAjust</sup><br>e/Eliminar/Notas|
||Empleador|Utilizado para Atributos del Empleador o<br>Emisor del Documento|E<br>|A||Eliminar|1-1|Elemento Vacio|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/Empleador|
|NIAE243|RazonSocial|Debe corresponder al Nombre de la<br>Razón Social del Empleador|A|A||Empleador|1-1|<sup>Debe ir el Nombre o Razón Social del</sup><br>Empleador|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/Empleador/@R<br>azonSocial|
|NIAE244|PrimerApellido|Primer Apellido del Empleador|A|A|60|Empleador|0-1|Debe ir el Primer Apellido del Empleador|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/Empleador/@P<br>rimerApellido|
|NIAE245|SegundoApellido|Segundo Apellido del Empleador|A|A|60|Empleador|0-1|Debe ir el Segundo Apellido del Empleador|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/Empleador/@S<br>egundoApellido|
|NIAE246|PrimerNombre|Primer Nombre del Empleador|A|A|60|Empleador|0-1|Debe ir el Primer Nombre del Empleador|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/Empleador/@P<br>rimerNombre|
|NIAE247|OtrosNombres|Otros Nombres del Empleador|A|A|60|Empleador|0-1|Deben ir los Otros Nombres del Empleador|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/Empleador/@<br>OtrosNombres|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 94 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_<br>_ns_|_Campo_|_Descripción_|_T_<br>|_F_<br>_Ta_|_m_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|NIAE248|NIT|Debe corresponder al NIT del Empleador<br>que realiza el DE|A|N|Empleador|1-1|<sup>Debe ir el NIT del Empleador sin guiones ni</sup><br>DV|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/Empleador/@<br>NIT|
|NIAE249|DV|Debe corresponder al DV del NIT del<br>Empleador que realiza el DE|A|N 2|Empleador|1-1|Debe ir el DV del Empleador|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/Empleador/@<br>DV|
|NIAE250|Pais|Codigo del país donde donde se<br>encuentra ubicado el empleador el mes<br>que se esta reportando|A|A 2|Empleador|1-1|<sup>Se debe colocar el Codigo alfa-2 de latabla</sup><br>5.4.1|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/Empleador/@P<br>ais|
|NIAE251|DepartamentoEstad<br>o|Código del departamento donde se<br>encuentra ubicado el empleador el mes<br>que se esta reportando|A|N 2|Empleador|1-1|Se debe colocar el Codigo de latabla 5.4.2|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/Empleador/@<br>DepartamentoEstado|
|NIAE252|MunicipioCiudad|Código del municipio o ciudad donde se<br>encuentra ubicado el empleador el mes<br>que se esta reportando|A|N 5|Empleador|1-1|Se debe colocar el Codigo de latabla 5.4.3|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/Empleador/@<br>MunicipioCiudad|
|NIAE253|Direccion|Debe corresponder a la dirección del<br>lugar físico de expedición del documento.|<sup>A</sup>|<sup>A</sup>|Empleador|1-1|Debe ir la Dirección Fisica del Empleador|1.0<br>/NominaIndividualDeAjust<br>e/Eliminar/Empleador/@<br>Direccion|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 95 de 269 



##### 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

- 3.3. Estándar del nombre del documento electrónico Documento Soporte de Pago de Nómina Electrónica XML. 

|Guía del nombre del archivo XML del|documento electrónico Documento Soporte de Pago de Nómina Electrónica requerido<br>por la DIAN|
|---|---|
|Ejemplo de Nomenclatura|Observaciones|
|niennnnnnnnnnaadddddddd.xml|nie: Documento Soporte de Pago de Nómina Electrónica.<br>nnnnnnnnnn:NIT del Sujeto Obligado sin DV, de diez (10) dígitos alineados a la<br>derecha y relleno con ceros a la izquierda.<br>aa:Dos (2) últimos dígitos año calendario.<br>dddddddd:consecutivo de archivos enviados, de ocho (8) dígitos hexadecimales<br>alineados a la derecha y ajustado a la izquierda con ceros, en el rango:<br>00000001 <= FFFFFFFF<br>Ejemplo del décimo segundo Documento Soporte de Pago de Nómina Electrónica<br>del Sujeto Obligado con NIT 800197268 con software propio para el año 2020.<br>nie0800197268200000000C.xml|



#### Notas : 

- Los tamaños de cada variable son constantes, es necesario generar el ajuste con ceros a la izquierda en cada uno de ellos. 

- El año “aa” corresponde al año en vigencia. 

- Cada Año, el 1ro de enero se debe reiniciar en consecutivo de archivos enviados “dddddddd” a 00000001. 

### 3.4. Estándar del nombre del documento electrónico Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica XML. 

Guía del nombre del archivo XML del documento electrónico Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica requerido por la DIAN Ejemplo de Nomenclatura Observaciones 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 96 de 269 

**Resolución No. 000013** 





### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

> niaennnnnnnnnnaadddddddd.xml niae: Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica. nnnnnnnnnn: NIT del Sujeto Obligado sin DV, de diez (10) dígitos alineados a la derecha y relleno con ceros a la izquierda. aa: Dos (2) últimos dígitos año calendario . dddddddd: consecutivo de archivos enviados, de ocho (8) dígitos hexadecimales alineados a la derecha y ajustado a la izquierda con ceros, en el rango: 00000001 <= FFFFFFFF Ejemplo del décimo segundo Documento Soporte de Pago de Nómina Electrónica del Sujeto Obligado con NIT 800197268 con software propio para el año 2020. niae0800197268200000000C.xml 

#### Notas : 

   - Los tamaños de cada variable son constantes, es necesario generar el ajuste con ceros a la izquierda en cada uno de ellos. 

   - El año “aa” corresponde al año en vigencia. 

   - Cada Año, el 1ro de enero se debe reiniciar en consecutivo de archivos enviados “dddddddd” a 00000001. 

- 3.5. Guía del nombre del archivo que contiene uno o más documentos electrónicos y que será entregado a la DIAN mediante un web service de recepción. 

|Guía del nombre del archivo ZIP que Contiene uno o má<br>web<br>|s documentos electrónicos y que será Entregado a la DIAN mediante un<br>service de recepción.<br>|
|---|---|
|Ejemplo de Nomenclatura|Observaciones|
|znnnnnnnnnnaadddddddd.zip<br><br>archivo comprimido que contiene uno o varios<br>archivos *.XML.<br><br>Si el archivo se transmitirá a la DIAN a través del<br>servicio asincrónico,entonces la cantidad de<br>documentos electrónicos será inferior a 51.<br><br>Este formato será el único para la entrega de<br>archivos comprimidos.|z:comprimido<br>nnnnnnnnnn:NIT del Sujeto Obligado sin DV, de diez (10) dígitos<br>alineados a la derecha y relleno con ceros a la izquierda.<br>aa:Dos (2) últimos dígitos año calendario.<br>dddddddd:consecutivo del paquete de archivos comprimidos<br>enviados; de ocho (8) dígitos hexadecimales alineados a la derecha y<br>ajustado a la izquierda con ceros; en el rango:<br>00000001 <= FFFFFFFF<br>Ejemplo de la décima segunda Nómina del Sujeto Obligado con NIT<br>800197268 con software propio para el año 2020.<br>z0800197268200000000C.zip<br>Regla: el consecutivo se iniciará en “00000001” cada primero de<br>enero.|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 97 de 269 

® 



<!-- Start of picture text -->
) | Ma. IN<br><!-- End of picture text -->

POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->



### **Resolución No. 000013** 



(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

## 3.6. firma digital del documento: _ds:Signature._ 

Datos de la firma de acuerdo con xmldsig-core-schema.xsd 

Ver documentación en 

- http://docs.oasis-open.org/ubl/os-UBL-2.1/UBL-2.1.html#S-PROFILES-FOR-UBL-DIGITAL-SIGNATURES 

- https://www.w3.org/TR/XadES/ 

|_ID_|_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_Tam_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
||ext|UBLExtensions||NominaIndividual||<br>NominaIndividualDe<br>Ajuste|||.../ext:UBLExtensions|
||ext|UBLExtension||UBLExtensions|||.../ext:UBLExtensions/ext:UBLEx<br>tension|
||ext|ExtensionContent||UBLExtension|||.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent|
|DC01|ds|Signature|Grupo de la firma XadES-EPES|G<br>ExtensionContent|1..1||1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature|
|DC02|ds|SignedInfo|Grupo de información donde contiene la<br>firma aplicada a todos los elementos del<br>Documento Soporte de Pago de Nómina<br>Electrónica, los elementos contenidos<br>dentro  del  elemento  SignedProperties<br>más  la  clave  pública  contenida  en  el<br>elemento KeyInfo.|G<br>Signature|1..1||1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:SignedInfo|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 99 de 269 



**Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_|<br>_Campo_|_Descripción_|_T_<br>_F_<br>_Tam_|<br>_Padre_|_Oc_<br>_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|DC03|ds|CanonicalizationM<br>ethod|Algoritmo para organizar los datos según el<br>canon usado sobre el elemento<br>«SignedInfo» para  la  firma  digital.||Signature|1..1<br>Para esto se debe usar el valor<br>http://www.w3.org/TR/2001/REC-<br>xml-c14n-20010315.|1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:SignedInfo/ds:Ca<br>nonicalizationMethod|
|DC04|ds|SignatureMethod|<sup>El algoritmo de firma usado sobre el</sup><br>elemento «SignedInfo»||Signature|1..1<br>Puede  ser  cualquiera  de  los<br>definidos  en  la especificación<br>XML-Signature   Syntax   and<br>Processing<br>(http://www.w3.org/TR/xmldsig-<br>core2/#sec-Algorithms) que<br>actualmente son:<br>RSAwithSHA256=http://www.w3.<br>org/2001/04/xmldsig-more#rsa-<br>sha256<br>RSAwithSHA384=http://www.w3.<br>org/2001/04/xmldsig-more#rsa-<br>sha384<br>RSAwithSHA512=http://www.w3.<br>org/2001/04/xmldsig-more#rsa-<br>sha512|1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:SignedInfo/ds:Sig<br>natureMethod|
|DC05|ds|Reference|Grupo de la primera referencia que<br>contiene la firma aplicada de todo el<br>documento|G|Signature|1..1<br>URI=""|1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:SignedInfo/ds:Re<br>ference|



Dirección de Gestión de Ingresos 

> Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 100 de 269 





### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_|<br>_Campo_|_Descripción_|_T_<br>_F_<br>_Tam_|_Padre_|_Oc_<br>_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|DC06|ds|Transforms|Grupo de trasformación del documento|G|Reference|1..1|1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:SignedInfo/ds:Re<br>ference/ds:Transforms|
|DC07|ds|TransForm|Transformación del documento. Se debe<br>especificar que la firma se aplica a todo el<br>documento y esta se encuentre embebida<br>en este.||Transforms|1..1<br>Algorithm="http://www.w3.org/2<br>000/09/xmldsig#enveloped-<br>signature"|1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:SignedInfo/ds:Re<br>ference/ds:Transforms/ds:Trans<br>Form|
|DC08|ds|DigestMethod|El algoritmo de firma usado sobre el<br>elemento||Reference|1..1<br>Puede  ser  cualquiera  de  los<br>definidos  en  la especificación<br>XML-Signature   Syntax   and<br>Processing<br>(http://www.w3.org/TR/xmldsig-<br>core2/#sec-Algorithms) que<br>actualmente son:<br>RSAwithSHA256=http://www.w3.<br>org/2001/04/xmldsig-more#rsa-<br>sha256<br>RSAwithSHA384=http://www.w3.<br>org/2001/04/xmldsig-more#rsa-<br>sha384<br>RSAwithSHA512=http://www.w3.<br>org/2001/04/xmldsig-more#rsa-<br>sha512|1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:SignedInfo/ds:Re<br>ference/ds:DigestMethod|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 101 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_|<br>_Campo_|_Descripción_|_T_<br>_F_<br>_Tam_|_Padre_|_Oc_<br>_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|DC09|ds|DigestValue|Resultado de aplicar el algoritmo de<br>generación hash especificado en el<br>“DigestMethod” en codificación base64||Reference|1..1|1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:SignedInfo/ds:Re<br>ference/ds:DigestValue|
|DC10|ds|Reference|Grupo de la segunda referencia donde se<br>especifica clave  pública  contenida  en  el<br>elemento KeyInfo.|G|Signature|1..1<br>URI="#{UUID}-KeyInfo"|1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:SignedInfo/ds:Re<br>ference|
|DC11|ds|DigestMethod|El algoritmo de firma usado sobre el<br>elemento||Reference|1..1<br>Puede  ser  cualquiera  de  los<br>definidos  en  la especificación<br>XML-Signature   Syntax   and<br>Processing<br>(http://www.w3.org/TR/xmldsig-<br>core2/#sec-Algorithms) que<br>actualmente son:<br>RSAwithSHA256=http://www.w3.<br>org/2001/04/xmldsig-more#rsa-<br>sha256<br>RSAwithSHA384=http://www.w3.<br>org/2001/04/xmldsig-more#rsa-<br>sha384<br>RSAwithSHA512=http://www.w3.<br>org/2001/04/xmldsig-more#rsa-<br>sha512|1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:SignedInfo/ds:Re<br>ference/ds:DigestMethod|



> www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

Página 102 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_|<br>_Campo_|_Descripción_|_T_<br>_F_<br>_Tam_|_Padre_|_Oc_<br>_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|DC12|ds|DigestValue|Resultado de aplicar el algoritmo de<br>generación hash especificado en el<br>“DigestMethod” en codificación base64||Reference|1..1|1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:SignedInfo/ds:Re<br>ference/ds:DigestValue|
|DC13|ds|Reference|Grupo de la tercera referencia de los<br>elementos contenidos dentro<br>“SignedProperties”|G|Signature|1..1<br>URI="#xmldsig-{UUID}-<br>signedprops"|1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:SignedInfo/ds:Re<br>ference|
|DC14|ds|DigestMethod|El  algoritmo  de  firma  usado  sobre  el<br>elemento||Reference|1..1<br>Puede  ser  cualquiera  de  los<br>definidos  en  la especificación<br>XML-Signature   Syntax   and<br>Processing<br>(http://www.w3.org/TR/xmldsig-<br>core2/#sec-Algorithms) que<br>actualmente son:<br>RSAwithSHA256=http://www.w3.<br>org/2001/04/xmldsig-more#rsa-<br>sha256<br>RSAwithSHA384=http://www.w3.<br>org/2001/04/xmldsig-more#rsa-<br>sha384<br>RSAwithSHA512=http://www.w3.<br>org/2001/04/xmldsig-more#rsa-<br>sha512|1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:SignedInfo/ds:Re<br>ference/ds:DigestMethod|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

> www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 103 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_|_Campo_|_Descripción_|_T_<br>_F_|_Tam_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|DC15|ds|DigestValue|Resultado de aplicar el algoritmo de<br>generación hash especificado en el<br>“DigestMethod” en codificación base64||Reference|1..1||1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:SignedInfo/ds:Re<br>ference/ds:DigestValue|
|DC16|ds|SignatureValue|Resultado de aplicar el algoritmo de<br>generación hash especificado en el<br>“SignatureMethod” en codificación base64||Signature|1..1||1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:SignatureValue|
|DC17|ds|KeyInfo|Grupo de información para embeber el<br>certificado público requerido para validar la<br>firma.|G|Signature|1..1||1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:KeyInfo|
|DC18|ds|X509Data|Grupo que contiene el certificado publico<br>del que firma el documento|G|KeyInfo|1..1||1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:KeyInfo/ds:X509<br>Data|
|DC19|ds|X509Certificate|Certificado publico requerido para validar la<br>firma del documento electronico||X509Data|1..1||1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:KeyInfo/ds:X509<br>Data/ds:X509Certificate|
|DC20|ds|Object|Grupo de objetos para definir las<br>propiedades de la firma|G|Signature|1..1||1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:Object|
|DC21|xade<br>s|QualifyingProperti<br>es|Grupo de elementos calificables de<br>comprobación del firma|G|Object|1..1||1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:Object/xades:Qu<br>alifyingProperties|



Dirección de Gestión de Ingresos 

> www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

Página 104 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_|_Campo_|_Descripción_|_T_<br>_F_<br>_Tam_|_Padre_|_Oc_<br>_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|
|DC22|xade<br>s|SignedProperties|Grupo de elementos para definir las<br>propiedades|G|QualifyingProperties|<br>1..1<br>|1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:Object/xades:Qu<br>alifyingProperties/xades:Signed<br>Properties|
|DC23|xade<br>s|SignedSignaturePr<br>operties|Grupo de elementos para definir las<br>propiedades de la firma|G|SignedProperties|1..1<br>|1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:Object/xades:Qu<br>alifyingProperties/xades:Signed<br>Properties/xades:SignedSignatur<br>eProperties|
|DC24|xade<br>s|SigningTime|Fecha y Hora de generación||SignedSignaturePro<br>perties|1..1<br>Es deber de los emisores de<br>nómina electrónicos que los<br>sistemas computacionales que<br>utilicen para el firmado de los<br>documentos deberán estar<br>sincronizados con el reloj de la<br>súper intendencia de industria y<br>comercio el cual determina la<br>hora legal<br>colombiana.http://www.sic.gov.co<br>/hora-legal-colombiana<br>|1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:Object/xades:Qu<br>alifyingProperties/xades:Signed<br>Properties/xades:SignedSignatur<br>eProperties/xades:SigningTime|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 105 de 269 



**Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_|_Campo_|_Descripción_|_T_<br>_F_|_Tam_<br>_Padre_|_Oc_|_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|DC25|xade<br>s|SigningCertificate|Grupo de elemento que contiene la cadena<br>de confianza del certificado con el que se<br>firmó el documento.|G|SignedSignaturePro<br>perties|1..1||1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:Object/xades:Qu<br>alifyingProperties/xades:Signed<br>Properties/xades:SignedSignatur<br>eProperties/xades:SigningCertifi<br>cate|
|DC26|xade<br>s|Cert|Grupo para definir un certificado|G|SignedSignaturePro<br>perties|1..1||1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:Object/xades:Qu<br>alifyingProperties/xades:Signed<br>Properties/xades:SignedSignatur<br>eProperties/xades:SigningCertifi<br>cate/xades:Cert|
|DC27|xade<br>s|CertDigest|Grupo de cifrado del certificado|G|SignedSignaturePro<br>perties|1..1||1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:Object/xades:Qu<br>alifyingProperties/xades:Signed<br>Properties/xades:SignedSignatur<br>eProperties/xades:SigningCertifi<br>cate/xades:Cert/xades:CertDige<br>st|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 106 de 269 



**Resolución No. 000013** 



(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_ns_|_Campo_||_Descripción_|_T_<br>_F_<br>_Tam_|<br>_Padre_|_Oc_<br>_Observaciones_|_V_<br>_Xpath_|
|---|---|---|---|---|---|---|---|---|
|DC28|ds|DigestMethod|El algoritmo d<br>elemento|e firma usado sobre el||SignedSignaturePro<br>perties|1..1<br>Puede ser cualquiera de los<br>definidos en la especificación<br>XML-Signature Syntax and<br>Processing<br>(http://www.w3.org/TR/xmldsig-<br>core2/#sec-Algorithms) que<br>actualmente son:<br>RSAwithSHA256=http://www.w3.<br>org/2001/04/xmldsig-more#rsa-<br>sha256|1<br>.../ext:UBLExtensions/ext:UBLEx<br>tension/ext:ExtensionContent/d<br>s:Signature/ds:Object/xades:Qu<br>alifyingProperties/xades:Signed<br>Properties/xades:SignedSignatur<br>eProperties/xades:SigningCertifi<br>cate/xades:Cert/xades:CertDige<br>st/ds:DigestMethod|



### 3.7. Respuesta DIAN con validaciones de documentos Nomina: ApplicationResponse. 

Tal como sucede con el modelo de Factura Electrónica en Validación Previa, los Documentos Soporte de Pago de Nómina Electrónica la DIAN devolverá la validación en un ApplicationRepsonse firmado por la entdad. 

Son adoptadas las siguientes definiciones: 

- Documento Electrónico: un Documento Soporte de Pago de Nómina Electrónica o una Nota de Ajuste del Documento Soporte de Pago de Nómina Electrónica; y 

- Evento: una ocurrencia relacionada con un Documento Electrónico, declarada por una entidad relacionada con estos documentos. 

### 3.7.1. Garantía de que el evento será registrado en el documento correcto. 

Algunos eventos necesitan que la persona o entidad que lo registra tenga absoluta seguridad del contenido del documento a que se refieren, y que este documento existe en la base de datos de la DIAN. 

> Dirección de Gestión de Ingresos 

> Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 107 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

Estos eventos requieren, para su registro, que se informe, en el cuerpo del documento las claves principales del documento a la que se esta aplicando el evento. 

### 3.7.2. Relacionamientos mutuos entre los eventos. 

_<u>Tabla 7 – Relacionamientos Mutuos Entre los Eventos</u>_ 

|<br>I|mpedido|por|
|---|---|---|
|Eventos|02|04|
|**¡Error! No se encuentra el origen de la referencia.**<br> 02||X|
|**¡Error! No se encuentra el origen de la referencia.**<br> 04|X||



La 

Tabla <u>7</u> muestra los efectos del registro de un evento sobre la posibilidad que otro evento sea registrado en el mismo documento electrónico. Los códigos y nombres de los eventos, que se utilizan en la 

Tabla <u>7</u> y en los elementos _/ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:ResponseCode_ y _/ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:Description_ , 

Es posible la existencia de casos en los cuales exista conflicto entre declaraciones; eso ocurre cuando no existe manera automática de decidir cuál de las dos informaciones debe prevalecer sobre la otra. En tales situaciones, será necesario intervención de la DIAN para resolver el conflicto, probablemente por medio de contacto con uno o ambos los declarantes. 

Las definiciones de los eventos se detallan en cada uno de los ítems que siguen el cuerpo común, detallado a continuación. 

> Dirección de Gestión de Ingresos 

> Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 108 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

### 3.7.3. Detalles de cada evento. 

### 3.7.3.1. <u>Documento validado por la DIAN.</u> 

Este documento es la respuesta del servicio de validación de la DIAN, cuando el documento electrónico enviado al servicio de validación previa es validado exitosamente por la DIAN. 

Teniendo en cuenta las definiciones del presente anexo, la DIAN puede emitir un ApplicationResponse Documento validado por la DIAN con notificaciones. 

Este evento debe ser enviado por la DIAN al emisor del DE validado. 

#### Responsable por la generación del DE: DIAN 

Efecto: El DE referenciado tiene validez de acuerdo con lo que dispone la normatividad vigente. 

Cardinalidad: Solo se puede generar si y solamente el resultado de la validación es exitosa para un determinado documento electrónico. 

Detalles particulares del DE ApplicationResponse Documento validado por la DIAN 

|**_ID_**|**_NS_**|**_Campo _**|**_Descripción_**|**_T_**<br>**_F_**|**_Tam_**<br>**_Padre_**<br>**_Oc_**|**_Observaciones_**|**_V_**<br>**_Xpath_**|
|---|---|---|---|---|---|---|---|
|AAH01|cac|DocumentRespon<br>se|Grupo de información del<br>evento a ser registrado|G|ApplicationRespons<br>e<br>1..1||1.0<br>/ApplicationResponse/cac:Docum<br>entResponse|
|AAH02|cac|Response|Descripción del evento<br>registrado|G|DocumentResponse<br>1..1||1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:Response|
|AAH03|cbc|ResponseCode|Código del evento registrado|E N|3<br>Response<br>1..1|<sup>Debe contener “02”</sup>|1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:Response/cbc:<br>ResponseCode|
|AAH04|cbc|Description|Descripción del evento<br>registrado|E<br>A|15-<br>100<br>Response<br>1..1|<sup>Debe contener el literal “Documento</sup><br>validado por la DIAN”|1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:Response/cbc:D<br>escription|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 109 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|**_ID_**|**_NS_**|**_Campo _**|**_Descripción_**|**_T_**<br>**_F_**|**_Tam_**<br>**_Padre_**<br>**_Oc_**|**_Observaciones_**|**_V_**<br>**_Xpath_**|
|---|---|---|---|---|---|---|---|
|AAH05|cac|DocumentReferen<br>ce|Documento al cual está<br>referenciado el evento siendo<br>registrado|G|DocumentResponse<br>1..1||1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:DocumentRefere<br>nce|
|AAH06|cbc|ID|_Prefijo y Número del_<br>_documento referenciado_|E<br>A|12<br>DocumentReferenc<br>e<br>0..1|_../cbc:ID_|1.0 ../cac:DocumentReference/cbc:ID|
|AAH07|cbc|UUID|CUNE del documento<br>referenciado|E<br>A|96<br>DocumentReferenc<br>e<br>0..1|<sup>**Notificación:** si este CUNE</sup> <sup>no existe en la</sup><br>base de datos de la DIAN|1.0<sup>../cac:DocumentReference/cbc:U</sup><br>UID|
|AAH08|cbc|@schemeName|<sup>Identificador del esquema de</sup><br>identificación|A A|11<br>UUID<br>1..1|<br>Algoritmo utilizado para el cálculo del<br>CUFE<br>Ver lista de valores posibles en**0**<br>**Rechazo:** si el contenido de este atributo<br>no corresponde a algún de los valores de<br>la columna “Código”|1.0<sup>../cac:DocumentReference/cbc:U</sup><br>UID/@schemeName|
|AAH09|cbc|<sup>DocumentTypeCo</sup><br>de|Identificador del tipo de<br>documento de referencia|A N|2<br>DocumentReferenc<br>e<br>1..1|<br>**Rechazo:** Si este elemento no<br>corresponde a un valor de la columna<br>"Código" de uso “Tipo de Documento”|1.0<sup>../cac:DocumentReference/cbc:Do</sup><br>cumentTypeCode|
|AAI01|cac|LineResponse|Grupo de información para<br>registro de la anotación|G|DocumentResponse<br>1..1||1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:LineResponse|
|AAI02|cac|LineReference|Grupo de información<br>correspondiente a la<br>anotación|G|LineResponse<br>1..1||1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:LineResponse<br>/cac:LineReference|
|AAI03|cbc|LineID||E N|LineReference<br>1..1||1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:LineResponse/ca<br>c:LineReference/cbc:LineID|
|AAI04|cac|Response|Grupo de información del NSU<br>del documento validado|G|LineResponse<br>1..N||1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:LineResponse<br>/cac:Response|



Dirección de Gestión de Ingresos 

> Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 110 de 269 



**Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|**_ID_**|**_NS_**|**_Campo _**|**_Descripción_**|**_T_**<br>**_F_**|**_Tam_**|**_Padre_**|**_Oc_**|**_Observaciones_**|**_V_**<br>**_Xpath_**|
|---|---|---|---|---|---|---|---|---|---|
|AAI05|cbc|ResponseCode|Código de la notificación|E<br>A|4-10|Response|1..1|<br>Si**TODAS**las reglas de validación previas<br>estan ok, entonces se generara una<br>**Aprobación**del documento el cual será<br>informado con  el literal “**0000**”.<br>Si**algunas reglas**de validación previas<br>apunta a una**discrepancia menos**<br>**importante (reglas no mandatorias)**,<br>pero que asimismo merece que se<br>advierta al emisor de un posible<br>problema con las información del<br>archivo, entonces se generara una<br>**Aprobación con Notificaciones**del<br>documento el cual será informado con  el<br>literal “**0001**”|1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:LineResponse<br>/cac:Response/cbc:ResponseCode|
|AAI06|cbc|Description|NSU del documento validado|E<br>A|4-150|Response|1..1|<sup>NSU generado por la DIAN para el</sup><br>documento validado|1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:LineResponse<br>/cac:Response/cbc:Description|
|AAI04|cac|Response|Grupo de información<br>correspondiente a las<br>notificaciones|G||LineResponse|1..N|<br>Grupo generado si existe por lo menos<br>una notificación|1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:LineResponse<br>/cac:Response|
|AAI05|cbc|ResponseCode|Código de la notificación|E<br>A|4-10|Response|1..1||1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:LineResponse<br>/cac:Response/cbc:ResponseCode|
|AAI06|cbc|Description|Descripción de la notificación|E<br>A|4-150|Response|1..1||1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:LineResponse<br>/cac:Response/cbc:Description|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 111 de 269 

**Resolución No. 000013** 





### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

### 3.7.3.2. <u>Documento Rechazado por la DIAN.</u> 

Este documento es la respuesta del servicio de validación de la DIAN, cuando el documento electrónico enviado al servicio de validación previa no es validado exitosamente por la DIAN. Este evento debe ser enviado por la DIAN al emisor del DE validado, en el mismo contenedor del DE. 

Responsable por la generación del DE: DIAN 

Efecto: El DE NO tiene validez de acuerdo con lo que dispone la normatividad vigente. 

Cardinalidad: Debe ser generado como resultado de una validación no exitosa ante la DIAN  para un determinado documento electrónico. 

|**_ID_**<br>**_NS_**|**_Campo _**|**_Descripción_**|**_T_**<br>**_F_**|**_Tam_**<br>**_Padre_**<br>**_Oc_**|**_Observaciones_**|**_V_**<br>**_Xpath_**|
|---|---|---|---|---|---|---|
|AAH01<br>cac|DocumentRespon<br>se|Grupo de información del evento<br>a ser registrado|G|ApplicationRespons<br>e<br>1..1||1.0<br>/ApplicationResponse/cac:Docum<br>entResponse|
|AAH02<br>cac|Response|Descripción del evento registrado|G|DocumentResponse<br>1..1||1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:Response|
|AAH03 cbc|ResponseCode|Código del evento registrado|E N|3<br>Response<br>1..1|<sup>Debe contener “04”</sup>|1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:Response/cbc:<br>ResponseCode|
|AAH04 cbc|Description|Descripción del evento registrado|E<br>A|15-<br>100<br>Response<br>1..1|<sup>Debe contener el literal “Documento</sup><br>Rechazado por la DIAN”|1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:Response/cbc:D<br>escription|
|AAH05<br>cac|DocumentReferen<br>ce|Documento al cual está<br>referenciado el evento siendo<br>registrado|G|DocumentResponse<br>1..1||1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:DocumentRefere<br>nce|
|AAH06 cbc|ID|_Prefijo y Número del documento_<br>_referenciado_|E<br>A|12<br>AddtionalDocument<br>Reference<br>0..1|_../cbc:ID_|1.0 ../cac:DocumentReference/cbc:ID|
|AAH07 cbc|UUID|CUNE del documento<br>referenciado|E<br>A|96<br>AddtionalDocument<br>Reference<br>0..1|<sup>Notificaciónsi esta</sup><sup>_UUID_no existe en la</sup><br>base de datos de la DIAN|1.0<sup>../cac:DocumentReference/cbc:U</sup><br>UID|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 112 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|**_ID_**<br>**_NS_**|**_Campo _**|**_Descripción_**|**_T_**<br>**_F_**|**_Tam_**<br>**_Padre_**<br>**_Oc_**|**_Observaciones_**|**_V_**<br>**_Xpath_**|
|---|---|---|---|---|---|---|
|AAH08 cbc|@schemeName|<sup>Identificador del esquema de</sup><br>identificación|A A|11<br>UUID<br>1..1|Algoritmo utilizado para el cáculo del<br>CUFE<br>Ver lista de valores posibles en**0**<br>Rechazosi el contenido de este atributo<br>no corresponde a algún de los valores<br>de la columna “Código”|1.0<sup>../cac:DocumentReference/cbc:U</sup><br>UID/@schemeName|
|AAH09 cbc|<sup>DocumentTypeCo</sup><br>de|Identificador del tipo de<br>documento de referencia|A N|2<br>DocumentReferenc<br>e<br>1..1|Ver lista de valores posibles en5.1.3<br>Rechazo:<br>Si este elemento no corresponde a un<br>valor de la columna "Código" de uso<br>“Tipo de Documento”|1.0<sup>../cac:DocumentReference/cbc:Do</sup><br>cumentTypeCode|
|AAI01<br>cac|LineResponse|Grupo de información para<br>registro de la anotación|G|DocumentResponse<br>1..1||1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:LineResponse|
|AAI02<br>cac|LineReference|Grupo de información<br>correspondiente a la anotación|G|LineResponse<br>1..1||1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:LineResponse<br>/cac:LineReference|
|AAI03 cbc|LineID||E N|LineReference<br>1..1||1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:LineResponse/ca<br>c:LineReference/cbc:LineID|
|AAI04<br>cac|Response|Grupo de información del NSU del<br>documento validado|G|LineResponse<br>1..N||1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:LineResponse<br>/cac:Response|
|AAI05 cbc|ResponseCode|Código de la notificación|E<br>A|4-10<br>Response<br>1..1|Si**algunas reglas**de validación previas<br>apunta a una**a mas discrepancia grave,**<br>**que indica que las información del**<br>**archivo no pueden ser utilizadas de**<br>**manera confiable o de manera legal;**,<br>entonces se generara un rechazo, el<br>cual contendrán**las  Notificaciones**del<br>documento el cual será informado con<br>el literal “**0003**”|1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:LineResponse<br>/cac:Response/cbc:ResponseCode|



Dirección de Gestión de Ingresos 

Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 113 de 269 



**Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|**_ID_**<br>**_NS_**|**_Campo _**|**_Descripción_**|**_T_**<br>**_F_**|**_Tam_**|**_Padre_**|**_Oc_**|**_Observaciones_**|**_V_**<br>**_Xpath_**|
|---|---|---|---|---|---|---|---|---|
|AAI06 cbc|Description|NSU del documento NO validado|E<br>A|4-150|Response|1..1|<sup>NSU generado por la DIAN para el</sup><br>documento NO validado|1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:LineResponse<br>/cac:Response/cbc:Description|
|AAI04<br>cac|Response|Grupo de información<br>correspondiente a las<br>notificaciones|G||LineResponse|1..N|Grupo generado si existe por lo menos<br>una notificación|1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:LineResponse<br>/cac:Response|
|AAI05 cbc|ResponseCode|Código de la notificación|E<br>A|4-10|Response|1..1||1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:LineResponse<br>/cac:Response/cbc:ResponseCode|
|AAI06 cbc|Description|Descripción de la notificación|E<br>A|4-150|Response|1..1||1.0<br>/ApplicationResponse/cac:Docum<br>entResponse/cac:LineResponse<br>/cac:Response/cbc:Description|



A continuación, se puede visualizar la estructura simplificada, asumiendo un documento rechazado con dos notificaciones 

<?xml version="1.0" encoding="utf-8" standalone="no"?> 

<ApplicationResponse xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" 

xmlns:ext="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2" xmlns:sts="dian:gov:co:facturaelectronica:Structures-2-1" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns="urn:oasis:names:specification:ubl:schema:xsd:ApplicationResponse-2"> 

<ext:UBLExtensions> 

<ext:UBLExtension> 

<ext:ExtensionContent> 

<sts:DianExtensions> 

<sts:InvoiceSource> 

<cbc:IdentificationCode listAgencyID="6" listAgencyName="United Nations Economic Commission for Europe" listSchemeURI="urn:oasis:names:specification:ubl:codelist:gc:CountryIdentificationCode-2.1">CO</cbc:IdentificationCode> 

> Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 

> www.dian.gov.co 

> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 114 de 269 

**Resolución No. 000013** 





### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

</sts:InvoiceSource> 

<sts:SoftwareProvider> 

<sts:ProviderID schemeID="4" schemeName="31" schemeAgencyID="195" schemeAgencyName="CO, 

DIAN (Dirección de Impuestos y Aduanas Nacionales)">800197268</sts:ProviderID> 

<sts:SoftwareID schemeAgencyID="195" schemeAgencyName="CO, DIAN (Dirección de Impuestos y 

Aduanas Nacionales)">...</sts:SoftwareID> 

</sts:SoftwareProvider> 

<sts:SoftwareSecurityCode schemeAgencyID="195" schemeAgencyName="CO, DIAN (Dirección de Impuestos 

y Aduanas Nacionales)">...</sts:SoftwareSecurityCode> 

<sts:AuthorizationProvider> 

<sts:AuthorizationProviderID schemeID="4" schemeName="31" schemeAgencyID="195" schemeAgencyName="CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)">800197268</sts:AuthorizationProviderID> 

</sts:AuthorizationProvider> 

</sts:DianExtensions> 

</ext:ExtensionContent> 

</ext:UBLExtension> 

<ext:UBLExtension> 

<ext:ExtensionContent> 

<ds:Signature> Información de la firma </ds:Signature> 

</ext:ExtensionContent> 

</ext:UBLExtension> 

</ext:UBLExtensions> 

<cbc:UBLVersionID>UBL 2.1</cbc:UBLVersionID> 

<cbc:CustomizationID>1</cbc:CustomizationID> <cbc:ProfileID>DIAN 2.1</cbc:ProfileID> <cbc:ProfileExecutionID>2</cbc:ProfileExecutionID> 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 115 de 269 

**Resolución No. 000013** 





### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

<cbc:ID>63200030</cbc:ID> 

<cbc:UUID schemeName="CUDE- 

SHA384">43a0738ec86966f9a7eb3314387508ca6adbf852a855fb4fc9b0c9396b87f64c9a711bd0046b3ef4c83b1c2c3eec9d32</cbc:UUID> <cbc:IssueDate>2021-01-25</cbc:IssueDate> <cbc:IssueTime>19:30:03-05:00</cbc:IssueTime> <cac:SenderParty> <cac:PartyTaxScheme> <cbc:RegistrationName>Unidad Especial Dirección de Impuestos y Aduanas Nacionales</cbc:RegistrationName> <cbc:CompanyID schemeID="4" schemeName="">800197268</cbc:CompanyID> <cac:TaxScheme> <cbc:ID>01</cbc:ID> <cbc:Name>IVA</cbc:Name> </cac:TaxScheme> </cac:PartyTaxScheme> </cac:SenderParty> <cac:ReceiverParty> <cac:PartyTaxScheme> <cbc:RegistrationName>Empresa Emisora</cbc:RegistrationName> <cbc:CompanyID schemeID="" schemeName="">456789123</cbc:CompanyID> <cac:TaxScheme> <cbc:ID>01</cbc:ID> <cbc:Name>IVA</cbc:Name> </cac:TaxScheme> 

</cac:PartyTaxScheme> 

</cac:ReceiverParty> 

<cac:DocumentResponse> 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 116 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

<cac:Response> 

<cbc:ResponseCode>04</cbc:ResponseCode> 

<cbc:Description>Documento rechazado por la DIAN</cbc:Description> </cac:Response> <cac:DocumentReference> <cbc:ID>CD001</cbc:ID> <cbc:UUID schemeName="CUNESHA384">210b27d90355411c95bae7532c91eb8e2fb57507c0a1cd55599c5063d65b4ac890016f8d5a6e48dbb3e949fc4994606f</cbc:UUID> </cac:DocumentReference> 

<cac:LineResponse> <cac:LineReference> <cbc:LineID>1</cbc:LineID> </cac:LineReference> <cac:Response> <cbc:ResponseCode>0000</cbc:ResponseCode> <cbc:Description>0</cbc:Description> </cac:Response> </cac:LineResponse> <cac:LineResponse> <cac:LineReference> <cbc:LineID>2</cbc:LineID> </cac:LineReference> <cac:Response> <cbc:ResponseCode>NIE901</cbc:ResponseCode> 

<cbc:Description>Error al validar regla Nómina Individual Electrónica - NominaIndividual (raíz): Namespace prefix 'xmlns' has not been declared</cbc:Description> 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 117 de 269 

® 



<!-- Start of picture text -->
) | Ma.IN<br><!-- End of picture text -->

POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
i esElemprendimientode todos | \jinhacienda<br><!-- End of picture text -->

**Resolución No. 000013** 





(11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

### 4. Inconvenientes tecnológicos. 

### 4.1. Por parte del Sujeto Obligado. 

Cuando se presenten inconvenientes tecnológicos por parte del sujeto obligado que impidan la transmisión de la información para la validación, el Documento Soporte de Pago de Nómina Electrónica se deberá trasmitir en un plazo máximo de cuarenta y ocho (48) horas contadas a partir del día siguiente al que se haya superado el inconveniente tecnológico. 

### 4.2. Por parte de la DIAN. 

Los sujetos obligados que utilicen los servicios del Documento Soporte de Pago de Nómina Electrónica que la DIAN disponga, podrán establecer automáticamente el procedimiento para establecer si la DIAN presenta inconvenientes tecnológicos,  señalado en la presente resolución, si se cumplen las siguientes condiciones: 

- Detección del error “500 – Internal Server Error” o “503 – Service Unavailable” o error “507 – Insufficient Storage” o error “508 - Loop Detected” o error “403 Site Disabled”. Únicamente estos errores. 

- Transmitir nuevamente a la DIAN el  Documento Soporte de Pago de Nómina Electrónica transcurridos 20 segundos después de la detección del error “500 – Internal Server Error” o “503 – Service Unavailable” o error “507 – Insufficient Storage” o error “508 - Loop Detected”. Si persiste el error, se deben realizar dos (2) intentos más, cada uno en intervalo de 20 segundos. Al finalizar el último intento, es decir un minuto después de la transmisión inicial y si persiste la condición de error, el Sujeto Obligado deberá esperar a que se restablezca el servicio de recepción del Documento Soporte de Pago de Nómina Electrónica para continuar con la transmisión de las mismas. 

- Mantener o archivar las evidencias del error “500 – Internal Server Error” o “503 – Service Unavailable” o error “507 – Insufficient Storage” o error “508 - Loop Detected” en sus registros digitales. 

- Monitorear la conexión y los servicios web de la DIAN del Documento Soporte de Pago de Nómina Electrónica a los 30 minutos después de haber recibido el primer mensaje (500 o 503), con el fin de identificar el restablecimiento del servicio por parte de la DIAN. Mientras que el servicio no este restablecido, continuar el monitoreo de la conexión y los servicios web de la DIAN del Documento Soporte de Pago de Nómina Electrónica. 

- Si el servicio está restablecido, transmitir normalmente el Documento Soporte de Pago de Nómina Electrónica. 

- El Sujeto Obligado tendrá 48 horas para transmitir a la DIAN el Documento Soporte de Pago de Nómina Electrónica, una vez el emisor de nómina detecte que el servicio de la DIAN está activo. 

### 5. Tablas de Contenidos de Elementos y de Atributos. 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 119 de 269 

**Resolución No. 000013** 





### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

### 5.1. Códigos Relacionados con Documentos. 

### _5.1.1._ Ambiente de Destino del Documento: _Ambiente._ 

Documentos enviados para el ambiente de pruebas no producen ningún tipo de efecto; documentos enviados para el ambiente de producción producen efectos para todas las finalidades legales: tributarios, financieros, económicos, comerciales y de del derecho del consumidor. 

|_Código _|_Ambiente de Destino_|
|---|---|
|1|Producción|
|2|Pruebas|



### _5.1.2._ Algoritmo: _EncripCUNE._ 

#### 5.1.2.1. <u>Algoritmo de CUNE: EncripCUNE.</u> 

Algoritmo utilizado para cálculo del Código Único de Documento Soporte de Pago de Nómina Electrónica. 

|_Código _|
|---|
|CUNE-SHA384|



### 5.2. Códigos para identificación fiscal. 

### _5.2.1._ Documento de identificación (Tipo de Identificador Fiscal): _TipoDocumento._ 

|_Código _|_Significado_|
|---|---|
|11|Registro civil|
|12|Tarjeta de identidad|
|13|Cédula de ciudadanía|
|21|Tarjeta de extranjería|
|22|Cédula de extranjería|
|31|NIT|
|41|Pasaporte|
|42|Documento de identificación extranjero|
|47|PEP|
|50|NIT de otropaís|
|91|NUIP *|



* Deberá utilizarse solamente para el empleado, debido a que este tipo de documento no pertenece a los tipos de documento en la base de datos del RUT 

> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Página 120 de 269 

r 

> me 6esElemprendimientodeElemprendimientodede todos | jyinhacienda 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientodeElemprendimientodede todos | jyinhacienda<br><!-- End of picture text -->

sm esElemprendimientodeElemprendimientodede todos | Winhacienda 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
sm esElemprendimientodeElemprendimientodede todos | Winhacienda<br><!-- End of picture text -->

scm esElemprendimientodeElemprendimientodede todos | Winhacienda 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
scm esElemprendimientodeElemprendimientodede todos | Winhacienda<br><!-- End of picture text -->

**Resolución No. 000013** 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_Nombre de idioma_|_ISO 639-1_|_ISO 639-2_|_Nombre de idioma_|_ISO 639-1_|_ISO 639-2_|
|---|---|---|---|---|---|
|Corea|ko|kor|Wolof|wo|wol|
|Kurdo|ku|kur|Oeste de Frisia|fy|fry|
|Kwanyama,<br>Kuanyama|kj|kua|Xhosa|xh|xho|
|Latin|la|lat|Yiddish|yi|yid|
|Luxemburgués,<br>Luxemburgués|lb|ltz|Yoruba|yo|yor|
|Luganda|lg|lug|Zhuang,Chuang|za|zha|
|Limburgués,<br>Limburgan,<br>Limburger|li|lim|Zulu|zu|zul|



### 5.3.2. Moneda (ISO 4217): _TipoMoneda._ 

El estándar internacional ISO 4217 fue creado por la ISO con el objetivo de definir códigos de tres letras para todas las divisas del mundo. Las dos primeras letras del código son las dos letras del código del país de la divisa según el estándar ISO 3166-1 y la tercera es normalmente la inicial de la divisa en sí. 

|_Código _|_Divisa_|_Paísesque Adoptan_|
|---|---|---|
|AED|Dírham de los Emiratos<br>Árabes Unidos|Emiratos Árabes Unidos|
|AFN|Afgani|Afganistán|
|ALL|Lek|Albania|
|AMD|Dram armenio|Armenia|
|ANG|Florín antillano neerlandés|Curazao,Saint Maarten|
|AOA|Kwanza|Angola|
|ARS|Peso argentino|Argentina|
|AUD|Dólar australiano|Australia, Isla de Navidad, Islas Cocos, Islas Heard y McDonald, Kiribati,<br>Nauru,Norfolk,Tuvalu|
|AWG|Florín arubeño|Aruba|
|AZN|Manat azerbaiyano|Azerbaiyán|
|BAM|Marco convertible|BosniayHerzegovina|
|BBD|Dólar de Barbados|Barbados|
|BDT|Taka|Bangladés|
|BGN|Lev búlgaro|Bulgaria|
|BHD|Dinar bareiní|Baréin|
|BIF|Franco de Burundi|Burundi|
|BMD|Dólar bermudeño|Bermudas|
|BND|Dólar de Brunéi|Brunéi|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 124 de 269 



### **Resolución No. 000013** 



(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_Código _|_Divisa_|_Paísesque Adoptan_|
|---|---|---|
|BOB|Boliviano|Bolivia|
|BOV|MVDOL|Bolivia|
|BRL|Real brasileño|Brasil|
|BSD|Dólar bahameño|Bahamas|
|BTN|Ngultrum|Bután|
|BWP|Pula|Botsuana|
|BYR|Rublo bielorruso|Bielorrusia|
|BZD|Dólar beliceño|Belice|
|CAD|Dólar canadiense|Canadá|
|CDF|Franco congoleño|República Democrática del Congo|
|CHE|Euro WIR|Suiza|
|CHF|Franco suizo|Liechtenstein,Suiza|
|CHW|Franco WIR|Suiza|
|CLF|Unidad de fomento|Chile|
|CLP|Peso chileno|Chile|
|CNY|Yuan chino|China|
|COP|Peso colombiano|Colombia|
|COU|Unidad de valor real|Colombia|
|CRC|Colón costarricense|Costa Rica|
|CUC|Peso convertible|Cuba|
|CUP|Peso cubano|Cuba|
|CVE|Escudo caboverdiano|Cabo Verde|
|CZK|Corona checa|República Checa|
|DJF|Francoyibutiano|Yibuti|
|DKK|Corona danesa|Dinamarca,Groenlandia,Islas Feroe|
|DOP|Peso dominicano|República Dominicana|
|DZD|Dinar argelino|Argelia|
|EGP|Libra egipcia|Egipto|
|ERN|Nakfa|Eritrea|
|ETB|Birr etíope|Etiopía|
|EUR|Euro|Alemania, Andorra, Austria, Bélgica, Chipre, Ciudad del Vaticano,<br>Eslovaquia, Eslovenia, España, Estonia, Finlandia, Francia, Grecia,<br>Guadalupe, Guayana Francesa, Irlanda, Italia, Letonia, Lituania,<br>Luxemburgo, Malta, Martinica, Mayotte, Mónaco, Montenegro, Países<br>Bajos, Portugal, Reunión, San Bartolomé, San Marino, San Martín, San<br>Pedro y Miquelón, Tierras Australes y Antárticas Francesas, Unión<br>Europea|
|FJD|Dólar fiyiano|Fiyi|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 125 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_Código _|_Divisa_|_Paísesque Adoptan_|
|---|---|---|
|FKP|Libra malvinense|Islas Malvinas|
|GBP|Libra esterlina|Guernsey,Isla de Man,Jersey,Reino Unido|
|GEL|Lari|Georgia|
|GHS|Cedighanés|Ghana|
|GIP|Libra de Gibraltar|Gibraltar|
|GMD|Dalasi|Gambia|
|GNF|Francoguineano|Guinea|
|GTQ|Quetzal|Guatemala|
|GYD|Dólarguyanés|Guyana|
|HKD|Dólar de HongKong|HongKong|
|HNL|Lempira|Honduras|
|HRK|Kuna|Croacia|
|HTG|Gourde|Haití|
|HUF|Forinto|Hungría|
|IDR|Rupia indonesia|Indonesia|
|ILS|Nuevo shéquel israelí|Israel|
|INR|Rupia india|Bután,India|
|IQD|Dinar iraquí|Irak|
|IRR|Rial iraní|Irán|
|ISK|Corona islandesa|Islandia|
|JMD|Dólarjamaiquino|Jamaica|
|JOD|Dinarjordano|Jordania|
|JPY|Yen|Japón|
|KES|Chelín keniano|Kenia|
|KGS|Som|Kirguistán|
|KHR|Riel|Camboya|
|KMF|Franco comorense|Comoras|
|KPW|Won norcoreano|Corea del Norte|
|KRW|Won|Corea del Sur|
|KWD|Dinar kuwaití|Kuwait|
|KYD|Dólar de las Islas Caimán|Islas Caimán|
|KZT|Tenge|Kazajistán|
|LAK|Kip|Laos|
|LBP|Libra libanesa|Líbano|
|LKR|Rupia de Sri Lanka|Sri Lanka|
|LRD|Dólar liberiano|Liberia|
|LSL|Loti|Lesoto|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 126 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_Código _|_Divisa_|_Paísesque Adoptan_|
|---|---|---|
|LYD|Dinar libio|Libia|
|MAD|Dírham marroquí|Marruecos,República Árabe Saharaui Democrática|
|MDL|Leu moldavo|Moldavia|
|MGA|Ariarymalgache|Madagascar|
|MKD|Denar|Macedonia|
|MMK|Kyat|Myanmar|
|MNT|Tugrik|Mongolia|
|MOP|Pataca|Macao|
|MRO|Uguiya|Mauritania|
|MUR|Rupia de Mauricio|Mauricio|
|MVR|Rufiyaa|Maldivas|
|MWK|Kwacha|Malaui|
|MXN|Peso mexicano|México|
|MXV|Unidad de Inversión (UDI)<br>mexicana|México|
|MYR|Ringgit malayo|Malasia|
|MZN|Metical mozambiqueño|Mozambique|
|NAD|Dólar namibio|Namibia|
|NGN|Naira|Nigeria|
|NIO|Córdoba|Nicaragua|
|NOK|Corona noruega|Isla Bouvet,Noruega,SvalbardyJan Mayen|
|NPR|Rupia nepalí|Nepal|
|NZD|Dólar neozelandés|Islas Cook,Islas Pitcairn,Niue,Nueva Zelanda,Tokelau|
|OMR|Rial omaní|Omán|
|PAB|Balboa|Panamá|
|PEN|Sol|Perú|
|PGK|Kina|Papúa Nueva Guinea|
|PHP|Peso filipino|Filipinas|
|PKR|Rupiapakistaní|Pakistán|
|PLN|Złoty|Polonia|
|PYG|Guaraní|Paraguay|
|QAR|Riyalqatarí|Catar|
|RON|Leu rumano|Rumania|
|RSD|Dinar serbio|Serbia|
|RUB|Rublo ruso|Rusia|
|RWF|Franco ruandés|Ruanda|
|SAR|Riyal saudí|Arabia Saudita|
|SBD|Dólar de las Islas Salomón|Islas Salomón|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 127 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_Código _|_Divisa_|_Paísesque Adoptan_|
|---|---|---|
|SCR|Rupia seychelense|Seychelles|
|SDG|Dinar sudanés|Sudán|
|SEK|Corona sueca|Suecia|
|SGD|Dólar de Singapur|Singapur|
|SHP|Libra de Santa Elena|Santa Elena,AscensiónyTristán de Acuña|
|SLL|Leone|Sierra Leona|
|SOS|Chelín somalí|Somalia|
|SRD|Dólar surinamés|Surinam|
|SSP|Libra sursudanesa|Sudán del Sur|
|STD|Dobra|Santo ToméyPríncipe|
|SVC|Colon Salvadoreño|El Salvador|
|SYP|Libra siria|Siria|
|SZL|Lilangeni|Suazilandia|
|THB|Baht|Tailandia|
|TJS|Somoni tayiko|Tayikistán|
|TMT|Manat turcomano|Turkmenistán|
|TND|Dinar tunecino|Túnez|
|TOP|Paʻanga|Tonga|
|TRY|Lira turca|Turquía|
|TTD|Dólar de TrinidadyTobago|TrinidadyTobago|
|TWD|Nuevo dólar taiwanés|República de China|
|TZS|Chelín tanzano|Tanzania|
|UAH|Grivna|Ucrania|
|UGX|Chelín ugandés|Uganda|
|USD|Dólar estadounidense|Caribe Neerlandés, Ecuador, El Salvador, Estados Unidos, Guam, Haití,<br>Islas Marianas del Norte, Islas Marshall, Islas Turcas y Caicos, Islas<br>ultramarinas de Estados Unidos, Islas Vírgenes Británicas, Islas Vírgenes<br>de los Estados Unidos, Micronesia, Palaos, Panamá, Puerto Rico, Samoa<br>Americana,Territorio Británico del Océano Índico,Timor Oriental|
|USN|Dólar estadounidense<br>(Siguiente día)|Estados Unidos|
|UYI|Peso en Unidades<br>Indexadas(Uruguay)|Uruguay|
|UYU|Peso uruguayo|Uruguay|
|UZS|Som uzbeko|Uzbekistán|
|VEF|Bolívar|Venezuela|
|VES|Bolívar soberano|Venezuela|
|VND|Dongvietnamita|Vietnam|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 128 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_Código _|_Divisa_|_Paísesque Adoptan_|
|---|---|---|
|VUV|Vatu|Vanuatu|
|WST|Tala|Samoa|
|XAF|Franco CFA de África<br>Central|Camerún, Chad, Gabón, Guinea Ecuatorial, República Centroafricana,<br>República del Congo|
|XAG|Plata(una onza troy)||
|XAU|Oro(una onza troy)||
|XBA|Unidad compuesta<br>europea (EURCO) (Unidad<br>del mercado de bonos)||
|XBB|Unidad Monetaria europea<br>(E.M.U.-6) (Unidad del<br>mercado de bonos)||
|XBC|Unidad europea de cuenta<br>9 (E.U.A.-9) (Unidad del<br>mercado de bonos)||
|XBD|Unidad europea de cuenta<br>17 (E.U.A.-17) (Unidad del<br>mercado de bonos)||
|XCD|Dólar del Caribe Oriental|Anguila, Antigua y Barbuda, Dominica, Granada, Montserrat, San<br>CristóbalyNieves,San Vicenteylas Granadinas,Santa Lucía|
|XDR|Derechos especiales de<br>giro|Fondo Monetario Internacional|
|XOF|Franco CFA de África<br>Occidental|Benín, Burkina Faso, Costa de Marfil, Guinea-Bisáu, Malí, Níger, Senegal,<br>Togo|
|XPD|Paladio(una onza troy)||
|XPF|Franco CFP|Nueva Caledonia,Polinesia Francesa,WallisyFutuna|
|XPT|Platino(una onza troy)||
|XSU|SUCRE|Sistema Unitario de Compensación Regional|
|XTS|Reservadoparapruebas||
|XUA|Unidad de cuenta BAD|Banco Africano de Desarrollo|
|XXX|Sin divisa||
|YER|Rialyemení|Yemen|
|ZAR|Rand|Lesoto,Namibia,Sudáfrica|
|ZMW|Kwacha zambiano|Zambia|
|ZWL|Dólar zimbabuense|Zimbabue|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 129 de 269 



### **Resolución No. 000013** 



(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

### 5.3.3. Pagos. 

#### 5.3.3.1. <u>Formas de Pago:</u> _<u>Forma.</u>_ 

_<mark>Código Significado</mark>_ 1 Contado 

5.3.3.2. <u>Medios de Pago:</u> _<u>Metodo.</u>_ Definición de los atributos del elemento: 

|_Código _|<br>Definición de los atributos del elemento:<br>_Medio_|_Código _|_Medio_|
|---|---|---|---|
|1|Instrumento no definido|40|Débito Negocio Intercambio Corporativo(CTX)|
|2|Crédito ACH|41|Concentración efectivo/Desembolso Crédito<br>plus(CCD+)|
|3|Débito ACH|42|Consignación bancaria|
|4|Reversión débito de demanda ACH|43|Concentración efectivo / Desembolso Débito<br>plus(CCD+)|
|5|Reversión crédito de demanda ACH|44|Nota cambiaria|
|6|Crédito de demanda ACH|45|Transferencia Crédito Bancario|
|7|Débito de demanda ACH|46|Transferencia Débito Interbancario|
|8|Mantener|47|Transferencia Débito Bancaria|
|9|ClearingNacional o Regional|48|Tarjeta Crédito|
|10|Efectivo|49|Tarjeta Débito|
|11|Reversión Crédito Ahorro|50|Postgiro|
|12|Reversión Débito Ahorro|51|Telex estándar bancario francés|
|13|Crédito Ahorro|52|Pago comercial urgente|
|14|Débito Ahorro|53|Pago Tesorería Urgente|
|15|BookentryCrédito|60|Notapromisoria|
|16|BookentryDébito|61|Notapromisoria firmadapor el acreedor|
|17|Concentración de la demanda en efectivo<br>/Desembolso Crédito(CCD)|62|Nota promisoria firmada por el acreedor,<br>avaladapor el banco|
|18|Concentración de la demanda en efectivo /<br>Desembolso(CCD)débito|63|Nota promisoria firmada por el acreedor,<br>avaladapor un tercero|
|19|Crédito Pago negocio corporativo(CTP)|64|Notapromisoria firmadapor el banco|
|20|Cheque|65|Nota promisoria firmada por un banco avalada<br>por otro banco|
|21|Proyecto bancario|66|Notapromisoria firmada|
|22|Proyecto bancario certificado|67|Nota promisoria firmada por un tercero avalada<br>por un banco|
|23|Cheque bancario|70|Retiro de notapor elpor el acreedor|
|24|Nota cambiaria esperando aceptación|71|Bonos|
|25|Cheque certificado|72|Vales|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 130 de 269 

r 

me 6esElemprendimientodeElemprendimientodede todos | jyinhacienda 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientodeElemprendimientodede todos | jyinhacienda<br><!-- End of picture text -->

® 



<!-- Start of picture text -->
) | Ma. IN<br><!-- End of picture text -->

POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->



##### 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

- Código numérico: Código ISO numérico de este país o territorio. 

- Observaciones: Información adicional relativa a los códigos de este país o territorio. 

Debe ser utilizado el Código alfa-2 : Código ISO de 2 letras asignado a este país o territorio en los elementos Pais. 

Si @Idioma es “es”, debe ser utilizado el Nombre Común en los elementos Name; si @Idioma es otro idioma, n estos elementos. 

|_Nombre común_|_Nombre ISO oficial_<br>_delpaís o territorio_|_Código_<br>_alfa-2_|_Código_<br>_alfa-3_|_Código_<br>_numérico_|_Observaciones_|
|---|---|---|---|---|---|
|Afganistán|Afganistán|AF|AFG|004||
|Åland|Åland, Islas|AX|ALA|248|Es una provincia autónoma de<br>Finlandia.|
|Albania|Albania|AL|ALB|008||
|Alemania|Alemania|DE|DEU|276|Códigos obtenidos del idioma<br>nativo (alemán): Deutschland<br><br>Códigos alfa usados por<br>Alemania Occidental antes de la<br>reunificación alemana en 1990.|
|Andorra|Andorra|AD|AND|020||
|Angola|Angola|AO|AGO|024||
|Anguila|Anguila|AI|AIA|660||
|Antártida|Antártida|AQ|ATA|010|Cubre el territorio al sur del<br>paralelo 60º sur.<br><br>Códigos obtenidos del<br>nombre en francés: Antarctique|
|AntiguayBarbuda|AntiguayBarbuda|AG|ATG|028||
|Arabia Saudita|Arabia Saudita|SA|SAU|682||
|Argelia|Argelia|DZ|DZA|012|Códigos obtenidos del idioma<br>nativo(cabilio): Dzayer|
|Argentina|Argentina|AR|ARG|032||
|Armenia|Armenia|AM|ARM|051||
|Aruba|Aruba|AW|ABW|533|Forma parte del Reino de los Países<br>Bajos.|
|Australia|Australia|AU|AUS|036|Incluye las Islas Ashmore y Cartier y<br>las Islas del Mar del Coral.|
|Austria|Austria|AT|AUT|040||
|Azerbaiyán|Azerbaiyán|AZ|AZE|031||
|Bahamas|Bahamas(las)|BS|BHS|044||
|Bangladés|Bangladesh|BD|BGD|050||



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 133 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_Nombre común_|_Nombre ISO oficial_<br>_delpaís o territorio_|_Código_<br>_alfa-2_|_Código_<br>_alfa-3_|_Código_<br>_numérico_|_Observaciones_|
|---|---|---|---|---|---|
|Barbados|Barbados|BB|BRB|052||
|Baréin|Bahrein|BH|BHR|048||
|Bélgica|Bélgica|BE|BEL|056||
|Belice|Belice|BZ|BLZ|084||
|Benín|Benin|BJ|BEN|204||
|Bermudas|Bermudas|BM|BMU|060||
|Bielorrusia|Belarús|BY|BLR|112|El nombre oficial del país es<br>Belarús, aunque tradicionalmente<br>se le sigue denominando<br>Bielorrusia.|
|Bolivia|Bolivia (Estado<br>Plurinacional de)|BO|BOL|068||
|Bonaire, San<br>Eustaquio y<br>Saba|Bonaire, San<br>Eustaquio y Saba|BQ|BES|535|Son tres municipios especiales que<br>forman parte de los Países Bajos.|
|Bosnia y Herzegovina|<sup>Bosnia y</sup><br>Herzegovina|BA|BIH|070||
|Botsuana|Botswana|BW|BWA|072||
|Brasil|Brasil|BR|BRA|076||
|Brunéi|Brunei Darussalam|BN|BRN|096||
|Bulgaria|Bulgaria|BG|BGR|100||
|Burkina Faso|Burkina Faso|BF|BFA|854||
|Burundi|Burundi|BI|BDI|108||
|Bután|Bhután|BT|BTN|064||
|Cabo Verde|Cabo Verde|CV|CPV|132||
|Camboya|Camboya|KH|KHM|116|Códigos obtenidos del anterior<br>nombre: Khmer Republic<br>(República Jemer)|
|Camerún|Camerún|CM|CMR|120||
|Canadá|Canadá|CA|CAN|124||
|Catar|Qatar|QA|QAT|634||
|Chad|Chad|TD|TCD|148|Códigos obtenidos del nombre en<br>francés: Tchad|
|Chile|Chile|CL|CHL|152||
|China|China|CN|CHN|156||
|Chipre|Chipre|CY|CYP|196||
|Colombia|Colombia|CO|COL|170||



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 134 de 269 



### **Resolución No. 000013** 



(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_Nombre común_|_Nombre ISO oficial_<br>_delpaís o territorio_|_Código_<br>_alfa-2_|_Código_<br>_alfa-3_|_Código_<br>_numérico_|_Observaciones_|
|---|---|---|---|---|---|
|Comoras|Comoras (las)|KM|CON|174|Códigos obtenidos del idioma<br>nativo(comorense): Komori|
|Corea del Norte|Corea (la República<br>Popular<br>Democrática de)|KP|PRK|408||
|Corea del Sur|Corea (la República<br>de)|KR|KOR|410||
|Costa de Marfil|Côte d’Ivoire|CI|CIV|384|Nombre oficial en la ISO en francés.|
|Costa Rica|Costa Rica|CR|CRI|188|Nombre oficial en la ISO en español.|
|Croacia|Croacia|HR|HRV|191|Códigos obtenidos del idioma<br>nativo(croata): Hrvatska|
|Cuba|Cuba|CU|CUB|192||
|Curazao|Curaçao|CW|CUW|531|Forma parte del Reino de los Países<br>Bajos.|
|Dinamarca|Dinamarca|DK|DNK|208||
|Dominica|Dominica|DM|DMA|212||
|Ecuador|Ecuador|EC|ECU|218||
|Egipto|Egipto|EG|EGY|818||
|El Salvador|El Salvador|SV|SLV|222|Nombre oficial en la ISO en español.|
|Emiratos Árabes<br>Unidos|Emiratos Árabes<br>Unidos(los)|AE|ARE|784||
|Eritrea|Eritrea|ER|ERI|232||
|Eslovaquia|Eslovaquia|SK|SVK|703||
|Eslovenia|Eslovenia|SI|SVN|705||
|España|España|ES|ESP|724|Códigos obtenidos del idioma<br>nativo(español): España|
|Estados Unidos|Estados Unidos de<br>América(los)|US|USA|840||
|Estonia|Estonia|EE|EST|233|Códigos obtenidos del idioma<br>nativo(estonio): Eesti|
|Etiopía|Etiopía|ET|ETH|231||
|Filipinas|Filipinas(las)|PH|PHL|608||
|Finlandia|Finlandia|FI|FIN|246||
|Fiyi|Fiji|FJ|FJI|242||
|Francia|Francia|FR|FRA|250|Incluye la Isla Clipperton.|
|Gabón|Gabón|GA|GAB|266||
|Gambia|Gambia(la)|GM|GMB|270||



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 135 de 269 



### **Resolución No. 000013** 



(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_Nombre común_|_Nombre ISO oficial_<br>_delpaís o territorio_|_Código_<br>_alfa-2_|_Código_<br>_alfa-3_|_Código_<br>_numérico_|_Observaciones_|
|---|---|---|---|---|---|
|Georgia|Georgia|GE|GEO|268||
|Ghana|Ghana|GH|GHA|288||
|Gibraltar|Gibraltar|GI|GIB|292|Pertenece al Reino Unido.|
|Granada|Granada|GD|GRD|308||
|Grecia|Grecia|GR|GRC|300||
|Groenlandia|Groenlandia|GL|GRL|304|Pertenece al Reino de Dinamarca.|
|Guadalupe|Guadeloupe|GP|GLP|312|Departamento de ultramar francés.<br>Nombre oficial en la ISO en francés.|
|Guam|Guam|GU|GUM|316|Territorio no incorporado de los<br>Estados Unidos.|
|Guatemala|Guatemala|GT|GTM|320||
|Guayana Francesa|Guayana Francesa|GF|GUF|254|Departamento de ultramar francés.<br><br>Códigos obtenidos del<br>nombre en francés: Guyane<br>française|
|Guernsey|Guernsey|GG|GGY|831|Una dependencia de la Corona<br>británica.|
|Guinea|Guinea|GN|GIN|324||
|Guinea-Bisáu|Guinea Bissau|GW|GNB|624||
|Guinea Ecuatorial|Guinea Ecuatorial|GQ|GNQ|226|Códigos obtenidos del nombre en<br>francés: Guinée équatoriale|
|Guyana|Guyana|GY|GUY|328||
|Haití|Haití|HT|HTI|332||
|Honduras|Honduras|HN|HND|340||
|Hong Kong|Hong Kong|HK|HKG|344|Región administrativa especial de<br>China.|
|Hungría|Hungría|HU|HUN|348||
|India|India|IN|IND|356||
|Indonesia|Indonesia|ID|IDN|360||
|Irak|Iraq|IQ|IRQ|368||
|Irán|Irán (República<br>Islámica de)|IR|IRN|364||
|Irlanda|Irlanda|IE|IRL|372||
|Isla Bouvet|Bouvet,Isla|BV|BVT|074|Pertenece a Noruega.|
|Isla de Man|Isla de Man|IM|IMN|833|Una dependencia de la Corona<br>británica.|
|Isla de Navidad|Navidad,Isla de|CX|CXR|162|Pertenece a Australia.|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 136 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_Nombre común_|_Nombre ISO oficial_<br>_delpaís o territorio_|_Código_<br>_alfa-2_|_Código_<br>_alfa-3_|_Código_<br>_numérico_|_Observaciones_|
|---|---|---|---|---|---|
||||||Códios obtenidos del idioma|
|Islandia|Islandia|IS|ISL|352|g<br>nativo(islandés): Ísland|
|Islas Caimán|Caimán, (las)Islas|KY|CYM|136||
|Islas Cocos|Cocos / Keeling,<br>(las)Islas|CC|CCK|166|Pertenecen a Australia.|
|Islas Cook|Cook, (las)Islas|CK|COK|184||
|Islas Feroe|Feroe, (las)Islas|FO|FRO|234|Pertenecen al Reino de Dinamarca.|
|Islas Georgias del Sur|Georgia del Sur (la)|||||
|y Sandwich del<br>Sur|y las Islas Sandwich<br>del Sur|GS|SGS|239||
|Islas Heard y<br>McDonald|Heard (Isla) e Islas<br>McDonald|HM|HMD|334|Pertenecen a Australia.|
|Islas Malvinas|Malvinas<br>[Falkland], (las)<br>Islas|FK|FLK|238|Códigos obtenidos del nombre en<br>(inglés): Falkland|
|Islas Marianas del<br>Norte|Marianas del<br>Norte, (las)Islas|MP|MNP|580|Territorio no incorporado de los<br>Estados Unidos.|
|Islas Marshall|Marshall, (las)Islas|MH|MHL|584||
|Islas Pitcairn|Pitcairn|PN|PCN|612||
|Islas Salomón|Salomón, Islas|SB|SLB|090|Códigos obtenidos de su anterior<br>nombre: British Solomon Islands|
|Islas Turcas y Caicos|Turcas y Caicos,<br>(las)Islas|TC|TCA|796||
|Islas ultramarinas de<br>Estados Unidos|Islas Ultramarinas<br>Menores de los<br>Estados Unidos<br>(las)|UM|UMI|581|Comprende nueve áreas insulares<br>menores de los Estados Unidos:<br>Arrecife Kingman, Atolón Johnston,<br>Atolón Palmyra, Isla Baker, Isla<br>Howland, Isla Jarvis, Islas Midway,<br>Isla de Navaza e Isla Wake.|
|Islas Vírgenes<br>Británicas|Vírgenes británicas,<br>Islas|VG|VGB|092||
|Islas Vírgenes de los<br>Estados Unidos|Vírgenes de los<br>Estados Unidos,<br>Islas|VI|VIR|850|Territorio no incorporado de los<br>Estados Unidos.|
|Israel|Israel|IL|ISR|376||
|Italia|Italia|IT|ITA|380||
|Jamaica|Jamaica|JM|JAM|388||



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 137 de 269 



### **Resolución No. 000013** 



(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_Nombre común_|_Nombre ISO oficial_<br>_delpaís o territorio_|_Código_<br>_alfa-2_|_Código_<br>_alfa-3_|_Código_<br>_numérico_|_Observaciones_|
|---|---|---|---|---|---|
|Japón|Japón|JP|JPN|392||
|Jersey|Jersey|JE|JEY|832|Una dependencia de la Corona<br>británica.|
|Jordania|Jordania|JO|JOR|400||
|Kazajistán|Kazajstán|KZ|KAZ|398||
|Kenia|Kenya|KE|KEN|404||
|Kirguistán|Kirguistán|KG|KGZ|417||
|Kiribati|Kiribati|KI|KIR|296||
|Kuwait|Kuwait|KW|KWT|414||
|Laos|Lao, (la) República<br>Democrática<br>Popular|LA|LAO|418||
|Lesoto|Lesotho|LS|LSO|426||
|Letonia|Letonia|LV|LVA|428||
|Líbano|Líbano|LB|LBN|422||
|Liberia|Liberia|LR|LBR|430||
|Libia|Libia|LY|LBY|434||
|Liechtenstein|Liechtenstein|LI|LIE|438||
|Lituania|Lituania|LT|LTU|440||
|Luxemburgo|Luxemburgo|LU|LUX|442||
|Macao|Macao|MO|MAC|446|Región administrativa especial de<br>China.|
|Macedonia|Macedonia (la ex<br>República<br>Yugoslava de)|MK|MKD|807|Códigos obtenidos del idioma<br>nativo (macedonio): Makedonija|
|Madagascar|Madagascar|MG|MDG|450||
|Malasia|Malasia|MY|MYS|458||
|Malaui|Malawi|MW|MWI|454||
|Maldivas|Maldivas|MV|MDV|462||
|Malí|Malí|ML|MLI|466||
|Malta|Malta|MT|MLT|470||
|Marruecos|Marruecos|MA|MAR|504|Códigos obtenidos del nombre en<br>francés: Maroc|
|Martinica|Martinique|MQ|MTQ|474|Departamento de ultramar francés.<br>Nombre oficial en la ISO en francés.|
|Mauricio|Mauricio|MU|MUS|480||
|Mauritania|Mauritania|MR|MRT|478||



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 138 de 269 



### **Resolución No. 000013** 



(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_Nombre común_|_Nombre ISO oficial_<br>_delpaís o territorio_|_Código_<br>_alfa-2_|_Código_<br>_alfa-3_|_Código_<br>_numérico_|_Observaciones_|
|---|---|---|---|---|---|
|Mayotte|Mayotte|YT|MYT|175|Departamento de ultramar francés.|
|México|México|MX|MEX|484||
|Micronesia|Micronesia<br>(Estados Federados<br>de)|FM|FSM|583||
|Moldavia|Moldova (la<br>República de)|MD|MDA|498||
|Mónaco|Mónaco|MC|MCO|492||
|Mongolia|Mongolia|MN|MNG|496||
|Montenegro|Montenegro|ME|MNE|499||
|Montserrat|Montserrat|MS|MSR|500||
|Mozambique|Mozambique|MZ|MOZ|508||
|Myanmar|Myanmar|MM|MMR|104|Anteriormente conocida como<br>Birmania.|
|Namibia|Namibia|NA|NAM|516||
|Nauru|Nauru|NR|NRU|520||
|Nepal|Nepal|NP|NPL|524||
|Nicaragua|Nicaragua|NI|NIC|558||
|Níger|Níger(el)|NE|NER|562||
|Nigeria|Nigeria|NG|NGA|566||
|Niue|Niue|UN|NIU|570|Asociado a Nueva Zelanda.|
|Norfolk|Norfolk,Isla|NF|NFK|574|Pertenece a Australia.|
|Noruega|Noruega|NO|NOR|578||
|Nueva Caledonia|Nueva Caledonia|NC|NCL|540||
|Nueva Zelanda|Nueva Zelandia|NZ|NZL|554||
|Omán|Omán|OM|OMN|512||
|Países Bajos|Países Bajos (los)|NL|NLD|528|Forma parte del Reino de los Países<br>Bajos.|
|Pakistán|Pakistán|PK|PAK|586||
|Palaos|Palau|PW|PLW|585||
|Palestina|Palestina, Estado<br>de|PS|PSE|275|Comprende los territorios de<br>CisjordaniayFranja de Gaza.|
|Panamá|Panamá|PA|PAN|591||
|Papúa Nueva Guinea|Papua Nueva<br>Guinea|PG|PNG|598||
|Paraguay|Paraguay|PY|PRY|600||
|Perú|Perú|PE|PER|604||



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 139 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_Nombre común_|_Nombre ISO oficial_<br>_delpaís o territorio_|_Código_<br>_alfa-2_|_Código_<br>_alfa-3_|_Código_<br>_numérico_|_Observaciones_|
|---|---|---|---|---|---|
||||||Códios obtenidos del nombre en|
|Polinesia Francesa|Polinesia Francesa|PF|PYF|258|g<br>francés: Polynésie française|
|Polonia|Polonia|PL|POL|616||
|Portugal|Portugal|PT|PRT|620||
|Puerto Rico|Puerto Rico|PR|PRI|630|Territorio no incorporado de los<br>Estados Unidos. Nombre oficial en<br>la ISO en español.|
|Reino Unido|Reino Unido de<br>Gran Bretaña e<br>Irlanda del Norte<br>(el)|GB|GBR|826|Debido a que para obtener los<br>códigos ISO no se utilizan las<br>palabras comunes de Reino y<br>Unido, los códigos se han obtenido<br>a partir del resto del nombre<br>oficial.|
|República Árabe<br>Saharaui<br>Democrática|Sahara Occidental|EH|ESH|732|Nombre provisional. Anterior<br>nombre en la ISO: Sahara español<br><br>Códigos obtenidos del<br>anterior nombre en español|
|República<br>Centroafricana|República<br>Centroafricana(la)|CF|CAF|140||
|República Checa|Chequia|CZ|CZE|203||
|República del Congo|Congo(el)|CG|COG|178||
|República<br>Democrática<br>del Congo|Congo (la República<br>Democrática del)|CD|COD|180||
|República<br>Dominicana|Dominicana, (la)<br>República|DO|DOM|214||
|Reunión|Reunión|RE|REU|638|Departamento de ultramar francés.|
|Ruanda|Rwanda|RW|RWA|646||
|Rumania|Rumania|RO|ROU|642||
|Rusia|Rusia, (la)<br>Federación de|RU|RUS|643||
|Samoa|Samoa|WS|WSM|882|Códigos obtenidos del anterior<br>nombre: Western Samoa (Samoa<br>Occidental)|
|Samoa Americana|Samoa Americana|AS|ASM|016|Territorio no incorporado de los<br>Estados Unidos.|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 140 de 269 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 

r 

me 6esElemprendimientodeElemprendimientodede todos | jyinhacienda 



<!-- Start of picture text -->
r me 6esElemprendimientodeElemprendimientodede todos | jyinhacienda<br><!-- End of picture text -->



### **Resolución No. 000013** 



(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_Nombre común_|_Nombre ISO oficial_<br>_delpaís o territorio_|_Código_<br>_alfa-2_|_Código_<br>_alfa-3_|_Código_<br>_numérico_|_Observaciones_|
|---|---|---|---|---|---|
|Suecia|Suecia|SE|SWE|752||
|Suiza|Suiza|CH|CHE|756|Códigos obtenidos del nombre en<br>latín: Confoederatio Helvetica|
|Surinam|Suriname|SR|SUR|740||
|Svalbard y Jan<br>Mayen|Svalbard y Jan<br>Mayen|SJ|SJM|744|Comprende dos territorios árticos<br>de Noruega: SvalbardyJan Mayen.|
|Tailandia|Tailandia|TH|THA|764||
|Taiwán (República de<br>China)|Taiwán (Provincia<br>de China)|TW|TWN|158|Cubre la jurisdicción actual de la<br>República de China (Taiwán),<br>excepto Kinmen e Islas Matsu.<br><br>La ONU considera a Taiwán<br>como una provincia de China,<br>debido a su estatuspolítico|
|Tanzania|Tanzania, República<br>Unida de|TZ|TZA|834||
|Tayikistán|Tayikistán|TJ|TJK|762||
|Territorio Británico<br>del Océano Índico|Territorio Británico<br>del Océano Índico<br>(el)|IO|IOT|086||
|Tierras Australes y<br>Antárticas Francesas|Tierras Australes<br>Francesas (las)|TF|ATF|260|Comprende las tierras australes y<br>antárticas francesas excepto la<br>parte incluida en la Antártida<br>conocida como Tierra Adelia.<br><br>Códigos obtenidos del<br>nombre en francés: Terres<br>australes françaises.|
|Timor Oriental|Timor-Leste|TL|TLS|626|Nombre oficial en la ISO en<br>portugués.|
|Togo|Togo|TG|TGO|768||
|Tokelau|Tokelau|TK|TKL|772||
|Tonga|Tonga|TO|TON|776||
|TrinidadyTobago|TrinidadyTobago|TT|TTO|780||
|Túnez|Túnez|TN|TUN|788||
|Turkmenistán|Turkmenistán|TM|TKM|795||
|Turquía|Turquía|TR|TUR|792||
|Tuvalu|Tuvalu|TV|TUV|798||
|Ucrania|Ucrania|UA|UKR|804||



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 142 de 269 



##### 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_Nombre común_|_Nombre ISO oficial_<br>_delpaís o territorio_|_Código_<br>_alfa-2_|_Código_<br>_alfa-3_|_Código_<br>_numérico_|_Observaciones_|
|---|---|---|---|---|---|
|Uganda|Uganda|UG|UGA|800||
|Uruguay|Uruguay|UY|URY|858||
|Uzbekistán|Uzbekistán|UZ|UZB|860||
|Vanuatu|Vanuatu|VU|VUT|548||
|Vaticano, Ciudad del|Santa Sede (la)|VA|VAT|336|La Santa Sede es la representante<br>diplomática del Estado de la Ciudad<br>del Vaticanoante la ONU y otros<br>países y organismos<br>internacionales, aunque<br>jurídicamente se trata de entes<br>distintos. Los códigos ISO se<br>asignan a la Santa Sede como<br>representante de este Estado, pero<br>se refieren al territorio del Estado<br>de la Ciudad del Vaticano.|
|Venezuela|Venezuela<br>(República<br>Bolivariana de)|VE|VEN|862||
|Vietnam|Viet Nam|VN|VNM|704||
|WallisyFutuna|WallisyFutuna|WF|WLF|876|Colectividad de ultramar francesa.|
|Yemen|Yemen|YE|YEM|887||
|Yibuti|Djibouti|DJ|DJI|262||
|Zambia|Zambia|ZM|ZMB|894||
|Zimbabue|Zimbabwe|ZW|ZWE|716||



### 5.4.2. Departamentos (ISO 3166-2:CO): _Departamento._ 

ISO 3166-2:CO es la serie de códigos ISO 3166-2 correspondientes a Colombia.  En ella se incluyen las 33 subdivisiones administrativas del país. Fue publicada en 1998 y actualizada por última vez en el sexto boletín de la primera edición en 2004. 

|_Código _|_Nombre_|_Código ISO_|_Código _|_Nombre_|_Código ISO_|
|---|---|---|---|---|---|
|91|Amazonas|AMA|41|Huila|HUI|
|05|Antioquia|ANT|44|La Guajira|LAG|
|81|Arauca|ARA|47|Magdalena|MAG|
|08|Atlántico|ATL|50|Meta|MET|
|11|Bogotá|DC|52|Nariño|NAR|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 143 de 269 



### **Resolución No. 000013** 



(11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|13|Bolívar|BOL|54|Norte de Santander|NSA|
|---|---|---|---|---|---|
|15|Boyacá|BOY|86|Putumayo|PUT|
|17|Caldas|CAL|63|Quindío|QUI|
|18|Caquetá|CAQ|66|Risaralda|RIS|
|85|Casanare|CAS|88|San AndrésyProvidencia|SAP|
|19|Cauca|CAU|68|Santander|SAN|
|20|Cesar|CES|70|Sucre|SUC|
|27|Chocó|CHO|73|Tolima|TOL|
|23|Córdoba|COR|76|Valle del Cauca|VAC|
|25|Cundinamarca|CUN|97|Vaupés|VAU|
|94|Guainía|GUA|99|Vichada|VID|
|95|Guaviare|GUV||||



### 5.4.3. Municipios: _Municipio._ 

Fuente: Departamento Administrativo Nacional de Estadística (DANE), entidad responsable de la planeación, levantamiento, procesamiento, análisis y difusión de las estadísticas oficiales de Colombia. 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|91|91001|Amazonas|LETICIA|
|91|91263|Amazonas|EL ENCANTO|
|91|91405|Amazonas|LA CHORRERA|
|91|91407|Amazonas|LA PEDRERA|
|91|91430|Amazonas|LA VICTORIA|
|91|91460|Amazonas|MIRITÍ – PARANÁ|
|91|91530|Amazonas|PUERTO ALEGRÍA|
|91|91536|Amazonas|PUERTO ARICA|
|91|91540|Amazonas|PUERTO NARIÑO|
|91|91669|Amazonas|PUERTO SANTANDER|
|91|91798|Amazonas|TARAPACÁ|
|05|05001|Antioquia|MEDELLÍN|
|05|05002|Antioquia|ABEJORRAL|
|05|05004|Antioquia|ABRIAQUÍ|
|05|05021|Antioquia|ALEJANDRÍA|
|05|05030|Antioquia|AMAGÁ|
|05|05031|Antioquia|AMALFI|
|05|05034|Antioquia|ANDES|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 144 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|05|05036|Antioquia|ANGELÓPOLIS|
|05|05038|Antioquia|ANGOSTURA|
|05|05040|Antioquia|ANORÍ|
|05|05042|Antioquia|SANTA FÉ DE ANTIOQUIA|
|05|05044|Antioquia|ANZÁ<br>|
|05|05045|Antioquia|APARTADÓ|
|05|05051|Antioquia|ARBOLETES|
|05|05055|Antioquia|ARGELIA|
|05|05059|Antioquia|ARMENIA|
|05|05079|Antioquia|BARBOSA|
|05|05086|Antioquia|BELMIRA|
|05|05088|Antioquia|BELLO|
|05|05091|Antioquia|BETANIA|
|05|05093|Antioquia|BETULIA|
|05|05101|Antioquia|CIUDAD BOLÍVAR|
|05|05107|Antioquia|BRICEÑO|
|05|05113|Antioquia|BURITICÁ|
|05|05120|Antioquia|CÁCERES|
|05|05125|Antioquia|CAICEDO|
|05|05129|Antioquia|CALDAS|
|05|05134|Antioquia|CAMPAMENTO|
|05|05138|Antioquia|CAÑASGORDAS|
|05|05142|Antioquia|CARACOLÍ|
|05|05145|Antioquia|CARAMANTA|
|05|05147|Antioquia|CAREPA|
|05|05148|Antioquia|EL CARMEN DE VIBORAL|
|05|05150|Antioquia|CAROLINA|
|05|05154|Antioquia|CAUCASIA|
|05|05172|Antioquia|CHIGORODÓ|
|05|05190|Antioquia|CISNEROS|
|05|05197|Antioquia|COCORNÁ|
|05|05206|Antioquia|CONCEPCIÓN|
|05|05209|Antioquia|CONCORDIA|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 145 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|05|05212|Antioquia|COPACABANA|
|05|05234|Antioquia|DABEIBA|
|05|05237|Antioquia|DONMATÍAS|
|05|05240|Antioquia|EBÉJICO|
|05|05250|Antioquia|EL BAGRE<br>|
|05|05264|Antioquia|ENTRERRÍOS|
|05|05266|Antioquia|ENVIGADO|
|05|05282|Antioquia|FREDONIA|
|05|05284|Antioquia|FRONTINO|
|05|05306|Antioquia|GIRALDO|
|05|05308|Antioquia|GIRARDOTA|
|05|05310|Antioquia|GÓMEZ PLATA|
|05|05313|Antioquia|GRANADA|
|05|05315|Antioquia|GUADALUPE|
|05|05318|Antioquia|GUARNE|
|05|05321|Antioquia|GUATAPÉ|
|05|05347|Antioquia|HELICONIA|
|05|05353|Antioquia|HISPANIA|
|05|05360|Antioquia|ITAGÜÍ|
|05|05361|Antioquia|ITUANGO|
|05|05364|Antioquia|JARDÍN|
|05|05368|Antioquia|JERICÓ|
|05|05376|Antioquia|LA CEJA|
|05|05380|Antioquia|LA ESTRELLA|
|05|05390|Antioquia|LA PINTADA|
|05|05400|Antioquia|LA UNIÓN|
|05|05411|Antioquia|LIBORINA|
|05|05425|Antioquia|MACEO|
|05|05440|Antioquia|MARINILLA|
|05|05467|Antioquia|MONTEBELLO|
|05|05475|Antioquia|MURINDÓ|
|05|05480|Antioquia|MUTATÁ|
|05|05483|Antioquia|NARIÑO|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 146 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|05|05490|Antioquia|NECOCLÍ|
|05|05495|Antioquia|NECHÍ|
|05|05501|Antioquia|OLAYA|
|05|05541|Antioquia|PEÑOL|
|05|05543|Antioquia|PEQUE|
|05|05576|Antioquia|PUEBLORRICO|
|05|05579|Antioquia|PUERTO BERRÍO|
|05|05585|Antioquia|PUERTO NARE|
|05|05591|Antioquia|PUERTO TRIUNFO|
|05|05604|Antioquia|REMEDIOS|
|05|05607|Antioquia|RETIRO|
|05|05615|Antioquia|RIONEGRO|
|05|05628|Antioquia|SABANALARGA|
|05|05631|Antioquia|SABANETA|
|05|05642|Antioquia|SALGAR|
|05|05647|Antioquia|SAN ANDRÉS DE CUERQUÍA|
|05|05649|Antioquia|SAN CARLOS|
|05|05652|Antioquia|SAN FRANCISCO|
|05|05656|Antioquia|SAN JERÓNIMO|
|05|05658|Antioquia|SAN JOSÉ DE LA MONTAÑA|
|05|05659|Antioquia|SAN JUAN DE URABÁ|
|05|05660|Antioquia|SAN LUIS|
|05|05664|Antioquia|SAN PEDRO DE LOS MILAGROS|
|05|05665|Antioquia|SAN PEDRO DE URABÁ|
|05|05667|Antioquia|SAN RAFAEL|
|05|05670|Antioquia|SAN ROQUE|
|05|05674|Antioquia|SAN VICENTE FERRER|
|05|05679|Antioquia|SANTA BÁRBARA|
|05|05686|Antioquia|SANTA ROSA DE OSOS|
|05|05690|Antioquia|SANTO DOMINGO|
|05|05697|Antioquia|EL SANTUARIO|
|05|05736|Antioquia|SEGOVIA|
|05|05756|Antioquia|SONSÓN|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 147 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|05|05761|Antioquia|SOPETRÁN|
|05|05789|Antioquia|TÁMESIS|
|05|05790|Antioquia|TARAZÁ|
|05|05792|Antioquia|TARSO|
|05|05809|Antioquia|TITIRIBÍ|
|05|05819|Antioquia|TOLEDO|
|05|05837|Antioquia|TURBO|
|05|05842|Antioquia|URAMITA|
|05|05847|Antioquia|URRAO|
|05|05854|Antioquia|VALDIVIA|
|05|05856|Antioquia|VALPARAÍSO|
|05|05858|Antioquia|VEGACHÍ|
|05|05861|Antioquia|VENECIA|
|05|05873|Antioquia|VIGÍA DEL FUERTE|
|05|05885|Antioquia|YALÍ|
|05|05887|Antioquia|YARUMAL|
|05|05890|Antioquia|YOLOMBÓ|
|05|05893|Antioquia|YONDÓ|
|05|05895|Antioquia|ZARAGOZA|
|05|05861|Antioquía|VENECIA|
|81|81001|Arauca|ARAUCA|
|81|81065|Arauca|ARAUQUITA|
|81|81220|Arauca|CRAVO NORTE|
|81|81300|Arauca|FORTUL|
|81|81591|Arauca|PUERTO RONDÓN|
|81|81736|Arauca|SARAVENA|
|81|81794|Arauca|TAME|
|88|88001|Archipiélago de San<br>Andrés, Providencia y Santa<br>Catalina|SAN ANDRÉS|
|88|88564|Archipiélago de San<br>Andrés, Providencia y Santa<br>Catalina|PROVIDENCIA|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 148 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|08|08001|Atlántico|BARRANQUILLA|
|08|08078|Atlántico|BARANOA|
|08|08137|Atlántico|CAMPO DE LA CRUZ|
|08|08141|Atlántico|CANDELARIA|
|08|08296|Atlántico|GALAPA|
|08|08372|Atlántico|JUAN DE ACOSTA|
|08|08421|Atlántico|LURUACO|
|08|08433|Atlántico|MALAMBO|
|08|08436|Atlántico|MANATÍ|
|08|08520|Atlántico|PALMAR DE VARELA|
|08|08549|Atlántico|PIOJÓ|
|08|08558|Atlántico|POLONUEVO|
|08|08560|Atlántico|PONEDERA|
|08|08573|Atlántico|PUERTO COLOMBIA|
|08|08606|Atlántico|REPELÓN|
|08|08634|Atlántico|SABANAGRANDE|
|08|08638|Atlántico|SABANALARGA|
|08|08675|Atlántico|SANTA LUCÍA|
|08|08685|Atlántico|SANTO TOMÁS|
|08|08758|Atlántico|SOLEDAD|
|08|08770|Atlántico|SUAN|
|08|08832|Atlántico|TUBARÁ|
|08|08849|Atlántico|USIACURÍ|
|11|11001|Bogotá,D.C.|BOGOTÁ,D.C.|
|13|13001|Bolívar|CARTAGENA DE INDIAS|
|13|13006|Bolívar|ACHÍ|
|13|13030|Bolívar|ALTOS DEL ROSARIO|
|13|13042|Bolívar|ARENAL|
|13|13052|Bolívar|ARJONA|
|13|13062|Bolívar|ARROYOHONDO|
|13|13074|Bolívar|BARRANCO DE LOBA|
|13|13140|Bolívar|CALAMAR|
|13|13160|Bolívar|CANTAGALLO|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 149 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|13|13188|Bolívar|CICUCO|
|13|13212|Bolívar|CÓRDOBA|
|13|13222|Bolívar|CLEMENCIA|
|13|13244|Bolívar|EL CARMEN DE BOLÍVAR|
|13|13248|Bolívar|EL GUAMO|
|13|13268|Bolívar|EL PEÑÓN|
|13|13300|Bolívar|HATILLO DE LOBA|
|13|13430|Bolívar|MAGANGUÉ|
|13|13433|Bolívar|MAHATES|
|13|13440|Bolívar|MARGARITA|
|13|13442|Bolívar|MARÍA LA BAJA|
|13|13458|Bolívar|MONTECRISTO|
|13|13468|Bolívar|MOMPÓS|
|13|13473|Bolívar|MORALES|
|13|13490|Bolívar|NOROSÍ|
|13|13549|Bolívar|PINILLOS|
|13|13580|Bolívar|REGIDOR|
|13|13600|Bolívar|RÍO VIEJO|
|13|13620|Bolívar|SAN CRISTÓBAL|
|13|13647|Bolívar|SAN ESTANISLAO|
|13|13650|Bolívar|SAN FERNANDO|
|13|13654|Bolívar|SAN JACINTO|
|13|13655|Bolívar|SAN JACINTO DEL CAUCA|
|13|13657|Bolívar|SAN JUAN NEPOMUCENO|
|13|13667|Bolívar|SAN MARTÍN DE LOBA|
|13|13670|Bolívar|SAN PABLO SUR|
|13|13673|Bolívar|SANTA CATALINA|
|13|13683|Bolívar|SANTA ROSA DE LIMA|
|13|13688|Bolívar|SANTA ROSA DEL SUR|
|13|13744|Bolívar|SIMITÍ|
|13|13760|Bolívar|SOPLAVIENTO|
|13|13780|Bolívar|TALAIGUA NUEVO|
|13|13810|Bolívar|TIQUISIO|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 150 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|13|13836|Bolívar|TURBACO|
|13|13838|Bolívar|TURBANÁ|
|13|13873|Bolívar|VILLANUEVA|
|13|13894|Bolívar|ZAMBRANO|
|15|15001|Boyacá|TUNJA|
|15|15022|Boyacá|ALMEIDA|
|15|15047|Boyacá|AQUITANIA|
|15|15051|Boyacá|ARCABUCO|
|15|15087|Boyacá|BELÉN|
|15|15090|Boyacá|BERBEO|
|15|15092|Boyacá|BETÉITIVA|
|15|15097|Boyacá|BOAVITA|
|15|15104|Boyacá|BOYACÁ|
|15|15106|Boyacá|BRICEÑO|
|15|15109|Boyacá|BUENAVISTA|
|15|15114|Boyacá|BUSBANZÁ|
|15|15131|Boyacá|CALDAS|
|15|15135|Boyacá|CAMPOHERMOSO|
|15|15162|Boyacá|CERINZA|
|15|15172|Boyacá|CHINAVITA|
|15|15176|Boyacá|CHIQUINQUIRÁ|
|15|15180|Boyacá|CHISCAS|
|15|15183|Boyacá|CHITA|
|15|15185|Boyacá|CHITARAQUE|
|15|15187|Boyacá|CHIVATÁ|
|15|15189|Boyacá|CIÉNEGA|
|15|15204|Boyacá|CÓMBITA|
|15|15212|Boyacá|COPER|
|15|15215|Boyacá|CORRALES|
|15|15218|Boyacá|COVARACHÍA|
|15|15223|Boyacá|CUBARÁ|
|15|15224|Boyacá|CUCAITA|
|15|15226|Boyacá|CUÍTIVA|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 151 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|15|15232|Boyacá|CHÍQUIZA|
|15|15236|Boyacá|CHIVOR|
|15|15238|Boyacá|DUITAMA|
|15|15244|Boyacá|EL COCUY|
|15|15248|Boyacá|EL ESPINO|
|15|15272|Boyacá|FIRAVITOBA|
|15|15276|Boyacá|FLORESTA|
|15|15293|Boyacá|GACHANTIVÁ|
|15|15296|Boyacá|GÁMEZA|
|15|15299|Boyacá|GARAGOA|
|15|15317|Boyacá|GUACAMAYAS|
|15|15322|Boyacá|GUATEQUE|
|15|15325|Boyacá|GUAYATÁ|
|15|15332|Boyacá|GÜICÁN DE LA SIERRA|
|15|15362|Boyacá|IZA|
|15|15367|Boyacá|JENESANO|
|15|15368|Boyacá|JERICÓ|
|15|15377|Boyacá|LABRANZAGRANDE|
|15|15380|Boyacá|LA CAPILLA|
|15|15401|Boyacá|LA VICTORIA|
|15|15403|Boyacá|LA UVITA|
|15|15407|Boyacá|VILLA DE LEYVA|
|15|15425|Boyacá|MACANAL|
|15|15442|Boyacá|MARIPÍ|
|15|15455|Boyacá|MIRAFLORES|
|15|15464|Boyacá|MONGUA|
|15|15466|Boyacá|MONGUÍ|
|15|15469|Boyacá|MONIQUIRÁ|
|15|15476|Boyacá|MOTAVITA|
|15|15480|Boyacá|MUZO|
|15|15491|Boyacá|NOBSA|
|15|15494|Boyacá|NUEVO COLÓN|
|15|15500|Boyacá|OICATÁ|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 152 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|15|15507|Boyacá|OTANCHE|
|15|15511|Boyacá|PACHAVITA|
|15|15514|Boyacá|PÁEZ|
|15|15516|Boyacá|PAIPA|
|15|15518|Boyacá|PAJARITO|
|15|15522|Boyacá|PANQUEBA|
|15|15531|Boyacá|PAUNA|
|15|15533|Boyacá|PAYA|
|15|15537|Boyacá|PAZ DE RÍO|
|15|15542|Boyacá|PESCA|
|15|15550|Boyacá|PISBA|
|15|15572|Boyacá|PUERTO BOYACÁ|
|15|15580|Boyacá|QUÍPAMA|
|15|15599|Boyacá|RAMIRIQUÍ|
|15|15600|Boyacá|RÁQUIRA|
|15|15621|Boyacá|RONDÓN|
|15|15632|Boyacá|SABOYÁ|
|15|15638|Boyacá|SÁCHICA|
|15|15646|Boyacá|SAMACÁ|
|15|15660|Boyacá|SAN EDUARDO|
|15|15664|Boyacá|SAN JOSÉ DE PARE|
|15|15667|Boyacá|SAN LUIS DE GACENO|
|15|15673|Boyacá|SAN MATEO|
|15|15676|Boyacá|SAN MIGUEL DE SEMA|
|15|15681|Boyacá|SAN PABLO DE BORBUR|
|15|15686|Boyacá|SANTANA|
|15|15690|Boyacá|SANTA MARÍA|
|15|15693|Boyacá|SANTA ROSA DE VITERBO|
|15|15696|Boyacá|SANTA SOFÍA|
|15|15720|Boyacá|SATIVANORTE|
|15|15723|Boyacá|SATIVASUR|
|15|15740|Boyacá|SIACHOQUE|
|15|15753|Boyacá|SOATÁ|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 153 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|15|15755|Boyacá|SOCOTÁ|
|15|15757|Boyacá|SOCHA|
|15|15759|Boyacá|SOGAMOSO|
|15|15761|Boyacá|SOMONDOCO|
|15|15762|Boyacá|SORA|
|15|15763|Boyacá|SOTAQUIRÁ|
|15|15764|Boyacá|SORACÁ|
|15|15774|Boyacá|SUSACÓN|
|15|15776|Boyacá|SUTAMARCHÁN|
|15|15778|Boyacá|SUTATENZA|
|15|15790|Boyacá|TASCO|
|15|15798|Boyacá|TENZA|
|15|15804|Boyacá|TIBANÁ|
|15|15806|Boyacá|TIBASOSA|
|15|15808|Boyacá|TINJACÁ|
|15|15810|Boyacá|TIPACOQUE|
|15|15814|Boyacá|TOCA|
|15|15816|Boyacá|TOGÜÍ|
|15|15820|Boyacá|TÓPAGA|
|15|15822|Boyacá|TOTA|
|15|15832|Boyacá|TUNUNGUÁ|
|15|15835|Boyacá|TURMEQUÉ|
|15|15837|Boyacá|TUTA|
|15|15839|Boyacá|TUTAZÁ|
|15|15842|Boyacá|ÚMBITA|
|15|15861|Boyacá|VENTAQUEMADA|
|15|15879|Boyacá|VIRACACHÁ|
|15|15897|Boyacá|ZETAQUIRA|
|17|17001|Caldas|MANIZALES|
|17|17013|Caldas|AGUADAS|
|17|17042|Caldas|ANSERMA|
|17|17050|Caldas|ARANZAZU|
|17|17088|Caldas|BELALCÁZAR|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 154 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Mun|icipio<br>Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|17|17174|Caldas|CHINCHINÁ|
|17|17272|Caldas|FILADELFIA|
|17|17380|Caldas|LA DORADA|
|17|17388|Caldas|LA MERCED|
|17|17433|Caldas|MANZANARES|
|17|17442|Caldas|MARMATO|
|17|17444|Caldas|MARQUETALIA|
|17|17446|Caldas|MARULANDA|
|17|17486|Caldas|NEIRA|
|17|17495|Caldas|NORCASIA|
|17|17513|Caldas|PÁCORA|
|17|17524|Caldas|PALESTINA|
|17|17541|Caldas|PENSILVANIA|
|17|17614|Caldas|RIOSUCIO|
|17|17616|Caldas|RISARALDA|
|17|17653|Caldas|SALAMINA|
|17|17662|Caldas|SAMANÁ|
|17|17665|Caldas|SAN JOSÉ|
|17|17777|Caldas|SUPÍA|
|17|17867|Caldas|VICTORIA|
|17|17873|Caldas|VILLAMARÍA|
|17|17877|Caldas|VITERBO|
|18|18001|Caquetá|FLORENCIA|
|18|18029|Caquetá|ALBANIA|
|18|18094|Caquetá|BELÉN DE LOS ANDAQUÍES|
|18|18150|Caquetá|CARTAGENA DEL CHAIRÁ|
|18|18205|Caquetá|CURILLO|
|18|18247|Caquetá|EL DONCELLO|
|18|18256|Caquetá|EL PAUJÍL|
|18|18410|Caquetá|LA MONTAÑITA|
|18|18460|Caquetá|MILÁN|
|18|18479|Caquetá|MORELIA|
|18|18592|Caquetá|PUERTO RICO|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 155 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|18|18610|Caquetá|SAN JOSÉ DEL FRAGUA|
|18|18753|Caquetá|SAN VICENTE DEL CAGUÁN|
|18|18756|Caquetá|SOLANO|
|18|18785|Caquetá|SOLITA|
|18|18860|Caquetá|VALPARAÍSO|
|85|85001|Casanare|YOPAL|
|85|85010|Casanare|AGUAZUL|
|85|85015|Casanare|CHÁMEZA|
|85|85125|Casanare|HATO COROZAL|
|85|85136|Casanare|LA SALINA|
|85|85139|Casanare|MANÍ|
|85|85162|Casanare|MONTERREY|
|85|85225|Casanare|NUNCHÍA|
|85|85230|Casanare|OROCUÉ|
|85|85250|Casanare|PAZ DE ARIPORO|
|85|85263|Casanare|PORE|
|85|85279|Casanare|RECETOR|
|85|85300|Casanare|SABANALARGA|
|85|85315|Casanare|SÁCAMA|
|85|85325|Casanare|SAN LUIS DE PALENQUE|
|85|85400|Casanare|TÁMARA|
|85|85410|Casanare|TAURAMENA|
|85|85430|Casanare|TRINIDAD|
|85|85440|Casanare|VILLANUEVA|
|19|19001|Cauca|POPAYÁN|
|19|19022|Cauca|ALMAGUER|
|19|19050|Cauca|ARGELIA|
|19|19075|Cauca|BALBOA|
|19|19100|Cauca|BOLÍVAR|
|19|19110|Cauca|BUENOS AIRES|
|19|19130|Cauca|CAJIBÍO|
|19|19137|Cauca|CALDONO|
|19|19142|Cauca|CALOTO|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 156 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|19|19212|Cauca|CORINTO|
|19|19256|Cauca|EL TAMBO|
|19|19290|Cauca|FLORENCIA|
|19|19300|Cauca|GUACHENÉ|
|19|19318|Cauca|GUAPÍ|
|19|19355|Cauca|INZÁ|
|19|19364|Cauca|JAMBALÓ|
|19|19392|Cauca|LA SIERRA|
|19|19397|Cauca|LA VEGA|
|19|19418|Cauca|LÓPEZ DE MICAY|
|19|19450|Cauca|MERCADERES|
|19|19455|Cauca|MIRANDA|
|19|19473|Cauca|MORALES|
|19|19513|Cauca|PADILLA|
|19|19517|Cauca|PÁEZ - BELALCAZAR|
|19|19532|Cauca|PATÍA – EL BORDO|
|19|19533|Cauca|PIAMONTE|
|19|19548|Cauca|PIENDAMÓ – TUNÍA|
|19|19573|Cauca|PUERTO TEJADA|
|19|19585|Cauca|PURACÉ - COCONUCO|
|19|19622|Cauca|ROSAS|
|19|19693|Cauca|SAN SEBASTIÁN|
|19|19698|Cauca|SANTANDER DE QUILICHAO|
|19|19701|Cauca|SANTA ROSA|
|19|19743|Cauca|SILVIA|
|19|19760|Cauca|SOTARA|
|19|19780|Cauca|SUÁREZ|
|19|19785|Cauca|SUCRE|
|19|19807|Cauca|TIMBÍO|
|19|19809|Cauca|TIMBIQUÍ|
|19|19821|Cauca|TORIBÍO|
|19|19824|Cauca|TOTORÓ|
|19|19845|Cauca|VILLA RICA|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 157 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|20|20001|Cesar|VALLEDUPAR|
|20|20011|Cesar|AGUACHICA|
|20|20013|Cesar|AGUSTÍN CODAZZI|
|20|20032|Cesar|ASTREA|
|20|20045|Cesar|BECERRIL|
|20|20060|Cesar|BOSCONIA|
|20|20175|Cesar|CHIMICHAGUA|
|20|20178|Cesar|CHIRIGUANÁ|
|20|20228|Cesar|CURUMANÍ|
|20|20238|Cesar|EL COPEY|
|20|20250|Cesar|EL PASO|
|20|20295|Cesar|GAMARRA|
|20|20310|Cesar|GONZÁLEZ|
|20|20383|Cesar|LA GLORIA|
|20|20400|Cesar|LA JAGUA DE IBIRICO|
|20|20443|Cesar|MANAURE BALCÓN DEL CESAR|
|20|20517|Cesar|PAILITAS|
|20|20550|Cesar|PELAYA|
|20|20570|Cesar|PUEBLO BELLO|
|20|20614|Cesar|RÍO DE ORO|
|20|20621|Cesar|LA PAZ|
|20|20710|Cesar|SAN ALBERTO|
|20|20750|Cesar|SAN DIEGO|
|20|20770|Cesar|SAN MARTÍN|
|20|20787|Cesar|TAMALAMEQUE|
|27|27001|Chocó|QUIBDÓ|
|27|27006|Chocó|ACANDÍ|
|27|27025|Chocó|ALTO BAUDÓ(PIE DE PATÓ)|
|27|27050|Chocó|ATRATO(YUTO)|
|27|27073|Chocó|BAGADÓ|
|27|27075|Chocó|BAHÍA SOLANO(MUTIS)|
|27|27077|Chocó|BAJO BAUDÓ(PIZARRO)|
|27|27099|Chocó|BOJAYÁ(BELLA VISTA)|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 158 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|27|27135|Chocó|EL CANTÓN DEL SAN PABLO|
|27|27150|Chocó|CARMEN DEL DARIÉN|
|27|27160|Chocó|CÉRTEGUI|
|27|27205|Chocó|CONDOTO|
|27|27245|Chocó|EL CARMEN DE ATRATO|
|27|27250|Chocó|EL LITORAL DEL SAN JUAN|
|27|27361|Chocó|ISTMINA|
|27|27372|Chocó|JURADÓ|
|27|27413|Chocó|LLORÓ|
|27|27425|Chocó|MEDIO ATRATO(BETÉ)|
|27|27430|Chocó|MEDIO BAUDÓ|
|27|27450|Chocó|MEDIO SAN JUAN (ANDAGOYA)|
|27|27491|Chocó|NÓVITA|
|27|27495|Chocó|NUQUÍ|
|27|27580|Chocó|RÍO IRÓ(SANTA RITA)|
|27|27600|Chocó|RÍO QUITO(PAIMADÓ)|
|27|27615|Chocó|RIOSUCIO|
|27|27660|Chocó|SAN JOSÉ DEL PALMAR|
|27|27745|Chocó|SIPÍ|
|27|27787|Chocó|TADÓ|
|27|27800|Chocó|UNGUÍA|
|27|27810|Chocó|UNIÓN PANAMERICANA (LAS<br>ÁNIMAS)|
|23|23001|Córdoba|MONTERÍA|
|23|23068|Córdoba|AYAPEL|
|23|23079|Córdoba|BUENAVISTA|
|23|23090|Córdoba|CANALETE|
|23|23162|Córdoba|CERETÉ|
|23|23168|Córdoba|CHIMÁ|
|23|23182|Córdoba|CHINÚ|
|23|23189|Córdoba|CIÉNAGA DE ORO|
|23|23300|Córdoba|COTORRA|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 159 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|23|23350|Córdoba|LA APARTADA|
|23|23417|Córdoba|LORICA|
|23|23419|Córdoba|LOS CÓRDOBAS|
|23|23464|Córdoba|MOMIL|
|23|23466|Córdoba|MONTELÍBANO|
|23|23500|Córdoba|MOÑITOS|
|23|23555|Córdoba|PLANETA RICA|
|23|23570|Córdoba|PUEBLO NUEVO|
|23|23574|Córdoba|PUERTO ESCONDIDO|
|23|23580|Córdoba|PUERTO LIBERTADOR|
|23|23586|Córdoba|PURÍSIMA DE LA CONCEPCIÓN|
|23|23660|Córdoba|SAHAGÚN|
|23|23670|Córdoba|SAN ANDRÉS DE SOTAVENTO|
|23|23672|Córdoba|SAN ANTERO|
|23|23675|Córdoba|SAN BERNARDO DEL VIENTO|
|23|23678|Córdoba|SAN CARLOS|
|23|23682|Córdoba|SAN JOSÉ DE URÉ|
|23|23686|Córdoba|SAN PELAYO|
|23|23807|Córdoba|TIERRALTA|
|23|23815|Córdoba|TUCHÍN|
|23|23855|Córdoba|VALENCIA|
|25|25001|Cundinamarca|AGUA DE DIOS|
|25|25019|Cundinamarca|ALBÁN|
|25|25035|Cundinamarca|ANAPOIMA|
|25|25040|Cundinamarca|ANOLAIMA|
|25|25053|Cundinamarca|ARBELÁEZ|
|25|25086|Cundinamarca|BELTRÁN|
|25|25095|Cundinamarca|BITUIMA|
|25|25099|Cundinamarca|BOJACÁ|
|25|25120|Cundinamarca|CABRERA|
|25|25123|Cundinamarca|CACHIPAY|
|25|25126|Cundinamarca|CAJICÁ|
|25|25148|Cundinamarca|CAPARRAPÍ|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 160 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|25|25151|Cundinamarca|CÁQUEZA|
|25|25154|Cundinamarca|CARMEN DE CARUPA|
|25|25168|Cundinamarca|CHAGUANÍ|
|25|25175|Cundinamarca|CHÍA|
|25|25178|Cundinamarca|CHIPAQUE|
|25|25181|Cundinamarca|CHOACHÍ|
|25|25183|Cundinamarca|CHOCONTÁ|
|25|25200|Cundinamarca|COGUA|
|25|25214|Cundinamarca|COTA|
|25|25224|Cundinamarca|CUCUNUBÁ|
|25|25245|Cundinamarca|EL COLEGIO|
|25|25258|Cundinamarca|EL PEÑÓN|
|25|25260|Cundinamarca|EL ROSAL|
|25|25269|Cundinamarca|FACATATIVÁ|
|25|25279|Cundinamarca|FÓMEQUE|
|25|25281|Cundinamarca|FOSCA|
|25|25286|Cundinamarca|FUNZA|
|25|25288|Cundinamarca|FÚQUENE|
|25|25290|Cundinamarca|FUSAGASUGÁ|
|25|25293|Cundinamarca|GACHALÁ|
|25|25295|Cundinamarca|GACHANCIPÁ|
|25|25297|Cundinamarca|GACHETÁ|
|25|25299|Cundinamarca|GAMA|
|25|25307|Cundinamarca|GIRARDOT|
|25|25312|Cundinamarca|GRANADA|
|25|25317|Cundinamarca|GUACHETÁ|
|25|25320|Cundinamarca|GUADUAS|
|25|25322|Cundinamarca|GUASCA|
|25|25324|Cundinamarca|GUATAQUÍ|
|25|25326|Cundinamarca|GUATAVITA|
|25|25328|Cundinamarca|GUAYABAL DE SÍQUIMA|
|25|25335|Cundinamarca|GUAYABETAL|
|25|25339|Cundinamarca|GUTIÉRREZ|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 161 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|25|25368|Cundinamarca|JERUSALÉN|
|25|25372|Cundinamarca|JUNÍN|
|25|25377|Cundinamarca|LA CALERA|
|25|25386|Cundinamarca|LA MESA|
|25|25394|Cundinamarca|LA PALMA|
|25|25398|Cundinamarca|LA PEÑA|
|25|25402|Cundinamarca|LA VEGA|
|25|25407|Cundinamarca|LENGUAZAQUE|
|25|25426|Cundinamarca|MACHETÁ|
|25|25430|Cundinamarca|MADRID|
|25|25436|Cundinamarca|MANTA|
|25|25438|Cundinamarca|MEDINA|
|25|25473|Cundinamarca|MOSQUERA|
|25|25483|Cundinamarca|NARIÑO|
|25|25486|Cundinamarca|NEMOCÓN|
|25|25488|Cundinamarca|NILO|
|25|25489|Cundinamarca|NIMAIMA|
|25|25491|Cundinamarca|NOCAIMA|
|25|25506|Cundinamarca|VENECIA|
|25|25513|Cundinamarca|PACHO|
|25|25518|Cundinamarca|PAIME|
|25|25524|Cundinamarca|PANDI|
|25|25530|Cundinamarca|PARATEBUENO|
|25|25535|Cundinamarca|PASCA|
|25|25572|Cundinamarca|PUERTO SALGAR|
|25|25580|Cundinamarca|PULÍ|
|25|25592|Cundinamarca|QUEBRADANEGRA|
|25|25594|Cundinamarca|QUETAME|
|25|25596|Cundinamarca|QUIPILE|
|25|25599|Cundinamarca|APULO|
|25|25612|Cundinamarca|RICAURTE|
|25|25645|Cundinamarca|SAN ANTONIO DEL<br>TEQUENDAMA|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 162 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|25|25649|Cundinamarca|SAN BERNARDO|
|25|25653|Cundinamarca|SAN CAYETANO|
|25|25658|Cundinamarca|SAN FRANCISCO|
|25|25662|Cundinamarca|SAN JUAN DE RIOSECO|
|25|25718|Cundinamarca|SASAIMA|
|25|25736|Cundinamarca|SESQUILÉ|
|25|25740|Cundinamarca|SIBATÉ|
|25|25743|Cundinamarca|SILVANIA|
|25|25745|Cundinamarca|SIMIJACA|
|25|25754|Cundinamarca|SOACHA|
|25|25758|Cundinamarca|SOPÓ|
|25|25769|Cundinamarca|SUBACHOQUE|
|25|25772|Cundinamarca|SUESCA|
|25|25777|Cundinamarca|SUPATÁ|
|25|25779|Cundinamarca|SUSA|
|25|25781|Cundinamarca|SUTATAUSA|
|25|25785|Cundinamarca|TABIO|
|25|25793|Cundinamarca|TAUSA|
|25|25797|Cundinamarca|TENA|
|25|25799|Cundinamarca|TENJO|
|25|25805|Cundinamarca|TIBACUY|
|25|25807|Cundinamarca|TIBIRITA|
|25|25815|Cundinamarca|TOCAIMA|
|25|25817|Cundinamarca|TOCANCIPÁ|
|25|25823|Cundinamarca|TOPAIPÍ|
|25|25839|Cundinamarca|UBALÁ|
|25|25841|Cundinamarca|UBAQUE|
|25|25843|Cundinamarca|VILLA DE SAN DIEGO DE UBATÉ|
|25|25845|Cundinamarca|UNE|
|25|25851|Cundinamarca|ÚTICA|
|25|25862|Cundinamarca|VERGARA|
|25|25867|Cundinamarca|VIANÍ|
|25|25871|Cundinamarca|VILLAGÓMEZ|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 163 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|25|25873|Cundinamarca|VILLAPINZÓN|
|25|25875|Cundinamarca|VILLETA|
|25|25878|Cundinamarca|VIOTÁ|
|25|25885|Cundinamarca|YACOPÍ|
|25|25898|Cundinamarca|ZIPACÓN|
|25|25899|Cundinamarca|ZIPAQUIRÁ|
|94|94001|Guainía|INÍRIDA|
|94|94343|Guainía|BARRANCOMINAS|
|94|94663|Guainía|MAPIRIPANA|
|94|94883|Guainía|SAN FELIPE|
|94|94884|Guainía|PUERTO COLOMBIA|
|94|94885|Guainía|LA GUADALUPE|
|94|94886|Guainía|CACAHUAL|
|94|94887|Guainía|PANA PANA|
|94|94888|Guainía|MORICHAL NUEVO|
|95|95001|Guaviare|SAN JOSÉ DEL GUAVIARE|
|95|95015|Guaviare|CALAMAR|
|95|95025|Guaviare|EL RETORNO|
|95|95200|Guaviare|MIRAFLORES|
|41|41001|Huila|NEIVA|
|41|41006|Huila|ACEVEDO|
|41|41013|Huila|AGRADO|
|41|41016|Huila|AIPE|
|41|41020|Huila|ALGECIRAS|
|41|41026|Huila|ALTAMIRA|
|41|41078|Huila|BARAYA|
|41|41132|Huila|CAMPOALEGRE|
|41|41206|Huila|COLOMBIA|
|41|41244|Huila|ELÍAS|
|41|41298|Huila|GARZÓN|
|41|41306|Huila|GIGANTE|
|41|41319|Huila|GUADALUPE|
|41|41349|Huila|HOBO|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 164 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|41|41357|Huila|ÍQUIRA|
|41|41359|Huila|ISNOS|
|41|41378|Huila|LA ARGENTINA (LA PLATA<br>VIEJA)|
|41|41396|Huila|LA PLATA|
|41|41483|Huila|NÁTAGA|
|41|41503|Huila|OPORAPA|
|41|41518|Huila|PAICOL|
|41|41524|Huila|PALERMO|
|41|41530|Huila|PALESTINA|
|41|41548|Huila|PITAL|
|41|41551|Huila|PITALITO|
|41|41615|Huila|RIVERA|
|41|41660|Huila|SALADOBLANCO|
|41|41668|Huila|SAN AGUSTÍN|
|41|41676|Huila|SANTA MARÍA|
|41|41770|Huila|SUAZA|
|41|41791|Huila|TARQUI|
|41|41797|Huila|TESALIA(CARNICERÍAS)|
|41|41799|Huila|TELLO|
|41|41801|Huila|TERUEL|
|41|41807|Huila|TIMANÁ|
|41|41872|Huila|VILLAVIEJA|
|41|41885|Huila|YAGUARÁ|
|44|44001|La Guajira|RIOHACHA|
|44|44035|La Guajira|ALBANIA|
|44|44078|La Guajira|BARRANCAS|
|44|44090|La Guajira|DIBULLA|
|44|44098|La Guajira|DISTRACCIÓN|
|44|44110|La Guajira|EL MOLINO|
|44|44279|La Guajira|FONSECA|
|44|44378|La Guajira|HATONUEVO|
|44|44420|La Guajira|LA JAGUA DEL PILAR|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 165 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|44|44430|La Guajira|MAICAO|
|44|44560|La Guajira|MANAURE|
|44|44650|La Guajira|SAN JUAN DEL CESAR|
|44|44847|La Guajira|URIBIA|
|44|44855|La Guajira|URUMITA|
|44|44874|La Guajira|VILLANUEVA|
|47|47001|Magdalena|SANTA MARTA|
|47|47030|Magdalena|ALGARROBO|
|47|47053|Magdalena|ARACATACA|
|47|47058|Magdalena|ARIGUANÍ|
|47|47161|Magdalena|CERRO DE SAN ANTONIO|
|47|47170|Magdalena|CHIBOLO|
|47|47189|Magdalena|CIÉNAGA|
|47|47205|Magdalena|CONCORDIA|
|47|47245|Magdalena|EL BANCO|
|47|47258|Magdalena|EL PIÑÓN|
|47|47268|Magdalena|EL RETÉN|
|47|47288|Magdalena|FUNDACIÓN|
|47|47318|Magdalena|GUAMAL|
|47|47460|Magdalena|NUEVA GRANADA|
|47|47541|Magdalena|PEDRAZA|
|47|47545|Magdalena|PIJIÑO DEL CARMEN|
|47|47551|Magdalena|PIVIJAY|
|47|47555|Magdalena|PLATO|
|47|47570|Magdalena|PUEBLOVIEJO|
|47|47605|Magdalena|REMOLINO|
|47|47660|Magdalena|SABANAS DE SAN ÁNGEL|
|47|47675|Magdalena|SALAMINA|
|47|47692|Magdalena|SAN SEBASTIÁN DE<br>BUENAVISTA|
|47|47703|Magdalena|SAN ZENÓN|
|47|47707|Magdalena|SANTA ANA|
|47|47720|Magdalena|SANTA BÁRBARA DE PINTO|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 166 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|47|47745|Magdalena|SITIONUEVO|
|47|47798|Magdalena|TENERIFE|
|47|47960|Magdalena|ZAPAYÁN|
|47|47980|Magdalena|ZONA BANANERA|
|50|50001|Meta|VILLAVICENCIO|
|50|50006|Meta|ACACÍAS|
|50|50110|Meta|BARRANCA DE UPÍA|
|50|50124|Meta|CABUYARO|
|50|50150|Meta|CASTILLA LA NUEVA|
|50|50223|Meta|CUBARRAL|
|50|50226|Meta|CUMARAL|
|50|50245|Meta|EL CALVARIO|
|50|50251|Meta|EL CASTILLO|
|50|50270|Meta|EL DORADO|
|50|50287|Meta|FUENTEDEORO|
|50|50313|Meta|GRANADA|
|50|50318|Meta|GUAMAL|
|50|50325|Meta|MAPIRIPÁN|
|50|50330|Meta|MESETAS|
|50|50350|Meta|LA MACARENA|
|50|50370|Meta|URIBE|
|50|50400|Meta|LEJANÍAS|
|50|50450|Meta|PUERTO CONCORDIA|
|50|50568|Meta|PUERTO GAITÁN|
|50|50573|Meta|PUERTO LÓPEZ|
|50|50577|Meta|PUERTO LLERAS|
|50|50590|Meta|PUERTO RICO|
|50|50606|Meta|RESTREPO|
|50|50680|Meta|SAN CARLOS DE GUAROA|
|50|50683|Meta|SAN JUAN DE ARAMA|
|50|50686|Meta|SAN JUANITO|
|50|50689|Meta|SAN MARTÍN DE LOS LLANOS|
|50|50711|Meta|VISTAHERMOSA|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 167 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|52|52001|Nariño|PASTO|
|52|52019|Nariño|ALBÁN(SAN JOSÉ)|
|52|52022|Nariño|ALDANA|
|52|52036|Nariño|ANCUYÁ|
|52|52051|Nariño|ARBOLEDA|
|52|52079|Nariño|BARBACOAS|
|52|52083|Nariño|BELÉN|
|52|52110|Nariño|BUESACO|
|52|52203|Nariño|COLÓN(GÉNOVA)|
|52|52207|Nariño|CONSACÁ|
|52|52210|Nariño|CONTADERO|
|52|52215|Nariño|CÓRDOBA|
|52|52224|Nariño|CUASPÚD|
|52|52227|Nariño|CUMBAL|
|52|52233|Nariño|CUMBITARA|
|52|52240|Nariño|CHACHAGÜÍ|
|52|52250|Nariño|EL CHARCO|
|52|52254|Nariño|EL PEÑOL|
|52|52256|Nariño|EL ROSARIO|
|52|52258|Nariño|EL TABLÓN DE GÓMEZ|
|52|52260|Nariño|EL TAMBO|
|52|52287|Nariño|FUNES|
|52|52317|Nariño|GUACHUCAL|
|52|52320|Nariño|GUAITARILLA|
|52|52323|Nariño|GUALMATÁN|
|52|52352|Nariño|ILES|
|52|52354|Nariño|IMUÉS|
|52|52356|Nariño|IPIALES|
|52|52378|Nariño|LA CRUZ|
|52|52381|Nariño|LA FLORIDA|
|52|52385|Nariño|LA LLANADA|
|52|52390|Nariño|LA TOLA|
|52|52399|Nariño|LA UNIÓN|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 168 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|52|52405|Nariño|LEIVA|
|52|52411|Nariño|LINARES|
|52|52418|Nariño|LOS ANDES(SOTOMAYOR)|
|52|52427|Nariño|MAGÜÍ(PAYÁN)|
|52|52435|Nariño|MALLAMA(PIEDRANCHA)|
|52|52473|Nariño|MOSQUERA|
|52|52480|Nariño|NARIÑO|
|52|52490|Nariño|OLAYA HERRERA|
|52|52506|Nariño|OSPINA|
|52|52520|Nariño|FRANCISCO PIZARRO|
|52|52540|Nariño|POLICARPA|
|52|52560|Nariño|POTOSÍ|
|52|52565|Nariño|PROVIDENCIA|
|52|52573|Nariño|PUERRES|
|52|52585|Nariño|PUPIALES|
|52|52612|Nariño|RICAURTE|
|52|52621|Nariño|ROBERTO PAYÁN(SAN JOSÉ)|
|52|52678|Nariño|SAMANIEGO|
|52|52683|Nariño|SANDONÁ|
|52|52685|Nariño|SAN BERNARDO|
|52|52687|Nariño|SAN LORENZO|
|52|52693|Nariño|SAN PABLO|
|52|52694|Nariño|SAN PEDRO DE CARTAGO|
|52|52696|Nariño|SANTA BÁRBARA|
|52|52699|Nariño|SANTACRUZ|
|52|52720|Nariño|SAPUYES|
|52|52786|Nariño|TAMINANGO|
|52|52788|Nariño|TANGUA|
|52|52835|Nariño|SAN ANDRÉS DE TUMACO|
|52|52838|Nariño|TÚQUERRES|
|52|52885|Nariño|YACUANQUER|
|54|54001|Norte de Santander|CÚCUTA|
|54|54003|Norte de Santander|ÁBREGO|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 169 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|54|54051|Norte de Santander|ARBOLEDAS|
|54|54099|Norte de Santander|BOCHALEMA|
|54|54109|Norte de Santander|BUCARASICA|
|54|54125|Norte de Santander|CÁCOTA DE VELASCO|
|54|54128|Norte de Santander|CÁCHIRA|
|54|54172|Norte de Santander|CHINÁCOTA|
|54|54174|Norte de Santander|CHITAGÁ|
|54|54206|Norte de Santander|CONVENCIÓN|
|54|54223|Norte de Santander|CUCUTILLA|
|54|54239|Norte de Santander|DURANIA|
|54|54245|Norte de Santander|EL CARMEN|
|54|54250|Norte de Santander|EL TARRA|
|54|54261|Norte de Santander|EL ZULIA|
|54|54313|Norte de Santander|GRAMALOTE|
|54|54344|Norte de Santander|HACARÍ|
|54|54347|Norte de Santander|HERRÁN|
|54|54377|Norte de Santander|LABATECA|
|54|54385|Norte de Santander|LA ESPERANZA|
|54|54398|Norte de Santander|LA PLAYA DE BELÉN|
|54|54405|Norte de Santander|LOS PATIOS|
|54|54418|Norte de Santander|LOURDES|
|54|54480|Norte de Santander|MUTISCUA|
|54|54498|Norte de Santander|OCAÑA|
|54|54518|Norte de Santander|PAMPLONA|
|54|54520|Norte de Santander|PAMPLONITA|
|54|54553|Norte de Santander|PUERTO SANTANDER|
|54|54599|Norte de Santander|RAGONVALIA|
|54|54660|Norte de Santander|SALAZAR DE LAS PALMAS|
|54|54670|Norte de Santander|SAN CALIXTO|
|54|54673|Norte de Santander|SAN CAYETANO|
|54|54680|Norte de Santander|SANTIAGO|
|54|54720|Norte de Santander|SARDINATA|
|54|54743|Norte de Santander|SANTO DOMINGO DE SILOS|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 170 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|54|54800|Norte de Santander|TEORAMA|
|54|54810|Norte de Santander|TIBÚ|
|54|54820|Norte de Santander|TOLEDO|
|54|54871|Norte de Santander|VILLA CARO|
|54|54874|Norte de Santander|VILLA DEL ROSARIO|
|86|86001|Putumayo|MOCOA|
|86|86219|Putumayo|COLÓN|
|86|86320|Putumayo|ORITO|
|86|86568|Putumayo|PUERTO ASÍS|
|86|86569|Putumayo|PUERTO CAICEDO|
|86|86571|Putumayo|PUERTO GUZMÁN|
|86|86573|Putumayo|PUERTO LEGUÍZAMO|
|86|86749|Putumayo|SIBUNDOY|
|86|86755|Putumayo|SAN FRANCISCO|
|86|86757|Putumayo|SAN MIGUEL|
|86|86760|Putumayo|SANTIAGO|
|86|86865|Putumayo|VALLE DEL GUAMUEZ|
|86|86885|Putumayo|VILLAGARZÓN|
|63|63001|Quindío|ARMENIA|
|63|63111|Quindío|BUENAVISTA|
|63|63130|Quindío|CALARCÁ|
|63|63190|Quindío|CIRCASIA|
|63|63212|Quindío|CÓRDOBA|
|63|63272|Quindío|FILANDIA|
|63|63302|Quindío|GÉNOVA|
|63|63401|Quindío|LA TEBAIDA|
|63|63470|Quindío|MONTENEGRO|
|63|63548|Quindío|PIJAO|
|63|63594|Quindío|QUIMBAYA|
|63|63690|Quindío|SALENTO|
|66|66001|Risaralda|PEREIRA|
|66|66045|Risaralda|APÍA|
|66|66075|Risaralda|BALBOA|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 171 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|66|66088|Risaralda|BELÉN DE UMBRÍA|
|66|66170|Risaralda|DOSQUEBRADAS|
|66|66318|Risaralda|GUÁTICA|
|66|66383|Risaralda|LA CELIA|
|66|66400|Risaralda|LA VIRGINIA|
|66|66440|Risaralda|MARSELLA|
|66|66456|Risaralda|MISTRATÓ|
|66|66572|Risaralda|PUEBLO RICO|
|66|66594|Risaralda|QUINCHÍA|
|66|66682|Risaralda|SANTA ROSA DE CABAL|
|66|66687|Risaralda|SANTUARIO|
|68|68001|Santander|BUCARAMANGA|
|68|68013|Santander|AGUADA|
|68|68020|Santander|ALBANIA|
|68|68051|Santander|ARATOCA|
|68|68077|Santander|BARBOSA|
|68|68079|Santander|BARICHARA|
|68|68081|Santander|BARRANCABERMEJA|
|68|68092|Santander|BETULIA|
|68|68101|Santander|BOLÍVAR|
|68|68121|Santander|CABRERA|
|68|68132|Santander|CALIFORNIA|
|68|68147|Santander|CAPITANEJO|
|68|68152|Santander|CARCASÍ|
|68|68160|Santander|CEPITÁ|
|68|68162|Santander|CERRITO|
|68|68167|Santander|CHARALÁ|
|68|68169|Santander|CHARTA|
|68|68176|Santander|CHIMA|
|68|68179|Santander|CHIPATÁ|
|68|68190|Santander|CIMITARRA|
|68|68207|Santander|CONCEPCIÓN|
|68|68209|Santander|CONFINES|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 172 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|68|68211|Santander|CONTRATACIÓN|
|68|68217|Santander|COROMORO|
|68|68229|Santander|CURITÍ|
|68|68235|Santander|EL CARMEN DE CHUCURÍ|
|68|68245|Santander|EL GUACAMAYO|
|68|68250|Santander|EL PEÑÓN|
|68|68255|Santander|EL PLAYÓN|
|68|68264|Santander|ENCINO|
|68|68266|Santander|ENCISO|
|68|68271|Santander|FLORIÁN|
|68|68276|Santander|FLORIDABLANCA|
|68|68296|Santander|GALÁN|
|68|68298|Santander|GÁMBITA|
|68|68307|Santander|GIRÓN|
|68|68318|Santander|GUACA|
|68|68320|Santander|GUADALUPE|
|68|68322|Santander|GUAPOTÁ|
|68|68324|Santander|GUAVATÁ|
|68|68327|Santander|GÜEPSA|
|68|68344|Santander|HATO|
|68|68368|Santander|JESÚS MARÍA|
|68|68370|Santander|JORDÁN|
|68|68377|Santander|LA BELLEZA|
|68|68385|Santander|LANDÁZURI|
|68|68397|Santander|LA PAZ|
|68|68406|Santander|LEBRIJA|
|68|68418|Santander|LOS SANTOS|
|68|68425|Santander|MACARAVITA|
|68|68432|Santander|MÁLAGA|
|68|68444|Santander|MATANZA|
|68|68464|Santander|MOGOTES|
|68|68468|Santander|MOLAGAVITA|
|68|68498|Santander|OCAMONTE|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 173 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|68|68500|Santander|OIBA|
|68|68502|Santander|ONZAGA|
|68|68522|Santander|PALMAR|
|68|68524|Santander|PALMAS DEL SOCORRO|
|68|68533|Santander|PÁRAMO|
|68|68547|Santander|PIEDECUESTA|
|68|68549|Santander|PINCHOTE|
|68|68572|Santander|PUENTE NACIONAL|
|68|68573|Santander|PUERTO PARRA|
|68|68575|Santander|PUERTO WILCHES|
|68|68615|Santander|RIONEGRO|
|68|68655|Santander|SABANA DE TORRES|
|68|68669|Santander|SAN ANDRÉS|
|68|68673|Santander|SAN BENITO|
|68|68679|Santander|SAN GIL|
|68|68682|Santander|SAN JOAQUÍN|
|68|68684|Santander|SAN JOSÉ DE MIRANDA|
|68|68686|Santander|SAN MIGUEL|
|68|68689|Santander|SAN VICENTE DE CHUCURÍ|
|68|68705|Santander|SANTA BÁRBARA|
|68|68720|Santander|SANTA HELENA DEL OPÓN|
|68|68745|Santander|SIMACOTA|
|68|68755|Santander|SOCORRO|
|68|68770|Santander|SUAITA|
|68|68773|Santander|SUCRE|
|68|68780|Santander|SURATÁ|
|68|68820|Santander|TONA|
|68|68855|Santander|VALLE DE SAN JOSÉ|
|68|68861|Santander|VÉLEZ|
|68|68867|Santander|VETAS|
|68|68872|Santander|VILLANUEVA|
|68|68895|Santander|ZAPATOCA|
|70|70001|Sucre|SINCELEJO|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 174 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|70|70110|Sucre|BUENAVISTA|
|70|70124|Sucre|CAIMITO|
|70|70204|Sucre|COLOSÓ|
|70|70215|Sucre|COROZAL|
|70|70221|Sucre|COVEÑAS|
|70|70230|Sucre|CHALÁN|
|70|70233|Sucre|EL ROBLE|
|70|70235|Sucre|GALERAS|
|70|70265|Sucre|GUARANDA|
|70|70400|Sucre|LA UNIÓN|
|70|70418|Sucre|LOS PALMITOS|
|70|70429|Sucre|MAJAGUAL|
|70|70473|Sucre|MORROA|
|70|70508|Sucre|OVEJAS|
|70|70523|Sucre|PALMITO|
|70|70670|Sucre|SAMPUÉS|
|70|70678|Sucre|SAN BENITO ABAD|
|70|70702|Sucre|SAN JUAN DE BETULIA|
|70|70708|Sucre|SAN MARCOS|
|70|70713|Sucre|SAN ONOFRE|
|70|70717|Sucre|SAN PEDRO|
|70|70742|Sucre|SAN LUIS DE SINCÉ|
|70|70771|Sucre|SUCRE|
|70|70820|Sucre|SANTIAGO DE TOLÚ|
|70|70823|Sucre|TOLÚ VIEJO|
|73|73001|Tolima|IBAGUÉ|
|73|73024|Tolima|ALPUJARRA|
|73|73026|Tolima|ALVARADO|
|73|73030|Tolima|AMBALEMA|
|73|73043|Tolima|ANZOÁTEGUI|
|73|73055|Tolima|ARMERO(GUAYABAL)|
|73|73067|Tolima|ATACO|
|73|73124|Tolima|CAJAMARCA|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 175 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|73|73148|Tolima|CARMEN DE APICALÁ|
|73|73152|Tolima|CASABIANCA|
|73|73168|Tolima|CHAPARRAL|
|73|73200|Tolima|COELLO|
|73|73217|Tolima|COYAIMA|
|73|73226|Tolima|CUNDAY|
|73|73236|Tolima|DOLORES|
|73|73268|Tolima|ESPINAL|
|73|73270|Tolima|FALAN|
|73|73275|Tolima|FLANDES|
|73|73283|Tolima|FRESNO|
|73|73319|Tolima|GUAMO|
|73|73347|Tolima|HERVEO|
|73|73349|Tolima|HONDA|
|73|73352|Tolima|ICONONZO|
|73|73408|Tolima|LÉRIDA|
|73|73411|Tolima|LÍBANO|
|73|73443|Tolima|SAN SEBASTIÁN DE MARIQUITA|
|73|73449|Tolima|MELGAR|
|73|73461|Tolima|MURILLO|
|73|73483|Tolima|NATAGAIMA|
|73|73504|Tolima|ORTEGA|
|73|73520|Tolima|PALOCABILDO|
|73|73547|Tolima|PIEDRAS|
|73|73555|Tolima|PLANADAS|
|73|73563|Tolima|PRADO|
|73|73585|Tolima|PURIFICACIÓN|
|73|73616|Tolima|RIOBLANCO|
|73|73622|Tolima|RONCESVALLES|
|73|73624|Tolima|ROVIRA|
|73|73671|Tolima|SALDAÑA|
|73|73675|Tolima|SAN ANTONIO|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 176 de 269 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|73|73678|Tolima|SAN LUIS|
|73|73686|Tolima|SANTA ISABEL|
|73|73770|Tolima|SUÁREZ|
|73|73854|Tolima|VALLE DE SAN JUAN|
|73|73861|Tolima|VENADILLO|
|73|73870|Tolima|VILLAHERMOSA|
|73|73873|Tolima|VILLARRICA|
|76|76001|Valle del Cauca|CALI|
|76|76020|Valle del Cauca|ALCALÁ|
|76|76036|Valle del Cauca|ANDALUCÍA|
|76|76041|Valle del Cauca|ANSERMANUEVO|
|76|76054|Valle del Cauca|ARGELIA|
|76|76100|Valle del Cauca|BOLÍVAR|
|76|76109|Valle del Cauca|BUENAVENTURA|
|76|76111|Valle del Cauca|GUADALAJARA DE BUGA|
|76|76113|Valle del Cauca|BUGALAGRANDE|
|76|76122|Valle del Cauca|CAICEDONIA|
|76|76126|Valle del Cauca|CALIMA(DARIEN)|
|76|76130|Valle del Cauca|CANDELARIA|
|76|76147|Valle del Cauca|CARTAGO|
|76|76233|Valle del Cauca|DAGUA|
|76|76243|Valle del Cauca|EL ÁGUILA|
|76|76246|Valle del Cauca|EL CAIRO|
|76|76248|Valle del Cauca|EL CERRITO|
|76|76250|Valle del Cauca|EL DOVIO|
|76|76275|Valle del Cauca|FLORIDA|
|76|76306|Valle del Cauca|GINEBRA|
|76|76318|Valle del Cauca|GUACARÍ|
|76|76364|Valle del Cauca|JAMUNDÍ|
|76|76377|Valle del Cauca|LA CUMBRE|
|76|76400|Valle del Cauca|LA UNIÓN|
|76|76403|Valle del Cauca|LA VICTORIA|
|76|76497|Valle del Cauca|OBANDO|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 177 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Código Departamento|Código Municipio|Nombre Departamento|Nombre Municipio|
|---|---|---|---|
|76|76520|Valle del Cauca|PALMIRA|
|76|76563|Valle del Cauca|PRADERA|
|76|76606|Valle del Cauca|RESTREPO|
|76|76616|Valle del Cauca|RIOFRÍO|
|76|76622|Valle del Cauca|ROLDANILLO|
|76|76670|Valle del Cauca|SAN PEDRO|
|76|76736|Valle del Cauca|SEVILLA|
|76|76823|Valle del Cauca|TORO|
|76|76828|Valle del Cauca|TRUJILLO|
|76|76834|Valle del Cauca|TULUÁ|
|76|76845|Valle del Cauca|ULLOA|
|76|76863|Valle del Cauca|VERSALLES|
|76|76869|Valle del Cauca|VIJES|
|76|76890|Valle del Cauca|YOTOCO|
|76|76892|Valle del Cauca|YUMBO|
|76|76895|Valle del Cauca|ZARZAL|
|97|97001|Vaupés|MITÚ|
|97|97161|Vaupés|CARURÚ|
|97|97511|Vaupés|PACOA|
|97|97666|Vaupés|TARAIRA|
|97|97777|Vaupés|PAPUNAHUA|
|97|97889|Vaupés|YAVARATÉ|
|99|99001|Vichada|PUERTO CARREÑO|
|99|99524|Vichada|LA PRIMAVERA|
|99|99624|Vichada|SANTA ROSALÍA|
|99|99773|Vichada|CUMARIBO|



### 5.5. Campos Nómina. 

### 5.5.1. Periodo de Nómina: PeriodoNomina. 

|_Código _|_Periodo de Nómina_|
|---|---|
|1|Semanal|
|2|Decenal|
|3|Catorcenal|
|4|Quincenal|



Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Página 178 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_Código _|_Periodo de Nómina_|
|---|---|
|5|Mensual|
|6|Otro|



### 5.5.2. Tipo de Contrato: TipoContrato. 

|_Código _|_Tipo de Contrato_|
|---|---|
|1|Termino Fijo|
|2|Término Indefinido|
|3|Obra o Labor|
|4|Aprendizaje|
|5|Prácticas o Pasantías|



### 5.5.3. Tipo de Trabajador: TipoTrabajador. 

|_Código _|_Tipo de Trabajador_|
|---|---|
|01|Dependiente|
|02|Servicio domestico|
|04|Madre comunitaria|
|12|Aprendices del Sena en etapa lectiva|
|18|Funcionariospúblicos sin tope máximo de ibc|
|19|Aprendices del SENA en etapaproductiva|
|21|Estudiantes depostgrado en salud|
|22|Profesor de establecimientoparticular|
|23|Estudiantes aportes solo riesgos laborales|
|30|Dependiente entidades o universidadespúblicas con régimen especial en salud|
|31|Cooperados opre cooperativas de trabajo asociado|
|47|Trabajador dependiente de entidad beneficiaria del sistema general de<br>participaciones - aportespatronales|
|51|Trabajador de tiempoparcial|
|54|Prepensionado de entidad en liquidación.|
|56|Prepensionado con aporte voluntario a salud|
|58|Estudiantes deprácticas laborales en el sectorpúblico|



### 5.5.4. Subtipo de Trabajador: SubTipoTrabajador. 

|_Código _|_Subtipo de Trabajador_|
|---|---|
|00|No Aplica|
|01|Dependientepensionadopor vejez activo|



> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Página 179 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

### 5.5.5. Tipo de Hora Extra o Recargo: Porcentaje. 

|_Código _|_Tipo de Hora Extra o Recargo _|_Porcentaje _|
|---|---|---|
|1|Hora Extra Diurna|25.00|
|2|Hora Extra Nocturna|75.00|
|3|Hora Recargo Nocturno|35.00|
|4|Hora Extra Diurna DominicalyFestivos|100.00|
|5|Hora Recargo Diurno DominicalyFestivos|75.00|
|6|Hora Extra Nocturna DominicalyFestivos|150.00|
|7|Hora Recargo Nocturno DominicalyFestivos|110.00|



### 5.5.6. Tipo de Incapacidad: Tipo. 

|_Código _|_Tipo de Incapacidad_|
|---|---|
|1|Común|
|2|Profesional|
|3|Laboral|



### 5.5.7. Tipo de XML: TipoXML. 

|_Código _|_Nombre XML_|_Tipo de XML_|
|---|---|---|
|102|NominaIndividual|Documento Soporte de Pago de Nómina Electrónica|
|103|NominaIndividualDeAjuste|Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica|



### 5.5.8. Tipo de Nota de Ajuste: TipoNota. 

|_Código _|_Tipo de Nota de Ajuste_|
|---|---|
|1|Reemplazar|
|2|Eliminar|



Reemplazar : Se utilizará este código cuando se requiera realizar ajustes sobre Documentos Soporte de Pago de Nómina Electrónica o Notas de Ajuste del Documento Soporte de Pago de Nómina Electrónica, por errores aritméticos, contables o de contenido. 

Eliminar: Se utilizará este código cuando se requiera eliminar el Documento Soporte de Pago de Nómina Electrónica, y/o una Nota de Ajuste del Documento Soporte de Pago de Nómina Electrónica, para los casos en los cuales se haya transmitido un documento por errores contables o de procedimiento. 

Nota: Se indica que el tipo de Nota de Ajuste del Documento Soporte de Pago de Nómina Electrónica con código 2 Eliminar, solo invalida los documentos enviados por error, no 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 180 de 269 

® 



<!-- Start of picture text -->
) | Ma. IN<br><!-- End of picture text -->

POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->

**Resolución No. 000013** 





### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

### 6. Reglas y Mensajes de Validación. 

En el presente capítulo se presentan los mensajes correspondientes a las reglas de validación. 

La Columna “Y” contiene, la definición si una regla determina rechazo (“R”) o notificación (”N”). 

Un documento solamente puede recibir el sello de “validado” si no falla en ninguna validación identificada por “R”. 

Un documento puede recibir el sello de “validado” independiente de fallar en cualquier número de las reglas identificadas por “N”. 

La construcción de las reglas puede ser encontrada en las tablas del capítulo 6.1.1 la columna ID: identifica la línea correspondiente en aquellos capítulos y en este capítulo. 

En el caso de que la evaluación de un determinado elemento pueda tener más que una regla, en el presente capítulo se adicionan letras (a, b, …) al correspondiente ID para diferenciar los resultados posibles. 

Algunos elementos pueden ocurrir en diferentes partes del documento XML; en estos casos, los mensajes deben explicitar el Xpath completo, para permitir la correcta identificación de la correspondiente ubicación. Estos elementos están identificados en la columna “Mensaje” por la expresión <Xpath>. 

El resultado de una validación fallida debe siempre ser la concatenación entre el ID, el resultado (“R” o “N”), y el mensaje correspondiente, como se puede ver en los siguientes ejemplos: 

_Tabla 8 – Ejemplos de Mensajes de Validación._ 

_<mark>Mensaje</mark>_ NIE022 – (R) Debe ir el literal: "V1.0: Documento Soporte de Pago de Nómina Electrónica" NIE013 – (R) Se debe colocar el Codigo alfa-2 correspondiente 

Se informa la incorporación de las siguientes reglas: 

|_ID_|_Y_|<br>_Elemento_|_Regla_|_Mensaje _|_V_|_Xpath_|
|---|---|---|---|---|---|---|
|90|R||Solo se podrá transmitir una única vez el Número del<br>documentopara el trabajador.|Documento procesado anteriormente|1.0||
|92|R||El Emisor del Documento debe encontrarse habilitado en<br>la plataforma de emisión de Nómina Electrónica (Para<br>NominaIndividualyNominaIndividualDeAjuste).|El Emisor del Documento no se<br>encuentra Habilitado en la<br>Plataforma.|1.0||
|VLR01|R||Los valores monetarios/porcentajes deben corresponder<br>a valores positivos|Los valores monetarios/porcentajes<br>deben corresponder a valores<br>Positivos|1.0||



### 6.1. Documentos Electrónicos. 

### 6.1.1. Documento Soporte de Pago de Nómina Electrónica: NominaIndividual. 

|_ID_|_Y_<br>_Campo_|_Regla_|_Mensaje_|_V_|_Xpath_|
|---|---|---|---|---|---|
|NIE901|R<br>-|El documento debe poseer<br>Todos los Namespace<br>correspondientes a su<br>estructura.|El documento debe poseer<br>Todos los Namespace<br>correspondientes a su<br>estructura.|1.0|/NominaIndividual/|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 182 de 269 





### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_Y_|<br>_Campo_|_Regla_|_Mensaje_|_V_|_Xpath_|
|---|---|---|---|---|---|---|
|NIE001|R|UBLExtensions|Solamente puede haber una<br>ocurrencia de un grupo<br>UBLExtensions conteniendo el<br>grupo ds:Signature. Ver<br>definición en numeral 3.6|Solamente puede haber una<br>ocurrencia de un grupo<br>UBLExtensions conteniendo el<br>grupo ds:Signature.|1.0|/NominaIndividual/ext:UB<br>LExtensions|
|NIE199|R|Novedad|Indica si existe alguna Novedad<br>Contractual en el Documento<br>Soporte de Pago de Nómina<br>Electrónica o Nota de Ajuste de<br>Documento Soporte de Pago de<br>Nómina Electrónica del<br>Trabajador en dicho Mes.|Se debe colocar "true" o "false".|1.0|/NominaIndividual/Noved<br>ad|
|NIE199a|R|Novedad|Indica si existe alguna Novedad<br>Contractual en el Documento<br>Soporte de Pago de Nómina<br>Electrónica o Nota de Ajuste de<br>Documento Soporte de Pago de<br>Nómina Electrónica del<br>Trabajador en dicho Mes.|Elemento Novedad con valor<br>“true” no puede ser recibido<br>por primera vez, ya que no<br>existe un Documento Soporte<br>de Pago de Nómina Electrónica<br>o Nota de Ajuste de Documento<br>Soporte de Pago de Nómina<br>Electrónica recibida para este<br>trabajador reportada por este<br>Emisor durante este mes.|1.0|/NominaIndividual/Noved<br>ad|
|NIE204|R|CUNENov|Debe ir el CUNE del documento<br>a Reemplazar|Debe ir el CUNE del documento<br>al cual se le realizará la novedad<br>contractual|1.0|/NominaIndividual/Noved<br>ad/@CUNENov|
|NIE204a|R|CUNENov|Debe ir el CUNE del documento<br>a Reemplazar|Documento a Realizar la<br>Novedad contractual no se<br>encuentra recibido en la Base<br>de Datos.|1.0|/NominaIndividual/Noved<br>ad/@CUNENov|
|NIE002|R|FechaIngreso|Se debe indicar la Fecha de<br>Ingreso del trabajador a la<br>empresa, en formato AAAA-<br>MM-DD|Se debe indicar la Fecha de<br>Ingreso del trabajador a la<br>empresa, en formato AAAA-<br>MM-DD|1.0|/NominaIndividual/Period<br>o/@FechaIngreso|
|NIE003|R|FechaRetiro|Se debe indicar la Fecha de<br>Retiro del trabajador a la<br>empresa, en formato AAAA-<br>MM-DD|Se debe indicar la Fecha de<br>Retiro del trabajador a la<br>empresa, en formato AAAA-<br>MM-DD|1.0|/NominaIndividual/Period<br>o/@FechaRetiro|
|NIE004|R|FechaLiquidacionIni<br>cio|Se debe indicar la Fecha de<br>Inicio del Periodo de Liquidación<br>del documento, en formato<br>AAAA-MM-DD|<br>Se debe indicar la Fecha de<br>Inicio del Periodo de Liquidación<br>del documento, en formato<br>AAAA-MM-DD|<br>1.0|/NominaIndividual/Period<br>o/@FechaLiquidacionInici<br>o|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 183 de 269 

r 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->

r 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->

r 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->

r 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->

r 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->

r 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->

r 

me 6esElemprendimientodeElemprendimientodede todos | jyinhacienda 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientodeElemprendimientodede todos | jyinhacienda<br><!-- End of picture text -->

r 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->

r 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->

r 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->

r 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->

r 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->

r 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->

r 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_Y_<br>_Campo_|_Regla_|_Mensaje_|_V_|_Xpath_|
|---|---|---|---|---|---|
|||Valor Pagado correspondiente a<br>|Se debe colocar el Valor Pagado<br>||/NominaIndividual/Deduc|
|NIE180|R<br>Cooperativa|Cooperativas por parte del<br>trabajador|correspondiente a Cooperativas<br>por parte del trabajador|1.0|ciones/Cooperativa|
|NIE181|R<br>EmbargoFiscal|Valor Pagado correspondiente<br>aEmbargos Fiscales por parte<br>del trabajador|Se debe colocar el Valor Pagado<br>correspondiente aEmbargos<br>Fiscales por parte del trabajador|<br>1.0|/NominaIndividual/Deduc<br>ciones/EmbargoFiscal|
|NIE182|R<br>PlanComplementari<br>os|Valor Pagado correspondiente a<br>Planes Complementarios por<br>parte del trabajador|Se debe colocar el Valor Pagado<br>correspondiente a Planes<br>Complementarios por parte del<br>trabajador|1.0|/NominaIndividual/Deduc<br>ciones/PlanComplementar<br>ios|
|NIE183|R<br>Educacion|Valor Pagado correspondiente a<br>Conceptos Educativos por parte<br>del trabajador|Se debe colocar el Valor Pagado<br>correspondiente a Conceptos<br>Educativos por parte del<br>trabajador|1.0|/NominaIndividual/Deduc<br>ciones/Educacion|
|NIE184|R<br>Reintegro|Valor Pagado correspondiente a<br>Reintegro por parte del<br>trabajador|Se debe colocar el Valor Pagado<br>correspondiente a Reintegro<br>por parte del trabajador|1.0|/NominaIndividual/Deduc<br>ciones/Reintegro|
|NIE185|R<br>Deuda|Valor Pagado correspondiente a<br>Deuda con la Empresa por parte<br>del trabajador|<br>Se debe colocar el Valor Pagado<br>correspondiente a Deuda con la<br>Empresa por parte del<br>trabajador|1.0|/NominaIndividual/Deduc<br>ciones/Deuda|
|NIE186|R<br>Redondeo|Definido en el numeral 1.1.1|Se debe indicar el Redondeo<br>según la definición establecida.|<sup>1.0</sup>|/NominaIndividual/Redon<br>deo|
|NIE187|R<br>DevengadosTotal|Debe ir el valor Total de Todos<br>los Devengados del Trabajador|Debe ir el valor Total de Todos<br>los Devengados del Trabajador|1.0|/NominaIndividual/Deven<br>gadosTotal|
|NIE188|R<br>DeduccionesTotal|Debe ir el valor Total de Todos<br>las Deducciones del Trabajador|Debe ir el valor Total de Todos<br>las Deducciones del Trabajador|<sup>1.0</sup>|/NominaIndividual/Deduc<br>cionesTotal|
|NIE189|R<br>ComprobanteTotal|Debe ser la Diferencia entre<br>DevengadosTotal -<br>DeduccionesTotal|Debe ser la Diferencia entre<br>DevengadosTotal -<br>DeduccionesTotal|1.0|/NominaIndividual/Compr<br>obanteTotal|



### 6.1.2. Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica: NominaIndividualDeAjuste. 

|_ID_|_Y_|_Campo_|_Regla_|_Mensaje_|_V_|_Xpath_|
|---|---|---|---|---|---|---|
|NIAE901|R|-|El documento debe poseer<br>Todos los Namespace<br>correspondientes a su<br>estructura.|El documento debe poseer<br>Todos los Namespace<br>correspondientes a su<br>estructura.|1.0|/NominaIndividualDeAjust<br>e/|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 198 de 269 

r 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->

r 

me 6esElemprendimientodeElemprendimientodede todos | jyinhacienda 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientodeElemprendimientodede todos | jyinhacienda<br><!-- End of picture text -->





### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_Y_|_Campo_|_Regla_|_Mensaje_|_V_|_Xpath_|
|---|---|---|---|---|---|---|
|NIAE206|R|PrimerApellido|Debe ir el Primer Apellido del<br>Proveedor de Soluciones<br>Tecnológicas|Debe ir el Primer Apellido del<br>Proveedor de Soluciones<br>Tecnológicas|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/ProveedorX<br>ML/@PrimerApellido|
|NIAE207|R|SegundoApellido|Debe ir el Segundo Apellido del<br>Proveedor de Soluciones<br>Tecnológicas|Debe ir el Segundo Apellido del<br>Proveedor de Soluciones<br>Tecnológicas|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/ProveedorX<br>ML/@SegundoApellido|
|NIAE208|R|PrimerNombre|Debe ir el Primer Nombre del<br>Proveedor de Soluciones<br>Tecnológicas|Debe ir el Primer Nombre del<br>Proveedor de Soluciones<br>Tecnológicas|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/ProveedorX<br>ML/@PrimerNombre|
|NIAE209|N|OtrosNombres|Deben ir los Otros Nombres del<br>Proveedor de Soluciones<br>Tecnológicas|Deben ir los Otros Nombres del<br>Proveedor de Soluciones<br>Tecnológicas|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/ProveedorX<br>ML/@OtrosNombres|
|NIAE017|R|NIT|Se debe colocar el NIT sin<br>guiones ni DV de la empresa<br>dueña del Software que genera<br>el Documento, debe estar<br>registrado en la DIAN|Se debe colocar el NIT sin<br>guiones ni DV de la empresa<br>dueña del Software que genera<br>el Documento, debe estar<br>registrado en la DIAN|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/ProveedorX<br>ML/@NIT|
|NIAE018|R|DV|Se debe colocar el DV de la<br>empresa dueña del Software<br>que genera el Documento, debe<br>estar registrado en la DIAN|<br>Se debe colocar el DV de la<br>empresa dueña del Software<br>que genera el Documento, debe<br>estar registrado en la DIAN|<br>1.0|/NominaIndividualDeAjust<br>e/Reemplazar/ProveedorX<br>ML/@DV|
||||Identificador del software<br>asignado cuando el software se<br>activa en el Sistema de|Identificador del software<br>asignado cuando el software se<br>activa en el Sistema de||/NominaIndividualDeAjust|
|NIAE019|R|SoftwareID|Documento Soporte de Pago de<br>Nómina Electrónica, debe<br>corresponder a un software<br>autorizado para este Emisor|Documento Soporte de Pago de<br>Nómina Electrónica, debe<br>corresponder a un software<br>autorizado para este Emisor|<br>1.0|e/Reemplazar/ProveedorX<br>ML/@SoftwareID|
|NIAE020|R|SoftwareSC|Definido en el numeral 8.3|Se debe indicar el Software<br>Security Code según la<br>definición establecida.|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/ProveedorX<br>ML/@SoftwareSC|
|NIAE021|R|CodigoQR|Debe corresponder a la<br>siguiente URL “https://catalogo-<br>vpfe.dian.gov.co/document/sea<br>rchqr?documentkey=CUNE”<br>donde la palabra CUNE debe ser<br>reemplazada por el CUNE del<br>documento electrónico|<br>Se debe indicar la información<br>detallada del docuemnto según<br>la definición establecida.|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/CodigoQR|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 201 de 269 

r 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->

r 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_Y_<br>_Campo_|_Regla_|_Mensaje_|_V_|_Xpath_|
|---|---|---|---|---|---|
|NIAE042|R<br>SubTipoTrabajador|Corresponde a una sub<br>clasificación de PILA para<br>conocer en que calidad se<br>realizan las cotizaciones a la<br>seguridad social. Se debe<br>colocar el Codigo de la tabla<br>5.5.4|Se debe colocar el Codigo<br>correspondiente|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador/<br>@SubTipoTrabajador|
|NIAE043|R<br>AltoRiesgoPension|Se debe colocar “true” o “false”|Se debe colocar “true” o “false”|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador/<br>@AltoRiesgoPension|
|NIAE044|R<br>TipoDocumento|Se debe colocar el Codigo de la<br>tabla 5.2.1|Se debe colocar el Codigo<br>correspondiente|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador/<br>@TipoDocumento|
|NIAE045|R<br>NumeroDocumento|Debe ir el Numero de<br>documento del trabajador, sin<br>puntos ni comas ni espacios|Debe ir el Numero de<br>documento del trabajador, sin<br>puntos ni comas ni espacios|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador/<br>@NumeroDocumento|
|NIAE046|R<br>PrimerApellido|Debe ir el Primer Apellido del<br>trabajador|Debe ir el Primer Apellido del<br>trabajador|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador/<br>@PrimerApellido|
|NIAE047|R<br>SegundoApellido|Debe ir el Segundo Apellido del<br>trabajador|Debe ir el Segundo Apellido del<br>trabajador|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador/<br>@SegundoApellido|
|NIAE048|R<br>PrimerNombre|Debe ir el Primer Nombre del<br>trabajador|Debe ir el Primer Nombre del<br>trabajador|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador/<br>@PrimerNombre|
|NIAE049|N<br>OtrosNombres|Deben ir los Otros Nombres del<br>trabajador|Deben ir los Otros Nombres del<br>trabajador|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador/<br>@OtrosNombres|
|NIAE050|R<br>LugarTrabajoPais|Se debe colocar el Codigo alfa-2<br>de la tabla 5.4.1|<br>Se debe colocar el Codigo alfa-2<br>correspondiente|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador/<br>@LugarTrabajoPais|
|NIAE051|R<br>LugarTrabajoDepart<br>amentoEstado|Se debe colocar el Codigo de la<br>tabla 5.4.2|Se debe colocar el Codigo<br>correspondiente|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador/<br>@LugarTrabajoDepartame<br>ntoEstado|
|NIAE052|R<br>LugarTrabajoMunici<br>pioCiudad|Se debe colocar el Codigo de la<br>tabla 5.4.3|Se debe colocar el Codigo<br>correspondiente|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Trabajador/<br>@LugarTrabajoMunicipioC<br>iudad|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 204 de 269 

r 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->

r 

> me 6esElemprendimientodeElemprendimientodede todos | jyinhacienda 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientodeElemprendimientodede todos | jyinhacienda<br><!-- End of picture text -->

r 

me 6esElemprendimientodeElemprendimientodede todos | jyinhacienda 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientodeElemprendimientodede todos | jyinhacienda<br><!-- End of picture text -->



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_Y_<br>_Campo_|_Regla_|_Mensaje_|_V_|_Xpath_|
|---|---|---|---|---|---|
||||||/NominaIndividualDeAjust|
|NIAE094|R<br>HoraInicio|En formato YYYY-MM-<br>DDTHH:MM:SS|Se debe colocar en formato<br>YYYY-MM-DDTHH:MM:SS|1.0|e/Reemplazar/Devengado<br>s/HRDDFs/HRDDF/@HoraI<br>nicio|
|NIAE095|R<br>HoraFin|En formato YYYY-MM-<br>DDTHH:MM:SS|Se debe colocar en formato<br>YYYY-MM-DDTHH:MM:SS|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRDDFs/HRDDF/@Hora<br>Fin|
|NIAE096|R<br>Cantidad|Cantidad de Horas|Se debe colocar la cantidad de<br>Horas|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRDDFs/HRDDF/@Canti<br>dad|
|NIAE097|R<br>Porcentaje|Se debe colocar el Porcentaje<br>que corresponda de la tabla<br>5.5.5|Se debe colocar el Porcentaje<br>que corresponda|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRDDFs/HRDDF/@Porce<br>ntaje|
|NIAE098|R<br>Pago|Valor Pagado por las Horas|Se debe colocar el Valor Pagado<br>por las Horas|<br>1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRDDFs/HRDDF/@Pago|
|NIAE099|R<br>HoraInicio|En formato YYYY-MM-<br>DDTHH:MM:SS|Se debe colocar en formato<br>YYYY-MM-DDTHH:MM:SS|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HENDFs/HENDF/@HoraI<br>nicio|
|NIAE100|R<br>HoraFin|En formato YYYY-MM-<br>DDTHH:MM:SS|Se debe colocar en formato<br>YYYY-MM-DDTHH:MM:SS|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HENDFs/HENDF/@Hora<br>Fin|
|NIAE101|R<br>Cantidad|Cantidad de Horas|Se debe colocar la cantidad de<br>Horas|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HENDFs/HENDF/@Canti<br>dad|
|NIAE102|R<br>Porcentaje|Se debe colocar el Porcentaje<br>que corresponda de la tabla<br>5.5.5|Se debe colocar el Porcentaje<br>que corresponda|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HENDFs/HENDF/@Porce<br>ntaje|
|NIAE103|R<br>Pago|Valor Pagado por las Horas|Se debe colocar el Valor Pagado<br>por las Horas|<br>1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HENDFs/HENDF/@Pago|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 208 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_Y_<br>_Campo_|_Regla_|_Mensaje_|_V_|_Xpath_|
|---|---|---|---|---|---|
|NIAE104|R<br>HoraInicio|En formato YYYY-MM-<br>DDTHH:MM:SS|Se debe colocar en formato<br>YYYY-MM-DDTHH:MM:SS|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRNDFs/HRNDF/@HoraI<br>nicio|
|NIAE105|R<br>HoraFin|En formato YYYY-MM-<br>DDTHH:MM:SS|Se debe colocar en formato<br>YYYY-MM-DDTHH:MM:SS|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRNDFs/HRNDF/@Hora<br>Fin|
|NIAE106|R<br>Cantidad|Cantidad de Horas|Se debe colocar la cantidad de<br>Horas|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRNDFs/HRNDF/@Canti<br>dad|
|NIAE107|R<br>Porcentaje|Se debe colocar el Porcentaje<br>que corresponda de la tabla<br>5.5.5|Se debe colocar el Porcentaje<br>que corresponda|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRNDFs/HRNDF/@Porc<br>entaje|
|NIAE108|R<br>Pago|Valor Pagado por las Horas|Se debe colocar el Valor Pagado<br>por las Horas|<br>1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HRNDFs/HRNDF/@Pago|
|NIAE109|R<br>FechaInicio|En formato AAAA-MM-DD|Se debe colocar en formato<br>AAAA-MM-DD|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Vacaciones/VacacionesC<br>omunes/@FechaInicio|
|NIAE110|R<br>FechaFin|En formato AAAA-MM-DD|Se debe colocar en formato<br>AAAA-MM-DD|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Vacaciones/VacacionesC<br>omunes/@FechaFin|
|NIAE111|R<br>Cantidad|Cantidad de Dias|Se debe colocar la cantidad de<br>Dias|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Vacaciones/VacacionesC<br>omunes/@Cantidad|
|NIAE112|R<br>Pago|Valor Pagado por Vacaciones Si<br>Disfrutadas|Se debe colocar el Valor Pagado<br>por Vacaciones Si Disfrutadas|<br>1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Vacaciones/VacacionesC<br>omunes/@Pago|
|NIAE115|R<br>Cantidad|Cantidad de Dias|Se debe colocar la cantidad de<br>Dias|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Vacaciones/VacacionesC<br>ompensadas/@Cantidad|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 209 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_Y_<br>_Campo_|_Regla_|_Mensaje_|_V_|_Xpath_|
|---|---|---|---|---|---|
||||||/NominaIndividualDeAjust|
|NIAE116|R<br>Pago|Valor Pagado por Vacaciones No<br>Disfrutadas|<br>Se debe colocar el Valor Pagado<br>por Vacaciones No Disfrutadas|1.0|e/Reemplazar/Devengado<br>s/Vacaciones/VacacionesC<br>ompensadas/@Pago|
|NIAE117|R<br>Cantidad|Cantidad de Dias a los cuales<br>corresponde el pago de la Prima<br>legal|<br>Se debe colocar la cantidad de<br>Dias a los cuales corresponde el<br>pago de la Prima legal|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Primas/@Cantidad|
|NIAE118|R<br>Pago|Valor Pagado por Prima Legal<br>con respecto a Cantidad de Dias|Se debe colocar el Valor Pagado<br>por Prima Legal con respecto a<br>Cantidad de Dias|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Primas/@Pago|
|NIAE119|R<br>PagoNS|Valor Pagado por Prima No<br>Salarial|Se debe colocar el Valor Pagado<br>por Prima No Salarial|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Primas/@PagoNS|
|NIAE120|R<br>Pago|Valor Pagado por Cesantias|Se debe colocar el Valor Pagado<br>por Cesantias|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Cesantias/@Pago|
|NIAE121|R<br>Porcentaje|Porcentaje de Interes de<br>Cesantias|Se debe colocar el Porcentaje<br>de Interes de Cesantias|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Cesantias/@Porcentaje|
|NIAE122|R<br>PagoIntereses|Valor Pagado por Intereses de<br>Cesantias|Se debe colocar el Valor Pagado<br>por Intereses de Cesantias|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Cesantias/@PagoInteres<br>es|
|NIAE123|R<br>FechaInicio|En formato AAAA-MM-DD|Se debe colocar en formato<br>AAAA-MM-DD|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Incapacidades/Incapacid<br>ad/@FechaInicio|
|NIAE124|R<br>FechaFin|En formato AAAA-MM-DD|Se debe colocar en formato<br>AAAA-MM-DD|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Incapacidades/Incapacid<br>ad/@FechaFin|
|NIAE125|R<br>Cantidad|Cantidad de Dias|Se debe colocar la cantidad de<br>Dias|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Incapacidades/Incapacid<br>ad/@Cantidad|
|NIAE126|R<br>Tipo|Se debe colocar el Codigo que<br>corresponda de la tabla 5.5.6|Se debe colocar el Codigo que<br>corresponda|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Incapacidades/Incapacid<br>ad/@Tipo|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 210 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_Y_<br>_Campo_|_Regla_|_Mensaje_|_V_|_Xpath_|
|---|---|---|---|---|---|
|NIAE127|R<br>Pago|Valor Pagado por Incapacidad<br>con respecto a Cantidad de Dias|<br>Se debe colocar el Valor Pagado<br>por Incapacidad con respecto a<br>Cantidad de Dias|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Incapacidades/Incapacid<br>ad/@Pago|
|NIAE128|R<br>FechaInicio|En formato AAAA-MM-DD|Se debe colocar en formato<br>AAAA-MM-DD|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaMP/@<br>FechaInicio|
|NIAE129|R<br>FechaFin|En formato AAAA-MM-DD|Se debe colocar en formato<br>AAAA-MM-DD|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaMP/@<br>FechaFin|
|NIAE130|R<br>Cantidad|Cantidad de Dias|Se debe colocar la cantidad de<br>Dias|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaMP/@<br>Cantidad|
|NIAE131|R<br>Pago|Valor Pagado por Licencia de<br>Maternidad o Paternidad con<br>respecto a Cantidad de Dias|Se debe colocar el Valor Pagado<br>por Licencia de Maternidad o<br>Paternidad con respecto a<br>Cantidad de Dias|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaMP/@<br>Pago|
|NIAE132|R<br>FechaInicio|En formato AAAA-MM-DD|Se debe colocar en formato<br>AAAA-MM-DD|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaR/@Fe<br>chaInicio|
|NIAE133|R<br>FechaFin|En formato AAAA-MM-DD|Se debe colocar en formato<br>AAAA-MM-DD|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaR/@Fe<br>chaFin|
|NIAE134|R<br>Cantidad|Cantidad de Dias|Se debe colocar la cantidad de<br>Dias|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaR/@Ca<br>ntidad|
|NIAE135|R<br>Pago|Valor Pagado por Licencia<br>Remunerada con respecto a<br>Cantidad de Dias|Se debe colocar el Valor Pagado<br>por Licencia Remunerada con<br>respecto a Cantidad de Dias|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaR/@Pa<br>go|
|NIAE136|R<br>FechaInicio|En formato AAAA-MM-DD|Se debe colocar en formato<br>AAAA-MM-DD|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaNR/@<br>FechaInicio|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 211 de 269 



### **Resolución No. 000013** 



(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_Y_<br>_Campo_|_Regla_|_Mensaje_|_V_|_Xpath_|
|---|---|---|---|---|---|
||||||/NominaIndividualDeAjust|
|NIAE137|R<br>FechaFin|En formato AAAA-MM-DD|Se debe colocar en formato<br>AAAA-MM-DD|1.0|e/Reemplazar/Devengado<br>s/Licencias/LicenciaNR/@<br>FechaFin|
|NIAE138|R<br>Cantidad|Cantidad de Dias|Se debe colocar la cantidad de<br>Dias|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Licencias/LicenciaNR/@<br>Cantidad|
|NIAE139|R<br>BonificacionS|Valor Pagado por Bonificación<br>Salarial|Se debe colocar el Valor Pagado<br>por Bonificación Salarial|<br>1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Bonificaciones/Bonificac<br>ion/@BonificacionS|
|NIAE140|R<br>BonificacionNS|Valor Pagado por Bonificación<br>No Salarial|Se debe colocar el Valor Pagado<br>por Bonificación No Salarial|<br>1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Bonificaciones/Bonificac<br>ion/@BonificacionNS|
|NIAE141|R<br>AuxilioS|Valor Pagado por Auxilios<br>Salariales|Se debe colocar el Valor Pagado<br>por Auxilios Salariales|<br>1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Auxilios/Auxilio/@Auxili<br>oS|
|NIAE142|R<br>AuxilioNS|Valor Pagado por Auxilios No<br>Salariales|Se debe colocar el Valor Pagado<br>por Auxilios No Salariales|<br>1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Auxilios/Auxilio/@Auxili<br>oNS|
|NIAE143|R<br>FechaInicio|En formato AAAA-MM-DD|Se debe colocar en formato<br>AAAA-MM-DD|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HuelgasLegales/HuelgaL<br>egal/@FechaInicio|
|NIAE144|R<br>FechaFIn|En formato AAAA-MM-DD|Se debe colocar en formato<br>AAAA-MM-DD|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HuelgasLegales/HuelgaL<br>egal/@FechaFIn|
|NIAE145|R<br>Cantidad|Cantidad de Dias|Se debe colocar la cantidad de<br>Dias|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/HuelgasLegales/HuelgaL<br>egal/@Cantidad|
|NIAE146|R<br>DescripcionConcept<br>o|Debe ir la Descripcion del<br>Concepto|Debe ir la Descripcion del<br>Concepto|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/OtroConceptos/OtroCon<br>cepto/@DescripcionConc<br>epto|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 212 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_Y_<br>_Campo_|_Regla_|_Mensaje_|_V_|_Xpath_|
|---|---|---|---|---|---|
||||||/NominaIndividualDeAjust|
|NIAE147|R<br>ConceptoS|Valor Pagado por Conceptos<br>Salariales|Se debe colocar el Valor Pagado<br>por Conceptos Salariales|1.0|e/Reemplazar/Devengado<br>s/OtroConceptos/OtroCon<br>cepto/@ConceptoS|
|NIAE148|R<br>ConceptoNS|Valor Pagado por Conceptos No<br>Salariales|Se debe colocar el Valor Pagado<br>por Conceptos No Salariales|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/OtroConceptos/OtroCon<br>cepto/@ConceptoNS|
|NIAE149|R<br>CompensacionO|Valor Pagado por<br>Compensaciones Ordinarias|Se debe colocar el Valor Pagado<br>por Compensaciones Ordinarias|<sup>1.0</sup>|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Compensaciones/Comp<br>ensacion/@Compensacio<br>nO|
|NIAE150|R<br>CompensacionE|Valor Pagado por<br>Compensaciones<br>Extraordinarias|Se debe colocar el Valor Pagado<br>por Compensaciones<br>Extraordinarias|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Compensaciones/Comp<br>ensacion/@Compensacio<br>nE|
|NIAE151|R<br>PagoS|Concepto Salarial|Se debe colocar el Concepto<br>Salarial|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/BonoEPCTVs/BonoEPCT<br>V/@PagoS|
|NIAE152|R<br>PagoNS|Concepto No Salarial|Se debe colocar el Concepto No<br>Salarial|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/BonoEPCTVs/BonoEPCT<br>V/@PagoNS|
|NIAE153|R<br>PagoAlimentacionS|Concepto Salarial|Se debe colocar el Concepto<br>Salarial|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/BonoEPCTVs/BonoEPCT<br>V/@PagoAlimentacionS|
|NIAE154|R<br>PagoAlimentacionN<br>S|Concepto No Salarial|Se debe colocar el Concepto No<br>Salarial|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/BonoEPCTVs/BonoEPCT<br>V/@PagoAlimentacionNS|
|NIAE155|R<br>Comision|Valor Pagado por Comision|Se debe colocar el Valor Pagado<br>por Comision|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/Comisiones/Comision|
|NIAE193|R<br>PagoTercero|Valor Pagado por Pago Tercero|<sup>Se debe colocar el Valor Pagado</sup><br>por Pago Tercero|1.0|/NominaIndividualDeAjust<br>e/Reemplazar/Devengado<br>s/PagosTerceros/PagoTerc<br>ero|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 213 de 269 

r 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->

r 

> me 6esElemprendimientodeElemprendimientodede todos | jyinhacienda 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientodeElemprendimientodede todos | jyinhacienda<br><!-- End of picture text -->

r 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->

r 

me 6esElemprendimientodeElemprendimientodede todos | jyinhacienda 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientodeElemprendimientodede todos | jyinhacienda<br><!-- End of picture text -->





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_Y_<br>_Campo_|_Regla_|_Mensaje_|_V_|_Xpath_|
|---|---|---|---|---|---|
|NIAE222|R<br>DepartamentoEstad<br>o|Se debe colocar el Codigo de la<br>tabla 5.4.2|Se debe colocar el Codigo<br>correspondiente|1.0|/NominaIndividualDeAjust<br>e/Eliminar/LugarGeneraci<br>onXML/@DepartamentoE<br>stado|
|NIAE223|R<br>MunicipioCiudad|Se debe colocar el Codigo de la<br>tabla 5.4.3|Se debe colocar el Codigo<br>correspondiente|1.0|/NominaIndividualDeAjust<br>e/Eliminar/LugarGeneraci<br>onXML/@MunicipioCiuda<br>d|
|NIAE224|R<br>Idioma|Se debe colocar el Codigo ISO<br>639-1 de la tabla 5.3.1. Para<br>Colombia se debe colocar "es"<br>(Español, Castellano)|Se debe colocar el Codigo ISO<br>639-1 correspondiente. Para<br>Colombia se debe colocar "es"<br>(Español, Castellano)|1.0|/NominaIndividualDeAjust<br>e/Eliminar/LugarGeneraci<br>onXML/@Idioma|
|NIAE225|R<br>RazonSocial|Debe ir el Nombre o Razón<br>Social del Proveedor de<br>Soluciones Tecnológicas|Debe ir el Nombre o Razón<br>Social del Proveedor de<br>Soluciones Tecnológicas|1.0|/NominaIndividualDeAjust<br>e/Eliminar/ProveedorXML<br>/@RazonSocial|
|NIAE226|R<br>PrimerApellido|Debe ir el Primer Apellido del<br>Proveedor de Soluciones<br>Tecnológicas|Debe ir el Primer Apellido del<br>Proveedor de Soluciones<br>Tecnológicas|1.0|/NominaIndividualDeAjust<br>e/Eliminar/ProveedorXML<br>/@PrimerApellido|
|NIAE227|R<br>SegundoApellido|Debe ir el Segundo Apellido del<br>Proveedor de Soluciones<br>Tecnológicas|Debe ir el Segundo Apellido del<br>Proveedor de Soluciones<br>Tecnológicas|1.0|/NominaIndividualDeAjust<br>e/Eliminar/ProveedorXML<br>/@SegundoApellido|
|NIAE228|R<br>PrimerNombre|Debe ir el Primer Nombre del<br>Proveedor de Soluciones<br>Tecnológicas|Debe ir el Primer Nombre del<br>Proveedor de Soluciones<br>Tecnológicas|1.0|/NominaIndividualDeAjust<br>e/Eliminar/ProveedorXML<br>/@PrimerNombre|
|||Deben ir los Otros Nombres del|Deben ir los Otros Nombres del||/NominaIndividualDeAjust|
|NIAE229|N<br>OtrosNombres|Proveedor de Soluciones<br>Tecnológicas|Proveedor de Soluciones<br>Tecnológicas|1.0|e/Eliminar/ProveedorXML<br>/@OtrosNombres|
|NIAE230|R<br>NIT|Se debe colocar el NIT sin<br>guiones ni DV de la empresa<br>dueña del Software que genera<br>el Documento, debe estar<br>registrado en la DIAN|Se debe colocar el NIT sin<br>guiones ni DV de la empresa<br>dueña del Software que genera<br>el Documento, debe estar<br>registrado en la DIAN|1.0|/NominaIndividualDeAjust<br>e/Eliminar/ProveedorXML<br>/@NIT|
|NIAE231|R<br>DV|Se debe colocar el DV de la<br>empresa dueña del Software<br>que genera el Documento, debe<br>estar registrado en la DIAN|<br>Se debe colocar el DV de la<br>empresa dueña del Software<br>que genera el Documento, debe<br>estar registrado en la DIAN|<br>1.0|/NominaIndividualDeAjust<br>e/Eliminar/ProveedorXML<br>/@DV|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 218 de 269 

r 

) | Ma. IN ® POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r me 6esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_ID_|_Y_<br>_Campo_|_Regla_|_Mensaje_|_V_|_Xpath_|
|---|---|---|---|---|---|
|NIAE242|N<br>Notas|Información adicional: Texto<br>libre, relativo al documento|Utilizado para agregar Notas al<br>documento|1.0|/NominaIndividualDeAjust<br>e/Eliminar/Notas|
|NIAE243|R<br>RazonSocial|Debe ir el Nombre o Razón<br>Social del Empleador|Debe ir el Nombre o Razón<br>Social del Empleador|1.0|/NominaIndividualDeAjust<br>e/Eliminar/Empleador/@R<br>azonSocial|
|NIAE244|R<br>PrimerApellido|Debe ir el Primer Apellido del<br>Empleador|Debe ir el Primer Apellido del<br>Empleador|1.0|/NominaIndividualDeAjust<br>e/Eliminar/Empleador/@P<br>rimerApellido|
|NIAE245|R<br>SegundoApellido|Debe ir el Segundo Apellido del<br>Empleador|Debe ir el Segundo Apellido del<br>Empleador|1.0|/NominaIndividualDeAjust<br>e/Eliminar/Empleador/@S<br>egundoApellido|
|NIAE246|R<br>PrimerNombre|Debe ir el Primer Nombre del<br>Empleador|Debe ir el Primer Nombre del<br>Empleador|1.0|/NominaIndividualDeAjust<br>e/Eliminar/Empleador/@P<br>rimerNombre|
|NIAE247|N<br>OtrosNombres|Deben ir los Otros Nombres del<br>Empleador|Deben ir los Otros Nombres del<br>Empleador|1.0|/NominaIndividualDeAjust<br>e/Eliminar/Empleador/@<br>OtrosNombres|
|NIAE248|R<br>NIT|Debe ir el NIT del Empleador sin<br>guiones ni DV|<br>Debe ir el NIT del Empleador sin<br>guiones ni DV|<br>1.0|/NominaIndividualDeAjust<br>e/Eliminar/Empleador/@<br>NIT|
|NIAE249|R<br>DV|Debe ir el DV del Empleador|Debe ir el DV del Empleador|1.0|/NominaIndividualDeAjust<br>e/Eliminar/Empleador/@<br>DV|
|NIAE250|R<br>Pais|Se debe colocar el Codigo alfa-2<br>de la tabla 5.4.1|<br>Se debe colocar el Codigo alfa-2<br>correspondiente|1.0|/NominaIndividualDeAjust<br>e/Eliminar/Empleador/@P<br>ais|
|NIAE251|R<br>DepartamentoEstad<br>o|Se debe colocar el Codigo de la<br>tabla 5.4.2|Se debe colocar el Codigo<br>correspondiente|1.0|/NominaIndividualDeAjust<br>e/Eliminar/Empleador/@<br>DepartamentoEstado|
|NIAE252|R<br>MunicipioCiudad|Se debe colocar el Codigo de la<br>tabla 5.4.3|Se debe colocar el Codigo<br>correspondiente|1.0|/NominaIndividualDeAjust<br>e/Eliminar/Empleador/@<br>MunicipioCiudad|
|NIAE253|R<br>Direccion|Debe ir la Dirección Fisica del<br>Empleador|Debe ir la Dirección Fisica del<br>Empleador|1.0|/NominaIndividualDeAjust<br>e/Eliminar/Empleador/@<br>Direccion|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 220 de 269 

**Resolución No. 000013** 





### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

### _6.1.3._ Firma Digital del Documento: _ds:Signature_ . 

|_ID_|_Y_|_Campo _|_Regla_|_Mensaje _|_V_|_Xpath_|
|---|---|---|---|---|---|---|
||||Solamente puede haber una<br>||||
|DC01|R|Signature|ocurrencia del Grupo<br>Ext:ExtensionContent<br>conteniendo información de la<br>firma información.|Más de un grupo  DIAN<br>_Extensión_conteniendo<br>información electrónica|1|…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature|
|DC02|R|SignedInfo|Este grupo debe contener tres<br>(3) grupos Reference|El Grupo Reference no aparece<br>tres veces.|1|…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:SignedInfo|
|DC03|R|Canonicalization<br>Method|Se verifica que el valor usado<br>corresponde al establecido<br>según<br>http://www.w3.org/TR/2001/R<br>EC-xml-c14n-20010315.|El valor usado en<br>Canonicalization Method no<br>corresponde al definido|1|…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:SignedInfo/ds:Canoni<br>calizationMethod|
|DC04|R|SignatureMethod|El método debe ser SHA 256 o<br>SHA 384 o SHA 512|El método de firma utilizado no<br>corresponde a la política de<br>firma de la DIAN.|1|…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:SignedInfo/ds:Signat<br>ureMethod|
|DC05|R|Reference|Debe contener la información<br>de la firma aplicada a todo el<br>documento.|La información suministrada<br>no corresponde a la contendia<br>en  URI=””|1|…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:SignedInfo/ds:Refere<br>nce|
|DC06|R|Transforms|El grupo debe existir una vez|El grupo NO existe una vez|1|…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:SignedInfo/ds:Refere<br>nce/ds:Transforms|
|DC07|R|TransForm|El contenido de la firma debe<br>estar embebido en el<br>documento.|El valor del elemento debe ser<br>igual a<br>Algorithm=”http://www.w3.or<br>g/2000/09/xmldsig#enveloped<br>-signature”|1|…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:SignedInfo/ds:Refere<br>nce/ds:Transforms/ds:Tr<br>ansForm|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 221 de 269 

**Resolución No. 000013** 





### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|DC08|R|DigestMethod|El algoritmo reportado debe<br>ser uno de los siguientes<br>valores:<br>RSAwithSHA256=http://www.<br>w3.org/2001/04/xmldsig-<br>more#rsa-sha256<br>RSAwithSHA384=http://www.<br>w3.org/2001/04/xmldsig-<br>more#rsa-sha384<br>RSAwithSHA512=http://www.<br>w3.org/2001/04/xmldsig-<br>more#rsa-sha512|El valor reportado no<br>corresponde a los definidos en<br>la política de firma.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:SignedInfo/ds:Refere<br>nce/ds:DigestMethod|
|---|---|---|---|---|---|
|DC09|R|DigestValue|El valor de hash generado a<br>partir del uso del algoritmo<br>reportado en DigestMethod en<br>base 64 debe corresponder.|El valor de hash generado a<br>partir del uso del algoritmo<br>reportado en DigestMethod no<br>corresponde.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:SignedInfo/ds:Refere<br>nce/ds:DigestValue|
|DC10|R|Reference|Debe contener la información<br>correspondiente a la clave<br>públic contenida en el<br>elemento KeyInfo|La información suministrada<br>no corresponde a la contendia<br>en  URI=”#{UUID}-KeyInfo”|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:SignedInfo/ds:Refere<br>nce|
|DC11|R|DigestMethod|El algoritmo reportado debe<br>ser uno de los siguientes<br>valores:<br>RSAwithSHA256=http://www.<br>w3.org/2001/04/xmldsig-<br>more#rsa-sha256<br>RSAwithSHA384=http://www.<br>w3.org/2001/04/xmldsig-<br>more#rsa-sha384<br>RSAwithSHA512=http://www.<br>w3.org/2001/04/xmldsig-<br>more#rsa-sha512|El valor reportado NO<br>corresponde a los definidos en<br>la política de firma|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:SignedInfo/ds:Refere<br>nce/ds:DigestMethod|
|DC12|R|DigestValue|El valor de hash generado a<br>partir del uso del algoritmo<br>reportado en DigestMethod en<br>base 64 debe corresponder.|El valor de hash generado a<br>partir del uso del algoritmo<br>reportado en DigestMethod no<br>corresponde.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:SignedInfo/ds:Refere<br>nce/ds:DigestValue|
|DC13|R|Reference|Debe contener la información<br>correspondiente al grupo<br>SignedProperties.|La información suministrada<br>no corresponde a la contendia<br>en  URI=”#xmldsig-{UUID}-<br>signedprops”|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 222 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

||||||/ds:SignedInfo/ds:Refere<br>nce|
|---|---|---|---|---|---|
|DC14|R|DigestMethod|El algoritmo reportado debe<br>ser uno de los siguientes<br>valores:<br>RSAwithSHA256=http://www.<br>w3.org/2001/04/xmldsig-<br>more#rsa-sha256<br>RSAwithSHA384=http://www.<br>w3.org/2001/04/xmldsig-<br>more#rsa-sha384<br>RSAwithSHA512=http://www.<br>w3.org/2001/04/xmldsig-<br>more#rsa-sha512|El valor reportado no<br>corresponde a los definidos en<br>la política de firma.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:SignedInfo/ds:Refere<br>nce/ds:DigestMethod|
|DC15|R|DigestValue|El valor de hash generado a<br>partir del uso del algoritmo<br>reportado en DigestMethod en<br>base 64 debe corresponder.|El valor de hash generado a<br>partir del uso del algoritmo<br>reportado en DigestMethod no<br>corresponde.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:SignedInfo/ds:Refere<br>nce/ds:DigestValue|
|DC16|R|SignatureValue|El valor de hash generado a<br>partir del uso del algoritmo<br>reportado en SignatureMethod<br>en base 64 debe corresponder.|El valor de hash generado a<br>partir del uso del algoritmo<br>reportado en SignatureMethod<br>NO corresponde.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:SignatureValue|
||||||//Ext:UBLExtensions/ex|
|DC17|R|KeyInfo|El grupo debe existir una vez.|El grupo no se reportó una vez.|1<br>…<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:KeyInfo|
|DC18|R|X509Data|El grupo debe existir una vez.|El grupo no se reportó una vez.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:KeyInfo/ds:X509Data|
|DC19|R|X509Certificate|Debe ser un certificado<br>público.|El certificado reportardo no es<br>un certificado público válido.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:KeyInfo/ds:X509Data<br>/ds:X509Certificate|
|DC20|R|Object|El grupo debe existir una vez.|El grupo no se reportó una vez.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object|
|DC21|R|Qualifying<br>Properties|El grupo debe existir una vez.|El grupo no se reportó una vez.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 223 de 269 

**Resolución No. 000013** 





### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|DC22|R|SignedProperties|El grupo debe existir una vez.|El grupo no se reportó una vez.|1|…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties|
|---|---|---|---|---|---|---|
|DC23|R|SignedSignature<br>Properties|El grupo debe existir una vez.|El grupo no se reportó una vez.|1|…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties|
|DC24|R|SigningTime|El valor de la fecha debe venir<br>en el formato definido en la<br>política de firma y debe ser<br>menor a la fecha del sistema.|Error en el valor de la fecha y<br>hora de firma. NO corresponde<br>al formato y/o el valor<br>reportado es superior a la<br>fecha del sistema.|1|…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningTime|
|DC25|R|SigningCertificate|El grupo debe existir una vez.<br>Dentro de este grupo deben<br>aparecer al menos tres grupos<br>Cert diferentes.|El grupo NO se reportó una vez<br>ó el grupo Cert aparece menos<br>de tres de veces.|1|…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningCertificate|
|DC26|R|Cert|El grupo debe existir una vez.|El grupo no se reportó una vez.|1|…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningCertificate/xa<br>des:Cert|
|DC27|R|CertDigest|El grupo debe existir una vez.|El grupo no se reportó una vez.|1|…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningCertificate/xa<br>des:Cert/xades:CertDiges<br>t|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 224 de 269 

**Resolución No. 000013** 





### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|DC28|R|DigestMethod|El algoritmo reportado debe<br>ser uno de los siguientes<br>valores:<br>RSAwithSHA256=http://www.<br>w3.org/2001/04/xmldsig-<br>more#rsa-sha256<br>RSAwithSHA384=http://www.<br>w3.org/2001/04/xmldsig-<br>more#rsa-sha384<br>RSAwithSHA512=http://www.<br>w3.org/2001/04/xmldsig-<br>more#rsa-sha512|El valor reportado NO<br>corresponde a los definidos en<br>la política de firma|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningCertificate/xa<br>des:Cert/xades:CertDiges<br>t/ds:DigestMethod|
|---|---|---|---|---|---|
|DC29|R|DigestValue|El valor de hash generado a<br>partir del uso del algoritmo<br>reportado en DigestMethod en<br>base 64 debe corresponder.|El valor de hash generado a<br>partir del uso del algoritmo<br>reportado en DigestMethod<br>NO corresponde.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningCertificate/xa<br>des:Cert/xades:CertDiges<br>t/ds:DigestValue|
|DC30|R|IssuerSerial|El grupo debe existir una vez.|El grupo no se reportó una vez.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningCertificate/xa<br>des:Cert/xades:IssuerSeri<br>al|
|DC31|R|X509IssuerName|Debe ser igual al Subject que<br>viene en el certificado público<br>informado en X509Certificate|El valor reportado NO<br>corresponde con el valor<br>informado en X509Certificate|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningCertificate/xa<br>des:Cert/xades:IssuerSeri<br>al/ds:X509IssuerName|
|DC32|R|X509Serial Number|Debe ser igual al Serial que<br>viene en el certificado público<br>informado en X509Certificate|El valor reportado no<br>corresponde con el valor<br>informado en X509Certificate|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 225 de 269 

**Resolución No. 000013** 





### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|||||ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningCertificate/xa<br>des:Cert/xades:IssuerSeri<br>al/ds:X509SerialNumber|
|---|---|---|---|---|
|DC33|R<br>Cert|El grupo debe existir una vez.|El grupo no se reportó una vez.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningCertificate/xa<br>des:Cert|
|DC34|CertDigest|||1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningCertificate/xa<br>des:Cert/xades:CertDiges<br>t|
|DC35|R<br>DigestMethod|El algoritmo reportado debe<br>ser uno de los siguientes<br>valores:<br>RSAwithSHA256=http://www.<br>w3.org/2001/04/xmldsig-<br>more#rsa-sha256<br>RSAwithSHA384=http://www.<br>w3.org/2001/04/xmldsig-<br>more#rsa-sha384<br>RSAwithSHA512=http://www.<br>w3.org/2001/04/xmldsig-<br>more#rsa-sha512|El valor reportado NO<br>corresponde a los definidos en<br>la política de firma.|<br>1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningCertificate/xa<br>des:Cert/xades:CertDiges<br>t/ds:DigestMethod|
|DC36|DigestValue|El valor de hash generado a<br>partir del uso del algoritmo<br>reportado en DigestMethod en<br>base 64 debe corresponder.|<br>El valor de hash generado a<br>partir del uso del algoritmo<br>reportado en DigestMethod<br>NO corresponde.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningCertificate/xa|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 226 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

||||||des:Cert/xades:CertDiges<br>t/ds:DigestValue|
|---|---|---|---|---|---|
|DC37|R|IssuerSerial|El IssuerName y IssuerSerial<br>deben pertenecer a una<br>entidad subordinada<br>certificadora abierta avalada<br>por la ONAC en Colombia.|El certificado NO pertenece a<br>una de las Entidades<br>certificadoras abiertas<br>subordinadas avaladas por la<br>ONAC en Colombia.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningCertificate/xa<br>des:Cert/xades:IssuerSeri<br>al|
|DC38|R|X509IssuerName|El IssuerName debe<br>pertenecer a una entidad<br>subordinada certificadora<br>abierta avalada por la ONAC en<br>Colombia.|El valor no corresponde a una<br>entidad subordinada<br>certificadora abierta avalada<br>por la ONAC en Colombia.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningCertificate/xa<br>des:Cert/xades:IssuerSeri<br>al/ds:X509IssuerName|
|DC39|R|X509Serial Number|El SerialNumber debe<br>pertenecer a una entidad<br>subordinada certificadora<br>abierta avalada por la ONAC en<br>Colombia.|El valor no corresponde a una<br>entidad subordinada<br>certificadora abierta avalada<br>por la ONAC en Colombia.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningCertificate/xa<br>des:Cert/xades:IssuerSeri<br>al/ds:X509SerialNumber|
|DC40|R|Cert|El grupo debe existir una vez.|El grupo no se reportó una vez.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningCertificate/xa<br>des:Cert|
|DC41|R|CertDigest|El grupo debe existir una vez.|El grupo no se reportó una vez.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningCertificate/xa|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 227 de 269 

**Resolución No. 000013** 





### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

||||||des:Cert/xades:CertDiges<br>t|
|---|---|---|---|---|---|
|DC42|R|DigestMethod|El algoritmo reportado debe<br>ser uno de los siguientes<br>valores:<br>RSAwithSHA256=http://www.<br>w3.org/2001/04/xmldsig-<br>more#rsa-sha256<br>RSAwithSHA384=http://www.<br>w3.org/2001/04/xmldsig-<br>more#rsa-sha384<br>RSAwithSHA512=http://www.<br>w3.org/2001/04/xmldsig-<br>more#rsa-sha512|El valor reportado NO<br>corresponde a los definidos en<br>la política de firma.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningCertificate/xa<br>des:Cert/xades:CertDiges<br>t/ds:DigestMethod|
|DC43|R|DigestValue|El valor de hash generado a<br>partir del uso del algoritmo<br>reportado en DigestMethod en<br>base 64 debe corresponder.|El valor de hash generado a<br>partir del uso del algoritmo<br>reportado en DigestMethod<br>NO corresponde.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningCertificate/xa<br>des:Cert/xades:CertDiges<br>t/ds:DigestValue|
|DC44|R|IssuerSerial|El IssuerName y IssuerSerial<br>deben pertenecer a una<br>entidad raíz certificadora<br>abierta avalada por la ONAC en<br>Colombia.|El certificado NO pertenece a<br>una de las Entidades<br>certificadoras abiertas raíces<br>avaladas por la ONAC en<br>Colombia.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningCertificate/xa<br>des:Cert/xades:IssuerSeri<br>al|
|DC45|R|X509IssuerName|El IssuerName debe<br>pertenecer a una entidad raíz<br>certificadora abierta avalada<br>por la ONAC en Colombia.|El valor NO corresponde a una<br>entidad raíz certificadora<br>abierta avalada por la ONAC en<br>Colombia.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningCertificate/xa<br>des:Cert/xades:IssuerSeri<br>al/ds:X509IssuerName|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 228 de 269 





### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|DC46|R|X509Serial Number|El SerialNumber debe<br>pertenecer a una entidad raíz<br>certificadora abierta avalada<br>por la ONAC en Colombia.|El valor NO corresponde a una<br>entidad raíz certificadora<br>abierta avalada por la ONAC en<br>Colombia.|1|…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SigningCertificate/xa<br>des:Cert/xades:IssuerSeri<br>al/ds:X509SerialNumber|
|---|---|---|---|---|---|---|
|DC47|R|SignaturePolicy<br>Identifier|El grupo debe existir una vez.|El grupo no se reportó una vez.|1|…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SignaturePolicyIdenti<br>fier|
|DC48|R|SignaturePolicyId|El grupo debe existir una vez.|El grupo no se reportó una vez.|1|…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SignaturePolicyIdenti<br>fier/xades:SignaturePolic<br>yId|
|DC49|R|SigPolicyId|El grupo debe existir una vez.|El grupo no se reportó una vez.|1|…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SignaturePolicyIdenti<br>fier/xades:SignaturePolic<br>yId/xades:SigPolicyId|
|DC50|R|Identifier|Debe incluir el identificador<br>definido por la DIAN.|El identificador NO<br>corresponde con el valor<br>definido por la DIAN.|1|…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SignaturePolicyIdenti<br>fier/xades:SignaturePolic|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 229 de 269 



##### 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

||||||yId/xades:SigPolicyId/xad<br>es:Identifier|
|---|---|---|---|---|---|
|DC51|R|SigPolicyHash|El grupo debe existir una vez.|El grupo no se reportó una vez.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SignaturePolicyIdenti<br>fier/xades:SignaturePolic<br>yId/xades:SigPolicyHash|
|DC52|R|DigestMethod|El algoritmo reportado debe<br>ser uno de los siguientes<br>valores:<br>RSAwithSHA256=http://www.<br>w3.org/2001/04/xmldsig-<br>more#rsa-sha256<br>RSAwithSHA384=http://www.<br>w3.org/2001/04/xmldsig-<br>more#rsa-sha384<br>RSAwithSHA512=http://www.<br>w3.org/2001/04/xmldsig-<br>more#rsa-sha512|El valor reportado NO<br>corresponde a los definidos en<br>la política de firma.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SignaturePolicyIdenti<br>fier/xades:SignaturePolic<br>yId/xades:SigPolicyHash/<br>ds:DigestMethod|
|DC53|R|DigestValue|El valor de hash generado a<br>partir del uso del algoritmo<br>reportado en DigestMethod en<br>base 64 debe corresponder.|<br>El valor de hash generado a<br>partir del uso del algoritmo<br>reportado en DigestMethod<br>NO corresponde.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SignaturePolicyIdenti<br>fier/xades:SignaturePolic<br>yId/xades:SigPolicyHash/<br>ds:DigestValue|
|DC54|R|SignerRole|El grupo debe existir una vez.|El grupo no se reportó una vez.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature<br>/ds:Object/xades:Qualifyi<br>ngProperties/xades:Signe<br>dProperties/xades:Signe<br>dSignatureProperties/xa<br>des:SignerRole|
|DC55|R|ClaimedRoles|El grupo debe existir una vez.|El grupo no se reportó una vez.|1<br>…//Ext:UBLExtensions/ex<br>t:UBLExtension/ext:Exten<br>sionContent/ds:Signature|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 230 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 



El valor del rol debe ser El valor NO contiene uno de los DC56 R ClaimedRole 1 thirdparty ó supplier. definidos. 

/ds:Object/xades:Qualifyi ngProperties/xades:Signe dProperties/xades:Signe dSignatureProperties/xa des:SignerRole/xades:Cla imedRoles 

…//Ext:UBLExtensions/ex t:UBLExtension/ext:Exten sionContent/ds:Signature /ds:Object/xades:Qualifyi ngProperties/xades:Signe dProperties/xades:Signe dSignatureProperties/xa des:SignerRole/xades:Cla imedRoles/xades:Claime dRole 

### 6.2. Reglas Relativas al Establecimiento de la Conexión. 

### 6.2.1. Mensaje del Web Service. 

|_#_<br>ZA01|_Regla_<br>Verificar si el tamaño del archivo XML es superior a 500 KB|_Y_<br>R|_Mensaje _<br>Tamaño del mensaje superior al límite establecido<br>[Máximo: 500 KB]|_V_<br>1.0|
|---|---|---|---|---|
|ZA02|Verificar si el servicio estáparado momentáneamente|N|Servicioparado momentáneamente[cortoplazo]|1.0|
|ZA03|Verificar si el servicio estáparado sinprevisión|N|Servicioparado sinprevisión|1.0|



### 6.2.2. Schema XML. 

|_#_|_Regla_|_Y_|<br>_Mensaje _|_V_|
|---|---|---|---|---|
|ZB01|Verificar si el esquema XML está correcto|R|<br>Fallo en el esquema XML del archivo|1.0|
|ZB02|Verificar la existencia de caracteres de edición en el inicio o<br>fin del mensaje o entre los tags|R|<br>No es permitida la presencia de caracteres de edición en<br>el inicio/fin o entre los tags del mensaje|1.0|
|ZB03|Verificar si el XML utiliza la codificación diferente de UTF-8|R|<br>XML con codificación diferente de UTF-8|1.0|
|ZB04|Verificar las personalizaciones de DIAN<br>(Prefijos de NameSpace)|R|<br>XML no cumple con las personalizaciones de XSD-<br>NóminaDIAN|1.0|



### 6.2.3. Certificado Digital de Transmisión (conexión). 

|_#_|_Regla_|_Y_|_Mensaje _|_V_|
|---|---|---|---|---|
|ZC01|Verificar validez del Certificado Digital de transmisión|R|Certificado de la Transmisión vencido|1.0|
|ZC02|Error en acceso a la Lista de Certificados revocados (CRL)<br>- Falta la dirección de la CRL (CRLDistributionPoint)<br>- Error en el acceso a la CRL o CRL inexistente|R|Certificado Firma – Error en el acceso a la CRL|1.0|
|ZC03|Verificar Lista de Certificados revocados (CRL)|R|Certificado de Transmisión revocado|1.0|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 231 de 269 



### **Resolución No. 000013** 



(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|_#_|_Regla_|_Y_|_Mensaje _|_V_|
|---|---|---|---|---|
|ZC04|Verificar Cadena de Certificación:<br>- Certificado de la AC emisora no registrado<br>- Certificado de AC revocado<br>- Certificado no asignadopor la AC emisora del Certificado|R|Certificado de Transmisión – Error en la Cadena de<br>Certificación|1.0|
|ZC05|Verificar la cadena de confianza del certificado|R|La cadena de confianza No se pudo verificar o se<br>encuentra revocada.|1.0|
|ZC06|El certificado tiene que tener los atributos de conexión|R|El certificado no contiene los atributos para realizar<br>conexión de trasmisión.|1.0|



### 6.2.4. Certificado Digital de Firma (Firma XML). 

|_#_|_Regla_|_Y_|_Mensaje _|_V_|
|---|---|---|---|---|
|ZD01|Verificar si existe certificado de firma|R|Certificado de Firma inexistente en el<br>archivo|1.0|
|ZD02|Verificar data validez (data inicio y data fin) del Certificado<br>Digital de la Firma|R|Certificado de la Firma con data de validez inválida|1.0|
|ZD03|Error en al acceso a la Lista de Certificados revocados (CRL)<br>- Falta la dirección de la CRL (CRLDistributionPoint)<br>- Error en el acceso a la CRL o CRL inexistente|R|Certificado de la Firma – Error en el acceso a la CRL|1.0|
|ZD04|Verificar Lista de Certificados revocados(CRL)|R|Certificado de la Firma revocado|1.0|
|ZD05|Verificar Cadena de Certificación:<br>- Certificado de la AC emisora no registrado<br>- Certificado de AC revocado<br>- Certificado no asignadopela AC emisora del Certificado|R|Certificado de la Firma – Error en la Cadena de<br>Certificación|1.0|
|ZD06|Verificar la cadena de confianza del certificado|R|La cadena de confianza no se puede verificar o se<br>encuentra revocada.|1.0|
|ZD07|El certificado tiene que tener los atributos de no repudio<br>para firmar digitalmente|R|El certificado no contiene los atributos para realizar la<br>firma digital con no repudio.|1.0|



### 6.2.5. Firma. 

|_#_|_Regla_|_Y_|_Mensaje _|_V_|
|---|---|---|---|---|
|ZE01|Verificar si la firma está en el estándar (XMLDSig con<br>formato XAdES-EPES)|R|Certificado de la Firma con estándar inválido|1.0|
|ZE02|Verificar si el valor de la Firma está válido (difiere del<br>calculado)|R|Valor de la Firma inválido|1.0|
|ZE03|Identificación (ID) del emisor difiere de la Identificación<br>(propietario)del Certificado Digital|R|ID del emisor difiere del propietario del Certificado<br>Digital|1.0|



### Abreviaturas Utilizadas. 

CIAT ......................... Centro Interamericano de Administraciones Tributarias. CUNE ....................... Código Único de Documento Soporte de Pago de Nómina Electrónica. DE ............................ Documento Electrónico. 

DIAN ........................ Dirección de Impuestos y Aduanas Nacionales. 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 232 de 269 

® 



<!-- Start of picture text -->
) | Ma. IN<br><!-- End of picture text -->

POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
r esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->

**Resolución No. 000013** 





(11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

### 7. Política de firma. 

### 7.1. Observaciones. 

Todo documento electrónico enviado a la DIAN para validación deberá ser firmado con un certificado digital, expedido por una entidad de certificación digital Abierta autorizada por la Organización Nacional de Acreditación de Colombia (ONAC) para tal fin, cualquier documento electrónico firmado que no cumpla con esta condición, se entenderá invalido y no tendrá los efectos fiscales establecidos en el artículo 616-1 del Estatuto Tributario y en la normativa vigente de factura electrónica.. 

### 7.2. Consideraciones Generales. 

El objetivo de esta Política define las principales características técnicas para la firma digital, que garantizan la integridad, autenticidad y no repudio de todos los procesos que soporten la implementación del Documento Soporte de Pago de Nómina Electrónica en Colombia con fines de masificación y control fiscal, y adicionalmente los criterios comunes para el reconocimiento mutuo de firmas digitales basadas en certificados digitales, que garanticen la seguridad e interoperabilidad. 

La Política de Firma está indicada y referenciada para todos los documentos electrónicos que componen el conjunto de documentos del negocio electrónico denominado Documento Soporte de Pago de Nómina Electrónica establecida por el Gobierno Nacional a cargo de la DIAN. Para todos los documentos que componen el Documento Soporte de Pago de Nómina Electrónica la firma se hará mediante la inclusión de una etiqueta i.e. <Signature …/> — dentro del formato estándar de intercambio XML, el cual está localizado en la siguiente ruta: XPath: 

- /NominaIndividual/Ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/ds:Signature 

- /NominaIndividualDeAjuste/Ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/ds:Signature 

La etiqueta contendrá los elementos que constituyen la implementación del estándar técnico XAdES, i.e. XML Advanced Electronic Signature asc; firma digital avanzada XML. 

La política de firma suministra la información que sobre la firma digital con destino al control fiscal de la DIAN, deberá aplicar el Sujeto Obligado como medida de ampliación del proceso de expedición de las nóminas electrónicas. Se advierte que los detalles de las técnicas informáticas de implementación no forman parte de esta política. Únicamente se incluyen las referencias a los estándares que describen las especificaciones técnicas sobre la implementación. 

La política de firma suministra la información que sobre la firma digital debiera verificar el Receptor de la Nómina, de acuerdo a la normatividad vigente. 

### 7.3. Especificaciones técnicas sobre la firma digital Avanzada. 

ETSI TS 101 903, v.1.2.2. v 1.3.2. y 1.4.1. Electronic Signatures and Infrastructures (SEI); XML Advanced Electronic Signatures (XAdES). 

> Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 234 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

ETSI TR 102 038, v.1.1.1. Electronic Signatures and Infraestructures (SEI); XML format for signature policies. ETSI TS 102 176-1 V2.0.0 Electronic Signatures and Infraestructures (ESI): Algorithms and Paremeters for Secure Electronic Signatures; Part 1: Hash functions and asymmetric algorithms. 

ETSI TR 102 041, v.1.1.1. Electronic Signatures and Infraestructures (SEI); Signature policies report. 

ETSI TR 102 045, v.1.1.1. Electronic Signatures and Infraestructures (SEI); Signature policy for extended business model. 

ETSI TR 102 272, v.1.1.1. Electronic Signatures and Infraestructures (SEI); ASN.1 format for signature policies. IETF RFC 2560, X.509 Public Key Infrastructure Online Certificate Status-Protocol-OCSP 

IETF RFC 3125, Electronic Signature Policies 

IETF RFC 5280, RFC 4325 y RFC 4630, Internet X.509 Public Key Infrastructure; Certificate and Certificate Revocation List (CRL) Profile. 

ITU-T Recommendation X.680 (1997): “Information technology – Abstract Syntax Notation One (ASN.1): Specification on basic notation”. 

### 7.4. Alcance de la Política de Firma. 

Este documento define la Política de Firma que detalla las condiciones para la validación del Documento Soporte de Pago de Nómina Electrónica y que deberán ser admitidas por todas las plataformas tecnológicas implicadas en el ciclo del Documento Soporte de Pago de Nómina Electrónica. 

### 7.5. Política de Firma. 

### 7.5.1. Actores de la Firma. 

Sujeto Obligado o Empleador: 

Persona natural o jurídica que como tal debe emitir electrónicamente el Documento Soporte de Pago de Nómina Electrónica en las condiciones establecidas en la normatividad vigente. Para el ámbito de la firma digital son los _firmantes_ vinculados a la persona natural o jurídica que ha cumplido la habilitación como Sujeto Obligado. 

Proveedor de Soluciones Tecnológicas: 

En el ámbito de la emisión del Documento Soporte de Pago de Nómina Electrónica podrá ser el _firmante_ autorizado por el Sujeto Obligado a actuar en su nombre, de acuerdo con lo señalado en el artículo 22 de la presente resolución. 

- El término _firmante_ se circunscribe a la definición dada en el Artículo 1.4 Decreto 2364 de 2012. 

- Entidades de Certificación Digital – ECD: 

En el ámbito del Documento Soporte de Pago de Nómina Electrónica es el tercero de confianza que tiene bajo su control la gestión de constatación, expedición, autenticación y registro histórico de los certificados digitales utilizados para las firmas digitales de las nóminas electrónicas. 

### 7.5.2. Formato de Firma. 

Se debe utilizar el estándar XMLDSig enveloped con formato XAdES-EPES según la especificación técnica ETSI TS 101 903, versión 1.2.2, versión 1.3.2 y versión 1.4.1 siendo obligatorio indicar la versión adoptada en las etiquetas XML, en las que se hace referencia al número de versión. 

> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Página 235 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

El formato XAdES de firma digital avanzada adoptado por la DIAN para el uso de firma digital corresponde a la Directiva XAdES-EPES, con el certificado digital y toda la cadena de certificación (desde el certificado raíz) incluida en los elementos «ds:X509Data» y «ds:Object», y la política de firma, es decir este documento, como un hiperenlace en el elemento «xades:SignaturePolicyIdentifier». 

Se admiten como válidos los algoritmos de generación de hash, codificación en base64, firma, normalización y transformación definidos en el estándar XMLDSig. 

### 7.6. Algoritmo de Firma. 

El algoritmo de firma usado sobre el elemento «SignedInfo» (organizado previamente como establece el cánon) para la firma digital (que se adiciona al elemento «SignatureValue») del Documento Soporte de Pago de Nómina Electrónica puede ser cualquiera de los definidos en la especificación XML-Signature Syntax and Processing (http:/www.w3.org/TR/xmldsig-core2/#sec-Algorithms) que actualmente son: <u>Recomendado RSAwithSHA256 http:/www.w3.org/2001/04/xmldsig-more#rsa-sha256 Recomendado RSAwithSHA384 http:/www.w3.org/2001/04/xmldsig-more#rsa-sha384 Recomendado RSAwithSHA512 http:/www.w3.org/2001/04/xmldsig-more#rsa-sha512</u> 

### 7.7. Algoritmo de Organización de Datos según el Canon. 

El algoritmo para organizar los datos según el canon usado sobre el elemento «SignedInfo» para la firma digital (que se adiciona al elemento «SignatureValue») del Documento Soporte de Pago de Nómina Electrónica es “Canonical XML (omits comments)”. Para esto se debe usar el valor “http:/www.w3.org/TR/2001/REC-xml-c14n20010315” dentro del elemento «CanonicalizationMethod». 

NOTA: atienda lo dicho en la sección “8 Sobre el CANON de los documentos electrónicos y la validez de la firma digital” 

_<ds:CanonicalizationMethod Algorithm="http:/www.w3.org/TR/2001/REC-xml-c14n-20010315" />_ 

### 7.8. Ubicación de la Firma. 

La firma se ubicará dentro del documento electrónico en el XPath: 

_/NominaIndividual||NominaIndividualDeAjuste/Ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent_ /ds:S ignature/ds:SignatureValue Para mayor detalle de los elementos que componen la firma ver el numeral <u>3.6</u> de este documento. 

### 7.9. Condiciones de la Firma. 

El emisor del Documento Soporte de Pago de Nómina Electrónica o el proveedor de soluciones tecnológicas expresamente autorizado por este para hacerlo deberá aplicar la firma digital sobre el documento completo, con un certificado digital vigente y no revocado al momento de la firma. 

La firma se aplica a todos los elementos del Documento Soporte de Pago de Nómina Electrónica, los elementos contenidos dentro del elemento SignedProperties más la clave pública contenida en el elemento KeyInfo. Cada uno de estos se adiciona como referencia dentro del elemento SignedInfo. 

#### _<ds:SignedInfo>_ 

_<ds:CanonicalizationMethod Algorithm="http:/www.w3.org/TR/2001/REC-xml-c14n-20010315"/>_ 

> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Página 236 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

_<ds:SignatureMethod Algorithm="http:/www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>_ 

_<ds:Reference Id="xmldsig-50280329-cdf3-4bb7-9d8f-edd480c8079c-ref0" URI="">_ 

- _<ds:Transforms>_ 

_<ds:Transform Algorithm="http:/www.w3.org/2000/09/xmldsig#enveloped-signature"/>_ 

_</ds:Transforms>_ 

_<ds:DigestMethod Algorithm="http:/www.w3.org/2001/04/xmlenc#sha256"/>_ 

_<ds:DigestValue>vDUXUvy+JoIsT1k4dFv7ay8eJ+7jOMyRTcqiVKkdXHI=</ds:DigestValue>_ 

_</ds:Reference>_ 

_<ds:Reference URI="#xmldsig-50280329-cdf3-4bb7-9d8f-edd480c8079c-keyinfo">_ 

_<ds:DigestMethod Algorithm="http:/www.w3.org/2001/04/xmlenc#sha256"/>_ 

_<ds:DigestValue>O5Bin7GRCjlH8qG1BFc3Cd2GlFx+IAp5DoEpn3nArgk=</ds:DigestValue>_ 

_</ds:Reference>_ 

_<ds:Reference Type="http:/uri.etsi.org/01903#SignedProperties" URI="#xmldsig-50280329-cdf3-4bb79d8f-edd480c8079c-signedprops">_ 

_<ds:DigestMethod Algorithm="http:/www.w3.org/2001/04/xmlenc#sha256"/>_ 

_<ds:DigestValue>scoM3Nb4cTlMm1GHP9ECfFetSUP+S9DqTVYVHW99KEw=</ds:DigestValue>_ 

_</ds:Reference>_ 

_</ds:SignedInfo>_ 

El certificado público requerido para validar la firma debe ser embebido dentro del XPath: 

/NominaIndividual||NominaIndividualDeAJuste/Ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/ds :Signature/ds:KeyInfo/ds:X509Data/ds:X509Certificate 

en formato base64: 

_<ds:KeyInfo Id="xmldsig-50280329-cdf3-4bb7-9d8f-edd480c8079c-keyinfo">_ 

- _<ds:X509Data>_ 

   - _<ds:X509Certificate>_ 

_MIIHEjCCBfqgAwIBAgIQRMochPrzPAhYXX/wKSkB/DANBgkqhkiG9w0BAQsFADCBqDEcMBoGA1UECQ wTd3d3LmNlcnRpY2FtYXJhLmNvbTEPMA0GA1UEBwwGQk9HT1RBMRkwFwYDVQQIDBBESVNUUklU TyBDQVBJVEFMMQswCQYDVQQGEwJDTzEYMBYGA1UECwwPTklUIDgzMDA4NDQzMy03MRgwFgY DVQQKDA9DRVJUSUNBTUFSQSBTLkExGzAZBgNVBAMMEkFDIFNVQiBDRVJUSUNBTUFSQTAgFw0xNj EyMjMxOTUwMDhaGA8yMDE4MTIyMzE5NTAwNVowggEZMRQwEgYDVQQIDAtCT0dPVEEgRC5DLjE NMAsGA1UECwwERElBTjEPMA0GA1UEBRMGNjQ0NjM1MRowGAYKKwYBBAGBtWMCAxMKODAw MTk3MjY4NDE7MDkGA1UECgwyVS5BLkUuIERJUkVDQ0lPTiBERSBJTVBVRVNUT1MgWSBBRFVBTkFT IE5BQ0lPTkFMRVMxFDASBgNVBAcMC0JPR09UQSBELkMuMSgwJgYJKoZIhvcNAQkBFhlTQU5USUFHT 1JPSkFTQERJQU4uR09WLkNPMQswCQYDVQQGEwJDTzE7MDkGA1UEAwwyVS5BLkUuIERJUkVDQ0lP TiBERSBJTVBVRVNUT1MgWSBBRFVBTkFTIE5BQ0lPTkFMRVMwggEiMA0GCSqGSIb3DQEBAQUAA4IB DwAwggEKAoIBAQCYyo2c1lRA4KgbH5mVB1fIhcZEKfTLP7OpOhsx9HfK8mbAM9tFv4Ep0wac8Vw2Ch E1/McEFajbMA3pF+Ks4xVRaeTYqrlSXwPicR/R+F25zwhM4twYMg4+Bp7aXeGecY+gCfE2omfjY4AIu9 UlVWYGI+NWjJqktnCp/RomAWWgmJS8cZ6n4WIolWcUfts/OAflDJDr66WmohkEfpYSbQJ6D0z1qwUh 0i79x6I4dQCaUw4HeNFwWe1RyZSPi15YUZ2glCPH22FhyMC2/83p8dMD0+Y8XNpk3IAaMrZZD+JnOU c3dvhO0LFHW1xniK6RrkHJNkHE3UxYaZ2SzhdbTi43AgMBAAGjggLAMIICvDA2BggrBgEFBQcBAQQq_ 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 237 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

_MCgwJgYIKwYBBQUHMAGGGmh0dHA6Ly9vY3NwLmNlcnRpY2FtYXJhLmNvMCQGA1UdEQQdMBuB GVNBTlRJQUdPUk9KQVNARElBTi5HT1YuQ08wgecGA1UdIASB3zCB3DCBmQYLKwYBBAGBtWMyAQg wgYkwKwYIKwYBBQUHAgEWH2h0dHA6Ly93d3cuY2VydGljYW1hcmEuY29tL2RwYy8wWgYIKwYBBQ UHAgIwThpMTGltaXRhY2lvbmVzIGRlIGdhcmFudO1hcyBkZSBlc3RlIGNlcnRpZmljYWRvIHNlIHB1ZWRl biBlbmNvbnRyYXIgZW4gbGEgRFBDLjA+BgsrBgEEAYG1YwoKATAvMC0GCCsGAQUFBwICMCEaH0Rpc 3Bvc2l0aXZvIGRlIGhhcmR3YXJlIChUb2tlbikwDAYDVR0TAQH/BAIwADAOBgNVHQ8BAf8EBAMCA/gwJ wYDVR0lBCAwHgYIKwYBBQUHAwEGCCsGAQUFBwMCBggrBgEFBQcDBDAdBgNVHQ4EFgQUxFbjYtGl lLfoIB2sE5ThQbAkjyMwHwYDVR0jBBgwFoAUgHHMMpJYdfQDITqrvhzTj/IgFe0wEQYJYIZIAYb4QgEBB AQDAgWgMIHXBgNVHR8Egc8wgcwwgcmggcaggcOGXmh0dHA6Ly93d3cuY2VydGljYW1hcmEuY29t L3JlcG9zaXRvcmlvcmV2b2NhY2lvbmVzL2FjX3N1Ym9yZGluYWRhX2NlcnRpY2FtYXJhXzIwMTQuY3JsP2 NybD1jcmyGYWh0dHA6Ly9taXJyb3IuY2VydGljYW1hcmEuY29tL3JlcG9zaXRvcmlvcmV2b2NhY2lvbmV zL2FjX3N1Ym9yZGluYWRhX2NlcnRpY2FtYXJhXzIwMTQuY3JsP2NybD1jcmwwDQYJKoZIhvcNAQELBQ ADggEBAFjwIciRfKLmswvqI1gLtF0wroegzv6bHPF+pB9jJS+FLMdTXqh9OnvEh6cMrOL6Dnpcpc6m9je Dn4dL9BdsMW3UFEur+QzbsL/H3bIVHXKFFmYPwaZZyD4xyEtyomSLtVe6LCV97Ojxg/Q48Kl3XORYC1 FJySfW89CMUPdm2QvSiYO3EC7wgeyfTiPrLhRqS3F0dmjYsDRQRqK7QfWtmGLJWlEFb6EE5mFUNUM NDhAHF1quC12cWMpcbu3JfM9Khd74lz2GxvMvWwwdwBfX68bwwmfcRktVXDKq6X7z8MflfvdbOLz 1IchxNa2AOqtqHtE/689WaOrHfeSSkzWVUAc=_ 

_</ds:X509Certificate>_ 

_</ds:X509Data>_ 

_</ds:KeyInfo>_ 

### 7.10. Identificador de la Política. 

Configuración del Identificador de Política para certificados digitales tipo sha-2 

- xPath: 

   - /NominaIndividual||NominaIndividualDeAjuste/Ext:UBLExtensions/ext:UBLExtension/ext:ExtensionCont ent/ds:Signature/ds:Object/xades:QualifyingProperties/xades:SignedProperties/xades:SignedSignaturePr operties/xades:SignaturePolicyIdentifier/xades:SignaturePolicyId/xades:SigPolicyId/xades:Identifier:= Valor: 

<u>https:/facturaelectronica.dian.gov.co/politicadefirma/v2/politicadefirmav2.pdf</u> 

- xPath 

/NominaIndividual||NominaIndividualDeAjuste/Ext:UBLExtensions/ext:UBLExtension/ext:ExtensionCont ent/ds:Signature/ds:Object/xades:QualifyingProperties/xades:SignedProperties/xades:SignedSignaturePr operties/xades:SignaturePolicyIdentifier/xades:SignaturePolicyId/xades:SigPolicyHash/ds:DigestMethod/ @Algorithm:= 

Valor: 2 Opciones 

<u>http:/www.w3.org/2001/04/xmlenc#sha256 o http:/www.w3.org/2001/04/xmlenc#sha512</u> 

- _xPath:_ 

   - /NominaIndividual||NominaIndividualDeAjuste/Ext:UBLExtensions/ext:UBLExtension/ext:ExtensionCont 

> Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 238 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

ent/ds:Signature/ds:Object/xades:QualifyingProperties/xades:SignedProperties/xades:SignedSignaturePr operties/xades:SignaturePolicyIdentifier/xades:SignaturePolicyId/xades:SigPolicyId/xades:Description _Valor:_ Política de firma para nóminas electrónicas de la República de Colombia. 

### 7.11. Hora de Firma. 

Se debe especificar en formato xsd:dateTime la fecha y hora en que reclama el firmante haber firmado el Documento Soporte de Pago de Nómina Electrónica. 

_<xades:SigningTime>2009-07-14T13:28:00+02:00</xades:SigningTime>_ 

NOTA: El deber de los emisores del Documento Soporte de Pago de Nómina Electrónica es que los sistemas computacionales que utilicen para el firmado de los documentos deberán estar sincronizados con el reloj de la súper intendencia de industria y comercio el cual determina la hora legal colombiana. http:/www.sic.gov.co/hora-legal-colombiana. 

### 7.12. Firmante. 

El elemento xades:SignerRole contiene uno y sólo uno de los siguientes atributos: 

- “supplier” cuando la firma de la nómina la realiza el Obligado a Emitir Documento Soporte de Pago de Nómina Electrónica. 

- “third party” cuando la firma la realiza un Proveedor de Soluciones Tecnológicas que en su caso, actué en su nombre. 

_<xades:SignerRole>supplier</xades:SignerRole>_ 

### 7.13. Mecanismo de firma digital. 

El mecanismo de firma digital a que se refiere el artículo 7 de la Ley 527 de 1999 y el Decreto 2364 de 2012 será considerada en el negocio electrónico denominado Emisión del Documento Soporte de Pago de Nómina Electrónica una vez sea reglamentada por la DIAN para tal efecto. 

### 7.14. Certificado digital desde la vigencia de la circular 03-2016 de la ONAC. 

- Este documento incluye los argumentos que deberán usarse como valores de los parámetros de: 

- Los certificados digitales _con no repudio_ previstos en el estándar RFC-5280, y que cumplan con la Ley de 

- Comercio Electrónico de Colombia, que utilicen los emisores electrónicos para firmar digitalmente los documentos desmaterializados del negocio del Documento Soporte de Pago de Nómina Electrónica. 

- Los atributos que resuelven las ambigüedades de los elementos que conforman los documentos 

- desmaterializados del negocio del Documento Soporte de Pago de Nómina Electrónica, precisando las características criptográficas empleadas para cumplir con la Ley de Comercio Electrónico de Colombia. Referencia: URL https:/es.wikipedia.org/wiki/SHA-2 

### Regla-1 

> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Página 239 de 269 



##### 



### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Lapso de Validez del certificado digital|Expedido ANTES de octubre 1 de 2016 T00:00:00, y hasta la terminación<br>de la vigencia|
|---|---|
|Signature Algorithm|Valores válidos dentro del certificado digital:<br>Sha1WithRSAEncryption<br>sha224WithRSAEncryption<br>sha256WithRSAEncryption<br>sha384WithRSAEncryption<br>sha512WithRSAEncryption|
|X509v3 Key Usage: critical|Valores necesarios dentro del certificado digital:<br>Digital Signature<br>Non Repudiation|



#### Descripción: 

Estamos aplicando la reglamentación de la ONAC, URL http:/onac.org.co/anexos/documentos/TRANSICIRCULARES/2016circulares/circular03-2016.pdf 

Si el valor “Validity” del lapso de vigencia del certificado empezó antes de octubre 1 de 2016, la firma digital del _Documento Soporte de Pago de Nómina Electrónica_ puede: 

- Emplear certificados digitales que hayan sido generados con resúmenes criptográficos del tipo SHA1 

- Que el fragmento SignedInfo al que se le aplicó el canon fue la entrada para calcular el resumen criptográfico que fue firmado digitalmente con << http:/www.w3.org/2000/09/xmldsig#rsa-sha1 >> 

- La aplicación del algoritmo de firma digital de las nóminass electrónicas depende del lapso de vigencia dentro del cual debió haber sido generada y firmada, y del método de generación del certificado digital utilizado. No podrá existir una nómina con fecha válida, i.e. 

_/_ NominaIndividual||NominaIndividualDeAjuste _/Ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/ds:Si gnature/ds:Object/xades:QualifyingProperties/xades:SignedProperties/xades:SignedSignatureProperties/xades:Si gningTime_ — diferente o por fuera del lapso de vigencia del certificado digital que se usó para calcular la firmadigital. 

El no cumplimiento de estos valores deberá registrarse como una firma digital _fallida_ para el documento electrónico, motivada en: 

- Algoritmo de Firma del certificado digital (tipo SHA1) no previsto por la DIAN 

- Uso de la clave pública del certificado digital carece de los propósitos “firma digital” o “no repudio”. 

- Pueden estar presentes ambos motivos. 

Si el lapso de validez inhabilita a 

/NominaIndividual||NominaIndividualDeAjuste/Ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/ds: Signature/ds:Object/xades:QualifyingProperties/xades:SignedProperties/xades:SignedSignatureProperties/xades:Sig ningTime, entonces deberá registrarse como una firma digital _fallida_ para el documento electrónico, motivada en: 

- Fecha de expedición del documento electrónico no corresponde con el lapso de vigencia del certificado digital. 

- Este motivo puede ser concurrente con los descritos en la celda anterior. 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 240 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

### Regla-2 

|Lapso de Validez del certificado<br>digital|Después de 30 de septiembre de 2016 T23:59:59|
|---|---|
|Signature Algorithm|Valores válidos dentro del certificado digital:<br>sha256WithRSAEncryption<br>sha384WithRSAEncryption<br>sha512WithRSAEncryption|
|X509v3 Key Usage: critical|Valores necesarios dentro del certificado digital:<br>Digital Signature<br>Non Repudiation|



#### Descripción: 

Estamos aplicando la reglamentación de la ONAC, URL http:/onac.org.co/anexos/documentos/TRANSICIRCULARES/2016circulares/circular03-2016.pdf 

Si el valor “Validity” del lapso de vigencia del certificado empezó después del 30 de septiembre de 2016 T23:59:59, la firma digital del _Documento Soporte de Pago de Nómina Electrónica_ tiene que: 

- Emplear certificados digitales que hayan sido generados con resúmenes criptográficos del tipo SHA256; existen otras opciones como aparece en la lista << Signature Algorithm >> 

- Que el resumen criptográfico que se aplicó al fragmento que fue firmado digitalmente corresponda con el << SignatureMethod >> empleado 

El no cumplimiento de estos valores deberá registrarse como una firma digital _fallida_ para el documento electrónico, motivada en: 

- Algoritmo de Firma del certificado digital (tipo SHA2) no previsto por la DIAN 

- Uso de la clave pública del certificado digital carece de los propósitos “firma digital” o “no repudio”. Vea Anexo 2. 

- Pueden estar presentes ambos motivos. 

Si el lapso de validez inhabilita a 

- _/_ NominaIndividual||NominaIndividualDeAjuste _/Ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/ds:S ignature/ds:Object/xades:QualifyingProperties/xades:SignedProperties/xades:SignedSignatureProperties/xades:Signi_ 

_ngTime_ , entonces deberá registrarse como una firma digital _fallida_ para el documento electrónico, motivada en: 

- Fecha de expedición del documento electrónico no corresponde con el lapso de vigencia del certificado digital. 

- Este motivo puede ser concurrente con los descritos en la celda anterior. 

### Regla-3 

|_Algoritmo de firma digital_aplicado<br>al Documento Soporte de Pago de<br>Nómina Electrónica|Certificado digital expedido después de 30 de septiembre de 2016 T23:59:59|
|---|---|
|_/NominaIndividual||NominaIndivid_<br>_ualDeAjuste/Ext:UBLExtensions/ext:_<br>_UBLExtension/ext:ExtensionContent_|Algoritmo=RSAwithSHA256<br>Use:http:/www.w3.org/2001/04/xmldsig-more#rsa-sha256<br>Algoritmo=RSAwithSHA384<br>Use:http:/www.w3.org/2001/04/xmldsig-more#rsa-sha384|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 241 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

_Algoritmo de firma digital_ aplicado Certificado digital expedido después de 30 de septiembre de 2016 T23:59:59 al Documento Soporte de Pago de Nómina Electrónica _/ds:Signature/ds:SignedInfo/ds:Sign_ Algoritmo=RSAwithSHA512 _atureMethod/@Algorithm=_ Use: http:/www.w3.org/2001/04/xmldsig-more#rsa-sha512 Descripción: Estamos aplicando la reglamentación de la ONAC, URL http:/onac.org.co/anexos/documentos/TRANSICIRCULARES/2016circulares/circular03-2016.pdf El algoritmo de _firma digital_ aplicado a la facture electrónica no tiene correspondencia directa con el _resumen criptográfico_ utilizado para obtener los fragmentos de la Regla-4, i.e. pueden usarse tamaños de 

Si el valor del _../ds:SignatureMethod/@Algorithm_ no corresponde con los valores paramétricos, entonces deberá registrarse como una firma digital _fallida_ para el documento electrónico, motivada en:  Empleó un algoritmo de _<u>firma digital</u>_ no previsto por la DIAN. 

Si el valor del _../ds:SignatureMethod/@Algorithm_ corresponde a _http:/www.w3.org/2000/09/xmldsig#rsa-sha1_ , entonces deberá registrarse como una firma digital _fallida_ para el documento electrónico, motivada en: 

 Empleó un algoritmo de _firma digital_ que está caducado según el reglamento de la Ley de Comercio Electrónico de Colombia. 

### Regla-4 

|_Algoritmos de resumen criptográfico_<br>aplicado a los fragmentos del Documento<br>Soporte de Pago de Nómina Electrónica<br>que se incluyen dentro del fragmento que<br>se firma digitalmente|Certificado digital expedido después de 30 de septiembre de 2016<br>T23:59:59|
|---|---|
|/NominaIndividual||NominaIndividualDeA<br>juste/Ext:UBLExtensions/ext:UBLExtension<br>/ext:ExtensionContent/ds:Signature/ds:Sig<br>nedInfo/ds:Reference/ds:DigestMethod/<br>@Algorithm=<br>/NominaIndividual||NominaIndividualDeA<br>juste/Ext:UBLExtensions/ext:UBLExtension<br>/ext:ExtensionContent/ds:Signature/ds:Sig<br>nedInfo/ds:Reference/ds:DigestMethod/<br>@Algorithm=<br>/NominaIndividual||NominaIndividualDeA<br>juste/Ext:UBLExtensions/ext:UBLExtension<br>/ext:ExtensionContent/ds:Signature/ds:Sig<br>nedInfo/ds:Reference[3]/ds:DigestMetho<br>d/@Algorithm|SHA256. Cadena de 256 bits.<br>Use: http:/www.w3.org/2001/04/xmlenc#sha256<br>SHA384. Cadena de 384 bits.<br>Use:<br>http:/www.w3.org/2001/04/xmldsig-more#sha384<br>SHA512. Cadena de 512 bits.<br>Use:<br>http:/www.w3.org/2001/04/xmlenc#sha512|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 242 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

_Algoritmos de resumen criptográfico_ Certificado digital expedido después de 30 de septiembre de 2016 aplicado a los fragmentos del Documento T23:59:59 Soporte de Pago de Nómina Electrónica que se incluyen dentro del fragmento que se firma digitalmente 

/NominaIndividual||NominaIndividualDeA juste/Ext:UBLExtensions/ext:UBLExtension /ext:ExtensionContent/ds:Signature/ds:Ob ject/xades:QualifyingProperties/xades:Sig nedProperties/xades:SignedSignatureProp erties/xades:SigningCertificate/xades:Cert /xades:CertDigest/ds:DigestMethod/@Alg orithm= /NominaIndividual||NominaIndividualDeA juste/Ext:UBLExtensions/ext:UBLExtension /ext:ExtensionContent/ds:Signature/ds:Ob ject/xades:QualifyingProperties/xades:Sig nedProperties/xades:SignedSignatureProp erties/xades:SigningCertificate/xades:Cert /xades:CertDigest/ds:DigestMethod/@Alg orithm= /NominaIndividual||NominaIndividualDeA juste/Ext:UBLExtensions/ext:UBLExtension /ext:ExtensionContent/ds:Signature/ds:Ob ject/xades:QualifyingProperties/xades:Sig nedProperties/xades:SignedSignatureProp erties/xades:SigningCertificate/xades:Cert [3]/xades:CertDigest/ds:DigestMethod/@ Algorithm= /NominaIndividual||NominaIndividualDeA juste/Ext:UBLExtensions/ext:UBLExtension /ext:ExtensionContent/ds:Signature/ds:Ob ject/xades:QualifyingProperties/xades:Sig nedProperties/xades:SignedSignatureProp erties/xades:SignaturePolicyIdentifier/xad es:SignaturePolicyId/xades:SigPolicyHash/ ds:DigestMethod/@Algorithm= 

Descripción: Estamos aplicando la reglamentación de la ONAC, URL http:/onac.org.co/anexos/documentos/TRANSICIRCULARES/2016circulares/circular03-2016.pdf 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 243 de 269 

**Resolución No. 000013** 





### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

_Algoritmos de resumen criptográfico_ Certificado digital expedido después de 30 de septiembre de 2016 aplicado a los fragmentos del Documento T23:59:59 Soporte de Pago de Nómina Electrónica que se incluyen dentro del fragmento que se firma digitalmente 

<mark>El algoritmo de resumen criptográfico utilizado para los fragmentos que intervienen y forman parte del elemento</mark> <u><mark>que se firma digitalmente no tiene correspondencia con el algoritmo de firma digital de la Regla-3.</mark></u> 

Si el valor del ../ds:DigestMethod/@Algorithm no corresponde con los valores paramétricos, entonces deberá registrarse como una firma digital _fallida_ para el documento electrónico, motivada en: 

- Empleó un algoritmo de _resumen criptográfico_ no previsto por la DIAN. Vea Anexo 2. 

- Si el valor del ../ds:DigestMethod/@Algorithm corresponde a http:/www.w3.org/2000/09/xmldsig#sha1, entonces deberá registrarse como una firma digital _fallida_ para el documento electrónico, motivada en: 

- Empleó un algoritmo de _resumen criptográfico_ que está caducado según el reglamento de la Ley de Comercio Electrónico de Colombia. Vea Anexo 2. 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 244 de 269 

r 



<!-- Start of picture text -->
) | Ma. IN<br><!-- End of picture text -->

POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
®<br><!-- End of picture text -->



<!-- Start of picture text -->
r me 6esElemprendimientode todos | jyinhacienda<br><!-- End of picture text -->

**Resolución No. 000013** 





### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

territorio nacional, lo cual se logra por medio de la generación de un código único usando una función _one-way hash_ . 

Para la generación del CUNE se debe utilizar el algoritmo SHA-384 que garantiza que dos (2) cadenas de texto no generarán el mismo hash. En expresión matemática tenemos que el Código Único del Documento Soporte de Pago de Nómina Electrónica es: 

|NumNE:|Numero de Documento Soporte de Pago de Nómina Electronica. (Prefijo concatenado con el<br>Consecutivo de la nómina)|
|---|---|
|FecNE:|Fecha de Generación del Documento.|
|HorNE:|Hora de Generación del Documento incluyendo GMT.|
|ValDev:|Total Devengos, con punto decimal, con decimales truncados a dos (2) dígitos, sin<br>separadores de miles, ni símbolo pesos.|
|ValDed:|Total Deducciones, con punto decimal, con decimales truncados a dos (2) dígitos, sin<br>separadores de miles, ni símbolo pesos.|
|ValTolNE:|Total Pagado (Devengado - Deducciones), con punto decimal, con decimales truncados a dos<br>(2) dígitos, sin separadores de miles, ni símbolo pesos.|
|NitNE:|NIT del Emisor del Documento,sinpuntos niguiones,sin digito de verificación.|
|DocEmp:|Número de Identificación del Empleado,sinpuntos niguiones,sin digito de verificación.|
|TipoXML:|Tipo de XML utilizado.|
|Software-Pin:|Pin del Software utilizado.|
|TipAmb:|Número de identificación del ambiente utilizado por el contribuyente para emitir la nómina,<br>validar el numeral 5.1.1.|



_Composición del CUNE = SHA-384 (NumNE + FecNE + HorNE + ValDev + ValDed + ValTolNE + NitNE + DocEmp + TipoXML +_ Software-Pin _+TipAmb)_ 

<u>Donde + significa la concatenación de las cadenas de caracteres.</u> 

### 8.1.1.2. <u>Ejemplos.</u> 

### 8.1.1.3. <u>Ejemplo de CUNE para Documento Soporte de Pago de Nómina Electrónica y Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica.</u> 

Teniendo en cuenta los siguientes datos de entrada, se presenta el resultado del CUNE. 

Ejemplo: CUNE de un Documento Soporte de Pago de Nómina Electrónica-e y Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica-e (Opción Reemplazar): SHA384 

|NumNE:|N00001|
|---|---|
|FecNE:|2020-01-16|
|HorNE:|10:53:10-05:00|
|ValDev:|3500000.00|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 246 de 269 

**Resolución No. 000013** 





### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|Ejemplo: CUN<br>|E de un Documento Soporte de Pago de Nómina Electrónica-e y Nota de Ajuste de Documento Soporte<br>de Pago de Nómina Electrónica-e(Opción Reemplazar): SHA384<br>|
|---|---|
|ValDed:|1000000.00|
|ValTolNE:|2500000.00|
|NitNE:|700085371|
|DocEmp:|800199436|
|TipoXML:|102|
|Software-Pin:|693|
|TipAmb:|1|
|Composición<br>del CUNE:|(N000012020-01-161053:10-<br>05:003500000.001000000.002500000.007000853718001994361026931)|
|CUNE.SHA384:|_16560dc8956122e84ffb743c817fe7d494e058a44d9ca3fa4c234c268b4f766003253fbee7ea4af9682dd_<br>_57210f3bac2_Destino: /NominaIndividual/InformacionGeneral/@CUNE y<br>/NominaIndividualDeAjuste/Reemplazar/InformacionGeneral/@CUNE o<br>/NominaIndividualDeAjuste/Eliminar/InformacionGeneral/@CUNE<br>Ref:http:/www.sha1-online.com/|



### 8.1.1.4. Xpath. 

De forma no ambigua se especifican las expresiones XPath que deben aplicarse a un Documento Soporte de Pago de Nómina Electrónica y Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica para obtener la información requerida y permitir la generación del CUNE. 

Definición CUNE de un Documento Soporte de Pago de Nómina Electrónica. 

|NumNIE:|/NominaIndividual/NumeroSecuenciaXML/@Numero|
|---|---|
|FecNIE:|/NominaIndividual/InformacionGeneral/@FechaGen|
|HorNIE:|/NominaIndividual/InformacionGeneral/@HoraGen|
|ValDev:|/NominaIndividual/DevengadosTotal|
|ValDed:|/NominaIndividual/DeduccionesTotal|
|ValTol:|/NominaIndividual/ComprobanteTotal|
|NitNIE:|/NominaIndividual/Empleador/@NIT|
|DocEmp:|/NominaIndividual/Trabajador/@NumeroDocumento|
|TipoXML:|/NominaIndividual/InformacionGeneral/@TipoXML|
|Software-Pin:|<br>No está incluido dentro del documento XML.<br><br>Valor reservado, de circulación restringida, asignado por quien obtuvo el Código de Activación<br>del software en laplataforma del Documento Soporte de Pago de Nómina Electrónica - DIAN|
|TipAmb:|/NominaIndividual/InformacionGeneral/@Ambiente|



Definición CUNE de una Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica (Opción 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 247 de 269 

**Resolución No. 000013** 





### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

Reemplazar). 

|NumNIAE:|/NominaIndividualDeAjuste/Reemplazar/NumeroSecuenciaXML/@Numero|
|---|---|
|FecNIAE:|/NominaIndividualDeAjuste/Reemplazar/InformacionGeneral/@FechaGen|
|HorNIAE:|/NominaIndividualDeAjuste/Reemplazar/InformacionGeneral/@HoraGen|
|ValDev:|/NominaIndividualDeAjuste/Reemplazar/DevengadosTotal|
|ValDed:|/NominaIndividualDeAjuste/Reemplazar/DeduccionesTotal|
|ValTol:|/NominaIndividualDeAjuste/Reemplazar/ComprobanteTotal|
|NitNIAE:|/NominaIndividualDeAjuste/Reemplazar/Empleador/@NIT|
|DocEmp:|/NominaIndividualDeAjuste/Reemplazar/Trabajador/@NumeroDocumento|
|TipoXML:|/NominaIndividualDeAjuste/Reemplazar/InformacionGeneral/@TipoXML|
|Software-Pin:|<br>No está incluido dentro del documento XML.<br><br>Valor reservado, de circulación restringida, asignado por quien obtuvo el Código de Activación<br>del software en laplataforma del Documento Soporte de Pago de Nómina Electrónica - DIAN|
|TipAmb:|/NominaIndividualDeAjuste/Reemplazar/InformacionGeneral/@Ambiente|



Definición CUNE de una Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica (Opción Eliminar). 

|NumNIAE:|/NominaIndividualDeAjuste/Eliminar/NumeroSecuenciaXML/@Numero|
|---|---|
|FecNIAE:|/NominaIndividualDeAjuste/Eliminar/InformacionGeneral/@FechaGen|
|HorNIAE:|/NominaIndividualDeAjuste/Eliminar/InformacionGeneral/@HoraGen|
|ValDev:|0.00|
|ValDed:|0.00|
|ValTol:|0.00|
|NitNIAE:|/NominaIndividualDeAjuste/Eliminar/Empleador/@NIT|
|DocEmp:|0|
|TipoXML:|/NominaIndividualDeAjuste/Eliminar/InformacionGeneral/@TipoXML|
|Software-Pin:|<br>No está incluido dentro del documento XML.<br><br>Valor reservado, de circulación restringida, asignado por quien obtuvo el Código de Activación<br>del software en laplataforma del Documento Soporte de Pago de Nómina Electrónica - DIAN|
|TipAmb:|/NominaIndividualDeAjuste/Eliminar/InformacionGeneral/@Ambiente|



### 8.2. Especificacón Técnica Del Código De Seguridad Del Software. 

El elemento /@SoftwareSC ubicado en: 

/NominaIndividual/ProveedorXML/@SoftwareSC (Documento Soporte de Pago de Nómina Electrónica) 

/NominaIndividualDeAjuste/Reemplazar/ProveedorXML/@SoftwareSC (Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica – Opción Reemplazar) 

/NominaIndividualDeAjuste/Eliminar/ProveedorXML/@SoftwareSC (Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica – Opción Eliminar) 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 248 de 269 

**Resolución No. 000013** 





### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

Es la huella de legitimidad del software que produjo las nóminas electrónicas, y que se basa en informaciones privadas que se usan para calcular un resumen criptográfico. Una parte de esa información fue asignada por el Emisor del Documento Soporte de Pago de Nómina Electrónica, i.e. el PIN del software— y la otra la asignó el sistema de Emisión del Documento Soporte de Pago de Nómina Electrónica. El Emisor del Documento Soporte de Pago de Nómina Electrónica directo y los PT deben mantener en reserva estas informaciones para evitar actividades maliciosas de quienes buscan explotar las vulnerabilidades de los usuarios de sistemas informáticos. Es el producto de un algoritmo criptográfico del tipo one-way hash function. Arma una cadena con dos valores: 

Identificador del software asignado desde el sistema de la DIAN cuando el software se activa en el Sistema de Emisión del Documento Soporte de Pago de Nómina Electrónica. i.e. código de activación. 

PIN del software que usted asignó en el sistema de la DIAN cuando el software se activa en el Sistema de Emisión del Documento Soporte de Pago de Nómina Electrónica. 

La cadena resultante es la semilla para el cálculo SHA-384. El resultado es la huella del software que autorizó la DIAN al Emisor del Documento Soporte de Pago de Nómina Electrónica o al Proveedor de Soluciones Tecnológicas. 

SoftwareSecurityCode:= SHA-384 (Id Software + Pin + NroDocumento) NroDocumento (Documento Soporte de Pago de Nómina Electrónica) = 

_/NominaIndividual/NumeroSecuenciaXML/@Numero_ 

NroDocumento (Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica) = _/NominaIndividualDeAjuste/Reemplazar/NumeroSecuenciaXML/@Numero ó_ 

_/NominaIndividualDeAjuste/Eliminar/NumeroSecuenciaXML/@Numero_ 

### 8.3. Métodos de Calculo. 

#### 8.3.1. Cálculo de Tiempo Laborado 

Para indicar el Tiempo laborado de un determinado trabajador en la empresa del emisor del Documento Soporte de Pago de Nómina Electrónica, debe utilizarse la siguiente Nomenclatura: 

|Calculo Tiempo Laborado<br>Significado<br>|
|---|
|1 Año = 360 Dias|
|1 Mes = 30 Dias|
|5 Años + 3 Meses + 18 Dias|
|(5*360)+(3*30)+18|
|1908.00|



### 9. Descripciónes Tecnológicas del Web Services de Método Síncrono. 

La solución de transmisión de documentos electrónicos de Documento Soporte de Pago de Nómina Electrónica 

> Dirección de Gestión de Ingresos 

> Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 249 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

y Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica involucra la utilización de UBL 2.1 como lenguaje para la sección de firmado de los documentos electrónicos a diferencia de la estructura definida y el contenido de todas las demás secciones requeridas ya que estas no cumplen con el lenguaje estándar UBL 2.1. El firmado de los documentos de Nómina se realiza mediante certificados digitales. 

### 9.1. Modelo conceptual de comunicación. 

El modelo de comunicación iniciará en el sistema del contribuyente posterior al proceso de habilitación, por medio del consumo del servicio que expone la DIAN para validar la transmisión de los documentos electrónicos de Documento Soporte de Pago de Nómina Electrónica y Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica. 

La DIAN expone sobre el mismo servicio web actual de Factura Electrónica en Validación Previa (WcfDianCustomerServices) una nueva la operación llamada SendNominaSync para la transmisión síncrona de 1 documento electrónico de Documento Soporte de Pago de Nómina Electrónica o Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica XML en contenedor .zip y la modificacion de la operación actual llamada GetStatus para incluir la consulta de Documentos Soporte de Pago de Nómina Electrónica. 

### 9.2. Servicio síncrono. 

Este servicio tiene la funcionalidad de transmitir a la DIAN los documentos de Nómina, de tal forma que la plataforma de validacion los evalúe de acuerdo a la estructura de firmado UBL 2.1 y a la estructura propia definida para el contenido de todas las demás secciones requeridas, y de forma síncrona de respuesta de validacion. 

El servicio puede recibir un .zip con un solo documento electrónico firmado digitalmente, construido según esquema detallado en el presente anexo técnico. 

### 9.2.1. Secuencia del servicio síncrono. 

Este servicio estará disponible en los ambientes de producción (Habilitación y Operación) como sucede con Factura Electrónica en Validación Previa.El software cliente realiza la conexión autenticando por medio de certificado digital. 

- Se adjunta archivo .zip con documento XML de NominaIndividual o NominaIndividualDeAjuste a validar.Se envía solicitud (Request) con los parámetros de consumo en la estructura del XML definida para este método. 

- Se descomprime ZIP y se evalúan los siguientes elementos. 

   - Archivo zip no este vacío. 

   - Archivo zip no este corrupto. 

   - Exista la sección UBL 2.1 con firmado digital. 

   - Corresponda a la estructura XSD de NominaINdividual o NominaIndividualDeAjuste definida 

> Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 250 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

para estos documentos. 

   - No existan errores en las reglas de validaciones de acuerdo al presente Anexo Técnico. 

- Posterior a las validaciones se genera respuesta (Response) síncrona con el detalle de la evaluación del documento, que incluye dentro de sus elementos un ApplicationResponse codificado en Base64 con la respuesta de validacion de la DIAN. 

### 9.3. Aspectos tecnológicos de las operaciones del web service. 

- Los participantes que estén registrados para operar con la plataforma de validacion previa de la DIAN, podrán hacer uso de las operaciones de transmisión y consulta de los documentos de Documento Soporte de Pago de Nómina Electrónica y Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica. 

- Los Proveedores Tecnológicos realizarán la transmisión de los documentos electrónicos consumiendo el servicio WEB que expone la DIAN sin operar intermediarios en dicha transmisión. 

Para ello el sistema cliente de los participantes deberán tener las siguientes consideraciones: 

- Para la transmisión de los DE deberán desarrollar un software cliente independiente del lenguaje de programación. 

- El lenguaje XML de los archivos de intercambio de información será el de UBL 2.1 para el proceso de firmado y las demás secciones del documento serán la estructura propia detallada en el presente Anexo Técnico. 

- Con el fin de garantizar la seguridad en la comunicación, el software cliente deberá autenticarse ante la DIAN utilizando certificado digital. 

- El medio de comunicación es internet con la utilización del protocolo TLS versión 1.2. con autenticación mutua a través de certificados digitales. 

- El intercambio de mensajes entre los Servicios Web de la DIAN y el particpante Habilitado será realizado mediante el estándar SOAP versión 1.2, con intercambio de mensajes XML en el estándar Style/Encoding: Document/Literal. 

### 9.4. Estándar de comunicación. 

La comunicación está basada en servicios Web expuestos por el Sistema de Validación y Gestión de Documentos de DIAN. 

El medio físico de comunicación es Internet, con la utilización del protocolo TLS versión 1.2, con autentificación mutua a través de certificados digitales. 

El modelo de comunicación sigue el estándar de servicios web definido por el WS-Security 1.0 Oasis, con autenticación X.509 Certificate Token Profile 1.1. 

El intercambio de mensajes entre los Servicios Web de la DIAN y el sistema del Habilitado para el Proveedor 

> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Página 251 de 269 

**Resolución No. 000013** 

(11 FEB 2021) 





### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

Tecnológico (PT) será realizado mediante el estándar SOAP versión 1.2, con intercambio de mensajes XML en el estándar Style/Encoding: Document/Literal. 

### 9.5. Estándar de mensajes de los servicios de La DIAN. 

La solicitud de consumo de los servicios dispuestos por la DIAN seguirá el siguiente estándar. 

<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" 

xmlns:wcf="http://wcf.dian.colombia"> 

<soap:Header/> 

<soap:Body> 

<wcf:SendNominaSync> 

<wcf:contentFile>------ Área de Dato: Archivo Nomina.zip en base 64 que contiene un documento XML que atiende al formato definido para la operación de nómina 

</wcf:contentFile> 

</wcf:SendNominaSync> 

</soap:Body> </soap:Envelope> 

El área de datos obedecerá a un formato XML definido para cada WS. 

### 9.6. Descripción de los servicios web de La DIAN. 

El sistema de validación y gestión de documentos de Documento Soporte de Pago de Nómina Electrónica y Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica DIAN, dispone de una capa de servicios que atienden las funcionalidades requeridas para operar, cada operación del servicio se encuentra respaldado por un Método Web específico. 

El modelo de comunicación e interoperabilidad siempre iniciará en el sistema del participante habilitado, por medio del consumo del servicio correspondiente de un PT, el cual posteriormente consumirá los servicios de la DIAN para validar la transmisión de los documentos. 

### 9.7. WS recepción documento electrónico – SendNominaSync. 

- Función: Recibir un ZIP con UBLs DE. 

- Proceso: Sincrónico 

- Método: SendBillSync 

### 9.7.1. Descripción de procesamiento. 

- El software cliente realiza la conexión autenticando por medio de certificado digital. 

- Se adjunta archivo .zip con documento XML de NominaIndividual o NominaIndividualDeAjuste a validar. 

> Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 252 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

- Se envía solicitud (Request) con los parámetros de consumo en la estructura del XML definida para este método. 

- Se descomprime ZIP y se evalúan los siguientes elementos. 

   - Archivo zip no este vacío. 

   - Archivo zip no este corrupto. 

   - Exista la sección UBL 2.1 con firmado digital. 

   - Corresponda a la estructura XSD de NominaIndividual o NominaINdividualDeAjuste definida para estos documentos. 

   - No existan errores en estructura XML propia de acuerdo al Anexo Técnico. 

- Posterior a las validaciones se genera respuesta (Response) síncrona con el detalle de la evaluación del documento, que incluye dentro de sus elementos un ApplicationResponse codificado en Base64 con la respuesta de validacion de la DIAN. 

### 9.7.2. Mensaje de petición. 

**Operación : SendNominaSync** 

**Descripción:** Operación que realiza la transmisión de eventos tipo NominaIndividual y NominaIndividualAjuste. 

### **Request** 

<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:wcf="http://wcf.dian.colombia"> <soap:Header/> <soap:Body> <wcf:SendNominaSync> <!--Optional:--> 

<wcf:contentFile>cid:1057568194758</wcf:contentFile> 

</wcf:SendNominaSync> </soap:Body> </soap:Envelope> 

### **Response** 

<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing" xmlns:u="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"> 

<s:Header> 

<a:Action 

s:mustUnderstand="1">http://wcf.dian.colombia/IWcfDianCustomerServices/SendNominaSyncResponse</a:Action> 

<o:Security s:mustUnderstand="1" xmlns:o="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext1.0.xsd"> 

<u:Timestamp u:Id="_0"> 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 253 de 269 

**Resolución No. 000013** 

(11 FEB 2021) 





### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

<u:Created>2021-01-02T07:27:17.048Z</u:Created> <u:Expires>2021-01-02T07:32:17.048Z</u:Expires> </u:Timestamp> </o:Security> </s:Header> <s:Body> <SendNominaSyncResponse xmlns="http://wcf.dian.colombia"> 

<SendNominaSyncResult xmlns:b="http://schemas.datacontract.org/2004/07/DianResponse" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"> <b:ErrorMessage xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"/> <b:IsValid>true</b:IsValid> 

<b:StatusCode>00</b:StatusCode> 

<b:StatusDescription> Procesado Correctamente </b:StatusDescription> 

<b:StatusMessage> Documento Nomina  689, ha sido autorizada.</b:StatusMessage> <b:XmlBase64Bytes>PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiIHN0YW5kYWxvbmU9Im5vIj8+……………. +DQogICAgPC9jYWM6TGluZVJlc3BvbnNlPg0KICA8L2NhYzpEb2N1bWVudFJlc3BvbnNlPg0KPC9BcHBsaWNhdGlvblJlc3BvbnNlPg==< /b:XmlBase64Bytes> 

<b:XmlBytes i:nil="true"/> <b:XmlDocumentKey>660ebb7fdd77b6d67a00448e7afde2959992c53ad1bf14b9a394272c56ee8cc64b75dc08940625e39390a0af 3d8d7cb9</b:XmlDocumentKey> 

<b:XmlFileName>Nomina (1)-firmado-SHA256</b:XmlFileName> </SendNominaSyncResult> </SendNominaSyncResponse> </s:Body> </s:Envelope> 

### 9.8. WS Consulta del estado de DE – GetStatus. 

- Función: Recibir una consulta para obtener el estado del documento en el proceso de validación y devuelve respuesta del estado del documento. 

- Proceso: Sincrónico 

- Método: GetStatus 

### 9.8.1. Descrición de procesamiento. 

Este servicio atiende la funcionalidad de consultar el estado del documento registrado en la DIAN, por medio del CUNE retornando el estado. 

> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Página 254 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

Este servicio estará disponible en los ambientes de producción en habilitación y producción en operación; es el mismo método actual que se usa para consultar documentos electrónicos de Factura Electronica en Validación Previa. 

### 9.8.2. Mensaje de petición. 

|**Operación :**|**GetStatus**|
|---|---|
|**Descripción:**|Operación que realiza la consulta del estado de validación de documentos<br>electrónicos incluyendo tipo NominaIndividual y NominaIndividualAjuste.<br>**Request**|
|<soap:Envelope xmlns:soa<br><soap:Header/><br><soap:Body><br><wcf:GetStatus><br><!--Optional:--><br><wcf:trackId>660ebb7fdd7<br></wcf:GetStatus><br></soap:Body><br></soap:Envelope>|p="http://www.w3.org/2003/05/soap-envelope" xmlns:wcf="http://wcf.dian.colombia"><br>7b6d67a00448e7afde2959992c53ad1bf14b9a394272c56ee8cc64b75dc08940625e39390a0af3d8d7cb9</wcf:trackId>|
||**Response**|
|<s:Envelope xmlns:s="http<br>xmlns:u="http://docs.oasi<br><s:Header><br><a:Action s:mustUnder<br><o:Security s:mustUnd<br><u:Timestamp u:Id="<br><u:Created>2021-0<br><u:Expires>2021-01<br></u:Timestamp><br></o:Security><br></s:Header><br><s:Body><br><GetStatusResponse x<br><GetStatusResult xml<br>instance"><br><b:ErrorMessage xm<br><c:string>Regla: N<br>has not been declared</c:<br><c:string>Regla: N<br><c:string>Regla: Z<br>'urn:un:unece:uncefact:da<br><c:string>Regla: N<br>Interno</c:string><br></b:ErrorMessage>|://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"<br>s-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"><br>stand="1">http://wcf.dian.colombia/IWcfDianCustomerServices/GetStatusResponse</a:Action><br>erstand="1" xmlns:o="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"><br>_0"><br>1-02T09:54:14.154Z</u:Created><br>-02T09:59:14.154Z</u:Expires><br>mlns="http://wcf.dian.colombia"><br>ns:b="http://schemas.datacontract.org/2004/07/DianResponse" xmlns:i="http://www.w3.org/2001/XMLSchema-<br>lns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"><br>IE901, Rechazo: Error al validar regla Nómina Individual Electrónica - NominaIndividual (raíz): Namespace prefix 'xmlns'<br>string><br>IE140, Rechazo: Se debe colocar el Valor Pagado por Bonificación No Salarial</c:string><br>B01, Rechazo: Fallo en el schema XML del archivo (Nomina Individual) - The complexType<br>ta:specification:CoreComponentTypeSchemaModule:2:AmountType' has already been declared. -</c:string><br>IE060, Notificación: Se debe colocar el Nombre del Cargo que el Trabajador ocupa en la empresa. Manejo<br>|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 255 de 269 



### **Resolución No. 000013** 



### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

<b:IsValid>false</b:IsValid> 

<b:StatusCode>99</b:StatusCode> 

<b:StatusDescription>Validación contiene errores en campos mandatorios.</b:StatusDescription> 

<b:StatusMessage>Documento con errores en campos mandatorios.</b:StatusMessage> 

<b:XmlBase64Bytes>PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiIHN0YW5kYWxvbmU9Im5vIj8+……………. 

+DQogICAgPC9jYWM6TGluZVJlc3BvbnNlPg0KICA8L2NhYzpEb2N1bWVudFJlc3BvbnNlPg0KPC9BcHBsaWNhdGlvblJlc3BvbnNlPg==</b:XmlBase64By tes> 

<b:XmlBytes i:nil="true"/> 

<b:XmlDocumentKey>660ebb7fdd77b6d67a00448e7afde2959992c53ad1bf14b9a394272c56ee8cc64b75dc08940625e39390a0af3d8d7cb9</b: XmlDocumentKey> 

<b:XmlFileName>Nomina Individual Electronica-firmado-SHA256</b:XmlFileName> 

</GetStatusResult> </GetStatusResponse> </s:Body> </s:Envelope> 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 256 de 269 

**Resolución No. 000013** 

(11 FEB 2021) 





### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

### 10. Campos definidos en las extensiones. 

Se establece por la DIAN como uso obligatorio por lo menos una Extensión que corresponde a la de la Firma Digital “ds:Signature” la cual esta informada en el numeral 4.2 y cuya extensión debe ser la ultima expresada en el grupo ext:UBLExtensions. 

### 10.1. Estructura para reporte de información adicional específica de cada sector. 

Este suplemento tiene por objeto explicar el uso de grupos de información opcional a nivel de cabecera, que faciliten el reporte de información de una operación comercial para un sector particular y cuya información no pueda ser incluida en los grupos establecidos por el estándar XML del “Anexo Técnico Documento Soporte de Pago de Nómina Electrónica”. 

Esta información no será sujeta a validaciones por parte de la DIAN. 

### 11. Elemento Novedad. 

Dentro del documento electrónico Documento Soporte de Pago de Nómina Electrónica (NominaIndividual), se ha introducido un elemento el cual es llamado Novedad. Éste elemento posee las siguientes caracteristicas, de acuerdo con el Artículo 1, Numeral 13 de la presente resolución, a saber: 

Novedades reportadas dentro del periodo: Las novedades reportadas dentro del periodo, son un elemento que permite informar aquellos eventos que se suscitan dentro del periodo de pago y que afectan la liquidación de los valores devengados de nómina y los valores deducidos de nómina, este elemento deberá informarse en la forma prevista según se define en el presente anexo técnico. 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 257 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

### 12. Preguntas Frecuentes. 

1. Como puedo agregar en el Documento Soporte de Pago de Nómina Electrónica los Retroactivos? R/: Los Retroactivos pueden ser agregados en el Documento Soporte de Pago de Nómina Electrónica dentro de la Ruta “/NominaIndividual/Devengados/OtrosConceptos/OtroConcepto” en la cual deberá agregar los datos de Descripción y el Pago Salarial respectivo a dicho trabajador. Con respecto a las Deducciones a que haya lugar con ese Concepto, deberán ser tenidas en cuenta en dicho documento XML en las Rutas que correspondan. 

### 13. Servicio de Consulta. 

### 13.1. Servicio de consulta a través de Código Bidimensional QR. 

Para la representación gráfica de las nóminas individuales electrónicas y nóminas Individual de Ajustes electrónicas, es requisito la generación de un código QR con la siguiente información: 

Documento Soporte de Pago de Nómina Electrónica: 

|Detalle:|Xpath:|
|---|---|
|NumNIE:[NUMERO_NOMINAINDIVIDUAL]|/NominaIndividual/NumeroSecuenciaXML/@Numero|
|FecNIE:[FECHA_NOMINAINDIVIDUAL]|/NominaIndividual/InformacionGeneral/@FechaGen|
|HorNIE: [HORA_NOMINAINDIVIDUAL(con<br>GMT)]|/NominaIndividual/InformacionGeneral/@HoraGen|
|NitNIE: [NIT<br>EMISOR_NOMINAINDIVIDUAL]|/NominaIndividual/Empleador/@NIT|
|DocEmp:[NUMERO_ID_EMPLEADO]|/NominaIndividual/Trabajador/@NumeroDocumento|
|ValDev:[VALOR_DEVENGADO_TOTAL]|/NominaIndividual/DevengadosTotal|
|ValDed:[VALOR_DEDUCCION_TOTAL]|/NominaIndividual/DeduccionesTotal|
|ValTol:<br>[VALOR_TOTAL_NOMINAINDIVIDUAL|/NominaIndividual/ComprobanteTotal|
|CUNE:[CUNE]|/NominaIndividual/InformacionGeneral/@CUNE|
|QRCode:|/NominaIndividual/CodigoQR|



Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica (Opción Reemplazar): 

|Detalle:|Xpath:|
|---|---|
|NumNIE:<br>[NUMERO_NOMINAINDIVIDUALDEAJUSTE<br>]|/NominaIndividualDeAjuste/Reemplazar/NumeroSecuenciaXML/@<br>Numero|
|FecNIE:<br>[FECHA_NOMINAINDIVIDUALDEAJUSTE]|/NominaIndividualDeAjuste/Reemplazar/InformacionGeneral/@Fec<br>haGen|
|HorNIE:|/NominaIndividualDeAjuste/Reemplazar/InformacionGeneral/@Hor|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 258 de 269 





### (11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

|[HORA_NOMINAINDIVIDUALDEAJUSTE(co<br>n GMT)]|aGen|
|---|---|
|TipoNota:[TIPO_NOTA]|/NominaIndividualDeAjuste/TipoNota|
|NitNIE:<br>[NIT<br>EMISOR_NOMINAINDIVIDUALDEAJUSTE]|/NominaIndividualDeAjuste/Reemplazar/Empleador/@NIT|
|DocEmp: [NUMERO_ID_EMPLEADO]|/NominaIndividualDeAjuste/Reemplazar/Trabajador/@NumeroDoc<br>umento|
|ValDev:[VALOR_DEVENGADO_TOTAL]|/NominaIndividualDeAjuste/Reemplazar/DevengadosTotal|
|ValDed:[VALOR_DEDUCCION_TOTAL]|/NominaIndividualDeAjuste/Reemplazar/DeduccionesTotal|
|ValTol:<br>[VALOR_TOTAL_NOMINAINDIVIDUALDEAJ<br>USTE|/NominaIndividualDeAjuste/Reemplazar/ComprobanteTotal|
|CUNE: [CUNE]|/NominaIndividualDeAjuste/Reemplazar/InformacionGeneral/@CU<br>NE|
|QRCode:|/NominaIndividualDeAjuste/Reemplazar/CodigoQR|
|Nota de Ajuste de Documento Soporte de|Pago de Nómina Electrónica(Opción Eliminar):|
|Detalle:|Xpath:|
|NumNIE:<br>[NUMERO_NOMINAINDIVIDUALDEAJUSTE]|/NominaIndividualDeAjuste/Eliminar/NumeroSecuenciaXML/@Nu<br>mero|
|FecNIE:<br>[FECHA_NOMINAINDIVIDUALDEAJUSTE]|/NominaIndividualDeAjuste/Eliminar/InformacionGeneral/@Fecha<br>Gen|
|HorNIE:<br>[HORA_NOMINAINDIVIDUALDEAJUSTE(con<br>GMT)]|/NominaIndividualDeAjuste/Eliminar/InformacionGeneral/@Hora<br>Gen|
|TipoNota:[TIPO_NOTA]|/NominaIndividualDeAjuste/TipoNota|
|NitNIE:<br>[NIT<br>EMISOR_NOMINAINDIVIDUALDEAJUSTE]|/NominaIndividualDeAjuste/Eliminar/Empleador/@NIT|
|DocEmp:[NUMERO_ID_EMPLEADO]|0|
|ValDev:[VALOR_DEVENGADO_TOTAL]|0.00|
|ValDed:[VALOR_DEDUCCION_TOTAL]|0.00|
|ValTol:||
|[VALOR_TOTAL_NOMINAINDIVIDUALDEAJU<br>STE|0.00|
|CUNE:[CUNE]|/NominaIndividualDeAjuste/Eliminar/InformacionGeneral/@CUNE|
|QRCode:|/NominaIndividualDeAjuste/Eliminar/CodigoQR|



Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 259 de 269 

**Resolución No. 000013** 





(11 FEB 2021) 

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

NumNIE: [NUMERO_NOMINAINDIVIDUAL] FecNIE: [FECHA_NOMINAINDIVIDUAL] HorNIE: [HORA_NOMINAINDIVIDUAL(con GMT)] NitNIE: [NIT EMISOR_NOMINAINDIVIDUAL] sin puntos ni guiones DocEmp: [NUMERO_ID_EMPLEADO] sin puntos ni guiones 

ValDev: [VALOR_DEVENGADO_TOTAL] con punto decimal, con decimales a dos (2) dígitos, sin separadores de miles, ni símbolo pesos. 

ValDed: [VALOR_DESDUCCION_TOTAL] con punto decimal, con decimales a dos (2) dígitos, sin separadores de miles, ni símbolo pesos. 

ValTol: [VALOR_TOTAL_NOMINAINDIVIDUAL con punto decimal, con decimales a dos (2) dígitos, sin separadores de miles, ni símbolo pesos. 

CUNE: [CUNE] 

QRCode: URL disponible por la DIAN 

- Ambiente Habilitación: https://catalogo-vpfe-hab.dian.gov.co/document/searchqr?documentkey=CUNE 

- Ambiente Producción: https://catalogo-vpfe.dian.gov.co/document/searchqr?documentkey=CUNE 

#### Ejemplo: 

Teniendo en cuenta los datos de entrada, se presenta el código QR que se incluye en la representación gráfica del Documento Soporte de Pago de Nómina Electrónica: 

NumNIE: 323200000129 FecNIE: 2019-16-01 HorNIE: 10:53:10-05:00 NitNIE: 700085371 DocEmp: 800199436 ValDev: 1500000.00 ValDed: 285000.00 ValTol: 1785000.00 CUNE: e5bac48e354bc907bccff0ea7d45fbf784f0a8e7243b58337361e1fbd430489d - <u>https://catalogo vpfe.dian.gov.co/document/searchqr?documentkey=e5bac48e354bc907bccff0ea7d45fbf784f0a8e7243b5833 7361e1fbd430489d</u> 

#### _Figura 1. - Ejemplo de código bidimensional QR_ 

#### Tamaño: 

El tamaño mínimo que debe tener el código bidimensional QR es de 2cm para facilitar la lectura por los diferentes dispositivos. 

La Representación Gráfica: 

> Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co 

Página 260 de 269 

**Resolución No. 000013** 





### (11 FEB 2021) 

### Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 

La representación gráfica puede ser diseñada de acuerdo con las necesidades del Emisor del Documento Soporte de Pago de Nómina Electrónica y las Notas de Ajuste del mencionado documento; como la generación está en formato XML, entonces cualquier herramienta informática de conversión de este formato a .pdf, .docx, u otros formatos digitales podrá ser utilizada, en todo caso deberá tener el código bidimensional QR tal como ya se indicó, según corresponda, ya que el mismo es el que permite la consulta de los documentos validados. 

Una alternativa adicional a los formatos digitales es la posibilidad de generar impresión en papel de la representación gráfica diseñada, la cual deberá de igual forma tener el código bidimensional QR. 

La representación gráfica debe incluir el código QR en todas las páginas de los formatos digitales y de la impresión en papel del Documento Soporte de Pago de Nómina Electrónica y Nota de Ajuste de Documento Soporte de Pago de Nómina Electrónica. 

La representación gráfica siempre será “una representación, una imagen” de la información consignada en el formato XML de los _perfiles de la DIAN_ . Esto significa que el documento electrónico siempre será el que tenga valor legal para las autoridades nacionales. Si cualquier persona requiere validar la autenticidad de una representación gráfica, entonces deberá acceder al sitio web que la DIAN disponga para ello, activar el hiperenlace, diligenciar los campos de información, disparar el botón de Validación, y comparar lo que le muestra la respuesta devuelta por el sistema de emisión del Documento Soporte de Pago de Nómina Electrónica de la DIAN con lo que le exhibe la representación que tiene a la mano, y proceder en consecuencia. Si la información difiere, podrá denunciar el hecho a la DIAN, porque puede tratarse de un documento apócrifo, sin validez legal, y que podría ser la evidencia de una acción que amerita ser investigada fiscalmente. 

### 14. Anexo: Herramienta para el consumo de Web Services. 

### 14.1. Introducción 

SoapUI es una herramienta, para la realización de pruebas a aplicaciones con arquitectura orientada a servicio (SOA). Soporta múltiples protocolos como SOAP, por tanto es adecuada para realizar pruebas del web services DIAN y sus distintos métodos. 

A continuación, se entregan lineamientos para su uso y configuración. 

### 14.2. Descargar SOAP UI. 

La descarga de la herramienta se recomienda hacerla visitando el sitio oficial de SOAP UI, en el link que se deja a continuación. 

<u>https:/www.soapui.org/downloads/soapui.html</u> 

### 14.3. Ejecutar SOAP UI. 

Una vez descargada la herramienta e instalada se procede a ejecutar la aplicación. 

### 14.4. Crear un nuevo proyecto tipo SOAP. 

> Dirección de Gestión de Ingresos Carrera 8 Nº 6C-38 piso 6º   PBX 607 9999 – 382 4500 Ext. 905101 Código postal 111711 www.dian.gov.co Formule su petición, queja, sugerencia o reclamo en el Sistema PQSR de la DIAN 

Página 261 de 269 

) | Ma. IN @® POR UNA COLOMBIA MAS HONESTA 

5 Elemprendimientoeses de todos | \yinhacienda 



<!-- Start of picture text -->
5 Elemprendimientoeses de todos | \yinhacienda<br><!-- End of picture text -->



<!-- Start of picture text -->
@ = Soapul-5.4.0 File Project Suite Case Step Tools Desktop Help<br>eee Create Fmnty Proiect SoapUI 5.4.0<br>PEPEoo NeW RES! Project NE,$ipreferences Proxy Crear nuevo proyecto de tipo SOAP<br>.| = Import Project #1 SoapUI Starter Page<br>2 Import Packed Project<br>Se Price import Remote Project<br>4 Import Postman Collection<br>Save All Projects one |<br>Open All Clos<br>Close All Open Projects<br>Rename Workspace F2 —————————— ————————————s<br>NewSnitch Workspace Workspece Getting Started. Sample Projects: Useful Resources<br>Save Preferences<br>Exit<br>Exit without saving “2Q<br>eve New SOAP Project<br>New SOAPCreates a  ProjectWSDL/SOAP based Project in this workspace Joe<br>ProjectName: || _|ngresar nombre del proyecto...<br>Initial WSDL: Ingresar url wsdl... Browse... |<br>Create Requests: vy Create sample requests for all operations?<br>Create TestSuite: Creates a TestSuite for the imported WSDL<br>Relative Paths: Stores all file paths in project relatively to project file (requires save)<br><!-- End of picture text -->

) | Ma.IN POR UNA COLOMBIA MAS HONESTA 



<!-- Start of picture text -->
®<br><!-- End of picture text -->



<!-- Start of picture text -->
; Elemprendimientoes de todos | Wyjnhacienda<br><!-- End of picture text -->



<!-- Start of picture text -->
Overview TestSuites | ‘WS-Security Configurations 7 Security Scan Defaults<br>Agregar nuevo certificado.<br>Outgoing WS-Security Configurations Incoming WS-Security Configurations Truststores<br>Ex<br>° Status Password Default Alias Alias Password<br>oK fessssnnsevevvoenseneeee®<br>Certificado agregado. Password del certificado<br><!-- End of picture text -->



<!-- Start of picture text -->
) | Ma.IN ®<br>POR UNA COLOMBIA MAS HONESTA<br><!-- End of picture text -->



<!-- Start of picture text -->
m™ Elemprendimientoes de todos | \yinhacienda<br><!-- End of picture text -->



<!-- Start of picture text -->
Overview TestSuites [sosos ee so aie ees] Security Scan Defaults<br>Agregar configuraci6én. a Listado de certificados agregados<br>Incoming WS-Securty Configurations Truststores<br>fx<br>Name Default Username/Alias Default Password Actor Must Understand<br>[outgoing_|— Nombre de la configuracién creada.<br>Agregar nueva entrada de WSS<br>ay<br>xXay<br>SETimestamp keystore:7 persona_jrsona_juridica_pruebas_vigente.p12I — ~ Certificadoif agregado en Keystores<br>Alias: usuario de pruebas persona juridica [)<br>Password: eececcccceccccccecscecees Contrasefia del certificado<br>Key Identifier Type: Binary Security Token<br>Signature Algorithm: http:/ /www.w3.org/2001/04/xmldsig-more#rsa-sha256<br>Signature Canonicalization: http:/ /www.w3.org/2001/10/xml-exc-cl4n¢ i}<br>Digest Algorithm: http://www.w3.org/2001/04/xmlenc#sha256 a<br>Use Single Certificate: Use single certificate for signing<br>La entrada WSS de tipo Signature, contiene Key Identifier Type,<br>Signature Algorithm, Signature Canonicalization, Digest Algorithm<br>Parts: +x yque Usese S in dicangle Certificate,en la imagen. estos deben tener los mismos valores<br>1D Name Namespace Encode<br>To [8/addressing|Element<br>http:/www.w3.org/2005/08/addressing<br><!-- End of picture text -->



<!-- Start of picture text -->
Overview TestSuites Security Scan Defaults<br>Incoming WS-Security Configurations _Keystores _Truststores<br>+x<br>Name‘outgoing Default Username/Alias Default Password ‘Actor ‘Must Understand<br>ay<br>+Xav<br>omer >| Time To Live: 60000<br>Millisecond Precision: Sets precision of timestamp to milliseconds:<br>Definir en mili segundos el tiempo de vigencia<br>del token de seguridad.<br><!-- End of picture text -->



<!-- Start of picture text -->
) | Ma.IN ®<br>POR UNA COLOMBIA MAS: HONESTA<br><!-- End of picture text -->



<!-- Start of picture text -->
4 Elemprendimientoes de todos | Wyjnhacienda<br><!-- End of picture text -->



<!-- Start of picture text -->
= eee 1F GerStatusReq)<br>Fim vlan We-tecurey > 2 EO S& © WB htps://colombia-dian-webservices-input-sbx.azurewebsites.net/WcfDianCustomerServices.svc/ws<br>> BasictittpsBinding WcfDianCustomerServices El <scapiEnvelope unlnaisoap="http://www.wi .org/1003705/scap-envelope” uminsiwef= http: //wet dian.colombia’> :<br>5 WSHitpBinding_ WefDianCustomerservices fo ioaptteager/><br>¥ DS Getstatus E <wcf icetstatus><br>YS SendBillAsynei </soap:Body>Oy SEESES Soha aLen9sous4ate2£133914935£907feS564390NebO</ wot tackts><br>LS SendBilAsyncRequest </soapi Envelope><br>© SendBiuanachmentAsyne 3<br>rc}<br>Username:<br>Password<br>Domain:<br>Pre-emptive auth: ©Use global preference<br>‘Authenticate pre-emptively<br>Agregar"Basic" authorization<br>Incoming WSS: rr UN Seleccionar configuracién WS-Security<br>creaday configurada previamente<br>Request Properties<br>Property. [valve J<br>weeDescription GopanaRequest Configuracién de autenticacién<br>Message Size 293<br>BindTimeoutEndpowntFollow AddressRedirects hetpsue //colombia—dian-w... 7<br>EncodingUsernamePasswordDomain ures VaHeaders(0) Attachments(0) WS-A WS-RM JMS Headers JMS Properties (0)<br><!-- End of picture text -->



<!-- Start of picture text -->
) | Ma.IN ®<br>POR UNA COLOMBIA MAS: HONESTA<br><!-- End of picture text -->



<!-- Start of picture text -->
2% Elemprendimientoes de todos | yinhacienda<br><!-- End of picture text -->



<!-- Start of picture text -->
= eee<br>Projects¥ Be Dian Ws-Security rP¥e2eOoh2eea29 29 https://colombia-dian-webservices-input:. ia-dian-' ices-ii = sbx.azurewebsites.net/WefDianii ian<br>>» & BasicHttpsBinding_IWcfDianCustomerServices E)<soap:Envelope xmins:soap="http://www.w3.org/2003/05/soap-envelope” xmins:wcf= "http ><br>¥_ 3 WSHttpBinding_IWcfDianCustomerServices __|5 <soap:Header/><soap:Body><br>a = E : Weistonetons<!--optional:-->Svcd trackid>31¢1950894a102£133314335£907£056d3908cb0</wcf<br>or dBillAsync </wef:GetStatus> :trackrd><br>‘© SendBillAttachmentAsync B)| <sscupstaveiose><br>c________]eee<br>Enable WS-A addressing: ——@> [Habilitar WS-A addressing<br>Must understand: none §<br>WS-A Version: 200508<br>Add default wsa:Action: Add default wsa:Action<br>Action: http://wef.dian.colombia/IWcfDianCustomerServices/Get<br>Add default wsa:To: Add default wsa:To |—® | Hablitar wsa:To<br>Reply to:<br>ReplyTo Reference Parameters:<br>Generate MessagelD: Randomly generate Messageld<br>MessagelD:<br>From:<br>Fault to:<br>FaultTo Reference Parameters:<br>Relates to:<br>Relationship type:<br>Request Properties<br>PropertyValue<br>Name GetStatusRequest<br>Description<br>Message Size 319<br>Encoding UTF-8<br>Endpoint https: //colombia-dian-w... WS-A addressing<br>Timeout<br>Bind Address<br>Follow Redirects true<br>Username<br>Password a Auth (Basic) Headers (0) Attachments (0) WS-RM JMSHeaders JMS Properties (0)<br>Domain<br><!-- End of picture text -->



<!-- Start of picture text -->
__ | f. \ IN®<br>POR UNA COLOMBIA MAS HONESTA<br><!-- End of picture text -->



<!-- Start of picture text -->
Elemprendimientoes de todos | \jinhacienda<br><!-- End of picture text -->



<!-- Start of picture text -->
eee 32 GetStatusRequest<br>¥ © GO & & OW & https://colombia-dian-webservices-input-sbx.azurewebsites.net/WcfDianCustomerServices.svc/ws<br>«<br>[)<soap:Envelope xminsisoap="http://www.w3 org/2003/05/soap-envelape” xminaiwcf="http > Ekstznvelope xmins:s-"http://www.w3-org/2003/05/soap-envelope” xminsta="http://www.w3-org/2005/08/addressing™<br><soap:feader/> EB) <a:neadex><br>G <soap:Body> <aiAction s:mustUnderstand="1">https//wet.dian.colonbia/1wcfDianCustonerServices/GetStatusResponse</a::<br>=he=s= | \/coap:zavelope></aoap:Body><wcf:GetStatus></wct<wet ;Getstatus:: tracktd]31e1950894aic2£133314335£907£e56a390beb0fTrackld /wet :trackrd> BIBI <activityId<orSecurity</oisecurity><a:Timestamp</u:Timestamp><u:created>2018-11-28714:16:44.629z</u:created><a:Expires>2018-11-28714:21:44.629Z¢/u:Expires>CorrelationId="97dd04d8-47aa-460e-9646-4823145a57cb"simustUnderstand="1"u:zd="_0"> xmins:o="http: //docs .oasis-open.org/wss/2004/01/oasis-200401-wes-wseedxmlna="http://schemas.microsoft.com/2q<br>‘a Be] <s:Body></siteader><br>Authorizigion:; Basic (7) BI5} <CetStatusResponse<GetStatusResult<bifrrortessage<b:<b:Statuscode>99</b: IsValid>false</b:1sValid>xmlns="http:xmlns:b="http://schemas.datacontract.org/2004/07/Gosocketi:nil="truo”StatusCode> //wcf-dian.colombia">xnlns:c="http://schomasmicrosoft -con/2003/10/Serialization/Arrays". Dian. Services .Utils.Commg<br><b:StatusDescription>Documento validado anteriormente con trackId: 31c1950894a1c2#133314335£9074<br><biStatusMessage>Validacion contiene errores en campos mandatorios.</b:Statustiessage><br>Username} D94bHWadmVyc?1vbjO1MS4wIiB1bmNv2G1uz20iSVNPLTgANTkEMSIgc3RhbaRhbG9uZT0ibasiP24B2Gu6G<br>Password:' </GetStatusRespons</cetstatuanes\it><br>Domain: /s:Envelope></siBody><br>OutgoingPre-emptivegoingjoins Wss:YS aul: © outgoin:UseAuthenticate pre-emptivelygoing global preference =z Soap| response XmIBytes representa el arreglo de bytes del ApplicationResponsei i<br>Incoming WSS: :<br>Ejecutar request<br>@ Auth (Basic) Headers (0) Attachments (0) WS-A_ WS-RM_— JMS Headers JMS Property(0) Headers (9) Attachments (0) SSLInfo = WSS(0)  JMS(0).<br><!-- End of picture text -->



<!-- Start of picture text -->
) | Ma.IN ®<br>POR UNA COLOMBIA MAS: HONESTA<br><!-- End of picture text -->



<!-- Start of picture text -->
<:s%m Elemprendimientoes de todos | \yinhacienda<br><!-- End of picture text -->



<!-- Start of picture text -->
= eee 42 SendBillAsyncRec<br>Projects¥ Bs Dian ws-Security >| ¥MW ©29 OS &zo WB https://colombia-dian-webservices:. ia-dian-" -iinput =Sbxcazurewebsites.net/WefDianCustomerservices.svc/Wsi i<br>> & BasicHttpsBinding_WcfDianCustomerServices [Ei <soap:Envelope xmlns:soap="http: //www.w3.org/2003/05/soap-envelope” xminsiwcf="http://wef.dian.colombia"> | | ><br>¥ 3> WSHttpBinding_lWcfDianCustomerServices© GetStatus [=]|a hoap:Header/>‘soap:<wef Body>:SendBillasy:<br>Y © SendBillasyncBBY sendBillAsyncRequest}; sag leotstenatinayae><wet<wef:fileName4File:content? namef/wctf:fileName>ATE>CTETI$#8936619540¢/wcf :contentPile><br>© SendBillAttachmentAsync </soap:Envelope>< :Body><br>= Nombre de archivo- zip.7<br>Ejecutar Agregar zip con xml's adjuntos.<br>request ZA a<br>fees °<br>Name Content type Size Part Type ContentiD Cached<br>FourXmls.zip application/zip 28583 1528936619540 | CONTENT FourXmls.zip<br>Habilitar Cached<br>Seleccionar Part.<br>Request Properties<br>Property Value<br>Name SendBillAsyncRequest<br>Description<br>Message Size 334<br>Encoding UTF-8<br>Endpoint https: //colombia-dian-w...<br>Timeout<br>Bind Address<br>Follow Redirects true<br>Username<br>PasswordDomain @ Auth (Basic) Headers (0) Attachments(1) WS-A_—WS-RM_— JMS Headers JMS Property(0)<br>Authentication Type Global HTTP Settings<br><!-- End of picture text -->



<!-- Start of picture text -->
) | Ma.IN ®<br>POR UNA COLOMBIA MAS HONESTA<br><!-- End of picture text -->



<!-- Start of picture text -->
Elemprendimientoes de todos | \yinhacienda<br><!-- End of picture text -->



<!-- Start of picture text -->
s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing" xmlns:u="http://docs.oasis-<br><s:Header><br><a:Action s:mustUnderstand="1">http://wcf.dian.colombia/IWcfDianCustomerServices/SendBillAsyncResponse</a:Action><br><ActivityId CorrelationId="dc00d7c3-634f£-43d1-b147-73aa63473364" xmlns="http://schemas.microsoft.com/2004/09/ServiceModel/Diagnos<br><o:Security s:mustUnderstand="1" xmlns:o="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"><br><u:Timestamp u:Id="_0"><br><u:Created>2018-11-28T18:07:42.327Z</u:Created><br><u:Expires>2018-11-28T18:12:42.327Z</u:Expires><br></u:Timestamp><br></o:Security><br></s:Header><br><s:Body><br><SendBillAsyncResponse xmlns="http://wef.dian.colombia"><br><SendBillAsyncResult xmlns:b="http://schemas.datacontract.org/2004/07/Gosocket.Dian.Services.Utils" xmlns:i="http://www.w3.org<br><b:XmlParamsResponseTrackIid><br><b:processedMessage>Documento<b:trackId/> procesado anteriormente con trackId: e9c0da902a4b9c4ed9b97c54121b2405b9ea842d</b:processedN<br><b:xmlFileName>DOC_19_7_907_</b:xmlFileName><br></b:XmlParamsResponseTrackIid><br><b:Xm1ParamsResponseTrackId><br><b:processedMessage>Documento<b:trackid/> procesado anteriormente con trackId: aabbb40bcd0217elcfef1£98b0e5398£239f76b3</b:processed)<br><b:xmlFileName>DOC_47_8_8_</b:xmlFileName><br></b:Xm1ParamsResponseTrackId><br></SendBillAsyncResult><br></SendBillAsyncResponse><br></s:Body><br>/s:Envelope><br>SenaBillAsync soap response<br><!-- End of picture text -->

