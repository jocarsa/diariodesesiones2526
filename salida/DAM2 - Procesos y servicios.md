# Informe de clases – DAM2 - Procesos y servicios

_Generado automáticamente. Vídeos incluidos: 10._

## Índice

1. [2025 09 11 19 06 28](#2025-09-11-19-06-28)
2. [2025 09 11 20 14 41](#2025-09-11-20-14-41)
3. [2025 09 18 19 03 41](#2025-09-18-19-03-41)
4. [2025 09 18 20 18 59](#2025-09-18-20-18-59)
5. [2025 09 25 19 21 11](#2025-09-25-19-21-11)
6. [2025 09 25 20 25 43](#2025-09-25-20-25-43)
7. [2025 10 02 19 41 13](#2025-10-02-19-41-13)
8. [2025 10 02 20 22 44](#2025-10-02-20-22-44)
9. [2025 10 16 19 35 03](#2025-10-16-19-35-03)
10. [2025 10 16 20 01 04](#2025-10-16-20-01-04)

---

## 2025 09 11 19 06 28

**Fecha/Hora:** 2025-09-11 19:06:28

**Día (ES):** jueves

**Enlace:** https://www.youtube.com/watch?v=JgPAxsVGHXo

_No hay subtítulos disponibles._

---

## 2025 09 11 20 14 41

**Fecha/Hora:** 2025-09-11 20:14:41

**Día (ES):** jueves

**Enlace:** https://www.youtube.com/watch?v=U1hCziJErOQ

**Resumen Extenso de la Clase**

**Objetivos:**

* Comprender el concepto de procesos y servicios en programación.
* Aprender a utilizar la biblioteca `multiprocessing` para realizar programación paralela.
* Conocer las diferencias entre Python, C++ y Node.js en términos de rendimiento y facilidad de uso.

**Conceptos Clave:**

* **Procesos:** En programación, un proceso es una unidad de ejecución que se crea cuando se ejecuta un script o programa. En Python, los procesos son creados automáticamente cuando se ejecuta un script.
* **Servicios:** Un servicio es un proceso que permanece en ejecución constantemente y espera a ser llamado por otro proceso. Ejemplos de servicios incluyen Apache y otros servidores web.
* **Programación Paralela:** La programación paralela es una técnica para realizar cálculos o tareas simultáneamente utilizando múltiples procesadores o núcleos.

**Explicación Didáctica:**

El profesor comienza explicando que ha creado un aplicación personalizada para gestionar sus videos y que se ha dado cuenta de la importancia de la programación paralela en la era del procesamiento artificial. Muestra cómo puede utilizar la biblioteca `multiprocessing` en Python para crear múltiples procesos que trabajen simultáneamente.

**Pasos/Comandos:**

* Importar la biblioteca `multiprocessing`
* Crear un proceso pool utilizando `Pool()`
* Definir una función que se ejecutará en cada proceso
* Ejecutar los procesos en paralelo utilizando `map()` o `apply_async()`

**Buenas Prácticas:**

* Utilizar la biblioteca `multiprocessing` para realizar programación paralela.
* Asegurarse de que el código sea conciso y fácil de leer.
* Comprobar los resultados y ajustar el código según sea necesario.

**Ejemplos de Código:**
```python
import multiprocessing

def calcular(x):
    return x * 2

if __name__ == '__main__':
    procesos = []
    for i in range(4):
        proceso = multiprocessing.Process(target=calcular, args=(10,))
        procesos.append(proceso)
        proceso.start()

    for p in procesos:
        p.join()
```
**Resumen:**

En esta clase, el profesor ha explicado los conceptos de procesos y servicios en programación, y cómo utilizar la biblioteca `multiprocessing` para realizar programación paralela. Ha proporcionado ejemplos de código y buenas prácticas para asegurarse de que el código sea conciso y fácil de leer. Los estudiantes pueden aplicar estos conceptos y técnicas a sus proyectos futuros, especialmente en la era del procesamiento artificial.

---

## 2025 09 18 19 03 41

**Fecha/Hora:** 2025-09-18 19:03:41

**Día (ES):** jueves

**Enlace:** https://www.youtube.com/watch?v=0TmE6XcFg0s

_No hay subtítulos disponibles._

---

## 2025 09 18 20 18 59

**Fecha/Hora:** 2025-09-18 20:18:59

**Día (ES):** jueves

**Enlace:** https://www.youtube.com/watch?v=VLLFGZwLCdY

_No hay subtítulos disponibles._

---

## 2025 09 25 19 21 11

**Fecha/Hora:** 2025-09-25 19:21:11

**Día (ES):** jueves

**Enlace:** https://www.youtube.com/watch?v=cHLD3KrKHfc

**Resumen Extenso:**

**Objetivos:**

* Comprender el concepto de Object-Relational Mapping (ORM) y su importancia en la programación.
* Aprender a crear un ORM personalizado para gestionar conexiones con bases de datos MySQL.
* Desarrollar habilidades para trabajar con estructuras de datos complejas y convertirlas en modelos relacionales.

**Conceptos Clave:**

* **Object-Relational Mapping (ORM):** Es una técnica que permite mapear objetos de programación a tablas de bases de datos. Esto facilita la interacción entre el código y la base de datos.
* **MySQL:** Es un sistema de gestión de bases de datos relacional ampliamente utilizado.
* **Estructuras de Datos Complejas:** Se refiere a estructuras como arreglos, diccionarios o objetos que contienen información compleja.

**Explicación Didáctica:**

El profesor comienza explicando el concepto de ORM y su importancia en la programación. Menciona que el objetivo es crear un mapeo entre los objetos de programación y las tablas de bases de datos, lo que facilita la interacción entre el código y la base de datos.

A continuación, se enfoca en la creación de un ORM personalizado para gestionar conexiones con bases de datos MySQL. Muestra cómo crear una estructura de datos compleja utilizando arreglos y diccionarios en Python.

El profesor explica que el objetivo es mapear esta estructura a una tabla de base de datos MySQL, creando así un modelo relacional. Utiliza ejemplos para ilustrar cada paso del proceso.

**Pasos/Comandos:**

* Crear una estructura de datos compleja utilizando arreglos y diccionarios en Python.
* Mapear esta estructura a una tabla de base de datos MySQL.
* Crear un ORM personalizado para gestionar conexiones con bases de datos MySQL.

**Buenas Prácticas:**

* Utilizar técnicas de mapeo objeto-relacional (ORM) para facilitar la interacción entre el código y la base de datos.
* Crear estructuras de datos complejas utilizando arreglos, diccionarios o objetos en Python.
* Mapear estas estructuras a tablas de bases de datos MySQL para crear modelos relacionales.

**Fragmentos de Código:**

```python
# Estructura de datos compleja
clientes = [
    {"nombre": "Juan", "apellido": "Pérez", "email": ["jperez@gmail.com", "jperez@hotmail.com"]},
    {"nombre": "María", "apellido": "García", "email": ["mgarcia@yahoo.com"]}
]

# Mapeo a tabla de base de datos MySQL
tabla_clientes = """
CREATE TABLE clientes (
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  apellido VARCHAR(255),
  email VARCHAR(255)
);
"""

# Creación del ORM personalizado
class ORM:
    def __init__(self, db_name):
        self.db_name = db_name

    def crear_tabla(self, tabla):
        # Código para crear la tabla en MySQL
        pass

    def insertar_datos(self, datos):
        # Código para insertar los datos en la tabla
        pass
```

**Notas:**

* El código proporcionado es incompleto y se utiliza solo para ilustrar el concepto.
* La creación de un ORM personalizado requiere una mayor complejidad y no se cubre completamente en este resumen.

---

## 2025 09 25 20 25 43

**Fecha/Hora:** 2025-09-25 20:25:43

**Día (ES):** jueves

**Enlace:** https://www.youtube.com/watch?v=3L4Tt-lhvH8

**Resumen Extenso: Procesos y Servicios en Programación**

**Objetivos**

* Comprender el concepto de procesos y servicios en programación
* Aprender a utilizar Socket Client y Socket Server para comunicación distribuida
* Explorar la figura del worker en JavaScript y su aplicación en paralelismo y distribución
* Desarrollar habilidades en sincronización entre procesos

**Conceptos Clave**

* **Procesos**: Un proceso es una unidad de ejecución que se puede crear, suspender, reanudar o eliminar. En programación, los procesos se utilizan para realizar tareas independientes y mejorar el rendimiento.
* **Servicios**: Un servicio es un proceso que proporciona funcionalidades específicas a otros procesos. Los servicios pueden ser locales o remotos.
* **Socket Client y Socket Server**: Los sockets son mecanismos de comunicación entre procesos. El cliente (socket client) se conecta al servidor (socket server) para intercambiar datos.

**Explicación Didáctica**

La explicación del profesor comienza con una introducción a los conceptos de procesos y servicios en programación. Se menciona la relación entre estos temas y el paralelismo y la distribución, que son fundamentales en la era de la inteligencia artificial.

El profesor introduce la figura del worker en JavaScript, que es básicamente un hilo de ejecución dentro del navegador. El worker se utiliza para realizar tareas pesadas o complejas sin bloquear la interfaz gráfica.

Se muestra un ejemplo mínimo de un worker en JavaScript utilizando el método `new Worker`. Se crea un nuevo worker y se le envía una función a ejecutar. El profesor explica que el worker puede comunicarse con el navegador mediante mensajes post.

El profesor introduce la idea de utilizar múltiples workers para realizar tareas paralelas. Se muestra cómo crear un array de workers y asignarles tareas independientes. Se utiliza la propiedad `postMessage` para enviar datos entre los workers y el navegador.

**Pasos/Comandos**

* Crear un nuevo worker utilizando el método `new Worker`
* Enviar una función a ejecutar en el worker
* Utilizar la propiedad `postMessage` para comunicarse con el worker
* Crear un array de workers y asignarles tareas independientes

**Buenas Prácticas**

* Utilizar la figura del worker para realizar tareas pesadas o complejas sin bloquear la interfaz gráfica.
* Comunicarse con los workers mediante mensajes post utilizando la propiedad `postMessage`.
* Crear un array de workers y asignarles tareas independientes para mejorar el rendimiento.

**Fragmentos de Código**

```javascript
// Crear un nuevo worker
const worker = new Worker('script.js');

// Enviar una función a ejecutar en el worker
worker.postMessage({ action: 'run', data: { foo: 'bar' } });

// Utilizar la propiedad postMessage para comunicarse con el worker
worker.onmessage = (event) => {
  console.log(event.data);
};

// Crear un array de workers y asignarles tareas independientes
const workers = [];
for (let i = 0; i < 8; i++) {
  const worker = new Worker('script.js');
  workers.push(worker);
}

workers.forEach((worker) => {
  worker.postMessage({ action: 'run', data: { foo: `bar ${i}` } });
});
```

**Objetivos Futuros**

* Desarrollar habilidades en sincronización entre procesos
* Aprender a utilizar técnicas de paralelismo y distribución para mejorar el rendimiento
* Explorar la figura del worker en otros lenguajes de programación

Espero que este resumen extenso haya sido útil. Recuerda que si tienes alguna pregunta o necesitas más información, no dudes en preguntar.

---

## 2025 10 02 19 41 13

**Fecha/Hora:** 2025-10-02 19:41:13

**Día (ES):** jueves

**Enlace:** https://www.youtube.com/watch?v=RPkE7KcQX1o

**Resumen Extensivo de la Clase**

**Objetivos:**

* Comprender los conceptos básicos de acceso a datos y manipulación de archivos en Python.
* Aprender a crear un motor de almacenamiento CSV que permita guardar y leer información en formato CSV.
* Desarrollar habilidades para procesar grandes conjuntos de datos utilizando Python.

**Conceptos Clave:**

* **CSV (Comma Separated Values):** Un archivo que almacena información en forma de tablas con valores separados por comas.
* **Acceso a Datos:** La capacidad de leer y escribir información en archivos o bases de datos.
* **Manipulación de Archivos:** La capacidad de crear, leer, escribir y eliminar archivos.

**Explicación Didáctica:**

La clase comenzó con una discusión sobre el acceso a datos y la manipulación de archivos. El profesor explicó que se trataba de crear un motor de almacenamiento CSV que permitiera guardar y leer información en formato CSV. Para lograr esto, se utilizaría Python.

**Pasos/Comandos:**

1. **Crear un archivo CSV:** Se utilizó la función `open()` para abrir un archivo llamado "clients.csv" en modo escritura.
2. **Guardar datos en el archivo CSV:** Se creó una tupla con información de clientes y se escribió en el archivo CSV utilizando la función `write()`.
3. **Leer datos del archivo CSV:** Se utilizó la función `read()` para leer los datos almacenados en el archivo CSV.
4. **Deserializar datos:** Se utilizaron funciones como `split()` y `join()` para deserializar los datos leídos del archivo CSV.

**Buenas Prácticas:**

* Utilizar funciones para encapsular código y hacer que sea más fácil de mantener y reutilizar.
* Leer y escribir información en archivos utilizando la función `open()`.
* Utilizar comandos como `split()` y `join()` para manipular cadenas de texto.

**Código Ejemplo:**
```python
# Crear un archivo CSV
with open('clients.csv', 'w') as file:
    # Guardar datos en el archivo CSV
    data = ('José Vicente', 'Carratalá', 'info@josicente.com')
    file.write(','.join(data))

# Leer datos del archivo CSV
with open('clients.csv', 'r') as file:
    # Deserializar datos
    lines = file.readlines()
    for line in lines:
        print(line.strip().split(','))
```
**Tarea:**

* Escribe un programa que lea un archivo CSV y muestre la información de cada cliente en pantalla.
* Utiliza funciones para encapsular código y hacer que sea más fácil de mantener y reutilizar.
* Asegúrate de seguir las buenas prácticas mencionadas anteriormente.

---

## 2025 10 02 20 22 44

**Fecha/Hora:** 2025-10-02 20:22:44

**Día (ES):** jueves

**Enlace:** https://www.youtube.com/watch?v=qjHH7D6eTts

_No hay subtítulos disponibles._

---

## 2025 10 16 19 35 03

**Fecha/Hora:** 2025-10-16 19:35:03

**Día (ES):** jueves

**Enlace:** https://www.youtube.com/watch?v=utmNSp-m-PA

**Resumen Extenso: Programación de Aplicaciones Móviles y Desarrollo Web**

En la clase del 16 de octubre de 2025, se abordaron temas relacionados con la programación de aplicaciones móviles y el desarrollo web. El profesor explicó conceptos clave y proporcionó ejemplos prácticos para ilustrar los mismos.

**Objetivos**

Los objetivos de esta clase fueron:

* Comprender los conceptos básicos de programación de aplicaciones móviles y desarrollo web.
* Aprender a diseñar y desarrollar aplicaciones móviles utilizando tecnologías web.
* Conocer las ventajas de utilizar tecnologías web para crear aplicaciones móviles.

**Conceptos Clave**

Algunos conceptos clave abordados en esta clase fueron:

* **Desarrollo Web**: El desarrollo web se refiere a la creación de sitios web y aplicaciones utilizando lenguajes como HTML, CSS y JavaScript.
* **Programación de Aplicaciones Móviles**: La programación de aplicaciones móviles implica crear aplicaciones para dispositivos móviles utilizando tecnologías como Android y iOS.
* **Tecnologías Web**: Las tecnologías web se refieren a las herramientas y lenguajes utilizados para desarrollar sitios web y aplicaciones, como HTML, CSS, JavaScript, PHP y MySQL.

**Explicación Didáctica**

El profesor explicó que en lugar de enfocarse en la programación específica de Android o iOS, se centraría en el desarrollo web utilizando tecnologías como HTML, CSS y JavaScript. Esto permite crear aplicaciones móviles que pueden ser deployadas en múltiples plataformas sin necesidad de reprogramar.

**Pasos/Comandos**

Algunos pasos y comandos mencionados en la clase fueron:

* **Crear una aplicación web**: Utilizar tecnologías como HTML, CSS y JavaScript para crear una aplicación web que pueda ser deployada en múltiples plataformas.
* **Diseñar una interfaz de usuario**: Crear una interfaz de usuario atractiva y fácil de usar utilizando tecnologías como HTML y CSS.

**Buenas Prácticas**

Algunas buenas prácticas mencionadas en la clase fueron:

* **Investigar las necesidades del cliente**: Antes de comenzar a desarrollar una aplicación, es importante investigar las necesidades y requisitos del cliente.
* **Crear un prototipo**: Crear un prototipo de la aplicación para asegurarse de que se ajusta a las necesidades del cliente.

**Tarea**

La tarea asignada en esta clase fue:

* Investigar sobre el desarrollo web y programación de aplicaciones móviles.
* Crear un prototipo de una aplicación web utilizando tecnologías como HTML, CSS y JavaScript.
* Presentar los resultados y reflexiones sobre la tarea realizada.

En resumen, esta clase abordó temas relacionados con la programación de aplicaciones móviles y el desarrollo web. El profesor explicó conceptos clave y proporcionó ejemplos prácticos para ilustrar los mismos. La tarea asignada fue investigar sobre el desarrollo web y programación de aplicaciones móviles, crear un prototipo de una aplicación web y presentar los resultados y reflexiones sobre la tarea realizada.

---

## 2025 10 16 20 01 04

**Fecha/Hora:** 2025-10-16 20:01:04

**Día (ES):** jueves

**Enlace:** https://www.youtube.com/watch?v=LMp3_-umf0M

_No hay subtítulos disponibles._

---
