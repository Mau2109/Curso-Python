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