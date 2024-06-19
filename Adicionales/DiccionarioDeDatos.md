# Diccionario de datos:

## Dataset: application_data_procesada

Archivo formato .parquet que contiene información acerca de los prestamos dados al cliente por el banco, datos personales del cliente como edad, estado civil, miembros de la familia, posesión de bienes personales como auto o vivienda, si tuvo dificultades de pago o no, sus ingresos, el monto del credito, anualidad, entre otros datos relevantes para el análisis.



* *ID_CREDITO*: **int**, identificador unico del credito otorgado por el banco, al cliente.

```python
        'ID_CREDITO': '101413'
```

* *OBJETIVO*: **int**, columna objetivo. Hace referencia a si el cliente tuvo dificultades de pago o no las tuvo; siendo 0 = "SIN dificultad de pago", y 1 = "CON dificultad de pago".

```python
        'OBJETIVO': '0'
```

* *TIPO_PAGO*: **category**, hace referencia al tipo de pago realizado por el cliente; Siendo "Cash loans" = "Pago en efectivo", y "Revolving loans" = "Pago con tarjeta de crédito". 

```python
        'TIPO_PAGO': 'Cash loans'
```

* *GENERO*: **category**, genero del cliente; siendo "F" = "Femenino" y "M" = Masculino.

```python
        'GENERO': 'F'
```

* *PROP_AUTO*: **category**, indica si el cliente posee automovil o no; siendo "N" = "No" y "Y" = "Si".

```python
        'PROP_AUTO': 'N'
```

* *PROP_INMUEBLE*: **category**, indica si el cliente posee inmueble/s o no; siendo "N" = "No" y "Y" = "Si".

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

* *ESTADO_CIVIL*: **category**, indica el estado civil del cliente que solicita el prestamo.

```python
        'ESTADO_CIVIL': 'Married'
```

* *TIPO_VIVIENDA*: **category**, indica el tipo de vivienda en que reside el cliente que solicita el prestamo.

```python
        'TIPO_VIVIENDA': 'House / apartment'
```

* *POBLACION_RELATIVA_REGION*: **float**, población normalizada de la región donde vive el cliente que solicita el prestamo.

```python
        'POBLACION_RELATIVA_REGION': '0.035792'
```

* *EDAD_DIAS*: **int**, indica la edad del cliente que solicita el prestamo, en días.

```python
        'EDAD_DIAS': '13749'
```

* *DIAS_EMPLEADO*: **int**, indica la cantidad de días trabajados por el cliente que solicita el prestamo.

```python
        'DIAS_EMPLEADO': '365243'
```

* *DIAS_MODIF_REGISTRO*: **float**, indica cuantos días antes de la solicitud el cliente cambió su registro.

```python
        'DIAS_MODIF_REGISTRO': '7.0'
```

* *DIAS_MODIF_DOCUMENTO*: **int**, indica cuantos días antes de la solicitud el cliente cambió su identificación.

```python
        'DIAS_MODIF_DOCUMENTO': '4053'
```

* *TIENE_CELULAR*: **int**, indica si el cliente tiene o no tiene celular movil. Siendo 1 = "Si", 0 = "No".

```python
        'TIENE_CELULAR': '1'
```

* *TELEFONO_EMPLEO*: **int**, indica si el cliente proporciono telefono del trabajo. Siendo 1 = "Si", 0 = "No".

```python
        'TELEFONO_EMPLEO': '1'
```

* *ATIENDE_CELULAR*: **int**, indica si el número de telefono proporcionado es accesible. Siendo 1 = "Si", 0 = "No".

```python
        'ATIENDE_CELULAR': '1'
```

* *TELEFONO_CASA*: **int**, indica si el cliente proporciono telefono residencial. Siendo 1 = "Si", 0 = "No".

```python
        'TELEFONO_CASA': '1'
```

* *EMAIL*: **int**, indica si el cliente proporciono email o no. Siendo 1 = "Si", 0 = "No".

```python
        'EMAIL': '1'
```

* *PROFESION*: **category**, indica la profesión del cleinte que solicita el prestamo.

```python
        'PROFESION': 'Laborers'
```

* *CANTIDAD_MIEMBROS_FAMILIA*: **int**, indica la cantidad de miembros de la familia del cliente que solicita el prestamo.

```python
        'CANTIDAD_MIEMBROS_FAMILIA': '0'
```

* *CALIFICACION_REGION_CLIENTE*: **int**, indica la calificación de la región donde vive el cliente .

```python
        'CALIFICACION_REGION_CLIENTE': '3'
```

* *CALIFICACION_REGION_CLIENTE_CIUDAD*: **int**, indica la calificación de la región donde vive el cliente teniendo en cuenta la ciudad.

```python
        'CALIFICACION_REGION_CLIENTE_CIUDAD': '2'
```

* *DIA_SEMANA_SOLICITUD*: **category**, indica el día de la semana en que fue solicitado el prestamo.

```python
        'DIA_SEMANA_SOLICITUD': 'TUESDAY'
```

* *HORA_SOLICITUD*: **int**, indica la hora en que fue solicitado el prestamo.

```python
        'HORA_SOLICITUD': '10'
```

* *DIRECCION_PERMANENTE_NO_DIRECCION_CONTACTO*: **int**, indica si la dirección permanente del cliente no coincide con la dirección de contacto. Siendo 1 = "Diferente", 0 = "Igual".

```python
        'DIRECCION_PERMANENTE_NO_DIRECCION_CONTACTO': '1'
```

* *DIRECCION_PERMANENTE_NO_DIRECCION_TRABAJO*: **int**, indica si la dirección permanente del cliente no coincide con la dirección del trabajo. Siendo 1 = "Diferente", 0 = "Igual".


```python
        'DIRECCION_PERMANENTE_NO_DIRECCION_TRABAJO': '1'
```

* *DIRECCION_CONTACTO_NO_DIRECCION_TRABAJO*: **int**, indica si la dirección de contacto del cliente no coincide con la dirección del trabajo. Siendo 1 = "Diferente", 0 = "Igual".

```python
        'DIRECCION_CONTACTO_NO_DIRECCION_TRABAJO': '1'
```

* *NO_VIVE_CIUDAD_REGISTRADA*: **int**, indica si el cliente no vive en la ciudad registrada. Siendo 1 = "Diferente", 0 = "Igual".

```python
        'NO_VIVE_CIUDAD_REGISTRADA': '1'
```

* *NO_TRABAJA_CIUDAD_REGISTRADA*: **int**, indica si el cliente no trabaja en la ciudad registrada. Siendo 1 = "Diferente", 0 = "Igual".
```python
        'NO_TRABAJA_CIUDAD_REGISTRADA': '1'
```

* *NO_VIVE_CIUDAD_DE_TRABAJO*: **int**, indica si el cliente no trabaja en la misma ciudad en que vive. Siendo 1 = "Diferente", 0 = "Igual".

```python
        'NO_VIVE_CIUDAD_DE_TRABAJO': '1'
```

* *TIPO_ORGANIZACION*: **category**, iinidica el tipo de organización a la que pertenece el cliente que solicita el prestamo.

```python
        'TIPO_ORGANIZACION': 'Medicine'
```
