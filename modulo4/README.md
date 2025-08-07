
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