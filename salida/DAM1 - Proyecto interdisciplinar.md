# Informe de clases – DAM1 - Proyecto interdisciplinar

_Generado automáticamente. Vídeos incluidos: 5._

## Índice

1. [2025 09 22 16 31 33](#2025-09-22-16-31-33)
2. [2025 09 22 16 47 55](#2025-09-22-16-47-55)
3. [2025 09 29 16 00 24](#2025-09-29-16-00-24)
4. [2025 10 06 16 49 29](#2025-10-06-16-49-29)
5. [2025 10 13 16 50 53](#2025-10-13-16-50-53)

---

## 2025 09 22 16 31 33

**Fecha/Hora:** 2025-09-22 16:31:33

**Día (ES):** lunes

**Enlace:** https://www.youtube.com/watch?v=Hu7QwWz_BQw

_No hay subtítulos disponibles._

---

## 2025 09 22 16 47 55

**Fecha/Hora:** 2025-09-22 16:47:55

**Día (ES):** lunes

**Enlace:** https://www.youtube.com/watch?v=IrC4zt96vAc

_No hay subtítulos disponibles._

---

## 2025 09 29 16 00 24

**Fecha/Hora:** 2025-09-29 16:00:24

**Día (ES):** lunes

**Enlace:** https://www.youtube.com/watch?v=bVaFjNCAyCk

**Resumen Extenso: Intermodularidad en Programación**

**Objetivos:**

* Comprender el concepto de intermodularidad y su importancia en la programación.
* Aprender a conectar diferentes tecnologías y habilidades para crear proyectos complejos.
* Desarrollar habilidades prácticas en programación utilizando lenguajes como Python y Flask.

**Conceptos Clave:**

* **Intermodularidad**: La capacidad de conectar diferentes módulos o tecnologías para crear un proyecto completo.
* **Flask**: Un micro servidor web que permite generar HTML desde Python.
* **Markup Languages**: Lenguajes de marcado como HTML, que se utilizan para presentar información en la pantalla.
* **Programming**: El proceso de escribir código para realizar tareas específicas.

**Explicación Didáctica:**

El profesor comienza explicando el concepto de intermodularidad y su importancia en la programación. Muestra cómo conectar diferentes tecnologías y habilidades para crear proyectos complejos, como un sitio web dinámico. Utiliza Flask como ejemplo de cómo conectar Python con HTML.

* **Crear un proyecto**: El profesor muestra cómo crear un proyecto básico utilizando Flask y Python.
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
```
* **Conectar tecnologías**: El profesor muestra cómo conectar diferentes tecnologías para crear un proyecto completo.
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

# Conectar con HTML
html_string = """
<html>
  <head>
    <title>Hello World</title>
  </head>
  <body>
    <h1>Hello, World!</h1>
  </body>
</html>
"""

return html_string
```
* **Crear un calendario**: El profesor muestra cómo crear un calendario utilizando Python y HTML.
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
<html>
  <head>
    <title>Calendario</title>
  </head>
  <body>
    <h1>Calendario</h1>
    {%- for day in range(31) %}
      <div class="day">{{ day + 1 }}</div>
    {%- endfor %}
  </body>
</html>
"""
```
* **Crear un tablero de ajedrez**: El profesor muestra cómo crear un tablero de ajedrez utilizando Python y HTML.
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
<html>
  <head>
    <title>Tablero de Ajedrez</title>
  </head>
  <body>
    {%- for x in range(8) %}
      {%- for y in range(8) %}
        <div class="cell">{{ (x + y) % 2 == 0 ? "black" : "white" }}</div>
      {%- endfor %}
    {%- endfor %}
  </body>
</html>
"""
```
**Pasos/Comandos:**

* Crear un proyecto básico utilizando Flask y Python.
* Conectar diferentes tecnologías para crear un proyecto completo.
* Utilizar Python y HTML para crear un calendario o tablero de ajedrez.

**Buenas Prácticas:**

* Aprender a conectar diferentes tecnologías y habilidades para crear proyectos complejos.
* Desarrollar habilidades prácticas en programación utilizando lenguajes como Python y Flask.
* Utilizar herramientas como Flask para generar HTML desde Python.

---

## 2025 10 06 16 49 29

**Fecha/Hora:** 2025-10-06 16:49:29

**Día (ES):** lunes

**Enlace:** https://www.youtube.com/watch?v=672rGRxyGlE

_No hay subtítulos disponibles._

---

## 2025 10 13 16 50 53

**Fecha/Hora:** 2025-10-13 16:50:53

**Día (ES):** lunes

**Enlace:** https://www.youtube.com/watch?v=FO12Y-grhQY

_No hay subtítulos disponibles._

---
