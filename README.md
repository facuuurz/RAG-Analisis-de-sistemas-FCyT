# 📚 Asistente Académico FCyT - Sistema RAG

¡Bienvenido! Este es un sistema de Inteligencia Artificial basado en RAG (Retrieval-Augmented Generation) diseñado para responder preguntas sobre las carreras de Sistemas de la FCyT (UADER) basándose estrictamente en los documentos y resoluciones oficiales.

Si nunca ejecutaste un script de Python o no sabes cómo usar este bot, ¡no te preocupes! Sigue esta guía de 3 pasos.

## 📋 Requisitos Previos

1. **Tener Python instalado:** Necesitas tener Python instalado en tu computadora. Si usas Windows, puedes descargarlo e instalarlo desde [python.org](https://www.python.org/downloads/). Asegúrate de marcar la opción "Add Python to PATH" durante la instalación.
2. **Conseguir una API Key de Google (Gratis):** 
   - Ingresa a [Google AI Studio](https://aistudio.google.com/app/apikey).
   - Inicia sesión con tu cuenta de Google.
   - Crea un "API Key" y cópialo. Es una clave secreta que luce algo así: `AIzaSy...` que le permitirá al programa hacer uso de la Inteligencia Artificial.

## 🚀 Guía de Instalación y Uso

### Paso 1: Instalar las dependencias
El programa utiliza librerías especiales para leer PDFs e Inteligencia Artificial. Para instalarlas, abre la terminal (o consola de Windows - Command Prompt / PowerShell), dirígete a la carpeta de este proyecto y ejecuta este comando:

```bash
pip install -r Requerimentos.txt
```
*(Si el comando de arriba tira un error, intenta escribir: `python -m pip install -r Requerimentos.txt`)*

### Paso 2: Agregar tus PDFs (Opcional)
Dentro de este proyecto existe una carpeta llamada `Datos`.
Si quieres agregar nuevos planes de estudio o resoluciones, simplemente arrastra tus archivos `.pdf` dentro de la carpeta `Datos`. ¡El bot los leerá y aprenderá su contenido automáticamente en la próxima ejecución!

### Paso 3: Ejecutar el Asistente
En la misma consola, ejecuta el programa principal con este comando:

```bash
python main.py
```

1. **Ingreso de Clave:** Al instante, la consola te pedirá de forma segura que ingreses tu `GOOGLE_API_KEY`. Haz "clic derecho" para pegarla o escríbela y presiona **Enter** (por seguridad, mientras pegas la clave no se verán los caracteres en la pantalla).
2. **Procesamiento Base de Datos:** Si es la primera vez que lo ejecutas, el script leerá los PDFs en la carpeta `Datos` lenta y minuciosamente para no exceder los límites gratuitos de Google. Puede demorar varios minutos. (La próxima vez que abras el programa cargará casi al instante).
3. **¡Comienza a preguntar!** Cuando veas la pantalla `SISTEMA RAG ACTIVO - LISTO PARA PREGUNTAS`, simplemente teclea tu duda (por ejemplo: *"¿Cuáles son las materias de 1er año?"*) y presiona Enter.

### 🛑 Cómo salir
Cuando quieras dejar de usar el asistente, simplemente escribe `salir` (o presiona las teclas `Ctrl + C` juntas) y el programa se cerrará.
