
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