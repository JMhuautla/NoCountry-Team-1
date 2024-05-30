import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def transform_parquet(path:str, file_name:str) -> str:
    """
    Carga un archivo CSV desde el directorio especificado, realiza transformaciones en los datos, 
    y guarda el DataFrame resultante en formato Parquet en el mismo directorio.

    Parameters:
    -----------
    path : str
        El directorio contenedor de los datos.
    file_name : str
        El nombre del archivo CSV con la data.

    Returns:
    --------
    path_data_transform : str
        La ruta completa del archivo Parquet guardado después de las transformaciones.
    """
    
    df = pd.read_csv(path + file_name)

    # Elimino columnas desde EXT_SOURCE_1 en adelante
    ext_source_1_index = df.columns.get_loc('EXT_SOURCE_1')
    df = df.iloc[:, :ext_source_1_index].drop(columns=['OWN_CAR_AGE'])

    # Imputación de datos nulos
    amt_goods_price_mean = df['AMT_GOODS_PRICE'].mean()
    amt_annuity_mean = df['AMT_ANNUITY'].mean()

    value_input = {
        'OCCUPATION_TYPE': 'Other',
        'NAME_TYPE_SUITE': 'Other',
        'AMT_ANNUITY': amt_annuity_mean,
        'AMT_GOODS_PRICE': amt_goods_price_mean,
        'CNT_FAM_MEMBERS': 0
        }
    df = df.fillna(value=value_input)

    # Reemplazo los valores Other_A y Other_B por Other
    df['NAME_TYPE_SUITE'] = df['NAME_TYPE_SUITE'].replace({'Other_A': 'Other', 'Other_B': 'Other'})

    # cambio tipos de datos
    new_type_cols = {
        'SK_ID_CURR': 'int64',
        'TARGET': 'int64',
        'NAME_CONTRACT_TYPE': 'category',
        'CODE_GENDER': 'category',
        'FLAG_OWN_CAR': 'category',
        'FLAG_OWN_REALTY': 'category',
        'CNT_CHILDREN': 'int64',
        'AMT_INCOME_TOTAL': 'float64',
        'AMT_CREDIT': 'float64',
        'AMT_ANNUITY': 'float64',
        'AMT_GOODS_PRICE': 'float64',
        'NAME_TYPE_SUITE': 'category',
        'NAME_INCOME_TYPE': 'category',
        'NAME_EDUCATION_TYPE': 'category',
        'NAME_FAMILY_STATUS': 'category',
        'NAME_HOUSING_TYPE': 'category',
        'REGION_POPULATION_RELATIVE': 'float64',
        'DAYS_BIRTH': 'int64',
        'DAYS_EMPLOYED': 'int64',
        'DAYS_REGISTRATION': 'float64',
        'DAYS_ID_PUBLISH': 'int64',
        'FLAG_MOBIL': 'int64',
        'FLAG_EMP_PHONE': 'int64',
        'FLAG_WORK_PHONE': 'int64',
        'FLAG_CONT_MOBILE': 'int64',
        'FLAG_PHONE': 'int64',
        'FLAG_EMAIL': 'int64',
        'OCCUPATION_TYPE': 'category',
        'CNT_FAM_MEMBERS': 'int64',
        'REGION_RATING_CLIENT': 'int64',
        'REGION_RATING_CLIENT_W_CITY': 'int64',
        'WEEKDAY_APPR_PROCESS_START': 'category',
        'HOUR_APPR_PROCESS_START': 'int64',
        'REG_REGION_NOT_LIVE_REGION': 'int64',
        'REG_REGION_NOT_WORK_REGION': 'int64',
        'LIVE_REGION_NOT_WORK_REGION': 'int64',
        'REG_CITY_NOT_LIVE_CITY': 'int64',
        'REG_CITY_NOT_WORK_CITY': 'int64',
        'LIVE_CITY_NOT_WORK_CITY': 'int64',
        'ORGANIZATION_TYPE': 'category'
        }
    df = df.astype(new_type_cols)

    # cambio nombre de columnas
    renamed_cols = {
        'SK_ID_CURR': 'ID_CREDITO',
        'TARGET': 'OBJETIVO',
        'NAME_CONTRACT_TYPE': 'TIPO_PAGO',
        'CODE_GENDER': 'GENERO',
        'FLAG_OWN_CAR': 'PROP_AUTO',
        'FLAG_OWN_REALTY': 'PROP_INMUEBLE',
        'CNT_CHILDREN': 'CANTIDAD_HIJOS',
        'AMT_INCOME_TOTAL': 'INGRESO',
        'AMT_CREDIT': 'MONTO_CREDITO',
        'AMT_ANNUITY': 'ANUALIDAD_PRESTAMO',
        'AMT_GOODS_PRICE': 'PRECIO_BIENES',
        'NAME_TYPE_SUITE': 'TIPO_ACOMPAÑANTE',
        'NAME_INCOME_TYPE': 'TIPO_INGRESO',
        'NAME_EDUCATION_TYPE': 'NIVEL_ESTUDIO',
        'NAME_FAMILY_STATUS': 'ESTADO_CIVIL',
        'NAME_HOUSING_TYPE': 'TIPO_VIVIENDA',
        'REGION_POPULATION_RELATIVE': 'POBLACION_RELATIVA_REGION',
        'DAYS_BIRTH': 'EDAD_DIAS',
        'DAYS_EMPLOYED': 'DIAS_EMPLEADO',
        'DAYS_REGISTRATION': 'DIAS_MODIF_REGISTRO',
        'DAYS_ID_PUBLISH': 'DIAS_MODIF_DOCUMENTO',
        'FLAG_MOBIL': 'TIENE_CELULAR',
        'FLAG_EMP_PHONE': 'TELEFONO_EMPLEO',
        'FLAG_WORK_PHONE': 'TELEFONO_TRABAJO',
        'FLAG_CONT_MOBILE': 'ATIENDE_CELULAR',
        'FLAG_PHONE': 'TELEFONO_CASA',
        'FLAG_EMAIL': 'EMAIL',
        'OCCUPATION_TYPE': 'PROFESION',
        'CNT_FAM_MEMBERS': 'CANTIDAD_MIEMBROS_FAMILIA',
        'REGION_RATING_CLIENT': 'CALIFICACION_REGION_CLIENTE',
        'REGION_RATING_CLIENT_W_CITY': 'CALIFICACION_REGION_CLIENTE_CIUDAD',
        'WEEKDAY_APPR_PROCESS_START': 'DIA_SEMANA_SOLICITUD',
        'HOUR_APPR_PROCESS_START': 'HORA_SOLICITUD',
        'REG_REGION_NOT_LIVE_REGION': 'DIRECCION_PERMANENTE_NO_DIRECCION_CONTACTO',
        'REG_REGION_NOT_WORK_REGION': 'DIRECCION_PERMANENTE_NO_DIRECCION_TRABAJO',
        'LIVE_REGION_NOT_WORK_REGION': 'DIRECCION_CONTACTO_NO_DIRECCION_TRABAJO',
        'REG_CITY_NOT_LIVE_CITY': 'NO_VIVE_CIUDAD_REGISTRADA',
        'REG_CITY_NOT_WORK_CITY': 'NO_TRABAJA_CIUDAD_REGISTRADA',
        'LIVE_CITY_NOT_WORK_CITY': 'NO_VIVE_CIUDAD_DE_TRABAJO',
        'ORGANIZATION_TYPE': 'TIPO_ORGANIZACION'
        }
    df = df.rename(columns=renamed_cols)

    file_name = file_name.replace('.csv', '.parquet')
    path_data_transform = f'{path}{file_name}'

    # conversion a parquet
    table = pa.Table.from_pandas(df)
    pq.write_table(table, path_data_transform)
    return path_data_transform

if __name__ == "__main__":
    
    path = '../DataSets/'
    data = 'application_data.csv'
    
    transform_parquet(path, data)