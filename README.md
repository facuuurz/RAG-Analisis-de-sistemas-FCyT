# Asistente Académico FCyT - Sistema RAG

Este es un sistema de Inteligencia Artificial basado en RAG (Retrieval-Augmented Generation) diseñado para responder preguntas sobre las carreras de Sistemas de la FCyT basándose estrictamente en los documentos y resoluciones oficiales.

## Requisitos Previos

1. **Tener Python instalado:** debes tener Python instalado en tu computadora. Desde Windows, podes descargarlo e instalarlo desde [python.org](https://www.python.org/downloads/). Marcá la opción "Add Python to PATH" durante la instalación.
2. **Conseguir una API KEY de Google:** 
   - ingresa a [Google AI Studio](https://aistudio.google.com/app/apikey).
   - inicia sesión con tu cuenta de Google.
   - crea una API KEY y cópialo.

## Guía de Instalación y Uso

### Paso 1: Instalar las dependencias
El programa usa librerías especiales para leer PDFs e Inteligencia Artificial. Para instalarlas, abrí la terminal, desde la carpeta de este proyecto, y ejecuta este comando:

```bash
pip install -r Requerimentos.txt
```

### Paso 2: Agregar tus PDFs
Dentro de este proyecto existe una carpeta llamada "Datos". Si queres agregar nuevos planes de estudio o resoluciones, simplemente arrastra tus archivos dentro de la carpeta.

### Paso 3: Ejecutar el Asistente
En la misma consola, ejecuta el programa principal con este comando:

```bash
python main.py
```

1. **Ingreso de Clave:** al instante, la consola te pedirá que ingreses tu API KEY de Google.
2. **Procesamiento Base de Datos:** si es la primera vez que lo ejecutas, el script leerá los PDFs en la carpeta "Datos". Puede darse una demora.
3. **Comenza a preguntar** cuando veas la pantalla "SISTEMA RAG ACTIVO - LISTO PARA PREGUNTAS", pasale tu duda y esperá la respuesta.

### Cómo salir
Cuando quieras dejar de usar el asistente, escribí "salir" o apretá las teclas "Ctrl + C" juntas.
