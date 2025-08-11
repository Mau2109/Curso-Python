# 📚 Módulo 5: Manejo de Errores y Archivos

> **Excepciones básicas y manejo de archivos en Python**

En este módulo aprenderás cómo controlar errores en tus programas y cómo trabajar con archivos de texto y CSV para lectura y escritura.

## 📖 Tabla de Contenidos

- [Manejo de Excepciones](#-manejo-de-excepciones)
- [Lectura y Escritura de Archivos](#️-lectura-y-escritura-de-archivos)
- [Manejo de Archivos CSV](#-manejo-de-archivos-csv)
- [Ejercicios Prácticos](#-ejercicios-prácticos)
- [Conceptos Clave](#-conceptos-clave)
- [Errores Comunes](#-errores-comunes)
- [Buenas Prácticas](#-buenas-prácticas)

---

## Manejo de Excepciones

Las excepciones permiten manejar errores sin que el programa se detenga de forma abrupta.

### Sintaxis básica

```python
try:
    # Código que puede fallar
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que se ejecuta si hay error
    print("No se puede dividir entre cero.")
finally:
    # Siempre se ejecuta
    print("Operación finalizada.")
```

### Tipos comunes de excepciones

| Excepción | Descripción |
|-----------|-------------|
| `ZeroDivisionError` | División entre cero |
| `ValueError` | Conversión inválida de tipo |
| `FileNotFoundError` | Archivo no encontrado |
| `TypeError` | Tipo de dato incorrecto |
| `IndexError` | Índice fuera de rango |
| `KeyError` | Clave no encontrada en diccionario |

### Captura de múltiples excepciones

```python
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Debes ingresar un número válido.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
except Exception as e:
    print(f"Error inesperado: {e}")
```

---

## Lectura y Escritura de Archivos

Python permite abrir, leer, escribir y cerrar archivos fácilmente.

### Abrir un archivo (método tradicional)

```python
archivo = open("datos.txt", "r")  # 'r' para lectura
contenido = archivo.read()
archivo.close()
print(contenido)
```

### Usar `with` para manejo automático (recomendado)

```python
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)  # No es necesario cerrar manualmente
```

### Modos de apertura

| Modo | Descripción |
|------|-------------|
| `'r'` | Leer (error si no existe) |
| `'w'` | Escribir (sobrescribe el archivo) |
| `'a'` | Agregar al final |
| `'x'` | Crear nuevo archivo (error si existe) |
| `'r+'` | Leer y escribir |
| `'rb'` | Leer en modo binario |
| `'wb'` | Escribir en modo binario |

### Escribir en un archivo

```python
with open("salida.txt", "w") as archivo:
    archivo.write("Hola mundo\n")
    archivo.write("Nueva línea de texto")
```

### Leer línea por línea

```python
with open("datos.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())  # Elimina saltos de línea
```

### Métodos útiles para archivos

```python
# Leer todo el contenido
contenido = archivo.read()

# Leer una línea
linea = archivo.readline()

# Leer todas las líneas en una lista
lineas = archivo.readlines()

# Escribir múltiples líneas
lineas = ["Línea 1\n", "Línea 2\n", "Línea 3\n"]
archivo.writelines(lineas)
```

---

## Manejo de Archivos CSV

Los archivos CSV (Comma Separated Values) son muy comunes para almacenar datos tabulares.

### Usando el módulo `csv`

```python
import csv

# Leer archivo CSV
with open("datos.csv", "r") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)  # fila es una lista
```

### Leer CSV con encabezados

```python
import csv

with open("empleados.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(f"Nombre: {fila['nombre']}, Edad: {fila['edad']}")
```

### Escribir archivo CSV

```python
import csv

datos = [
    ["Nombre", "Edad", "Ciudad"],
    ["Ana", 25, "Madrid"],
    ["Luis", 30, "Barcelona"],
    ["María", 28, "Valencia"]
]

with open("personas.csv", "w", newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)
```

### Escribir CSV con diccionarios

```python
import csv

empleados = [
    {"nombre": "Ana", "edad": 25, "salario": 50000},
    {"nombre": "Luis", "edad": 30, "salario": 60000},
    {"nombre": "María", "edad": 28, "salario": 55000}
]

with open("empleados.csv", "w", newline='') as archivo:
    campos = ["nombre", "edad", "salario"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    
    escritor.writeheader()  # Escribir encabezados
    escritor.writerows(empleados)
```

### CSV con diferentes delimitadores

```python
import csv

# Leer CSV con punto y coma como delimitador
with open("datos.csv", "r") as archivo:
    lector = csv.reader(archivo, delimiter=';')
    for fila in lector:
        print(fila)

# Escribir CSV con tabulación como delimitador
with open("datos.tsv", "w", newline='') as archivo:
    escritor = csv.writer(archivo, delimiter='\t')
    escritor.writerow(["Columna1", "Columna2", "Columna3"])
```

---

### Leer csv con Pandas(libreria)
```python
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
```
### Lectura CSV datos sensores

```Python

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

```




## Ejercicios Prácticos

### Ejercicio 1: División segura
**Nivel:** Principiante

Solicita un número al usuario y divídelo entre 10. Maneja los posibles errores.

<details>
<summary>👁️ Ver solución</summary>

```python
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Error: debes ingresar un número entero.")
except ZeroDivisionError:
    print("Error: no puedes dividir entre cero.")
```

</details>

### Ejercicio 2: Crear y leer archivo
**Nivel:** Principiante

Crea un archivo llamado `info.txt`, escribe tu nombre y luego léelo.

<details>
<summary>👁️ Ver solución</summary>

```python
# Escribir
with open("info.txt", "w") as archivo:
    archivo.write("Mi nombre es Python\nEstoy aprendiendo a programar.")

# Leer
with open("info.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
```

</details>

### Ejercicio 3: Registro de errores
**Nivel:** Intermedio

Pide al usuario 3 números y guarda los errores en un archivo `errores.log`.

<details>
<summary>👁️ Ver solución</summary>

```python
for i in range(3):
    try:
        numero = int(input(f"Número {i+1}: "))
        resultado = 10 / numero
        print(f"10 / {numero} = {resultado}")
    except Exception as e:
        with open("errores.log", "a") as log:
            log.write(f"Error en intento {i+1}: {str(e)}\n")
        print("Se ha registrado un error.")
```

</details>

### Ejercicio 4: Contar líneas de archivo
**Nivel:** Intermedio

Lee un archivo y muestra cuántas líneas tiene.

<details>
<summary>👁️ Ver solución</summary>

```python
try:
    with open("datos.txt", "r") as archivo:
        lineas = archivo.readlines()
        print(f"El archivo tiene {len(lineas)} líneas.")
except FileNotFoundError:
    print("El archivo no existe.")
```

</details>

### Ejercicio 5: Procesar archivo CSV
**Nivel:** Intermedio

Crea un archivo CSV con información de estudiantes y luego léelo para calcular la nota promedio.

<details>
<summary>👁️ Ver solución</summary>

```python
import csv

# Crear archivo CSV
estudiantes = [
    ["Nombre", "Nota1", "Nota2", "Nota3"],
    ["Ana", 85, 90, 88],
    ["Luis", 76, 82, 79],
    ["María", 92, 95, 93]
]

with open("estudiantes.csv", "w", newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(estudiantes)

# Leer y procesar
with open("estudiantes.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        notas = [int(fila["Nota1"]), int(fila["Nota2"]), int(fila["Nota3"])]
        promedio = sum(notas) / len(notas)
        print(f"{fila['Nombre']}: Promedio = {promedio:.2f}")
```

</details>

### Ejercicio 6: Sistema de inventario CSV
**Nivel:** Avanzado

Crea un sistema que permita agregar, leer y actualizar productos en un inventario usando CSV.

<details>
<summary>👁️ Ver solución</summary>

```python
import csv
import os

def crear_inventario():
    if not os.path.exists("inventario.csv"):
        with open("inventario.csv", "w", newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["ID", "Producto", "Cantidad", "Precio"])

def agregar_producto():
    try:
        id_producto = input("ID del producto: ")
        nombre = input("Nombre del producto: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
        
        with open("inventario.csv", "a", newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([id_producto, nombre, cantidad, precio])
        
        print("Producto agregado exitosamente.")
    except ValueError:
        print("Error: Cantidad y precio deben ser números.")

def mostrar_inventario():
    try:
        with open("inventario.csv", "r") as archivo:
            lector = csv.DictReader(archivo)
            print("\n--- INVENTARIO ---")
            for fila in lector:
                print(f"ID: {fila['ID']}, Producto: {fila['Producto']}, "
                      f"Cantidad: {fila['Cantidad']}, Precio: ${fila['Precio']}")
    except FileNotFoundError:
        print("No existe el archivo de inventario.")

# Uso del sistema
crear_inventario()
while True:
    print("\n1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        break
    else:
        print("Opción inválida.")
```

</details>

---

## 📝 Conceptos Clave

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| `try-except` | Bloques para manejar errores | `try: ... except: ...` |
| `finally` | Se ejecuta siempre | `finally: cerrar archivo` |
| `open()` | Abrir un archivo | `open("archivo.txt", "r")` |
| `with` | Manejo automático de archivos | `with open(...) as f:` |
| `.read()` | Lee todo el contenido | `contenido = f.read()` |
| `.write()` | Escribe texto | `f.write("Hola")` |
| `.readlines()` | Lista de líneas | `lineas = f.readlines()` |
| `csv.reader()` | Leer archivos CSV | `csv.reader(archivo)` |
| `csv.writer()` | Escribir archivos CSV | `csv.writer(archivo)` |
| `csv.DictReader()` | Leer CSV como diccionarios | `csv.DictReader(archivo)` |

---

## ⚠️ Errores Comunes

| Error | Descripción | Solución |
|-------|-------------|----------|
| `FileNotFoundError` | Archivo no encontrado | Verifica la ruta y el nombre del archivo |
| `PermissionError` | Permiso denegado | Evita abrir archivos protegidos o en uso |
| `ValueError` | Conversión inválida | Validar entrada antes de convertir |
| `ZeroDivisionError` | División por cero | Verifica que el divisor no sea cero |
| `UnicodeDecodeError` | Error de codificación | Especifica la codificación correcta |
| `csv.Error` | Error en formato CSV | Verifica delimitadores y formato |

---

## ✅ Buenas Prácticas

### Manejo de Archivos
- **Usar `with`**: Evita olvidarse de cerrar archivos
- **Especificar codificación**: `open("archivo.txt", "r", encoding="utf-8")`
- **Manejar excepciones**: Siempre captura `FileNotFoundError`
- **Usar rutas absolutas**: Cuando sea necesario para evitar confusión

### Manejo de Excepciones
- **Capturar excepciones específicas**: Mejora la claridad del código
- **Validar entradas del usuario**: Antes de procesarlas
- **Guardar logs de errores**: Útil para debugging
- **No silenciar errores**: A menos que sea intencionalmente

### Archivos CSV
- **Usar `newline=''`**: Al escribir CSV en Windows
- **Especificar delimitadores**: Cuando no sea coma
- **Usar `DictReader/DictWriter`**: Para mejor legibilidad
- **Manejar encabezados**: Consistentemente

### Gestión de Datos
- **Hacer copias de seguridad**: Antes de modificar archivos importantes
- **Validar datos**: Antes de escribir en archivos
- **Usar nombres descriptivos**: Para archivos y variables
- **Documentar formato de datos**: En archivos CSV complejos

---

## Recursos Adicionales

- [Documentación oficial de Python - Manejo de errores](https://docs.python.org/es/3/tutorial/errors.html)
- [Documentación del módulo csv](https://docs.python.org/es/3/library/csv.html)
- [Guía de mejores prácticas para archivos en Python](https://realpython.com/python-file-handling/)

---

[Siguiente módulo](../modulo6/README.md)