# 📚 Módulo 1: Fundamentos de Python

> **Variables, Tipos de Datos y Operadores Básicos**
> 
> En este módulo aprenderás los conceptos fundamentales de Python para comenzar tu viaje en la programación.

## 📖 Tabla de Contenidos

1. [🔤 Variables en Python](#-variables-en-python)
2. [📊 Tipos de Datos Básicos](#-tipos-de-datos-básicos)
3. [⚡ Operadores Básicos](#-operadores-básicos)
4. [📝 Entrada y Salida de Datos](#-entrada-y-salida-de-datos)
5. [💻 Ejercicios Prácticos](#-ejercicios-prácticos)
6. [📝 Conceptos Clave](#-conceptos-clave-para-recordar)
7. [⚠️ Errores Comunes](#️-errores-comunes)

---

## 🔤 Variables en Python

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

## 📊 Tipos de Datos Básicos

Python tiene varios tipos de datos fundamentales:

### 🔢 Números (int y float)
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

### 📝 Cadenas de texto (str)
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

### ✅❌ Booleanos (bool)
```python
verdadero = True
falso = False

# Los booleanos son útiles para condiciones
mayor_de_edad = edad >= 18
print(mayor_de_edad)  # True (si edad es 25)
```

---

## ⚡ Operadores Básicos

### 🔢 Operadores Aritméticos
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

### 📊 Operadores de Comparación
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

### 🔗 Operadores Lógicos
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

## 📝 Entrada y Salida de Datos

### 🖨️ Función print()
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

### ⌨️ Función input()
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

## 💻 Ejercicios Prácticos

### Ejercicio 1: Variables Básicas
**Nivel:** 🟢 Principiante

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
**Nivel:** 🟢 Principiante

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
**Nivel:** 🟡 Intermedio

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
**Nivel:** 🟡 Intermedio

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
**Nivel:** 🟡 Intermedio

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
| 🔴 **No convertir input()** | `input()` siempre devuelve string | Usar `int()`, `float()` para convertir |
| 🔴 **División por cero** | Dividir entre 0 causa error | Verificar antes de dividir |
| 🔴 **Nombres de variables** | Usar nombres no descriptivos | Usar nombres que expliquen el contenido |
| 🔴 **Mayúsculas/minúsculas** | `Nombre` ≠ `nombre` | Ser consistente con la nomenclatura |

## ✅ Buenas Prácticas

1. **Nombres descriptivos**: `edad` en lugar de `x`
2. **Usar f-strings**: Más legible que concatenación
3. **Comentar código**: Explicar partes complejas
4. **Verificar tipos**: Usar `type()` para debugging
5. **Validar entradas**: Asegurar que el usuario ingrese datos válidos

# 📚 Módulo 2: Estructuras de Control

> **Condicionales y Bucles en Python**
> 
> En este módulo aprenderás a tomar decisiones en tu código y a repetir acciones de manera eficiente.

## 📖 Tabla de Contenidos

1. [🔀 Condicionales](#-condicionales)
   - [La sentencia if](#la-sentencia-if)
   - [La sentencia if-else](#la-sentencia-if-else)
   - [La sentencia elif](#la-sentencia-elif-else-if)
   - [Condicionales anidados](#condicionales-anidados)
   - [Operadores lógicos](#operadores-lógicos-en-condicionales)
2. [🔄 Bucles](#-bucles)
   - [Bucle for](#bucle-for)
   - [Bucle while](#bucle-while)
   - [Control de bucles](#control-de-bucles-break-y-continue)
   - [Bucles anidados](#bucles-anidados)
3. [💻 Ejercicios Prácticos](#-ejercicios-prácticos)
4. [📝 Conceptos Clave](#-conceptos-clave-para-recordar)
5. [⚠️ Errores Comunes](#️-errores-comunes)

---

### 1. Condicionales

## 🔀 Condicionales

Los condicionales nos permiten ejecutar código solo cuando se cumple una condición específica. Python usa **indentación** (espacios o tabs) para definir bloques de código.

### La sentencia if

```python
# Estructura básica
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
    print("Puedes votar")

print("Esta línea siempre se ejecuta")
```

> **💡 Puntos importantes:**
> - Los dos puntos `:` son obligatorios
> - La indentación (4 espacios recomendados) define el bloque
> - Todo el código indentado se ejecuta si la condición es verdadera

### La sentencia if-else

```python
edad = int(input("¿Cuántos años tienes? "))

if edad >= 18:
    print("Eres mayor de edad")
    print("Puedes conducir y votar")
else:
    print("Eres menor de edad")
    print(f"Te faltan {18 - edad} años para ser mayor de edad")

print("¡Que tengas un buen día!")
```

### La sentencia elif (else if)

```python
nota = float(input("Ingresa tu nota (0-10): "))

if nota >= 9:
    print("¡Excelente! Calificación: A")
elif nota >= 7:
    print("Muy bien. Calificación: B")
elif nota >= 5:
    print("Aprobado. Calificación: C")
else:
    print("Reprobado. Calificación: F")
    print("Necesitas estudiar más")
```

### Condicionales anidados

```python
edad = int(input("¿Cuántos años tienes? "))
tiene_licencia = input("¿Tienes licencia de conducir? (si/no): ").lower()

if edad >= 18:
    if tiene_licencia == "si":
        print("Puedes conducir")
    else:
        print("Necesitas obtener tu licencia")
else:
    print("Eres menor de edad, no puedes conducir")
```

### Operadores lógicos en condicionales

```python
usuario = input("Usuario: ")
contraseña = input("Contraseña: ")

# Operador AND
if usuario == "admin" and contraseña == "123456":
    print("Acceso concedido")
else:
    print("Usuario o contraseña incorrectos")

# Operador OR
dia = input("¿Qué día es hoy? ").lower()
if dia == "sabado" or dia == "domingo":
    print("¡Es fin de semana!")
else:
    print("Es día laboral")

# Operador NOT
edad = int(input("Edad: "))
if not edad < 18:  # Equivale a: if edad >= 18
    print("Eres mayor de edad")
```

## 🔄 Bucles

Los bucles nos permiten repetir código múltiples veces.

### Bucle for

El bucle `for` se usa para iterar sobre una secuencia (números, listas, strings, etc.).

#### Con la función range()

```python
# range(inicio, fin, paso)
print("Números del 1 al 5:")
for i in range(1, 6):
    print(i)

print("\nNúmeros pares del 0 al 10:")
for num in range(0, 11, 2):
    print(num)

print("\nCuenta regresiva:")
for i in range(10, 0, -1):
    print(i)
print("¡Despegue!")
```

#### Iterando sobre strings

```python
palabra = "Python"
print("Letras de la palabra Python:")
for letra in palabra:
    print(letra)

# Con índice y valor
for i, letra in enumerate(palabra):
    print(f"Posición {i}: {letra}")
```

#### Tabla de multiplicar

```python
numero = int(input("¿De qué número quieres la tabla de multiplicar? "))

print(f"\nTabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
```

### Bucle while

El bucle `while` se ejecuta mientras una condición sea verdadera.

```python
# Contador básico
contador = 1
while contador <= 5:
    print(f"Vuelta número {contador}")
    contador += 1  # Equivale a: contador = contador + 1

print("Bucle terminado")
```

#### Validación de entrada

```python
# Pedir un número hasta que sea válido
while True:
    try:
        numero = int(input("Ingresa un número entero: "))
        break  # Sale del bucle si la conversión es exitosa
    except ValueError:
        print("Por favor, ingresa un número válido")

print(f"Has ingresado: {numero}")
```

#### Menú interactivo

```python
while True:
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Calcular suma")
    print("3. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        nombre = input("¿Cómo te llamas? ")
        print(f"¡Hola {nombre}!")
    elif opcion == "2":
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        print(f"La suma es: {a + b}")
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida")
```

### Control de bucles: break y continue

#### break - Termina el bucle

```python
print("Buscar el primer número par:")
for i in range(1, 10):
    if i % 2 == 0:
        print(f"Primer número par encontrado: {i}")
        break
    print(f"{i} es impar")
```

#### continue - Salta a la siguiente iteración

```python
print("Números impares del 1 al 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Salta los números pares
    print(i)
```

### Bucles anidados

```python
print("Patrón de asteriscos:")
for fila in range(5):
    for columna in range(fila + 1):
        print("*", end="")
    print()  # Nueva línea

# Resultado:
# *
# **
# ***
# ****
# *****
```

---

## 💻 Ejercicios Prácticos

### Ejercicio 1: Clasificador de Edad
**Nivel:** 🟢 Principiante

Crea un programa que clasifique a una persona según su edad.

<details>
<summary>👁️ Ver solución</summary>

```python
edad = int(input("¿Cuántos años tienes? "))

if edad < 13:
    categoria = "Niño"
elif edad < 20:
    categoria = "Adolescente"
elif edad < 60:
    categoria = "Adulto"
else:
    categoria = "Adulto mayor"

print(f"Según tu edad ({edad} años), eres: {categoria}")
```
</details>

### Ejercicio 2: Calculadora de IMC
**Nivel:** 🟡 Principiante-Intermedio

Crea un programa que calcule el IMC y determine el estado de peso.

<details>
<summary>👁️ Ver solución</summary>

```python
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

print(f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    estado = "Bajo peso"
elif imc < 25:
    estado = "Peso normal"
elif imc < 30:
    estado = "Sobrepeso"
else:
    estado = "Obesidad"

print(f"Estado: {estado}")
```
</details>

### Ejercicio 3: Juego de Adivinanza
**Nivel:** 🟠 Intermedio

Crea un juego donde el usuario debe adivinar un número.

<details>
<summary>👁️ Ver solución</summary>

```python
import random

numero_secreto = random.randint(1, 100)
intentos = 0
max_intentos = 7

print("¡Adivina el número entre 1 y 100!")
print(f"Tienes {max_intentos} intentos")

while intentos < max_intentos:
    intento = int(input("\nIngresa tu número: "))
    intentos += 1
    
    if intento == numero_secreto:
        print(f"¡Felicitaciones! Adivinaste en {intentos} intentos")
        break
    elif intento < numero_secreto:
        print("El número es mayor")
    else:
        print("El número es menor")
    
    print(f"Te quedan {max_intentos - intentos} intentos")
else:
    print(f"\nSe acabaron los intentos. El número era: {numero_secreto}")
```
</details>

### Ejercicio 4: Contador de Vocales
**Nivel:** 🟠 Intermedio

Cuenta las vocales en una palabra o frase.

<details>
<summary>👁️ Ver solución</summary>

```python
texto = input("Ingresa una palabra o frase: ").lower()
vocales = "aeiou"
contador_vocales = 0
detalle_vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for letra in texto:
    if letra in vocales:
        contador_vocales += 1
        detalle_vocales[letra] += 1

print(f"\nTexto: '{texto}'")
print(f"Total de vocales: {contador_vocales}")
print("Detalle por vocal:")
for vocal, cantidad in detalle_vocales.items():
    if cantidad > 0:
        print(f"  {vocal}: {cantidad}")
```
</details>

### Ejercicio 5: Generador de Patrones
**Nivel:** 🟠 Intermedio

Crea diferentes patrones usando bucles anidados.

<details>
<summary>👁️ Ver solución</summary>

```python
print("Selecciona un patrón:")
print("1. Triángulo de asteriscos")
print("2. Pirámide")
print("3. Cuadrado hueco")

opcion = input("Opción: ")
tamaño = int(input("Tamaño: "))

if opcion == "1":
    print("\nTriángulo de asteriscos:")
    for i in range(1, tamaño + 1):
        print("*" * i)

elif opcion == "2":
    print("\nPirámide:")
    for i in range(1, tamaño + 1):
        espacios = " " * (tamaño - i)
        asteriscos = "*" * (2 * i - 1)
        print(espacios + asteriscos)

elif opcion == "3":
    print("\nCuadrado hueco:")
    for i in range(tamaño):
        if i == 0 or i == tamaño - 1:
            print("*" * tamaño)
        else:
            print("*" + " " * (tamaño - 2) + "*")
```
</details>

### Ejercicio 6: Sistema de Login Simple
**Nivel:** 🔴 Avanzado

Sistema con múltiples intentos y usuarios.

<details>
<summary>👁️ Ver solución</summary>

```python
# Base de datos simple de usuarios
usuarios = {
    "admin": "admin123",
    "user1": "password1",
    "user2": "password2"
}

max_intentos = 3
intentos = 0

print("=== SISTEMA DE LOGIN ===")

while intentos < max_intentos:
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print(f"¡Bienvenido, {usuario}!")
        
        # Menú post-login
        while True:
            print(f"\n--- Menú de {usuario} ---")
            print("1. Ver perfil")
            print("2. Cambiar contraseña")
            print("3. Cerrar sesión")
            
            opcion = input("Opción: ")
            
            if opcion == "1":
                print(f"Usuario: {usuario}")
                print("Estado: Conectado")
            elif opcion == "2":
                nueva_contraseña = input("Nueva contraseña: ")
                usuarios[usuario] = nueva_contraseña
                print("Contraseña actualizada exitosamente")
            elif opcion == "3":
                print("Cerrando sesión...")
                break
            else:
                print("Opción no válida")
        break
    else:
        intentos += 1
        restantes = max_intentos - intentos
        if restantes > 0:
            print(f"Usuario o contraseña incorrectos. Te quedan {restantes} intentos")
        else:
            print("Demasiados intentos fallidos. Acceso bloqueado.")
```
</details>

---

## 📝 Conceptos Clave para Recordar

### 🔀 Condicionales
- **if**: Ejecuta código si la condición es verdadera
- **elif**: Múltiples condiciones alternativas  
- **else**: Se ejecuta si ninguna condición anterior es verdadera
- **Indentación**: Define los bloques de código (4 espacios)
- **Operadores lógicos**: `and`, `or`, `not`

### 🔄 Bucles
- **for**: Itera sobre secuencias (range, strings, listas)
- **while**: Se ejecuta mientras la condición sea verdadera
- **range()**: Genera secuencias de números
- **break**: Termina el bucle
- **continue**: Salta a la siguiente iteración
- **else en bucles**: Se ejecuta si el bucle termina normalmente

## ⚠️ Errores Comunes

| Error | Descripción | Solución |
|-------|-------------|----------|
| 🔴 **Indentación incorrecta** | Python es muy estricto con la indentación | Usar 4 espacios consistentemente |
| 🔴 **Bucles infinitos** | La condición del while nunca es falsa | Asegurar que la condición eventualmente cambie |
| 🔴 **Comparación vs asignación** | Confundir `=` con `==` | Usar `==` para comparar, `=` para asignar |
| 🔴 **Olvidar el break** | En bucles `while True` sin salida | Siempre incluir una condición de salida |
| 🔴 **Rango incorrecto** | `range(5)` va de 0 a 4, no hasta 5 | Recordar que el límite superior es exclusivo |

## ✅ Buenas Prácticas

1. **Usa nombres descriptivos** para variables de control
2. **Evita bucles anidados profundos** (más de 2-3 niveles)
3. **Valida las entradas del usuario** antes de procesarlas
4. **Usa elif** en lugar de múltiples if cuando las condiciones son mutuamente excluyentes
5. **Comenta código complejo** especialmente en bucles anidados


## 📋 Resumen del Módulo

En este módulo has aprendido:

- ✅ Cómo usar condicionales para tomar decisiones
- ✅ Diferentes tipos de bucles para repetir código
- ✅ Control de flujo con `break` y `continue`
- ✅ Creación de patrones con bucles anidados
- ✅ Desarrollo de programas interactivos

## Errores Comunes

1. **Indentación incorrecta**: Python es muy estricto con la indentación
2. **Bucles infinitos**: Asegúrate de que la condición del while eventualmente sea falsa
3. **Comparación vs asignación**: Usar `==` para comparar, `=` para asignar
4. **Olvidar el break**: En bucles while True, siempre incluir una condición de salida
5. **Rango incorrecto**: Recordar que range(5) va de 0 a 4, no hasta 5

# 📚 Módulo 3: Estructuras de Datos

> **Listas, Tuplas y Diccionarios en Python**
> 
> En este módulo aprenderás a organizar y manipular colecciones de datos de manera eficiente usando las estructuras fundamentales de Python.

## 📖 Tabla de Contenidos

1. [📋 Listas (Lists)](#-listas-lists)
2. [📦 Tuplas (Tuples)](#-tuplas-tuples)
3. [📖 Diccionarios (Dictionaries)](#-diccionarios-dictionaries)
4. [🔄 Iteración sobre Estructuras](#-iteración-sobre-estructuras)
5. [💻 Ejercicios Prácticos](#-ejercicios-prácticos)
6. [📝 Conceptos Clave](#-conceptos-clave-para-recordar)
7. [⚠️ Errores Comunes](#️-errores-comunes)

---

## 📋 Listas (Lists)

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

## 📦 Tuplas (Tuples)

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

## 📖 Diccionarios (Dictionaries)

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

## 🔄 Iteración sobre Estructuras

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

## 💻 Ejercicios Prácticos

### Ejercicio 1: Gestión de Calificaciones
**Nivel:** 🟢 Principiante

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
**Nivel:** 🟡 Intermedio

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
**Nivel:** 🟡 Intermedio

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
**Nivel:** 🟠 Intermedio-Avanzado

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
            print("⚠️  ALERTA: Stock por debajo del mínimo!")
            
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
        print(f"Estado: {'🔴 STOCK BAJO' if p['stock'] <= p['stock_minimo'] else '🟢 STOCK OK'}")
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
        estado = "🔴 BAJO" if datos['stock'] <= datos['stock_minimo'] else "🟢 OK"
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
**Nivel:** 🟠 Intermedio-Avanzado

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
    
    print(f"\n🎮 NUEVA PALABRA - {len(palabra)} letras")
    print(f"Tienes {max_intentos} intentos fallidos permitidos")
    
    while True:
        # Mostrar progreso
        progreso = mostrar_progreso(palabra, letras_adivinadas)
        print(f"\nProgreso: {progreso}")
        
        # Verificar si ganó
        if "_" not in progreso:
            print(f"🎉 ¡FELICITACIONES! Adivinaste la palabra: {palabra.upper()}")
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
# 📚 Módulo 4: Funciones en Python

> **Organiza y Reutiliza tu Código**
> 
> En este módulo aprenderás a crear funciones para organizar tu código, evitar repetición y hacer programas más modulares y mantenibles.

## 📖 Tabla de Contenidos

1. [🔧 Introducción a las Funciones](#-introducción-a-las-funciones)
2. [📥 Parámetros y Argumentos](#-parámetros-y-argumentos)
3. [📤 Valores de Retorno](#-valores-de-retorno)
4. [🎯 Ámbito de Variables (Scope)](#-ámbito-de-variables-scope)
5. [⭐ Funciones Avanzadas](#-funciones-avanzadas)
6. [🔄 Funciones como Objetos](#-funciones-como-objetos)
7. [💻 Ejercicios Prácticos](#-ejercicios-prácticos)
8. [📝 Conceptos Clave](#-conceptos-clave-para-recordar)
9. [⚠️ Errores Comunes](#️-errores-comunes)

---

## 🔧 Introducción a las Funciones

Las funciones son bloques de código reutilizable que realizan una tarea específica. Ayudan a organizar el código y evitar repetición.

### Sintaxis básica

```python
def nombre_funcion():
    """Docstring opcional - describe qué hace la función"""
    # Código de la función
    print("¡Hola desde la función!")

# Llamar a la función
nombre_funcion()  # ¡Hola desde la función!
```

### Ejemplo básico

```python
def saludar():
    """Función que muestra un saludo"""
    print("¡Hola, bienvenido al programa!")
    print("Esperamos que disfrutes aprendiendo Python")

def despedir():
    """Función que muestra una despedida"""
    print("¡Gracias por usar nuestro programa!")
    print("¡Hasta la próxima!")

# Usar las funciones
saludar()
print("--- Contenido del programa ---")
despedir()
```

### Ventajas de usar funciones

```python
# SIN funciones - código repetitivo
print("=== CALCULADORA ===")
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
print(f"Suma: {num1 + num2}")
print("==================")

print("=== CALCULADORA ===")
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
print(f"Resta: {num1 - num2}")
print("==================")

# CON funciones - código organizado
def obtener_numeros():
    """Obtiene dos números del usuario"""
    print("=== CALCULADORA ===")
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))
    print("==================")
    return num1, num2

def sumar():
    a, b = obtener_numeros()
    print(f"Suma: {a + b}")

def restar():
    a, b = obtener_numeros()
    print(f"Resta: {a - b}")
```

---

## 📥 Parámetros y Argumentos

Los parámetros permiten que las funciones reciban datos para procesar.

### Parámetros básicos

```python
def saludar_persona(nombre):
    """Saluda a una persona específica"""
    print(f"¡Hola, {nombre}!")
    print("¡Bienvenido!")

def sumar_numeros(a, b):
    """Suma dos números y muestra el resultado"""
    resultado = a + b
    print(f"{a} + {b} = {resultado}")

# Llamar funciones con argumentos
saludar_persona("María")
saludar_persona("Carlos")
sumar_numeros(5, 3)
sumar_numeros(10, 20)
```

### Parámetros con valores por defecto

```python
def presentarse(nombre, edad=18, ciudad="No especificada"):
    """Presenta a una persona con información opcional"""
    print(f"Hola, soy {nombre}")
    print(f"Tengo {edad} años")
    print(f"Vivo en {ciudad}")
    print("-" * 20)

# Diferentes formas de llamar la función
presentarse("Ana")  # Usa valores por defecto
presentarse("Luis", 25)  # Especifica edad
presentarse("María", 30, "Madrid")  # Especifica todo
presentarse("Carlos", ciudad="Barcelona")  # Argumentos con nombre
```

### Argumentos posicionales vs. con nombre

```python
def crear_perfil(nombre, edad, profesion, activo=True):
    """Crea un perfil de usuario"""
    estado = "Activo" if activo else "Inactivo"
    print(f"Perfil: {nombre}, {edad} años, {profesion} - {estado}")

# Argumentos posicionales
crear_perfil("Juan", 28, "Ingeniero")

# Argumentos con nombre (keywords)
crear_perfil(profesion="Doctor", nombre="Ana", edad=35)

# Combinación (posicionales primero, luego con nombre)
crear_perfil("Luis", 40, profesion="Abogado", activo=False)
```

### Parámetros *args y **kwargs

```python
def sumar_todos(*numeros):
    """Suma cualquier cantidad de números"""
    total = sum(numeros)
    print(f"Números: {numeros}")
    print(f"Suma total: {total}")
    return total

# Diferentes cantidades de argumentos
sumar_todos(1, 2, 3)
sumar_todos(5, 10, 15, 20, 25)

def mostrar_info(**datos):
    """Muestra información usando argumentos con nombre"""
    print("Información recibida:")
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")

mostrar_info(nombre="Pedro", edad=25, trabajo="Programador")
mostrar_info(producto="Laptop", precio=999.99, marca="TechBrand")

def funcion_completa(obligatorio, por_defecto="valor", *args, **kwargs):
    """Función que combina todos los tipos de parámetros"""
    print(f"Obligatorio: {obligatorio}")
    print(f"Por defecto: {por_defecto}")
    print(f"Args adicionales: {args}")
    print(f"Kwargs: {kwargs}")

funcion_completa("requerido", "nuevo_valor", 1, 2, 3, extra="dato", otro=True)
```

---

## 📤 Valores de Retorno

Las funciones pueden devolver valores usando la palabra clave `return`.

### Return básico

```python
def sumar(a, b):
    """Suma dos números y retorna el resultado"""
    resultado = a + b
    return resultado

def es_par(numero):
    """Verifica si un número es par"""
    return numero % 2 == 0

def obtener_mayor(x, y):
    """Retorna el mayor de dos números"""
    if x > y:
        return x
    else:
        return y

# Usar valores de retorno
suma = sumar(10, 5)
print(f"La suma es: {suma}")

if es_par(8):
    print("8 es par")

mayor = obtener_mayor(15, 23)
print(f"El mayor es: {mayor}")
```

### Retornar múltiples valores

```python
def operaciones_basicas(a, b):
    """Realiza operaciones básicas y retorna todos los resultados"""
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None
    return suma, resta, multiplicacion, division

def analizar_texto(texto):
    """Analiza un texto y retorna estadísticas"""
    palabras = texto.split()
    caracteres = len(texto)
    palabras_count = len(palabras)
    palabra_mas_larga = max(palabras, key=len) if palabras else ""
    
    return caracteres, palabras_count, palabra_mas_larga

# Desempaquetar múltiples valores de retorno
s, r, m, d = operaciones_basicas(10, 3)
print(f"Suma: {s}, Resta: {r}, Multiplicación: {m}, División: {d}")

# O recibir como tupla
resultados = operaciones_basicas(8, 4)
print(f"Resultados: {resultados}")

# Análisis de texto
chars, words, longest = analizar_texto("Python es un lenguaje fantástico")
print(f"Caracteres: {chars}, Palabras: {words}, Más larga: {longest}")
```

### Return temprano

```python
def validar_edad(edad):
    """Valida si una edad es válida para votar"""
    if edad < 0:
        return "Error: La edad no puede ser negativa"
    
    if edad > 150:
        return "Error: Edad demasiado alta"
    
    if edad < 18:
        return "No puede votar, es menor de edad"
    
    return "Puede votar"

def dividir_seguro(a, b):
    """División segura que maneja división por cero"""
    if b == 0:
        return None, "Error: División por cero"
    
    return a / b, "Operación exitosa"

# Usar return temprano
print(validar_edad(25))  # Puede votar
print(validar_edad(-5))  # Error: La edad no puede ser negativa
print(validar_edad(16))  # No puede votar, es menor de edad

resultado, mensaje = dividir_seguro(10, 2)
print(f"Resultado: {resultado}, Mensaje: {mensaje}")

resultado, mensaje = dividir_seguro(10, 0)
print(f"Resultado: {resultado}, Mensaje: {mensaje}")
```

---

## 🎯 Ámbito de Variables (Scope)

El ámbito determina dónde se pueden usar las variables.

### Variables locales vs globales

```python
# Variable global
contador_global = 0

def incrementar_local():
    """Función con variable local"""
    contador_local = 0  # Variable local
    contador_local += 1
    print(f"Contador local: {contador_local}")
    # contador_local se "destruye" al terminar la función

def incrementar_global():
    """Función que modifica variable global"""
    global contador_global  # Necesario para modificar
    contador_global += 1
    print(f"Contador global: {contador_global}")

def mostrar_ambos():
    """Muestra acceso a variables de diferentes ámbitos"""
    variable_local = "Solo existe aquí"
    print(f"Local: {variable_local}")
    print(f"Global: {contador_global}")  # Puede leer global sin 'global'

# Demostración
incrementar_local()  # Contador local: 1
incrementar_local()  # Contador local: 1 (se reinicia)

incrementar_global()  # Contador global: 1
incrementar_global()  # Contador global: 2

mostrar_ambos()
print(f"Contador global fuera de funciones: {contador_global}")
```

### Funciones anidadas y closures

```python
def funcion_externa(x):
    """Función que contiene otra función"""
    
    def funcion_interna(y):
        """Función anidada que accede a variables de la función externa"""
        return x + y  # Accede a 'x' de la función externa
    
    return funcion_interna

# Crear una función específica
sumar_10 = funcion_externa(10)
print(sumar_10(5))  # 15
print(sumar_10(3))  # 13

# Otro ejemplo con closures
def crear_multiplicador(factor):
    """Crea una función que multiplica por un factor específico"""
    
    def multiplicar(numero):
        return numero * factor
    
    return multiplicar

# Crear diferentes multiplicadores
por_2 = crear_multiplicador(2)
por_5 = crear_multiplicador(5)

print(por_2(10))  # 20
print(por_5(4))   # 20
```

---

## ⭐ Funciones Avanzadas

### Funciones lambda

```python
# Función normal
def cuadrado(x):
    return x ** 2

# Función lambda equivalente
cuadrado_lambda = lambda x: x ** 2

print(cuadrado(5))        # 25
print(cuadrado_lambda(5)) # 25

# Lambdas con múltiples parámetros
suma = lambda a, b: a + b
mayor = lambda x, y: x if x > y else y

print(suma(3, 4))    # 7
print(mayor(10, 8))  # 10

# Uso común con funciones como map, filter, sort
numeros = [1, 2, 3, 4, 5]

# map: aplica función a cada elemento
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # [1, 4, 9, 16, 25]

# filter: filtra elementos que cumplen condición
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4]

# sorted: ordena con función personalizada
palabras = ["Python", "es", "fantástico", "para", "aprender"]
por_longitud = sorted(palabras, key=lambda palabra: len(palabra))
print(por_longitud)  # ['es', 'para', 'Python', 'aprender', 'fantástico']
```

### Decoradores básicos

```python
def medir_tiempo(func):
    """Decorador que mide el tiempo de ejecución de una función"""
    import time
    
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"{func.__name__} tardó {fin - inicio:.4f} segundos")
        return resultado
    
    return wrapper

def validar_positivo(func):
    """Decorador que valida que los argumentos sean positivos"""
    
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("Los argumentos deben ser positivos")
        resultado = func(*args, **kwargs)
        return resultado
    
    return wrapper

# Usar decoradores
@medir_tiempo
@validar_positivo
def calcular_potencia(base, exponente):
    """Calcula base elevado a exponente"""
    return base ** exponente

# La función está "decorada"
resultado = calcular_potencia(2, 10)  # Valida y mide tiempo
print(f"Resultado: {resultado}")
```

### Generadores

```python
def contador_simple():
    """Generador que cuenta del 1 al 5"""
    for i in range(1, 6):
        yield i  # yield en lugar de return

# Usar el generador
gen = contador_simple()
for numero in gen:
    print(numero)

def fibonacci(limite):
    """Generador de números de Fibonacci"""
    a, b = 0, 1
    while a < limite:
        yield a
        a, b = b, a + b

# Generar primeros números de Fibonacci menores a 100
for fib in fibonacci(100):
    print(fib, end=" ")
print()

# Generator expression (similar a list comprehension)
cuadrados_gen = (x**2 for x in range(10))
print(list(cuadrados_gen))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

---

## 🔄 Funciones como Objetos

En Python, las funciones son objetos de primera clase.

### Asignar funciones a variables

```python
def saludar():
    return "¡Hola!"

def despedir():
    return "¡Adiós!"

# Asignar función a variable
mi_funcion = saludar
print(mi_funcion())  # ¡Hola!

# Lista de funciones
funciones = [saludar, despedir]
for func in funciones:
    print(func())

# Diccionario de funciones
operaciones = {
    "suma": lambda x, y: x + y,
    "resta": lambda x, y: x - y,
    "multiplicacion": lambda x, y: x * y
}

print(operaciones["suma"](5, 3))  # 8
```

### Pasar funciones como argumentos

```python
def aplicar_operacion(lista, operacion):
    """Aplica una operación a todos los elementos de una lista"""
    return [operacion(x) for x in lista]

def cuadrado(x):
    return x ** 2

def cubo(x):
    return x ** 3

numeros = [1, 2, 3, 4, 5]

cuadrados = aplicar_operacion(numeros, cuadrado)
cubos = aplicar_operacion(numeros, cubo)

print(f"Números: {numeros}")
print(f"Cuadrados: {cuadrados}")
print(f"Cubos: {cubos}")

def ejecutar_con_validacion(func, *args):
    """Ejecuta una función con validación de errores"""
    try:
        resultado = func(*args)
        print(f"Resultado: {resultado}")
        return resultado
    except Exception as e:
        print(f"Error al ejecutar {func.__name__}: {e}")
        return None

# Usar función como argumento
ejecutar_con_validacion(int, "123")    # Funciona
ejecutar_con_validacion(int, "abc")    # Error controlado
```

---

## 💻 Ejercicios Prácticos

### Ejercicio 1: Calculadora con Funciones
**Nivel:** 🟢 Principiante

Crea una calculadora usando funciones para cada operación.

<details>
<summary>👁️ Ver solución</summary>

```python
def sumar(a, b):
    """Suma dos números"""
    return a + b

def restar(a, b):
    """Resta dos números"""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números"""
    return a * b

def dividir(a, b):
    """Divide dos números (con validación)"""
    if b == 0:
        return None, "Error: División por cero"
    return a / b, "Operación exitosa"

def potencia(a, b):
    """Calcula a elevado a b"""
    return a ** b

def obtener_numero(mensaje):
    """Obtiene un número del usuario con validación"""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingresa un número válido")

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Salir")

def calculadora():
    """Función principal de la calculadora"""
    operaciones = {
        "1": ("Suma", sumar),
        "2": ("Resta", restar),
        "3": ("Multiplicación", multiplicar),
        "4": ("División", dividir),
        "5": ("Potencia", potencia)
    }
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == "6":
            print("¡Hasta luego!")
            break
        
        if opcion in operaciones:
            nombre_op, func = operaciones[opcion]
            
            num1 = obtener_numero("Primer número: ")
            num2 = obtener_numero("Segundo número: ")
            
            if func == dividir:
                resultado, mensaje = func(num1, num2)
                if resultado is None:
                    print(mensaje)
                else:
                    print(f"{nombre_op}: {num1} / {num2} = {resultado}")
            else:
                resultado = func(num1, num2)
                simbolos = {
                    sumar: "+", restar: "-", 
                    multiplicar: "×", potencia: "^"
                }
                simbolo = simbolos.get(func, "?")
                print(f"{nombre_op}: {num1} {simbolo} {num2} = {resultado}")
        else:
            print("Opción no válida")

# Ejecutar calculadora
calculadora()
```
</details>

### Ejercicio 2: Validador de Datos
**Nivel:** 🟡 Intermedio

Crea funciones para validar diferentes tipos de datos.

<details>
<summary>👁️ Ver solución</summary>

```python
def validar_email(email):
    """Valida formato básico de email"""
    if "@" not in email:
        return False, "Debe contener @"
    
    partes = email.split("@")
    if len(partes) != 2:
        return False, "Formato de email inválido"
    
    usuario, dominio = partes
    
    if len(usuario) == 0:
        return False, "El usuario no puede estar vacío"
    
    if "." not in dominio:
        return False, "El dominio debe contener al menos un punto"
    
    if len(dominio) < 3:
        return False, "Dominio demasiado corto"
    
    return True, "Email válido"

def validar_telefono(telefono):
    """Valida formato de teléfono"""
    # Remover espacios, guiones y paréntesis
    telefono_limpio = telefono.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    
    if not telefono_limpio.isdigit():
        return False, "Solo debe contener números"
    
    if len(telefono_limpio) < 7:
        return False, "Teléfono demasiado corto"
    
    if len(telefono_limpio) > 15:
        return False, "Teléfono demasiado largo"
    
    return True, "Teléfono válido"

def validar_contraseña(contraseña):
    """Valida que la contraseña sea segura"""
    errores = []
    
    if len(contraseña) < 8:
        errores.append("Debe tener al menos 8 caracteres")
    
    if not any(c.isupper() for c in contraseña):
        errores.append("Debe contener al menos una mayúscula")
    
    if not any(c.islower() for c in contraseña):
        errores.append("Debe contener al menos una minúscula")
    
    if not any(c.isdigit() for c in contraseña):
        errores.append("Debe contener al menos un número")
    
    if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in contraseña):
        errores.append("Debe contener al menos un carácter especial")
    
    if errores:
        return False, "; ".join(errores)
    
    return True, "Contraseña segura"

def validar_edad(edad_str):
    """Valida que la edad sea un número válido"""
    try:
        edad = int(edad_str)
        if edad < 0:
            return False, "La edad no puede ser negativa"
        if edad > 150:
            return False, "Edad no realista"
        return True, f"Edad válida: {edad} años"
    except ValueError:
        return False, "La edad debe ser un número entero"

def solicitar_datos_validados():
    """Solicita datos del usuario con validación"""
    datos = {}
    
    validadores = {
        "email": ("Ingresa tu email: ", validar_email),
        "telefono": ("Ingresa tu teléfono: ", validar_telefono),
        "contraseña": ("Ingresa tu contraseña: ", validar_contraseña),
        "edad": ("Ingresa tu edad: ", validar_edad)
    }
    
    for campo, (mensaje, validador) in validadores.items():
        while True:
            valor = input(mensaje)
            valido, mensaje_resultado = validador(valor)
            
            if valido:
                datos[campo] = valor
                print(f"✅ {mensaje_resultado}")
                break
            else:
                print(f"❌ {mensaje_resultado}")
                print("Intenta de nuevo.\n")
    
    return datos

# Programa principal
print("=== VALIDADOR DE DATOS ===")
datos_usuario = solicitar_datos_validados()

print(f"\n--- DATOS VALIDADOS ---")
for campo, valor in datos_usuario.items():
    if campo == "contraseña":
        print(f"{campo.capitalize()}: {'*' * len(valor)}")
    else:
        print(f"{campo.capitalize()}: {valor}")
```
</details>
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

🧠 Módulo 6: Métodos Integrados en Python

En este módulo aprenderás a utilizar los métodos integrados más comunes en Python para cadenas de texto (strings), listas, diccionarios y otros tipos de datos. Dominar estos métodos te hará mucho más productivo y te permitirá escribir código más limpio y eficiente.
📌 Tabla de Contenido

    Métodos para Strings

    Métodos para Listas

    Métodos para Diccionarios

    Otros Métodos Útiles

1️⃣ Métodos para Strings

# upper() - Convierte todos los caracteres a mayúsculas
texto = "hola mundo"
print(texto.upper())  # "HOLA MUNDO"

# lower() - Convierte todos los caracteres a minúsculas
print("PYTHON".lower())  # "python"

# capitalize() - Capitaliza la primera letra
print("python".capitalize())  # "Python"

# title() - Capitaliza la primera letra de cada palabra
print("hola mundo".title())  # "Hola Mundo"

# strip() - Elimina espacios en blanco al inicio y final
print("   espacio   ".strip())  # "espacio"

# replace() - Reemplaza subcadenas
print("hola mundo".replace("mundo", "Python"))  # "hola Python"

# split() - Divide la cadena en una lista
print("uno,dos,tres".split(","))  # ["uno", "dos", "tres"]

# join() - Une elementos de una lista en una cadena
palabras = ["Hola", "mundo"]
print(" ".join(palabras))  # "Hola mundo"

# find() - Devuelve el índice de la primera ocurrencia
print("banana".find("na"))  # 2

# count() - Cuenta cuántas veces aparece una subcadena
print("banana".count("na"))  # 2

2️⃣ Métodos para Listas

numeros = [1, 2, 3, 4, 5]

# append() - Agrega un elemento al final
numeros.append(6)
print(numeros)  # [1, 2, 3, 4, 5, 6]

# insert() - Inserta en un índice específico
numeros.insert(0, 0)
print(numeros)  # [0, 1, 2, 3, 4, 5, 6]

# remove() - Elimina la primera ocurrencia
numeros.remove(3)
print(numeros)  # [0, 1, 2, 4, 5, 6]

# pop() - Elimina y devuelve el último elemento
ultimo = numeros.pop()
print(ultimo)  # 6
print(numeros)

# sort() - Ordena la lista
numeros.sort()
print(numeros)  # [0, 1, 2, 4, 5]

# reverse() - Invierte el orden
numeros.reverse()
print(numeros)  # [5, 4, 2, 1, 0]

# count() - Cuenta las veces que aparece un valor
print(numeros.count(4))  # 1

# index() - Devuelve el índice del primer valor encontrado
print(numeros.index(2))  # 2

3️⃣ Métodos para Diccionarios

persona = {"nombre": "Juan", "edad": 30}

# get() - Obtiene un valor de forma segura
print(persona.get("nombre"))  # Juan
print(persona.get("altura", "No disponible"))  # No disponible

# keys() - Devuelve las llaves
print(persona.keys())  # dict_keys(['nombre', 'edad'])

# values() - Devuelve los valores
print(persona.values())  # dict_values(['Juan', 30])

# items() - Devuelve pares (llave, valor)
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# update() - Agrega o actualiza claves
persona.update({"edad": 31, "altura": 1.75})
print(persona)

# pop() - Elimina una clave y devuelve su valor
edad = persona.pop("edad")
print(edad)  # 31
print(persona)

4️⃣ Otros Métodos Útiles

# len() - Devuelve la longitud de una colección
print(len("Python"))  # 6
print(len([1, 2, 3]))  # 3

# type() - Devuelve el tipo de un dato
print(type(42))  # <class 'int'>
print(type([1, 2, 3]))  # <class 'list'>

# isinstance() - Verifica si un objeto es de cierto tipo
print(isinstance(3.14, float))  # True

# enumerate() - Devuelve índice y valor
for i, letra in enumerate("hola"):
    print(i, letra)

# zip() - Une dos listas en pares
nombres = ["Ana", "Luis"]
edades = [25, 30]
print(list(zip(nombres, edades)))  # [('Ana', 25), ('Luis', 30)]

🧪 Ejercicio Práctico

# Crea una función que reciba una lista de nombres,
# elimine los espacios, los capitalice y los ordene.

def limpiar_y_ordenar(nombres):
    return sorted([nombre.strip().capitalize() for nombre in nombres])

# Prueba:
nombres_crudos = ["  pedro", "ana  ", "LUIS"]
print(limpiar_y_ordenar(nombres_crudos))
# Resultado: ['Ana', 'Luis', 'Pedro']

# 📚 Módulo 6: Métodos Integrados en Python

> **Productividad y Buenas Prácticas con Tipos de Datos Comunes**
>
> En este módulo explorarás los métodos más utilizados para manipular cadenas de texto, listas, diccionarios y otros tipos de datos en Python. Aprenderlos te hará escribir código más limpio, corto y eficiente.

## 📖 Tabla de Contenidos

1. [🔢 Métodos para Strings](#-métodos-para-strings)
2. [📃 Métodos para Listas](#-métodos-para-listas)
3. [🔐 Métodos para Diccionarios](#-métodos-para-diccionarios)
4. [🔄 Otros Métodos Útiles](#-otros-métodos-útiles)
5. [💻 Ejercicio Práctico](#-ejercicio-práctico)
6. [📅 Conceptos Clave](#-conceptos-clave)
7. [⚠️ Errores Comunes](#⚠️-errores-comunes)

---

## 🔢 Métodos para Strings

```python
texto = "hola mundo"

print(texto.upper())       # HOLA MUNDO
print(texto.lower())       # hola mundo
print(texto.capitalize())  # Hola mundo
print(texto.title())       # Hola Mundo
print("  hola  ".strip())  # hola
print(texto.replace("mundo", "Python"))  # hola Python
print("uno,dos,tres".split(","))  # ['uno', 'dos', 'tres']

palabras = ["Hola", "mundo"]
print(" ".join(palabras))  # Hola mundo
print("banana".find("na"))  # 2
print("banana".count("na")) # 2
```

---

## 📃 Métodos para Listas

```python
numeros = [1, 2, 3, 4, 5]

numeros.append(6)          # Agrega al final
numeros.insert(0, 0)       # Inserta en la posición 0
numeros.remove(3)          # Elimina el primer 3
ultimo = numeros.pop()     # Quita el último y lo guarda
numeros.sort()             # Ordena de menor a mayor
numeros.reverse()          # Invierte el orden

print(numeros.count(2))    # Cuenta ocurrencias de 2
print(numeros.index(4))    # Posición de 4
```

---

## 🔐 Métodos para Diccionarios

```python
persona = {"nombre": "Juan", "edad": 30}

print(persona.get("nombre"))  # Juan
print(persona.get("altura", "No disponible"))
print(persona.keys())         # dict_keys(['nombre', 'edad'])
print(persona.values())       # dict_values(['Juan', 30])
print(persona.items())        # dict_items([('nombre', 'Juan'), ('edad', 30)])

persona.update({"edad": 31, "altura": 1.75})
edad = persona.pop("edad")
```

---

## 🔄 Otros Métodos Útiles

```python
print(len("Python"))         # Longitud
print(type([1, 2]))           # Tipo
print(isinstance(3.14, float)) # Verifica tipo

for i, letra in enumerate("hola"):
    print(i, letra)

nombres = ["Ana", "Luis"]
edades = [25, 30]
print(list(zip(nombres, edades)))
```

---

## 💻 Ejercicio Práctico

```python
def limpiar_y_ordenar(nombres):
    """Limpia espacios, capitaliza y ordena nombres"""
    return sorted([nombre.strip().capitalize() for nombre in nombres])

nombres_crudos = ["  pedro", "ana  ", "LUIS"]
print(limpiar_y_ordenar(nombres_crudos))
# ['Ana', 'Luis', 'Pedro']
```

---

## 📅 Conceptos Clave

* Los **métodos integrados** te permiten manipular objetos de forma eficiente sin importar su tipo (str, list, dict, etc).
* Aprende la diferencia entre `append()` y `insert()`, `get()` y acceso directo a claves.
* `join()` y `split()` son métodos poderosos para trabajar con texto.

---

## ⚠️ Errores Comunes

* Usar `replace()` en listas (solo es válido en strings).
* Olvidar que `pop()` modifica la lista original.
* Acceder a claves inexistentes sin usar `get()`.

---



