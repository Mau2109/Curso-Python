import csv  # Importamos la librería estándar csv para trabajar con archivos CSV en Python

def leer_csv_con_csv(ruta_archivo):
    """
    Lee un archivo CSV con datos de sensores y devuelve una lista de diccionarios.

    Parámetros:
    ruta_archivo (str): Ruta completa del archivo CSV a leer.

    Retorna:
    list: Lista de diccionarios, donde cada diccionario representa una fila del CSV
          con las claves 'AppTimestamp', 'GyroX', 'GyroY', 'GyroZ' y 'Estado'.
    """
    
    datos = []  # Lista vacía para almacenar cada fila del CSV como un diccionario
    
    # Abrimos el archivo en modo lectura ('r') con codificación UTF-8
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        
        # Creamos un lector CSV que interpreta cada fila como un diccionario.
        # 'delimiter' se establece en coma (',') porque el archivo está separado por comas.
        lector = csv.DictReader(archivo, delimiter=',')
        
        # Iteramos sobre cada fila del archivo
        for fila in lector:
            # Convertimos las columnas numéricas de texto a float (valores decimales)
            fila['GyroX'] = float(fila['GyroX'])
            fila['GyroY'] = float(fila['GyroY'])
            fila['GyroZ'] = float(fila['GyroZ'])
            
            # Convertimos la columna 'Estado' a entero
            fila['Estado'] = int(fila['Estado'])
            
            # Agregamos el diccionario procesado a la lista de datos
            datos.append(fila)
    
    # Mostramos las primeras 5 filas como vista previa
    print("Vista previa de los datos:")
    for fila in datos[:5]:  # [:5] significa "solo mostrar las primeras 5 filas"
        print(fila)

    return datos  # Retornamos la lista de diccionarios


# Uso del script
ruta = "/home/mauricio/Documentos/python/Curso-Python/modulo5/giro_20250725_105331_1.csv_1753462419.csv"
datos = leer_csv_con_csv(ruta)  # Llamamos a la función y guardamos el resultado
