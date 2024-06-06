# Diccionario de datos:

## Dataset: application_data_procesada

Archivo formato .csv que contiene información acerca de los prestamos dados al cliente por el banco, datos personales del cliente como edad, estado civil, miembros de la familia, posesión de bienes personales como auto o vivienda, si tuvo dificultades de pago o no, sus ingresos, el monto del credito, anualidad, entre otros datos relevantes para el análisis.



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

* *MONTO_CREDITO*: **int**, indica el monto del crédito solicitado..

```python
        'MONTO_CREDITO': '314100'
```