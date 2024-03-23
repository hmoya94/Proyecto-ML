# Detector de Fumadores

Este proyecto de Machine Learning tiene como objetivo predecir si una persona es fumadora o no basándose en un conjunto de características biomédicas.

## Estructura del Proyecto

El proyecto sigue la siguiente estructura de carpetas:

- `.venv`: Entorno virtual de Python con las dependencias necesarias para el proyecto.
- `src`: Contiene el código fuente del proyecto.
  - `app`: Carpeta con la aplicación Flask.
    - `app.py`: Script de la aplicación Flask para servir el modelo de ML como una API.
    - `Dockerfile`: Definiciones para construir la imagen de Docker de la aplicación Flask.
    - `requirements.txt`: Dependencias de Python requeridas para el proyecto.
  - `data`: Datos utilizados y generados por el modelo.
    - `predictions`: Predicciones realizadas por el modelo.
    - `processed`: Datos procesados listos para ser utilizados por el modelo.
    - `raw`: Datos crudos originales.
  - `model`: Modelo de Machine Learning guardado.
  - `notebooks`: Jupyter Notebooks utilizados para el análisis y desarrollo del modelo.
  - `utils`: Scripts auxiliares para el procesamiento de datos y otros.

## Instalación

Instrucciones sobre cómo instalar y configurar el entorno de desarrollo:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r src/app/requirements.txt


Para ejecutar la aplicación localmente necesitaras:
python src/app/app.py
