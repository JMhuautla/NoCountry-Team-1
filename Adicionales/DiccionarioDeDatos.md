# Diccionario de datos:

## Dataset: application_data_procesada

Archivo formato .parquet que contiene información acerca de los prestamos dados al cliente por el banco, datos personales del cliente como edad, estado civil, miembros de la familia, posesión de bienes personales como auto o vivienda, si tuvo dificultades de pago o no, sus ingresos, el monto del credito, anualidad, entre otros datos relevantes para el análisis.



* *ID_CREDITO*: **int**, identificador unico del credito otorgado por el banco, al cliente.

```python
        'ID_CREDITO': '101413'
```

* *OBJETIVO*: **int**, columna objetivo. Hace referencia a si el cliente tuvo dificultades de pago o no las tuvo; siendo 0 SIN dificultad de pago, y 1 CON dificultad de pago.

```python
        'OBJETIVO': '0'
```

* *TIPO_PAGO*: **string**, hace referencia al tipo de pago realizado por el cliente; Siendo "Cash loans" = "Pago en efectivo", y "Revolving loans" = "Pago con tarjeta de crédito". 

```python
        'TIPO_PAGO': 'Cash loans'
```

* *GENERO*: **string**, genero del cliente; siendo "F" = "Femenino" y "M" = Masculino.

```python
        'GENERO': 'F'
```

* *PROP_AUTO*: **string**, indica si el cliente posee automovil o no; siendo "N" = "No" y "Y" = "Si".

```python
        'PROP_AUTO': 'N'
```

* *PROP_INMUEBLE*: **string**, indica si el cliente posee inmueble/s o no; siendo "N" = "No" y "Y" = "Si".

```python
        'PROP_INMUEBLE': 'Y'
```

* *CANTIDAD_HIJOS*: **int**, indica la cantidad de hijos que tiene el cliente.

```python
        'CANTIDAD_HIJOS': '0'
```

* *INGRESO*: **int**, indica el ingreso anual del cliente.

```python
        'INGRESO': '67050'
```

* *MONTO_CREDITO*: **int**, indica el monto del crédito solicitado.

```python
        'MONTO_CREDITO': '314100'
```
* *ANUALIDAD_PRESTAMO*: **float**, indica el monto que se paga anualmente con el fin de ir amortizando el préstamo.

```python
        'ANUALIDAD_PRESTAMO': '24701'
```

* *PRECIO_BIENES*: **float**, es el precio de los bienes por los que se concede el préstamo.

```python
        'PRECIO_BIENES': '314100'
```

* *TIPO_ACOMPAÑANTE'*: **category**, indica quien acompaño al cliente cuando solicito el prestamo.

```python
        'TIPO_ACOMPAÑANTE': 'Unaccompanied'
```

* *TIPO_INGRESO*: **category**, indica el tipo de ingreso del cliente que solicita el prestamo.

```python
        'TIPO_INGRESO': 'Working'
```

* *NIVEL_ESTUDIO*: **category**, indica el nivel de estudios realizados por el cliente que solicita el prestamo.

```python
        'NIVEL_ESTUDIO': 'Secondary / secondary special'
```

* *ESTADO_CIVIL*: **int**, indica el monto del crédito solicitado..

```python
        'ESTADO_CIVIL': '314100'
```

* *TIPO_VIVIENDA*: **int**, indica el monto del crédito solicitado..

```python
        'TIPO_VIVIENDA': '314100'
```

* *POBLACION_RELATIVA_REGION*: **int**, indica el monto del crédito solicitado..

```python
        'POBLACION_RELATIVA_REGION': '314100'
```

* *EDAD_DIAS*: **int**, indica el monto del crédito solicitado..

```python
        'EDAD_DIAS': '314100'
```

* *DIAS_EMPLEADO*: **int**, indica el monto del crédito solicitado..

```python
        'DIAS_EMPLEADO': '314100'
```

* *DIAS_MODIF_REGISTRO*: **int**, indica el monto del crédito solicitado..

```python
        'DIAS_MODIF_REGISTRO': '314100'
```

* *DIAS_MODIF_DOCUMENTO*: **int**, indica el monto del crédito solicitado..

```python
        'DIAS_MODIF_DOCUMENTO': '314100'
```

* *ANTIGUEDAD_AUTO*: **int**, indica el monto del crédito solicitado..

```python
        'ANTIGUEDAD_AUTO': '314100'
```

* *TIENE_CELULAR*: **int**, indica el monto del crédito solicitado..

```python
        'TIENE_CELULAR': '314100'
```

* *TELEFONO_EMPLEO*: **int**, indica el monto del crédito solicitado..

```python
        'TELEFONO_EMPLEO': '314100'
```

* *TELEFONO_TRABAJO*: **int**, indica el monto del crédito solicitado..

```python
        'TELEFONO_TRABAJO': '314100'
```

* *ATIENDE_CELULAR*: **int**, indica el monto del crédito solicitado..

```python
        'ATIENDE_CELULAR': '314100'
```

* *TELEFONO_CASA*: **int**, indica el monto del crédito solicitado..

```python
        'TELEFONO_CASA': '314100'
```

* *EMAIL*: **int**, indica el monto del crédito solicitado..

```python
        'EMAIL': '314100'
```

* *PROFESION*: **int**, indica el monto del crédito solicitado..

```python
        'PROFESION': '314100'
```

* *CANTIDAD_MIEMBROS_FAMILIA*: **int**, indica el monto del crédito solicitado..

```python
        'CANTIDAD_MIEMBROS_FAMILIA': '314100'
```

* *CALIFICACION_REGION_CLIENTE*: **int**, indica el monto del crédito solicitado..

```python
        'CALIFICACION_REGION_CLIENTE': '314100'
```

* *CALIFICACION_REGION_CLIENTE_CIUDAD*: **int**, indica el monto del crédito solicitado..

```python
        'CALIFICACION_REGION_CLIENTE_CIUDAD': '314100'
```

* *DIA_SEMANA_SOLICITUD*: **int**, indica el monto del crédito solicitado..

```python
        'DIA_SEMANA_SOLICITUD': '314100'
```

* *HORA_SOLICITUD*: **int**, indica el monto del crédito solicitado..

```python
        'HORA_SOLICITUD': '314100'
```

* *DIRECCION_PERMANENTE_NO_DIRECCION_CONTACTO*: **int**, indica el monto del crédito solicitado..

```python
        'DIRECCION_PERMANENTE_NO_DIRECCION_CONTACTO': '314100'
```

* *DIRECCION_PERMANENTE_NO_DIRECCION_TRABAJO*: **int**, indica el monto del crédito solicitado..

```python
        'DIRECCION_PERMANENTE_NO_DIRECCION_TRABAJO': '314100'
```

* *DIRECCION_CONTACTO_NO_DIRECCION_TRABAJO*: **int**, indica el monto del crédito solicitado..

```python
        'DIRECCION_CONTACTO_NO_DIRECCION_TRABAJO': '314100'
```

* *NO_VIVE_CIUDAD_REGISTRADA*: **int**, indica el monto del crédito solicitado..

```python
        'NO_VIVE_CIUDAD_REGISTRADA': '314100'
```

* *NO_TRABAJA_CIUDAD_REGISTRADA*: **int**, indica el monto del crédito solicitado..

```python
        'NO_TRABAJA_CIUDAD_REGISTRADA': '314100'
```

* *NO_VIVE_CIUDAD_DE_TRABAJO*: **int**, indica el monto del crédito solicitado..

```python
        'NO_VIVE_CIUDAD_DE_TRABAJO': '314100'
```

* *TIPO_ORGANIZACION*: **int**, indica el monto del crédito solicitado..

```python
        'TIPO_ORGANIZACION': '314100'
```
