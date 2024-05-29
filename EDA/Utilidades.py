import pandas as pd

def porcentaje_valores_nulos(dataframe):
    '''
    Función que recibe como parametro un DataFrame
    y retorna el porcentaje de valores nulos por columna.

    '''
    total_filas = dataframe.shape[0]
    porcentaje_nulos = (dataframe.isnull().sum() / total_filas) * 100
    
    for columna, porcentaje in porcentaje_nulos.items():
        print(f'La columna {columna} tiene un {porcentaje: .2f} % de valores nulos')

def registros_duplicados(df):
    '''
    Función que recibe como parametro un DataFrame
    y retorna un DataFrame con los registros duplicados.
    
    '''
    df = df[df.duplicated(keep=False)]
    return df