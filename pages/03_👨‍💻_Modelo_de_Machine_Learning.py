import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from category_encoders import OrdinalEncoder, OneHotEncoder

st.set_page_config(page_icon="👨‍💻", page_title="Modelo de Machine Learning", layout="wide")
st.image("https://i.imgur.com/IWEpAbC.png", width=250) 
st.title("Modelo de Machine Learning") 
st.markdown('***') 

st.markdown('##### En esta página se encuentra el modelo de machine learning para detectar futuros clientes con dificultades de pago y decidir si otorgarles créditos o no hacerlo.')

st.markdown('***')

# Cargar el modelo entrenado
best_model = joblib.load('best_model.joblib')

# Definir las columnas que se utilizaron en el modelo
xt_columns = [
 'tipo_pago',
 'prop_inmueble',
 'prop_auto',
 'precio_bienes',
 'nivel_estudio',
 'profesion',
 'monto_credito',
 'edad_dias',
 'dias_empleado',
 'anualidad_prestamo',
 'tipo_ingreso',
]

# Crear la interfaz de Streamlit
st.title('Predicción de Probabilidad de Dificultad de Pago')

# Formularios de entrada para cada variable
monto_credito = st.number_input('Monto del Crédito')
anualidad_prestamo = st.number_input('Anualidad del Préstamo')
tipo_ingreso = st.selectbox('Ocupación', options=['Commercial associate', 'Working', 'Pensioner', 'State servant', 'Student', 'Maternity leave', 'Unemployed', 'Businessman'])
ingreso = st.number_input('Ingreso')
profesion = st.selectbox('Profesión', options=['Laborers', 'Core staff', 'Accountants', 'Managers', 'Other', 'Drivers', 'Sales staff', 'Cleaning staff', 'Cooking staff', 'Private service staff', 'Medicine staff', 'Security staff', 'High skill tech staff', 'Waiters/barmen staff', 'Low-skill Laborers', 'Realty agents', 'Secretaries', 'IT staff', 'HR staff'])
nivel_estudio = st.selectbox('Nivel de Estudio', options=['Secondary / secondary special', 'Higher education', 'Incomplete higher', 'Lower secondary', 'Academic degree'])
edad_dias = st.number_input('Edad')
dias_empleado = st.number_input('Años empleados')
prop_inmueble = st.selectbox('Propiedad de Inmueble', options=['Y', 'N'])
prop_auto = st.selectbox('Propiedad de Automóvil', options=['Y', 'N'])
precio_bienes = st.number_input('Precio de los Bienes')
tipo_pago = st.selectbox('Tipo de Pago', options=['Cash loans', 'Revolving loans']) 


# Convertir las entradas a un DataFrame
data = pd.DataFrame({
    'tipo_pago': [tipo_pago],
    'prop_inmueble': [1 if prop_inmueble == 'Y' else 0],
    'prop_auto': [1 if prop_auto == 'Y' else 0],
    'precio_bienes': [precio_bienes],
    'nivel_estudio': [nivel_estudio],
    'profesion': [profesion],
    'monto_credito': [monto_credito],
    'edad_dias': [int(edad_dias)],
    'dias_empleado': [int(dias_empleado)],
    'anualidad_prestamo': [anualidad_prestamo],
    'tipo_ingreso': [tipo_ingreso]
})

# Aplicar las mismas transformaciones que en el entrenamiento
# Escalar las variables numéricas
scaler = StandardScaler()
numerical_x = ['precio_bienes', 'monto_credito', 'edad_dias', 'dias_empleado', 'anualidad_prestamo',]
data[numerical_x] = scaler.fit_transform(data[numerical_x])

# Definir el mapeo para OrdinalEncoder
maplist = [
    {'col':'nivel_estudio', 'mapping':{None:0, 'Lower secondary':1, 'Secondary / secondary special':2, 'Incomplete higher':3, 'Higher education':4, 'Academic degree':5}},
    {'col':'tipo_ingreso', 'mapping':{None:0, 'Commercial associate':6, 'Working':5, 'Pensioner':4, 'State servant':7, 'Student':2, 'Maternity leave':3, 'Unemployed':1, 'Businessman':8}},
    {'col': 'profesion', 'mapping': {None:0, 'Laborers':1, 'Core staff':2, 'Accountants':3, 'Managers':4, 'Other':5, 'Drivers':6, 'Sales staff':7, 'Cleaning staff':8, 'Cooking staff':9, 'Private service staff':10, 'Medicine staff':11, 'Security staff':12, 'High skill tech staff':13, 'Waiters/barmen staff':14, 'Low-skill Laborers':15, 'Realty agents':16, 'Secretaries':17, 'IT staff':18, 'HR staff':19}}
    ] 
oe = OrdinalEncoder(mapping=maplist)
data = oe.fit_transform(data)

# Aplicar OneHotEncoder a las variables binarias
dichotomic_x = ['prop_inmueble', 'prop_auto', 'tipo_pago']
ohe = OneHotEncoder(handle_unknown='ignore')
ohe_data = ohe.fit_transform(data[dichotomic_x])

# Obtener los nombres de las columnas después de la codificación
ohe_columns = ohe.get_feature_names_out(dichotomic_x)
ohe_data = pd.DataFrame(ohe_data, columns=ohe_columns)

# Concatenar las columnas codificadas
data = pd.concat([data.drop(columns=dichotomic_x).reset_index(drop=True), ohe_data], axis=1)

# Asegúrate de que las columnas resultantes se alineen con las que el modelo espera
for col in xt_columns:
    if col not in data.columns:
        data[col] = 0

# Reordenar las columnas para asegurarse de que coincidan con el entrenamiento del modelo
data = data[xt_columns]


# Botón para realizar la predicción
if st.button('Predecir'):

    # Realizar la predicción
    probabilidad = best_model.predict_proba(data)[:, 1]  

    st.markdown('***')

    # Mostrar el resultado
    st.markdown(f'La probabilidad de que el cliente tenga dificultades de pago es: {probabilidad[0] * 100:.2f}%')

    st.markdown('***')
