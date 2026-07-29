# Guía de Instalación y Uso: Asistente Virtual Académico FCyT (RAG)

Este documento explica paso a paso cómo una persona sin conocimientos previos del proyecto puede configurarlo y ejecutarlo en su computadora desde cero.

## 1. Requisitos Previos

Antes de comenzar, asegúrate de tener instalado en tu computadora:

1. **Python**: Necesitas Python 3.9 o superior. Puedes descargarlo e instalarlo desde [python.org](https://www.python.org/downloads/).
   > [!IMPORTANT]
   > Durante la instalación en Windows, asegúrate de marcar la casilla que dice **"Add Python to PATH"** (Añadir Python al PATH) antes de pulsar "Install Now".

## 2. Preparación del Proyecto

### Clonar o descargar el proyecto
1. Descarga esta carpeta del proyecto (`RAG-Analisis-de-sistemas-FCyT`) y colócala en tu escritorio o documentos.
2. Abre una terminal (Símbolo del sistema `cmd` o PowerShell) y navega hasta la carpeta del proyecto. Por ejemplo:
   ```bash
   cd ruta\hasta\la\carpeta\RAG-Analisis-de-sistemas-FCyT
   ```

### Crear un Entorno Virtual (Recomendado)
Para evitar conflictos con otras cosas que tengas instaladas, es mejor aislar este proyecto.
1. En la terminal y dentro de la carpeta del proyecto, ejecuta:
   ```bash
   python -m venv venv
   ```
2. **Activa el entorno virtual**:
   - En Windows (Command Prompt o PowerShell):
     ```bash
     venv\Scripts\activate
     ```
   - *Nota: Sabrás que funcionó porque verás un `(venv)` al principio de la línea en tu terminal.*

## 3. Instalación de Dependencias

El archivo `Requerimentos.txt` contiene todas las librerías necesarias para correr modelos de Google, interactuar con PDF y manejar la base de datos vectorial ChromaDB.

1. Con el entorno activado, instala todo ejecutando:
   ```bash
   pip install -r Requerimentos.txt
   ```
   *(Esto puede tardar unos minutos)*

## 4. Estructura de Datos

Asegúrate de que exista una carpeta llamada `Datos` dentro de la carpeta raíz del proyectoy que dentro de la misma estén los PDF académicos cargados..

## 5. Configurar la Clave de API (API Key)

El sistema utiliza la API de Google Gemini y lee la clave desde una variable de entorno. Conseguí tu key gratis en Google AI Studio y, antes de ejecutar, definila en la terminal:

```bash
# PowerShell (Windows)
$env:GOOGLE_API_KEY = "tu-api-key"
```
## 6. Ejecución del Sistema

Una vez realizados todos los pasos anteriores, estás listo para iniciar el sistema:

1. En la terminal (con el entorno `(venv)` aún activado), ejecuta:
   ```bash
   python main.py
   ```

### ¿Qué sucederá a continuación?
- **Primer inicio (Creación de Base de Datos)**: Si es la primera vez que corre, el programa empezará a leer todos los PDFs de la carpeta `Datos`, los dividirá en fragmentos y los guardará en una carpeta nueva llamada `DB_RAG_3`. Verás mensajes indicando que guarda "en lotes" y hace pausas (para proteger la cuota de la API). **Ten paciencia, este proceso puede demorar varios minutos.**
- **Inicios posteriores**: Si la carpeta `DB_RAG_3` ya existe, el sistema se la salteará conectándose instantáneamente a la base de datos guardada.

¡Listo! Cuando aparezca en consola el cuadro:
```text
==================================================
 SISTEMA RAG ACTIVO - LISTO PARA PREGUNTAS
 (Escribí 'salir' para terminar el programa)
==================================================
```
Ya puedes escribir tus preguntas sobre las materias de las carreras de Sistemas en la FCyT y el Asistente Virtual responderá.

