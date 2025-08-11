# 📚 Módulo 1: Fundamentos de Python

> **Variables, Tipos de Datos y Operadores Básicos**
> 
> En este módulo aprenderás los conceptos fundamentales de Python para comenzar tu viaje en la programación.

## 📖 Tabla de Contenidos

1. [Variables en Python](#-variables-en-python)
2. [Tipos de Datos Básicos](#-tipos-de-datos-básicos)
3. [Operadores Básicos](#-operadores-básicos)
4. [Entrada y Salida de Datos](#-entrada-y-salida-de-datos)
5. [Ejercicios Prácticos](#-ejercicios-prácticos)
6. [Conceptos Clave](#-conceptos-clave-para-recordar)
7. [Errores Comunes](#-errores-comunes)

---

##  Variables en Python

Una variable es un contenedor que almacena datos. En Python, no necesitas declarar el tipo de variable, el intérprete lo deduce automáticamente.

### Reglas para nombres de variables:
- ✅ Pueden contener letras, números y guiones bajos (_)
- ❌ No pueden empezar con un número
- ⚠️ Son sensibles a mayúsculas y minúsculas
- ❌ No pueden usar palabras reservadas de Python

### Ejemplo básico:
```python
# Asignación de variables
nombre = "Juan"
edad = 25
altura = 1.75
es_estudiante = True

print(nombre)        # Juan
print(edad)          # 25
print(altura)        # 1.75
print(es_estudiante) # True
```

---

## Tipos de Datos Básicos

Python tiene varios tipos de datos fundamentales:

### Números (int y float)
```python
# Números enteros (int)
numero_entero = 42
temperatura = -10

# Números decimales (float)
precio = 19.99
pi = 3.14159

# Verificar el tipo de dato
print(type(numero_entero))  # <class 'int'>
print(type(precio))         # <class 'float'>
```

### Cadenas de texto (str)
```python
# Diferentes formas de crear strings
nombre = "María"
apellido = 'González'
mensaje = """Este es un
mensaje de
varias líneas"""

# Concatenación
nombre_completo = nombre + " " + apellido
print(nombre_completo)  # María González

# Métodos útiles de strings
print(nombre.upper())      # MARÍA
print(apellido.lower())    # gonzález
print(len(nombre))         # 5
```

### Booleanos (bool)
```python
verdadero = True
falso = False

# Los booleanos son útiles para condiciones
mayor_de_edad = edad >= 18
print(mayor_de_edad)  # True (si edad es 25)
```

---

## ⚡ Operadores Básicos

### Operadores Aritméticos
```python
a = 10
b = 3

suma = a + b        # 13
resta = a - b       # 7
multiplicacion = a * b  # 30
division = a / b    # 3.3333...
division_entera = a // b  # 3
modulo = a % b      # 1 (resto de la división)
potencia = a ** b   # 1000 (10 elevado a la 3)
```

### Operadores de Comparación
```python
x = 5
y = 8

print(x == y)  # False (igual)
print(x != y)  # True (diferente)
print(x < y)   # True (menor que)
print(x > y)   # False (mayor que)
print(x <= y)  # True (menor o igual)
print(x >= y)  # False (mayor o igual)
```

### Operadores Lógicos
```python
# AND, OR, NOT
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
print(not b)    # True
```

---

## Entrada y Salida de Datos

### Función print()
```python
# Imprimir texto
print("Hola mundo")

# Imprimir variables
nombre = "Ana"
edad = 20
print("Mi nombre es", nombre, "y tengo", edad, "años")

# Usando f-strings (recomendado)
print(f"Mi nombre es {nombre} y tengo {edad} años")

# Separadores y terminadores
print("A", "B", "C", sep="-")  # A-B-C
print("Línea 1", end=" | ")
print("Línea 2")  # Línea 1 | Línea 2
```

###  Función input()
```python
# Obtener entrada del usuario
nombre_usuario = input("¿Cuál es tu nombre? ")
print(f"Hola, {nombre_usuario}")

# Convertir entrada a número
edad_str = input("¿Cuántos años tienes? ")
edad_num = int(edad_str)  # Convertir string a entero

# O en una sola línea
edad = int(input("¿Cuántos años tienes? "))
```

---

## Ejercicios Prácticos

### Ejercicio 1: Variables Básicas
**Nivel:** Principiante

Crea un programa que:
1. Defina variables para tu nombre, edad y ciudad
2. Imprima una presentación usando estas variables

<details>
<summary>👁️ Ver solución</summary>

```python
nombre = "Carlos"
edad = 28
ciudad = "Madrid"

print(f"Hola, mi nombre es {nombre}, tengo {edad} años y vivo en {ciudad}")
```
</details>

### Ejercicio 2: Calculadora Básica
**Nivel:** Principiante

Crea un programa que pida dos números al usuario y muestre todas las operaciones aritméticas básicas.

<details>
<summary>👁️ Ver solución</summary>

```python
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

print(f"Suma: {num1} + {num2} = {num1 + num2}")
print(f"Resta: {num1} - {num2} = {num1 - num2}")
print(f"Multiplicación: {num1} * {num2} = {num1 * num2}")
print(f"División: {num1} / {num2} = {num1 / num2}")
```
</details>

### Ejercicio 3: Información Personal
**Nivel:** Intermedio

Crea un programa que pida información personal al usuario y calcule su año de nacimiento.

<details>
<summary>👁️ Ver solución</summary>

```python
nombre = input("¿Cuál es tu nombre completo? ")
edad = int(input("¿Cuál es tu edad? "))
profesion = input("¿Cuál es tu profesión? ")

año_actual = 2024  # Puedes usar datetime para obtener el año actual
año_nacimiento = año_actual - edad

print(f"\n--- INFORMACIÓN PERSONAL ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Profesión: {profesion}")
print(f"Año de nacimiento aproximado: {año_nacimiento}")
```
</details>

### Ejercicio 4: Validación de Tipos
**Nivel:** Intermedio

Crea un programa que muestre el tipo de dato de diferentes variables.

<details>
<summary>👁️ Ver solución</summary>

```python
# Crear diferentes tipos de variables
entero = 42
decimal = 3.14
texto = "Python"
booleano = True

print("Variable:", entero, "- Tipo:", type(entero))
print("Variable:", decimal, "- Tipo:", type(decimal))
print("Variable:", texto, "- Tipo:", type(texto))
print("Variable:", booleano, "- Tipo:", type(booleano))

# Conversiones de tipo
numero_como_texto = "123"
numero_convertido = int(numero_como_texto)
print(f"'{numero_como_texto}' convertido a entero: {numero_convertido}")
```
</details>

### Ejercicio 5: Operaciones con Strings
**Nivel:** Intermedio

Crea un programa que manipule cadenas de texto.

<details>
<summary>👁️ Ver solución</summary>

```python
frase = input("Escribe una frase: ")

print(f"Frase original: {frase}")
print(f"En mayúsculas: {frase.upper()}")
print(f"En minúsculas: {frase.lower()}")
print(f"Número de caracteres: {len(frase)}")
print(f"Número de palabras: {len(frase.split())}")
print(f"Primera letra: {frase[0] if frase else 'No hay caracteres'}")
print(f"Última letra: {frase[-1] if frase else 'No hay caracteres'}")
```
</details>

---

## 📝 Conceptos Clave para Recordar

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| **Variables** | Contenedores para almacenar datos | `nombre = "Juan"` |
| **int** | Números enteros | `edad = 25` |
| **float** | Números decimales | `precio = 19.99` |
| **str** | Cadenas de texto | `saludo = "Hola"` |
| **bool** | Valores verdadero/falso | `activo = True` |
| **input()** | Obtener datos del usuario | `nombre = input("Nombre: ")` |
| **print()** | Mostrar información | `print("Hola mundo")` |
| **f-strings** | Formato moderno de cadenas | `f"Hola {nombre}"` |

---

## ⚠️ Errores Comunes

| Error | Descripción | Solución |
|-------|-------------|----------|
| **No convertir input()** | `input()` siempre devuelve string | Usar `int()`, `float()` para convertir |
| **División por cero** | Dividir entre 0 causa error | Verificar antes de dividir |
| **Nombres de variables** | Usar nombres no descriptivos | Usar nombres que expliquen el contenido |
| **Mayúsculas/minúsculas** | `Nombre` ≠ `nombre` | Ser consistente con la nomenclatura |

## ✅ Buenas Prácticas

1. **Nombres descriptivos**: `edad` en lugar de `x`
2. **Usar f-strings**: Más legible que concatenación
3. **Comentar código**: Explicar partes complejas
4. **Verificar tipos**: Usar `type()` para debugging
5. **Validar entradas**: Asegurar que el usuario ingrese datos válidos

[Siguiente módulo](../modulo2/README.md)