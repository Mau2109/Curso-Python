import pandas as pd

def leer_csv(ruta_archivo):
    """
    Lee un archivo CSV con datos de sensores y devuelve un DataFrame de pandas.

    Parámetros:
    ruta_archivo (str): La ruta del archivo CSV que se quiere leer.

    Retorna:
    pd.DataFrame: Un DataFrame con las columnas 'AppTimestamp', 'GyroX', 'GyroY', 'GyroZ' y 'Estado'.
    """
    # Leer el archivo CSV con separador de tabulación (\t)
    df = pd.read_csv(ruta_archivo, sep='\t')

    # Mostrar las primeras filas para verificar la lectura correcta
    print("Vista previa de los datos:")
    print(df.head())

    return df

ruta = "/home/mauricio/Documentos/python/Curso-Python/modulo5/giro_20250725_105331_1.csv_1753462419.csv"  # Cambia por la ruta real del archivo
datos = leer_csv(ruta)
