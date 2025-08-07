
📁 Módulo 5: Manejo de Errores y Archivos

    Excepciones básicas y manejo de archivos en Python

    En este módulo aprenderás cómo controlar errores en tus programas y cómo trabajar con archivos de texto para lectura y escritura.

📖 Tabla de Contenidos

    🚨 Manejo de Excepciones

    🗃️ Lectura y Escritura de Archivos

    💻 Ejercicios Prácticos

    📝 Conceptos Clave

    ⚠️ Errores Comunes

    ✅ Buenas Prácticas

🚨 Manejo de Excepciones

Las excepciones permiten manejar errores sin que el programa se detenga de forma abrupta.
Sintaxis básica

try:
    # Código que puede fallar
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que se ejecuta si hay error
    print("No se puede dividir entre cero.")
finally:
    # Siempre se ejecuta
    print("Operación finalizada.")

Tipos comunes de excepciones

    ZeroDivisionError: División entre cero

    ValueError: Conversión inválida de tipo

    FileNotFoundError: Archivo no encontrado

    TypeError: Tipo de dato incorrecto

Captura de múltiples excepciones

try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
except ValueError:
    print("Debes ingresar un número válido.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")

🗃️ Lectura y Escritura de Archivos

Python permite abrir, leer, escribir y cerrar archivos fácilmente.
Abrir un archivo

archivo = open("datos.txt", "r")  # 'r' para lectura
contenido = archivo.read()
archivo.close()
print(contenido)

Usar with para manejo automático

with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)  # No es necesario cerrar manualmente

Modos de apertura
Modo	Descripción
'r'	Leer (error si no existe)
'w'	Escribir (sobrescribe)
'a'	Agregar al final
'x'	Crear nuevo archivo
Escribir en un archivo

with open("salida.txt", "w") as archivo:
    archivo.write("Hola mundo\n")
    archivo.write("Nueva línea de texto")

Leer línea por línea

with open("datos.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())  # Elimina saltos de línea

💻 Ejercicios Prácticos
Ejercicio 1: División segura

Nivel: 🟢 Principiante

Solicita un número al usuario y divídelo entre 10. Maneja los posibles errores.
<details> <summary>👁️ Ver solución</summary>

try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except ValueError:
    print("Error: debes ingresar un número entero.")
except ZeroDivisionError:
    print("Error: no puedes dividir entre cero.")

</details>
Ejercicio 2: Crear y leer archivo

Nivel: 🟢 Principiante

Crea un archivo llamado info.txt, escribe tu nombre y luego léelo.
<details> <summary>👁️ Ver solución</summary>

# Escribir
with open("info.txt", "w") as archivo:
    archivo.write("Mi nombre es Python\nEstoy aprendiendo a programar.")

# Leer
with open("info.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

</details>
Ejercicio 3: Registro de errores

Nivel: 🟡 Intermedio

Pide al usuario 3 números y guarda los errores en un archivo errores.log.
<details> <summary>👁️ Ver solución</summary>

for i in range(3):
    try:
        numero = int(input("Número: "))
        print("10 /", numero, "=", 10 / numero)
    except Exception as e:
        with open("errores.log", "a") as log:
            log.write(f"Error en intento {i+1}: {str(e)}\n")
        print("Se ha registrado un error.")

</details>
Ejercicio 4: Contar líneas de archivo

Nivel: 🟡 Intermedio

Lee un archivo y muestra cuántas líneas tiene.
<details> <summary>👁️ Ver solución</summary>

try:
    with open("datos.txt", "r") as archivo:
        lineas = archivo.readlines()
        print(f"El archivo tiene {len(lineas)} líneas.")
except FileNotFoundError:
    print("El archivo no existe.")

</details>
📝 Conceptos Clave para Recordar
Concepto	Descripción	Ejemplo
try-except	Bloques para manejar errores	try: ... except: ...
finally	Se ejecuta siempre	finally: cerrar archivo
open()	Abrir un archivo	open("archivo.txt", "r")
with	Manejo automático de archivos	with open(...) as f:
.read()	Lee todo el contenido	contenido = f.read()
.write()	Escribe texto	f.write("Hola")
.readlines()	Lista de líneas	lineas = f.readlines()
⚠️ Errores Comunes
Error	Descripción	Solución
FileNotFoundError	Archivo no encontrado	Verifica la ruta y el nombre
PermissionError	Permiso denegado	Evita abrir archivos protegidos
ValueError	Conversión inválida	Validar entrada antes de convertir
ZeroDivisionError	División por cero	Verifica que el divisor no sea cero
✅ Buenas Prácticas

    Usar with: evita olvidarse de cerrar archivos

    Capturar excepciones específicas: mejora la claridad del código

    Validar entradas del usuario

    Guardar logs de errores: útil para debugging

    Evitar sobrescribir archivos sin confirmación

    Usar strip() al leer líneas: elimina espacios y saltos de línea
