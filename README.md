# Samuel Flores y Santiago Becerra

# ETL y análisis de la calidad del aire en India

## Descripción del proyecto

Este proyecto implementa un proceso ETL para analizar la calidad del aire en cinco ciudades de India entre 2015 y 2024.

El proceso incluye:

1. Extracción de datos desde un archivo CSV.
2. Validación y transformación de la información.
3. Carga de los datos en una base de datos SQLite.
4. Construcción de un modelo dimensional tipo estrella.
5. Consultas y visualizaciones realizadas directamente desde la base de datos.

## Relación con los Objetivos de Desarrollo Sostenible

El proyecto se relaciona principalmente con:

### ODS 3: Salud y bienestar

La contaminación atmosférica puede afectar la salud de las personas. El análisis permite identificar los niveles del índice de calidad del aire y la frecuencia de las categorías de contaminación.

### ODS 11: Ciudades y comunidades sostenibles

El proyecto compara la calidad del aire en diferentes ciudades y ayuda a comprender los desafíos ambientales de las zonas urbanas.

## Fuente de los datos

Los datos fueron obtenidos del siguiente dataset de Kaggle:

[AQI Air Quality Data India 2015–2024](https://www.kaggle.com/datasets/sathvikisikella/cleaned-air-quality-india)

Archivo utilizado:

```text
Air_quality_data.csv
