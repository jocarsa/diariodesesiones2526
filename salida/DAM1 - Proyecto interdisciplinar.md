# Informe de clases – DAM1 - Proyecto interdisciplinar

_Generado automáticamente. Vídeos incluidos: 7._

## Índice

1. [2025 09 22 16 31 33](#2025-09-22-16-31-33)
2. [2025 09 22 16 47 55](#2025-09-22-16-47-55)
3. [2025 09 29 16 00 24](#2025-09-29-16-00-24)
4. [2025 10 06 16 49 29](#2025-10-06-16-49-29)
5. [2025 10 13 16 50 53](#2025-10-13-16-50-53)
6. [2025 10 20 16 29 39](#2025-10-20-16-29-39)
7. [2025 10 20 16 56 04](#2025-10-20-16-56-04)

---

## 2025 09 22 16 31 33

**Fecha/Hora:** 2025-09-22 16:31:33

**Día (ES):** lunes

**Enlace:** https://www.youtube.com/watch?v=Hu7QwWz_BQw

**Resumen Extenso: Instalación de Sistemas Operativos y Virtualización**

**Objetivos**

* Comprender el proceso de instalación de sistemas operativos en un entorno virtualizado.
* Conocer las herramientas y tecnologías necesarias para realizar una instalación segura y efectiva.

**Conceptos Clave**

* **Virtualización**: la capacidad de emular un sistema operativo dentro de otro, permitiendo la creación de máquinas virtuales (VMs) con características similares a las del hardware físico.
* **Máquina Virtual** (VM): una entidad virtual que simula el comportamiento de un sistema operativo en un entorno físico.
* **Herramientas de virtualización**: software que permite la creación y gestión de VMs, como Oracle Virtual Box.

**Explicación Didáctica**

La instalación de sistemas operativos en un entorno virtualizado es un proceso fundamental en la administración de sistemas informáticos. A continuación, se presentan los pasos para realizar una instalación segura y efectiva utilizando herramientas de virtualización como Oracle Virtual Box.

### Paso 1: Descargar el Media de Instalación

* **ISO Image**: el formato estándar para almacenar la imagen de un disco óptico.
* **Descarga del media de instalación**: se puede descargar desde Internet o utilizar una copia física del disco.
```bash
# Ejemplo de descarga de Ubuntu Desktop
wget https://ubuntu.com/download/desktop/thunderbird?lang=es
```

### Paso 2: Crear una Máquina Virtual

* **Oracle Virtual Box**: herramienta de virtualización para crear y gestionar máquinas virtuales.
* **Crear una nueva VM**: seleccionar el tipo de sistema operativo, la cantidad de RAM y el tamaño del disco duro.
```python
# Ejemplo de creación de una nueva VM en Virtual Box
new_vm = vbox.create_machine(
    name='Ubuntu Linux',
    os_type='Linux',
    ram=4096,
    hd_size=125000)
```

### Paso 3: Configurar la Máquina Virtual

* **Configuración de la VM**: seleccionar el tipo de sistema operativo, la cantidad de RAM y el tamaño del disco duro.
* **ISO Image**: seleccionar la imagen de instalación del sistema operativo.
```bash
# Ejemplo de configuración de la VM en Virtual Box
vbox.set_machine_property(
    new_vm,
    'boot1',
    'Ubuntu Desktop')
```

### Paso 4: Iniciar la Instalación

* **Iniciar la instalación**: iniciar el proceso de instalación del sistema operativo.
```bash
# Ejemplo de inicio de la instalación en Virtual Box
vbox.start_machine(new_vm)
```

**Buenas Prácticas**

* Utilizar herramientas de virtualización como Oracle Virtual Box para crear y gestionar máquinas virtuales.
* Descargar el media de instalación desde Internet o utilizar una copia física del disco.
* Crear una nueva VM con características similares al hardware físico.
* Configurar la VM seleccionando el tipo de sistema operativo, la cantidad de RAM y el tamaño del disco duro.
* Iniciar la instalación del sistema operativo.

**Conclusión**

La instalación de sistemas operativos en un entorno virtualizado es un proceso fundamental en la administración de sistemas informáticos. Al seguir los pasos y recomendaciones presentadas en este resumen, se puede realizar una instalación segura y efectiva utilizando herramientas de virtualización como Oracle Virtual Box.

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

_No hay subtítulos disponibles._

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

## 2025 10 20 16 29 39

**Fecha/Hora:** 2025-10-20 16:29:39

**Día (ES):** lunes

**Enlace:** https://www.youtube.com/watch?v=-eKMWDFRw1M

_No hay subtítulos disponibles._

---

## 2025 10 20 16 56 04

**Fecha/Hora:** 2025-10-20 16:56:04

**Día (ES):** lunes

**Enlace:** https://www.youtube.com/watch?v=6NdDZ2nxS9I

**Resumen Extenso: 2025 10 20 16 56 04**

**Objetivos del Taller**

* Comprender cómo aplicar los conceptos aprendidos en el proyecto intermodular dentro de sistemas informáticos.
* Aprender a mover software desde un entorno de desarrollo a producción utilizando herramientas como FileCilla y SFTP.

**Conceptos Clave**

* **Servidor**: Un programa que ejecuta una aplicación en un entorno de producción.
* **Entorno de Desarrollo**: El lugar donde se crea y prueba el software antes de lanzarlo al público.
* **Entorno de Producción**: El lugar donde se ejecuta el software después de haber sido probado y aprobado.
* **FileCilla**: Una herramienta que permite transferir archivos entre un entorno local y un servidor remoto utilizando SFTP (Secure File Transfer Protocol).
* **SFTP**: Un protocolo de seguridad para transferir archivos entre dos puntos.

**Explicación Didáctica**

El profesor comienza explicando que el objetivo del taller es aplicar los conceptos aprendidos en el proyecto intermodular dentro de sistemas informáticos. Se enfoca en la creación de un servidor y su posterior lanzamiento a producción, utilizando herramientas como FileCilla y SFTP.

**Pasos para Mover Software desde Desarrollo a Producción**

1. **Crear un Nuevo Directorio**: En el entorno local, se crea un nuevo directorio llamado "producción" donde se almacenarán los archivos del proyecto.
2. **Transferir Archivos con FileCilla**: Se utiliza FileCilla para transferir los archivos del proyecto desde el entorno local al servidor remoto, utilizando SFTP como protocolo de seguridad.
3. **Configurar el Servidor**: Se configura el servidor para que pueda ejecutar la aplicación creada en el entorno de desarrollo.

**Explicación de Buenas Prácticas**

El profesor destaca la importancia de seguir buenas prácticas al mover software desde un entorno de desarrollo a producción. Algunas de estas prácticas incluyen:

* **Crear un Entorno de Producción**: Es importante crear un entorno de producción separado del entorno de desarrollo para evitar conflictos y problemas.
* **Utilizar Herramientas Seguras**: Se debe utilizar herramientas seguras como FileCilla y SFTP para transferir archivos entre el entorno local y el servidor remoto.
* **Configurar el Servidor Correctamente**: Es crucial configurar el servidor correctamente para que pueda ejecutar la aplicación creada en el entorno de desarrollo.

**Explicación del Gráfico de Aprendizaje**

El profesor presenta un gráfico que representa la relación entre esfuerzo y resultado en la aprendizaje de programación. El gráfico muestra cómo, al principio, se aplica mucho esfuerzo pero se obtienen resultados limitados. Sin embargo, a medida que se avanza, el esfuerzo se vuelve más efectivo y los resultados aumentan.

**Resumen**

En resumen, este taller busca enseñar a los estudiantes cómo aplicar los conceptos aprendidos en el proyecto intermodular dentro de sistemas informáticos. Se enfoca en la creación de un servidor y su posterior lanzamiento a producción utilizando herramientas como FileCilla y SFTP. El profesor destaca la importancia de seguir buenas prácticas al mover software desde un entorno de desarrollo a producción y presenta un gráfico que representa la relación entre esfuerzo y resultado en la aprendizaje de programación.

**Tarea**

* Escribe un resumen extenso (aprox. 450-700 palabras) de este taller.
* Incluye objetivos, conceptos clave, explicación didáctica, pasos/comandos si aparecen, y buenas prácticas.
* Usa bullets cuando mejore la claridad.
* Si hay fragmentos de código, usa bloques con triple backtick y el lenguaje correcto (```python```, ```bash```, ```js```, etc.).
* No inventes APIs ni resultados; si algo es incompleto, indícalo brevemente.

**Conclusión**

Este taller busca brindar a los estudiantes una comprensión profunda de cómo aplicar los conceptos aprendidos en el proyecto intermodular dentro de sistemas informáticos. Al seguir las buenas prácticas y utilizar herramientas seguras, los estudiantes pueden asegurarse de que su software sea lanzado con éxito al mercado.

---
