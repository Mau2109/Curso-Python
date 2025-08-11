
# 📚 Módulo 3: Estructuras de Datos

> **Listas, Tuplas y Diccionarios en Python**
> 
> En este módulo aprenderás a organizar y manipular colecciones de datos de manera eficiente usando las estructuras fundamentales de Python.

## 📖 Tabla de Contenidos

1. [Listas (Lists)](#-listas-lists)
2. [Tuplas (Tuples)](#-tuplas-tuples)
3. [Diccionarios (Dictionaries)](#-diccionarios-dictionaries)
4. [Iteración sobre Estructuras](#-iteración-sobre-estructuras)
5. [Ejercicios Prácticos](#-ejercicios-prácticos)
6. [Conceptos Clave](#-conceptos-clave-para-recordar)
7. [Errores Comunes](#️-errores-comunes)

---

## Listas (Lists)

Las listas son colecciones **ordenadas** y **modificables** de elementos. Pueden contener diferentes tipos de datos.

### Creación de listas

```python
# Lista vacía
lista_vacia = []
lista_vacia2 = list()

# Lista con elementos
numeros = [1, 2, 3, 4, 5]
nombres = ["Ana", "Luis", "María", "Carlos"]
mixta = [1, "Hola", 3.14, True, [1, 2, 3]]

print(numeros)  # [1, 2, 3, 4, 5]
print(len(nombres))  # 4 (longitud de la lista)
```

### Acceso a elementos

```python
frutas = ["manzana", "banana", "naranja", "uva"]

# Índices positivos (desde el inicio)
print(frutas[0])   # manzana (primer elemento)
print(frutas[1])   # banana
print(frutas[3])   # uva (último elemento)

# Índices negativos (desde el final)
print(frutas[-1])  # uva (último elemento)
print(frutas[-2])  # naranja (penúltimo elemento)

# Slicing (cortes de lista)
print(frutas[1:3])   # ['banana', 'naranja'] (desde índice 1 hasta 2)
print(frutas[:2])    # ['manzana', 'banana'] (desde inicio hasta índice 1)
print(frutas[2:])    # ['naranja', 'uva'] (desde índice 2 hasta el final)
print(frutas[::2])   # ['manzana', 'naranja'] (cada 2 elementos)
print(frutas[::-1])  # ['uva', 'naranja', 'banana', 'manzana'] (reversa)
```

### Métodos de listas

```python
colores = ["rojo", "verde", "azul"]

# Agregar elementos
colores.append("amarillo")        # Agrega al final
print(colores)  # ['rojo', 'verde', 'azul', 'amarillo']

colores.insert(1, "rosa")         # Inserta en posición específica
print(colores)  # ['rojo', 'rosa', 'verde', 'azul', 'amarillo']

# Remover elementos
colores.remove("rosa")            # Remueve primera ocurrencia
print(colores)  # ['rojo', 'verde', 'azul', 'amarillo']

ultimo = colores.pop()            # Remueve y retorna último elemento
print(ultimo)   # amarillo
print(colores)  # ['rojo', 'verde', 'azul']

segundo = colores.pop(1)          # Remueve elemento en índice específico
print(segundo)  # verde
print(colores)  # ['rojo', 'azul']

# Otros métodos útiles
numeros = [3, 1, 4, 1, 5, 9, 2]
print(numeros.count(1))           # 2 (cuenta ocurrencias)
print(numeros.index(4))           # 2 (encuentra índice del elemento)

numeros.sort()                    # Ordena la lista
print(numeros)  # [1, 1, 2, 3, 4, 5, 9]

numeros.reverse()                 # Invierte la lista
print(numeros)  # [9, 5, 4, 3, 2, 1, 1]

copia = numeros.copy()            # Crea una copia de la lista
numeros.clear()                   # Vacía la lista
print(numeros)  # []
print(copia)    # [9, 5, 4, 3, 2, 1, 1]
```

### List comprehensions (comprensiones de lista)

```python
# Forma tradicional
cuadrados = []
for i in range(1, 6):
    cuadrados.append(i ** 2)
print(cuadrados)  # [1, 4, 9, 16, 25]

# List comprehension (más pythónico)
cuadrados = [i ** 2 for i in range(1, 6)]
print(cuadrados)  # [1, 4, 9, 16, 25]

# Con condición
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]

# Procesamiento de strings
palabras = ["Python", "Java", "JavaScript", "C++"]
mayusculas = [palabra.upper() for palabra in palabras]
print(mayusculas)  # ['PYTHON', 'JAVA', 'JAVASCRIPT', 'C++']
```

---

## Tuplas (Tuples)

Las tuplas son colecciones **ordenadas** pero **inmutables** (no se pueden modificar después de crearlas).

### Creación de tuplas

```python
# Tupla vacía
tupla_vacia = ()
tupla_vacia2 = tuple()

# Tupla con elementos
coordenadas = (3, 5)
colores = ("rojo", "verde", "azul")
mixta = (1, "Hola", 3.14, True)

# Tupla de un elemento (nota la coma)
un_elemento = (42,)
print(type(un_elemento))  # <class 'tuple'>

# Sin paréntesis también funciona
punto = 10, 20
print(type(punto))  # <class 'tuple'>
```

### Acceso a elementos

```python
persona = ("Juan", "Pérez", 30, "Ingeniero")

# Acceso por índice (igual que las listas)
print(persona[0])   # Juan
print(persona[-1])  # Ingeniero

# Slicing
print(persona[1:3])  # ('Pérez', 30)

# Desempaquetado de tuplas
nombre, apellido, edad, profesion = persona
print(f"{nombre} {apellido}, {edad} años, {profesion}")

# Desempaquetado parcial
nombre, *resto = persona
print(nombre)  # Juan
print(resto)   # ['Pérez', 30, 'Ingeniero']
```

### Métodos de tuplas

```python
numeros = (1, 2, 3, 2, 4, 2, 5)

# Solo tiene dos métodos
print(numeros.count(2))   # 3 (cuenta ocurrencias)
print(numeros.index(4))   # 4 (encuentra índice)

# Conversión entre listas y tuplas
lista = [1, 2, 3]
tupla = tuple(lista)      # Lista a tupla
nueva_lista = list(tupla) # Tupla a lista
```

### Cuándo usar tuplas

```python
# Para coordenadas
punto = (10, 20)
rectangulo = ((0, 0), (100, 50))  # esquina superior izq y inferior der

# Para datos que no cambian
fecha = (2024, 12, 25)  # año, mes, día
rgb = (255, 128, 0)     # valores de color

# Como claves de diccionario (las listas no se pueden usar)
ubicaciones = {
    (0, 0): "origen",
    (10, 20): "punto A",
    (30, 40): "punto B"
}
```

---

## Diccionarios (Dictionaries)

Los diccionarios son colecciones **no ordenadas** de pares **clave-valor**. Son muy eficientes para búsquedas.

### Creación de diccionarios

```python
# Diccionario vacío
dict_vacio = {}
dict_vacio2 = dict()

# Diccionario con datos
estudiante = {
    "nombre": "María",
    "edad": 22,
    "carrera": "Informática",
    "activo": True
}

# Usando dict()
persona = dict(nombre="Juan", edad=30, ciudad="Madrid")

# Desde lista de tuplas
pares = [("a", 1), ("b", 2), ("c", 3)]
dict_desde_pares = dict(pares)
print(dict_desde_pares)  # {'a': 1, 'b': 2, 'c': 3}
```

### Acceso y modificación

```python
producto = {
    "nombre": "Laptop",
    "precio": 999.99,
    "marca": "TechBrand",
    "disponible": True
}

# Acceso a valores
print(producto["nombre"])        # Laptop
print(producto.get("precio"))    # 999.99
print(producto.get("color", "No especificado"))  # No especificado (valor por defecto)

# Modificar valores
producto["precio"] = 899.99
producto["color"] = "Negro"      # Agrega nueva clave-valor

# Eliminar elementos
del producto["disponible"]       # Elimina clave y valor
descuento = producto.pop("precio", 0)  # Remueve y retorna valor
print(descuento)  # 899.99

print(producto)  # {'nombre': 'Laptop', 'marca': 'TechBrand', 'color': 'Negro'}
```

### Métodos de diccionarios

```python
contactos = {
    "Ana": "123-456-7890",
    "Luis": "098-765-4321",
    "María": "555-123-4567"
}

# Obtener claves, valores y pares
print(contactos.keys())    # dict_keys(['Ana', 'Luis', 'María'])
print(contactos.values())  # dict_values(['123-456-7890', '098-765-4321', '555-123-4567'])
print(contactos.items())   # dict_items([('Ana', '123-456-7890'), ('Luis', '098-765-4321'), ('María', '555-123-4567')])

# Actualizar diccionario
nuevos_contactos = {"Carlos": "777-888-9999", "Ana": "111-222-3333"}
contactos.update(nuevos_contactos)
print(contactos)  # Ana se actualiza, Carlos se agrega

# Limpiar diccionario
copia = contactos.copy()
contactos.clear()
print(contactos)  # {}
print(copia)      # Mantiene los datos
```

### Dictionary comprehensions

```python
# Crear diccionario de cuadrados
cuadrados = {x: x**2 for x in range(1, 6)}
print(cuadrados)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filtrar diccionario
numeros = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
pares = {k: v for k, v in numeros.items() if v % 2 == 0}
print(pares)  # {'b': 2, 'd': 4}

# Procesar strings
palabras = ["python", "java", "javascript"]
longitudes = {palabra: len(palabra) for palabra in palabras}
print(longitudes)  # {'python': 6, 'java': 4, 'javascript': 10}
```

---

## Iteración sobre Estructuras

### Iteración sobre listas

```python
frutas = ["manzana", "banana", "naranja"]

# Método básico
for fruta in frutas:
    print(fruta)

# Con índice
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")

# Solo índices
for i in range(len(frutas)):
    print(f"Índice {i}: {frutas[i]}")
```

### Iteración sobre tuplas

```python
coordenadas = [(0, 0), (1, 2), (3, 4)]

for x, y in coordenadas:
    print(f"Punto: ({x}, {y})")
    
# Con enumerate
for i, (x, y) in enumerate(coordenadas):
    print(f"Punto {i+1}: ({x}, {y})")
```

### Iteración sobre diccionarios

```python
estudiante = {"nombre": "Ana", "edad": 22, "carrera": "CS"}

# Solo claves
for clave in estudiante:
    print(clave)

# Solo valores
for valor in estudiante.values():
    print(valor)

# Claves y valores
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")
```

---

## Ejercicios Prácticos

### Ejercicio 1: Gestión de Calificaciones
**Nivel:** Principiante

Crea un programa que maneje las calificaciones de un estudiante.

<details>
<summary>👁️ Ver solución</summary>

```python
# Lista de calificaciones
calificaciones = []

print("=== GESTIÓN DE CALIFICACIONES ===")

# Agregar calificaciones
while True:
    entrada = input("Ingresa una calificación (o 'fin' para terminar): ")
    if entrada.lower() == 'fin':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            calificaciones.append(nota)
        else:
            print("La nota debe estar entre 0 y 10")
    except ValueError:
        print("Por favor, ingresa un número válido")

if calificaciones:
    # Estadísticas
    print(f"\n--- ESTADÍSTICAS ---")
    print(f"Calificaciones: {calificaciones}")
    print(f"Número de calificaciones: {len(calificaciones)}")
    print(f"Nota más alta: {max(calificaciones)}")
    print(f"Nota más baja: {min(calificaciones)}")
    print(f"Promedio: {sum(calificaciones) / len(calificaciones):.2f}")
    
    # Clasificar notas
    aprobadas = [nota for nota in calificaciones if nota >= 5]
    reprobadas = [nota for nota in calificaciones if nota < 5]
    
    print(f"Aprobadas ({len(aprobadas)}): {aprobadas}")
    print(f"Reprobadas ({len(reprobadas)}): {reprobadas}")
else:
    print("No se ingresaron calificaciones")
```
</details>

### Ejercicio 2: Agenda de Contactos
**Nivel:** Intermedio

Crea una agenda de contactos usando diccionarios.

<details>
<summary>👁️ Ver solución</summary>

```python
agenda = {}

def mostrar_menu():
    print("\n=== AGENDA DE CONTACTOS ===")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Listar todos")
    print("6. Salir")

def agregar_contacto():
    nombre = input("Nombre: ").strip().title()
    if nombre in agenda:
        print("El contacto ya existe")
        return
    
    telefono = input("Teléfono: ").strip()
    email = input("Email: ").strip().lower()
    
    agenda[nombre] = {
        "telefono": telefono,
        "email": email
    }
    print(f"Contacto {nombre} agregado exitosamente")

def buscar_contacto():
    nombre = input("Nombre a buscar: ").strip().title()
    if nombre in agenda:
        contacto = agenda[nombre]
        print(f"\n--- CONTACTO ENCONTRADO ---")
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {contacto['telefono']}")
        print(f"Email: {contacto['email']}")
    else:
        print("Contacto no encontrado")

def listar_contactos():
    if not agenda:
        print("No hay contactos en la agenda")
        return
    
    print(f"\n--- TODOS LOS CONTACTOS ({len(agenda)}) ---")
    for nombre, datos in sorted(agenda.items()):
        print(f"{nombre}: {datos['telefono']} - {datos['email']}")

def eliminar_contacto():
    nombre = input("Nombre a eliminar: ").strip().title()
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado")
    else:
        print("Contacto no encontrado")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ").strip()
    
    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        buscar_contacto()  # Mostrar actual
        agregar_contacto()  # Permitir "sobrescribir"
    elif opcion == "4":
        eliminar_contacto()
    elif opcion == "5":
        listar_contactos()
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida")
```
</details>

### Ejercicio 3: Análisis de Texto
**Nivel:** Intermedio

Analiza un texto y cuenta frecuencia de palabras.

<details>
<summary>👁️ Ver solución</summary>

```python
def analizar_texto(texto):
    # Limpiar y procesar texto
    texto = texto.lower()
    # Remover puntuación básica
    for char in ".,!?;:":
        texto = texto.replace(char, "")
    
    palabras = texto.split()
    
    # Contar frecuencias
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    
    return palabras, frecuencias

def mostrar_estadisticas(palabras, frecuencias):
    print(f"\n--- ESTADÍSTICAS DEL TEXTO ---")
    print(f"Total de palabras: {len(palabras)}")
    print(f"Palabras únicas: {len(frecuencias)}")
    
    # Palabra más común
    palabra_mas_comun = max(frecuencias, key=frecuencias.get)
    print(f"Palabra más común: '{palabra_mas_comun}' ({frecuencias[palabra_mas_comun]} veces)")
    
    # Top 5 palabras más frecuentes
    top_palabras = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:5]
    print(f"\nTop 5 palabras más frecuentes:")
    for i, (palabra, freq) in enumerate(top_palabras, 1):
        print(f"{i}. {palabra}: {freq} veces")
    
    # Palabras que aparecen solo una vez
    palabras_unicas = [palabra for palabra, freq in frecuencias.items() if freq == 1]
    print(f"\nPalabras que aparecen solo una vez: {len(palabras_unicas)}")
    if len(palabras_unicas) <= 10:  # Mostrar solo si son pocas
        print(f"Ejemplos: {', '.join(palabras_unicas)}")

# Programa principal
print("=== ANALIZADOR DE TEXTO ===")
texto = input("Ingresa el texto a analizar: ")

if texto.strip():
    palabras, frecuencias = analizar_texto(texto)
    mostrar_estadisticas(palabras, frecuencias)
    
    # Buscar palabra específica
    while True:
        buscar = input("\n¿Buscar frecuencia de alguna palabra? (Enter para salir): ").strip().lower()
        if not buscar:
            break
        if buscar in frecuencias:
            print(f"La palabra '{buscar}' aparece {frecuencias[buscar]} veces")
        else:
            print(f"La palabra '{buscar}' no se encontró en el texto")
else:
    print("No se ingresó ningún texto")
```
</details>

### Ejercicio 4: Sistema de Inventario
**Nivel:** Intermedio-Avanzado

Sistema para gestionar inventario de productos.

<details>
<summary>👁️ Ver solución</summary>

```python
inventario = {}

def mostrar_menu():
    print("\n=== SISTEMA DE INVENTARIO ===")
    print("1. Agregar producto")
    print("2. Actualizar stock")
    print("3. Buscar producto")
    print("4. Productos con stock bajo")
    print("5. Reporte completo")
    print("6. Eliminar producto")
    print("7. Salir")

def agregar_producto():
    codigo = input("Código del producto: ").upper().strip()
    
    if codigo in inventario:
        print("El producto ya existe")
        return
    
    nombre = input("Nombre: ").title().strip()
    try:
        precio = float(input("Precio: $"))
        stock = int(input("Stock inicial: "))
        stock_minimo = int(input("Stock mínimo: "))
        
        inventario[codigo] = {
            "nombre": nombre,
            "precio": precio,
            "stock": stock,
            "stock_minimo": stock_minimo
        }
        print(f"Producto {nombre} agregado exitosamente")
    except ValueError:
        print("Error: Precio debe ser número decimal, stock debe ser entero")

def actualizar_stock():
    codigo = input("Código del producto: ").upper().strip()
    
    if codigo not in inventario:
        print("Producto no encontrado")
        return
    
    producto = inventario[codigo]
    print(f"Producto: {producto['nombre']}")
    print(f"Stock actual: {producto['stock']}")
    
    try:
        cambio = int(input("Cambio en stock (+/-): "))
        nuevo_stock = producto['stock'] + cambio
        
        if nuevo_stock < 0:
            print("Error: El stock no puede ser negativo")
            return
        
        producto['stock'] = nuevo_stock
        print(f"Stock actualizado: {nuevo_stock}")
        
        if nuevo_stock <= producto['stock_minimo']:
            print(" ALERTA: Stock por debajo del mínimo!")
            
    except ValueError:
        print("Error: Ingresa un número entero")

def buscar_producto():
    codigo = input("Código del producto: ").upper().strip()
    
    if codigo in inventario:
        p = inventario[codigo]
        print(f"\n--- INFORMACIÓN DEL PRODUCTO ---")
        print(f"Código: {codigo}")
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']:.2f}")
        print(f"Stock: {p['stock']}")
        print(f"Stock mínimo: {p['stock_minimo']}")
        print(f"Estado: {'STOCK BAJO' if p['stock'] <= p['stock_minimo'] else '🟢 STOCK OK'}")
    else:
        print("Producto no encontrado")

def productos_stock_bajo():
    productos_bajos = [(codigo, datos) for codigo, datos in inventario.items() 
                      if datos['stock'] <= datos['stock_minimo']]
    
    if productos_bajos:
        print(f"\n--- PRODUCTOS CON STOCK BAJO ({len(productos_bajos)}) ---")
        for codigo, datos in productos_bajos:
            print(f"{codigo}: {datos['nombre']} - Stock: {datos['stock']} (Mín: {datos['stock_minimo']})")
    else:
        print("Todos los productos tienen stock suficiente")

def reporte_completo():
    if not inventario:
        print("No hay productos en el inventario")
        return
    
    print(f"\n--- REPORTE COMPLETO ({len(inventario)} productos) ---")
    
    total_productos = len(inventario)
    valor_total = sum(p['precio'] * p['stock'] for p in inventario.values())
    stock_bajo = sum(1 for p in inventario.values() if p['stock'] <= p['stock_minimo'])
    
    print(f"Total productos: {total_productos}")
    print(f"Valor total inventario: ${valor_total:.2f}")
    print(f"Productos con stock bajo: {stock_bajo}")
    
    print("\nDetalle por producto:")
    for codigo, datos in sorted(inventario.items()):
        estado = " BAJO" if datos['stock'] <= datos['stock_minimo'] else "🟢 OK"
        valor = datos['precio'] * datos['stock']
        print(f"{codigo}: {datos['nombre']} | Stock: {datos['stock']} | Valor: ${valor:.2f} | {estado}")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ").strip()
    
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        actualizar_stock()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        productos_stock_bajo()
    elif opcion == "5":
        reporte_completo()
    elif opcion == "6":
        codigo = input("Código del producto a eliminar: ").upper().strip()
        if codigo in inventario:
            nombre = inventario[codigo]['nombre']
            del inventario[codigo]
            print(f"Producto {nombre} eliminado")
        else:
            print("Producto no encontrado")
    elif opcion == "7":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida")
```
</details>

### Ejercicio 5: Juego de Palabras
**Nivel:** Intermedio-Avanzado

Juego donde el usuario debe adivinar palabras con pistas.

<details>
<summary>👁️ Ver solución</summary>

```python
import random

# Base de datos de palabras con pistas
palabras_db = {
    "python": ["Lenguaje de programación", "Serpiente grande", "Tiene una mascota que es una serpiente"],
    "computadora": ["Máquina para procesar datos", "Tiene teclado y monitor", "Se usa para programar"],
    "internet": ["Red mundial", "WWW", "Conecta computadoras globalmente"],
    "programacion": ["Actividad de crear software", "Escribir código", "Usar algoritmos"],
    "algoritmo": ["Secuencia de pasos", "Receta para resolver problemas", "Base de la programación"],
    "variable": ["Almacena datos", "Puede cambiar su valor", "Tiene un nombre y contenido"],
    "funcion": ["Bloque de código reutilizable", "Puede recibir parámetros", "Retorna un valor"],
    "lista": ["Colección ordenada", "Se puede modificar", "Usa corchetes []"],
    "diccionario": ["Estructura clave-valor", "Usa llaves {}", "Búsqueda eficiente"]
}

def seleccionar_palabra():
    return random.choice(list(palabras_db.keys()))

def mostrar_progreso(palabra, letras_adivinadas):
    progreso = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            progreso += letra + " "
        else:
            progreso += "_ "
    return progreso.strip()

def mostrar_pistas(palabra, nivel_pista):
    pistas = palabras_db[palabra]
    if nivel_pista <= len(pistas):
        print(f"Pista {nivel_pista}: {pistas[nivel_pista - 1]}")

def jugar_ronda():
    palabra = seleccionar_palabra()
    letras_adivinadas = set()
    intentos_fallidos = 0
    max_intentos = 6
    pistas_usadas = 0
    
    print(f"\nNUEVA PALABRA - {len(palabra)} letras")
    print(f"Tienes {max_intentos} intentos fallidos permitidos")
    
    while True:
        # Mostrar progreso
        progreso = mostrar_progreso(palabra, letras_adivinadas)
        print(f"\nProgreso: {progreso}")
        
        # Verificar si ganó
        if "_" not in progreso:
            print(f" ¡FELICITACIONES! Adivinaste la palabra: {palabra.upper()}")
            return True
        
        # Mostrar estado
        print(f"Intentos fallidos: {intentos_fallidos}/{max_intentos}")
        if letras_adivinadas:
            print(f"Letras usadas: {', '.join(sorted(letras_adivinadas))}")
        
        # Opciones del jugador
        print("\nOpciones:")
        print("- Escribe una letra")
        print("- Escribe 'pista' para obtener una pista")
        print("- Escribe la palabra completa si la sabes")
        
        entrada = input("Tu jugada: ").lower().strip()
        
        if not entrada:
            continue
        
        if entrada == "pista":
            pistas_usadas += 1
            if pistas_usadas <= len(palabras_db[palabra]):
                mostrar_pistas(palabra, pistas_usadas)
```

---
## Siguiente módulo
[Siguiente módulo](../modulo4/README.md)