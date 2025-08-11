# 📚 Módulo 7: Interfaces Gráficas y Machine Learning

> **Creación de ventanas con Tkinter y introducción a Machine Learning**

En este módulo aprenderás a crear interfaces gráficas de usuario (GUI) usando Tkinter y te introducirás al mundo del Machine Learning con las librerías más populares de Python.

## 📖 Tabla de Contenidos

- [Interfaces Gráficas con Tkinter](#-interfaces-gráficas-con-tkinter)
- [Componentes Avanzados de GUI](#-componentes-avanzados-de-gui)
- [Introducción a Machine Learning](#-introducción-a-machine-learning)
- [Análisis de Datos con Pandas](#-análisis-de-datos-con-pandas)
- [Visualización con Matplotlib y Seaborn](#-visualización-con-matplotlib-y-seaborn)
- [Scikit-learn: Tu Primera IA](#-scikit-learn-tu-primera-ia)
- [Proyectos Prácticos](#-proyectos-prácticos)
- [Conceptos Clave](#-conceptos-clave)
- [Errores Comunes](#-errores-comunes)
- [Buenas Prácticas](#-buenas-prácticas)

---

## Interfaces Gráficas con Tkinter

Tkinter es la librería estándar de Python para crear interfaces gráficas de usuario.

### Ventana básica

```python
import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Mi Primera Aplicación")
ventana.geometry("400x300")
ventana.resizable(False, False)

# Ejecutar el bucle principal
ventana.mainloop()
```

### Widgets básicos

```python
import tkinter as tk
from tkinter import messagebox

def saludar():
    nombre = entrada.get()
    messagebox.showinfo("Saludo", f"¡Hola, {nombre}!")

ventana = tk.Tk()
ventana.title("Aplicación de Saludo")
ventana.geometry("300x200")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta.pack(pady=10)

# Campo de entrada
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Botón
boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack(pady=10)

ventana.mainloop()
```

### Layout Managers

#### Pack
```python
import tkinter as tk

ventana = tk.Tk()

tk.Label(ventana, text="Superior", bg="red").pack(side=tk.TOP, fill=tk.X)
tk.Label(ventana, text="Izquierda", bg="blue").pack(side=tk.LEFT)
tk.Label(ventana, text="Derecha", bg="green").pack(side=tk.RIGHT)

ventana.mainloop()
```

#### Grid
```python
import tkinter as tk

ventana = tk.Tk()

tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(ventana).grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Email:").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(ventana).grid(row=1, column=1, padx=5, pady=5)

tk.Button(ventana, text="Enviar").grid(row=2, column=0, columnspan=2, pady=10)

ventana.mainloop()
```

---

## Componentes Avanzados de GUI

### Menús

```python
import tkinter as tk
from tkinter import messagebox, filedialog

def nuevo_archivo():
    messagebox.showinfo("Nuevo", "Crear nuevo archivo")

def abrir_archivo():
    archivo = filedialog.askopenfilename()
    if archivo:
        messagebox.showinfo("Abrir", f"Archivo seleccionado: {archivo}")

ventana = tk.Tk()
ventana.title("Editor Básico")
ventana.geometry("500x400")

# Crear barra de menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# Menú Archivo
menu_archivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Nuevo", command=nuevo_archivo)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.quit)

ventana.mainloop()
```

### Canvas para dibujo

```python
import tkinter as tk

def dibujar(event):
    x, y = event.x, event.y
    canvas.create_oval(x-2, y-2, x+2, y+2, fill="black")

ventana = tk.Tk()
ventana.title("Aplicación de Dibujo")

canvas = tk.Canvas(ventana, width=400, height=300, bg="white")
canvas.pack(pady=10)

canvas.bind("<B1-Motion>", dibujar)  # Arrastrar con botón izquierdo

tk.Button(ventana, text="Limpiar", 
          command=lambda: canvas.delete("all")).pack()

ventana.mainloop()
```

### Frames y organización

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora Básica")
ventana.geometry("300x400")

# Frame para la pantalla
frame_pantalla = tk.Frame(ventana, bg="lightgray")
frame_pantalla.pack(fill=tk.X, padx=5, pady=5)

pantalla = tk.Entry(frame_pantalla, font=("Arial", 20), justify="right")
pantalla.pack(fill=tk.X, padx=5, pady=5)

# Frame para botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

# Crear botones numéricos
def agregar_numero(num):
    actual = pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(0, actual + str(num))

for i in range(10):
    fila = (9 - i) // 3
    columna = (i - 1) % 3 if i != 0 else 1
    if i == 0:
        fila = 3
    
    tk.Button(frame_botones, text=str(i), 
              command=lambda x=i: agregar_numero(x)).grid(
              row=fila, column=columna, sticky="nsew", padx=2, pady=2)

# Configurar redimensionamiento
for i in range(4):
    frame_botones.grid_rowconfigure(i, weight=1)
    frame_botones.grid_columnconfigure(i, weight=1)

ventana.mainloop()
```

---

## Introducción a Machine Learning

Machine Learning es una rama de la inteligencia artificial que permite a las computadoras aprender patrones sin ser programadas explícitamente.

### Instalación de librerías esenciales

```bash
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
```

### Tipos de Machine Learning

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Supervisado** | Aprende de datos etiquetados | Clasificación de emails (spam/no spam) |
| **No Supervisado** | Encuentra patrones en datos sin etiquetas | Agrupación de clientes |
| **Reforzamiento** | Aprende mediante recompensas | Juegos, robots |

---

## Análisis de Datos con Pandas

Pandas es la librería fundamental para manipulación y análisis de datos.

### Operaciones básicas

```python
import pandas as pd
import numpy as np

# Crear DataFrame
datos = {
    'Nombre': ['Ana', 'Luis', 'María', 'Carlos'],
    'Edad': [25, 30, 28, 35],
    'Salario': [50000, 60000, 55000, 70000],
    'Departamento': ['IT', 'Ventas', 'IT', 'Marketing']
}

df = pd.DataFrame(datos)
print(df)
```

### Análisis exploratorio

```python
# Información básica
print(df.info())
print(df.describe())

# Filtrar datos
it_empleados = df[df['Departamento'] == 'IT']
print(it_empleados)

# Agrupar datos
por_departamento = df.groupby('Departamento')['Salario'].mean()
print(por_departamento)

# Operaciones con columnas
df['Salario_Anual'] = df['Salario'] * 12
df['Categoria_Edad'] = df['Edad'].apply(
    lambda x: 'Joven' if x < 30 else 'Adulto'
)
```
---

## Visualización con Matplotlib y Seaborn

### Matplotlib básico

```python
import matplotlib.pyplot as plt
import numpy as np

# Gráfico de líneas
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sen(x)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Función Seno')
plt.legend()
plt.grid(True)
plt.show()
```

### Gráficos con Pandas

```python
import pandas as pd
import matplotlib.pyplot as plt

# Datos de ejemplo
ventas = pd.DataFrame({
    'Mes': ['Ene', 'Feb', 'Mar', 'Abr', 'May'],
    'Ventas': [1200, 1500, 1800, 1400, 1900],
    'Gastos': [800, 900, 1100, 950, 1200]
})

# Gráfico de barras
ventas.set_index('Mes')[['Ventas', 'Gastos']].plot(kind='bar')
plt.title('Ventas vs Gastos por Mes')
plt.ylabel('Cantidad ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

---

## Scikit-learn: Tu Primera IA

### Clasificación: Predictor de especies de flores

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

# Cargar datos
iris = load_iris()
X = iris.data  # Características
y = iris.target  # Etiquetas

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Crear y entrenar modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Hacer predicciones
predicciones = modelo.predict(X_test)

# Evaluar modelo
precision = accuracy_score(y_test, predicciones)
print(f"Precisión: {precision:.2%}")
print(classification_report(y_test, predicciones, 
                          target_names=iris.target_names))
```

### Clustering: Agrupación de clientes

```python
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np

# Crear datos sintéticos de clientes
np.random.seed(42)
clientes = np.random.rand(200, 2) * 100  # 200 clientes, 2 características

# Aplicar K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(clientes)

# Visualizar
plt.figure(figsize=(10, 8))
colores = ['red', 'blue', 'green']
for i in range(3):
    cluster_points = clientes[clusters == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], 
               c=colores[i], label=f'Cluster {i+1}')

# Mostrar centroides
centroides = kmeans.cluster_centers_
plt.scatter(centroides[:, 0], centroides[:, 1], 
           c='black', marker='x', s=200, label='Centroides')

plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.title('Segmentación de Clientes')
plt.legend()
plt.show()
```

---

## Proyectos Prácticos

### Proyecto 1: Calculadora con GUI
**Nivel:** Principiante

Crear una calculadora funcional con interfaz gráfica.

<details>
<summary>👁️ Ver solución</summary>

```python
import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora")
        self.ventana.geometry("300x400")
        self.ventana.resizable(False, False)
        
        self.resultado = tk.StringVar()
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Pantalla
        pantalla = tk.Entry(self.ventana, textvariable=self.resultado,
                           font=("Arial", 16), state="readonly", justify="right")
        pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="ew")
        
        # Botones
        botones = [
            ('C', 1, 0), ('±', 1, 1), ('%', 1, 2), ('÷', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 2), ('=', 5, 3)
        ]
        
        for (texto, fila, col) in botones:
            if texto == '0':
                tk.Button(self.ventana, text=texto, font=("Arial", 14),
                         command=lambda t=texto: self.click_boton(t)).grid(
                         row=fila, column=col, columnspan=2, sticky="ew", padx=2, pady=2)
            else:
                tk.Button(self.ventana, text=texto, font=("Arial", 14),
                         command=lambda t=texto: self.click_boton(t)).grid(
                         row=fila, column=col, sticky="ew", padx=2, pady=2)
        
        # Configurar redimensionamiento
        for i in range(6):
            self.ventana.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.ventana.grid_columnconfigure(i, weight=1)
    
    def click_boton(self, caracter):
        if caracter == '=':
            try:
                expresion = self.resultado.get()
                expresion = expresion.replace('×', '*').replace('÷', '/')
                resultado = eval(expresion)
                self.resultado.set(resultado)
            except:
                messagebox.showerror("Error", "Expresión inválida")
                self.resultado.set("")
        elif caracter == 'C':
            self.resultado.set("")
        else:
            actual = self.resultado.get()
            self.resultado.set(actual + caracter)
    
    def ejecutar(self):
        self.ventana.mainloop()

# Ejecutar calculadora
calc = Calculadora()
calc.ejecutar()
```

</details>

### Proyecto 2: Analizador de Datos de Ventas
**Nivel:** Intermedio

Crear una aplicación que analice datos de ventas con gráficos.

<details>
<summary>👁️ Ver solución</summary>

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import numpy as np

# Generar datos de ejemplo
np.random.seed(42)
fechas = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
n_dias = len(fechas)

datos_ventas = pd.DataFrame({
    'fecha': fechas,
    'ventas': np.random.poisson(100, n_dias) + np.sin(np.arange(n_dias) * 2 * np.pi / 365) * 20,
    'producto': np.random.choice(['A', 'B', 'C'], n_dias),
    'region': np.random.choice(['Norte', 'Sur', 'Este', 'Oeste'], n_dias),
    'vendedor': np.random.choice(['Juan', 'María', 'Carlos', 'Ana'], n_dias)
})

class AnalizadorVentas:
    def __init__(self, datos):
        self.datos = datos
        self.datos['mes'] = self.datos['fecha'].dt.month
        self.datos['dia_semana'] = self.datos['fecha'].dt.day_name()
    
    def resumen_general(self):
        print("=== RESUMEN GENERAL ===")
        print(f"Total de ventas: ${self.datos['ventas'].sum():,.2f}")
        print(f"Promedio diario: ${self.datos['ventas'].mean():.2f}")
        print(f"Mejor día: {self.datos.loc[self.datos['ventas'].idxmax(), 'fecha']}")
        print(f"Ventas del mejor día: ${self.datos['ventas'].max():.2f}")
        print()
    
    def analisis_mensual(self):
        mensual = self.datos.groupby('mes')['ventas'].agg(['sum', 'mean'])
        
        plt.figure(figsize=(15, 5))
        
        plt.subplot(1, 2, 1)
        mensual['sum'].plot(kind='bar')
        plt.title('Ventas Totales por Mes')
        plt.ylabel('Ventas ($)')
        plt.xlabel('Mes')
        
        plt.subplot(1, 2, 2)
        mensual['mean'].plot(kind='line', marker='o')
        plt.title('Promedio de Ventas por Mes')
        plt.ylabel('Promedio ($)')
        plt.xlabel('Mes')
        
        plt.tight_layout()
        plt.show()
    
    def analisis_por_producto(self):
        por_producto = self.datos.groupby('producto')['ventas'].agg(['sum', 'count'])
        
        plt.figure(figsize=(12, 5))
        
        plt.subplot(1, 2, 1)
        por_producto['sum'].plot(kind='pie', autopct='%1.1f%%')
        plt.title('Distribución de Ventas por Producto')
        
        plt.subplot(1, 2, 2)
        sns.boxplot(x='producto', y='ventas', data=self.datos)
        plt.title('Distribución de Ventas por Producto')
        
        plt.tight_layout()
        plt.show()
    
    def generar_reporte(self):
        self.resumen_general()
        self.analisis_mensual()
        self.analisis_por_producto()

# Ejecutar análisis
analizador = AnalizadorVentas(datos_ventas)
analizador.generar_reporte()
```

</details>

### Proyecto 3: Predictor de Precios con GUI
**Nivel:** Avanzado

Aplicación completa que predice precios usando Machine Learning.

<details>
<summary>👁️ Ver solución</summary>

```python
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PredictorPrecios:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Predictor de Precios de Casas")
        self.ventana.geometry("800x600")
        
        self.modelo = None
        self.datos = None
        self.crear_interfaz()
        self.generar_datos()
    
    def crear_interfaz(self):
        # Notebook para pestañas
        notebook = ttk.Notebook(self.ventana)
        
        # Pestaña de entrenamiento
        self.frame_entrenamiento = ttk.Frame(notebook)
        notebook.add(self.frame_entrenamiento, text="Entrenamiento")
        
        # Pestaña de predicción
        self.frame_prediccion = ttk.Frame(notebook)
        notebook.add(self.frame_prediccion, text="Predicción")
        
        notebook.pack(expand=True, fill='both')
        
        self.crear_pestana_entrenamiento()
        self.crear_pestana_prediccion()
    
    def crear_pestana_entrenamiento(self):
        # Botón para generar/entrenar
        tk.Button(self.frame_entrenamiento, text="Generar Datos y Entrenar", 
                 command=self.entrenar_modelo, bg="lightblue").pack(pady=10)
        
        # Área para mostrar resultados
        self.texto_resultados = tk.Text(self.frame_entrenamiento, height=10, width=80)
        self.texto_resultados.pack(pady=10)
        
        # Frame para gráfico
        self.frame_grafico = tk.Frame(self.frame_entrenamiento)
        self.frame_grafico.pack(expand=True, fill='both')
    
    def crear_pestana_prediccion(self):
        # Campos de entrada
        tk.Label(self.frame_prediccion, text="Características de la Casa:", 
                font=("Arial", 14, "bold")).pack(pady=10)
        
        campos_frame = tk.Frame(self.frame_prediccion)
        campos_frame.pack(pady=10)
        
        self.entradas = {}
        campos = [
            ("Área (m²):", "area"),
            ("Habitaciones:", "habitaciones"),
            ("Baños:", "banos"),
            ("Edad (años):", "edad"),
            ("Distancia centro (km):", "distancia")
        ]
        
        for i, (label, key) in enumerate(campos):
            tk.Label(campos_frame, text=label).grid(row=i, column=0, sticky="w", padx=5, pady=2)
            entrada = tk.Entry(campos_frame)
            entrada.grid(row=i, column=1, padx=5, pady=2)
            self.entradas[key] = entrada
        
        # Botón de predicción
        tk.Button(self.frame_prediccion, text="Predecir Precio", 
                 command=self.predecir_precio, bg="lightgreen").pack(pady=20)
        
        # Resultado
        self.resultado_prediccion = tk.Label(self.frame_prediccion, text="", 
                                           font=("Arial", 16, "bold"))
        self.resultado_prediccion.pack(pady=10)
    
    def generar_datos(self):
        """Generar datos sintéticos de casas"""
        np.random.seed(42)
        n_samples = 1000
        
        self.datos = pd.DataFrame({
            'area': np.random.normal(150, 50, n_samples),
            'habitaciones': np.random.randint(1, 6, n_samples),
            'banos': np.random.randint(1, 4, n_samples),
            'edad': np.random.randint(0, 30, n_samples),
            'distancia': np.random.exponential(10, n_samples)
        })
        
        # Generar precios basados en las características
        precio = (self.datos['area'] * 2000 + 
                 self.datos['habitaciones'] * 15000 + 
                 self.datos['banos'] * 10000 - 
                 self.datos['edad'] * 1000 - 
                 self.datos['distancia'] * 500 + 
                 np.random.normal(0, 20000, n_samples))
        
        self.datos['precio'] = np.maximum(precio, 50000)  # Precio mínimo
    
    def entrenar_modelo(self):
        if self.datos is None:
            self.generar_datos()
        
        # Preparar datos
        X = self.datos[['area', 'habitaciones', 'banos', 'edad', 'distancia']]
        y = self.datos['precio']
        
        # Dividir datos
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Entrenar modelo
        self.modelo = RandomForestRegressor(n_estimators=100, random_state=42)
        self.modelo.fit(X_train, y_train)
        
        # Evaluar
        predicciones = self.modelo.predict(X_test)
        mse = mean_squared_error(y_test, predicciones)
        r2 = r2_score(y_test, predicciones)
        
        # Mostrar resultados
        resultados = f"""
RESULTADOS DEL ENTRENAMIENTO
============================
Datos utilizados: {len(self.datos)} casas
Error Cuadrático Medio: ${mse:,.2f}
R² Score: {r2:.4f}
Precisión: {r2*100:.2f}%

IMPORTANCIA DE CARACTERÍSTICAS:
"""
        
        for feature, importance in zip(X.columns, self.modelo.feature_importances_):
            resultados += f"{feature}: {importance:.4f}\n"
        
        self.texto_resultados.delete(1.0, tk.END)
        self.texto_resultados.insert(tk.END, resultados)
        
        # Crear gráfico de predicciones vs reales
        self.crear_grafico_evaluacion(y_test, predicciones)
        
        messagebox.showinfo("Éxito", "Modelo entrenado correctamente")
    
    def crear_grafico_evaluacion(self, y_real, y_pred):
        # Limpiar frame de gráfico
        for widget in self.frame_grafico.winfo_children():
            widget.destroy()
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Gráfico de dispersión: Real
```
</details>

---
### Ultimo modulo

[Siguiente módulo](../End/README.md)


