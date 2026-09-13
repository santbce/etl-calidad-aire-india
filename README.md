# ETL y análisis de la calidad del aire en India

**Integrantes:**  
Samuel Flores  
Santiago Becerra  

---

# Descripción del proyecto

Este proyecto implementa un proceso ETL (Extract, Transform, Load) para analizar la calidad del aire en cinco ciudades de India entre los años 2015 y 2024.

El objetivo principal es transformar datos ambientales en información organizada que permita estudiar el comportamiento del AQI (Air Quality Index), los contaminantes presentes y las condiciones generales de calidad del aire.

El proceso desarrollado incluye:

1. Extracción de datos desde un archivo CSV.
2. Exploración y validación inicial de la información.
3. Transformación de variables y creación de datos temporales.
4. Carga de los datos en una base de datos SQLite.
5. Construcción de un modelo dimensional tipo estrella.
6. Consultas SQL y análisis realizados directamente desde la base de datos.
7. Creación de visualizaciones para interpretar los resultados.

---

# Relación con los Objetivos de Desarrollo Sostenible

El proyecto se relaciona principalmente con los siguientes Objetivos de Desarrollo Sostenible:

## ODS 3: Salud y bienestar

La contaminación atmosférica puede afectar la salud de las personas. El análisis de los niveles del AQI permite identificar condiciones desfavorables de calidad del aire y estudiar la frecuencia de categorías de contaminación.

## ODS 11: Ciudades y comunidades sostenibles

El análisis de información ambiental permite comparar la calidad del aire entre ciudades y comprender algunos de los desafíos ambientales presentes en zonas urbanas.

---

# Fuente de los datos

Los datos fueron obtenidos del siguiente dataset de Kaggle:

AQI Air Quality Data India 2015–2024

https://www.kaggle.com/datasets/sathvikisikella/cleaned-air-quality-india

Archivo utilizado:

Air_quality_data.csv

Características principales del dataset:

- 18.265 registros.
- 13 variables originales.
- Información desde 2015 hasta 2024.
- Cinco ciudades:
  - Delhi
  - Mumbai
  - Chennai
  - Kolkata
  - Bangalore

Variables principales:

- PM2.5
- PM10
- NO
- NO2
- NOx
- NH3
- CO
- SO2
- O3
- AQI
- AQI_Bucket

---

# Arquitectura del proyecto

El flujo implementado corresponde a una arquitectura ETL:

Archivo CSV

↓

Extracción con Python

↓

Validación y transformación de datos

↓

Base de datos SQLite

↓

Modelo dimensional estrella

↓

Consultas SQL

↓

Visualizaciones y análisis

---

# Estructura del proyecto

etl-calidad-aire-india/

├── data/

│   └── raw/

│       └── Air_quality_data.csv

├── database/

│   └── air_quality.db

├── notebooks/

│   ├── 01_exploracion_inicial.ipynb

│   └── 02_analisis_desde_bd.ipynb

├── src/

│   ├── etl.py

│   └── cargar_modelo_dimensional.py

├── sql/

│   └── schema.sql

├── report/

│   ├── informe_tecnico.md

│   └── figuras/

├── requirements.txt

└── README.md

---

# Tecnologías utilizadas

## Python

Utilizado para desarrollar el proceso ETL, transformación y procesamiento de datos.

## Pandas

Utilizado para lectura, limpieza y transformación del dataset.

## NumPy

Utilizado para operaciones numéricas.

## SQLite

Utilizado como base de datos relacional para almacenar los datos procesados.

## SQL

Utilizado para crear consultas, organizar la información y construir el modelo dimensional.

## Jupyter Notebook

Utilizado para exploración de datos, análisis y generación de resultados.

## Matplotlib y Seaborn

Utilizados para crear las visualizaciones del análisis.

## Git y GitHub

Utilizados para control de versiones y almacenamiento del proyecto.

---

# Modelo dimensional

El proyecto implementa un modelo estrella compuesto por:

## Tabla de hechos

### fact_air_quality

Contiene las mediciones principales:

- PM2.5
- PM10
- NO
- NO2
- NOx
- NH3
- CO
- SO2
- O3
- AQI

## Tablas de dimensiones

### dim_city

Contiene la información de las ciudades analizadas.

### dim_date

Contiene la información temporal:

- año
- mes
- día
- trimestre
- día de la semana

### dim_aqi

Contiene las categorías de calidad del aire.

---

# Instalación

Clonar el repositorio:

git clone https://github.com/santbce/etl-calidad-aire-india.git

Ingresar a la carpeta del proyecto:

cd etl-calidad-aire-india

Instalar las dependencias:

pip install -r requirements.txt

---

# Ejecución del proyecto

## 1. Ejecutar proceso ETL

python src/etl.py

Este proceso realiza:

- Lectura del archivo CSV.
- Validación de datos.
- Transformación de fechas.
- Creación de variables temporales.
- Carga de información en SQLite.

---

## 2. Crear modelo dimensional

python src/cargar_modelo_dimensional.py

Este proceso genera:

- dim_city
- dim_date
- dim_aqi
- fact_air_quality

---

## 3. Ejecutar análisis

Los análisis se encuentran en:

notebooks/01_exploracion_inicial.ipynb

notebooks/02_analisis_desde_bd.ipynb

Las consultas y visualizaciones utilizan los datos almacenados en la base de datos SQLite.

---

# Análisis realizado

Durante el proyecto se realizaron:

- Revisión de estructura del dataset.
- Identificación de valores nulos.
- Detección de registros duplicados.
- Validación de fechas.
- Estadísticas descriptivas.
- Distribución de categorías AQI.
- Comparación del AQI entre ciudades.
- Evolución temporal del AQI.
- Correlación entre contaminantes.
- Análisis de distribución mediante diagramas de caja.

---

# Resultados principales

Los principales resultados obtenidos fueron:

- AQI promedio general aproximado de 317.51.
- Las categorías más frecuentes fueron Very Poor y Severe.
- Las ciudades presentan valores promedio de AQI similares.
- PM10 presentó la mayor relación con el AQI, aunque con una correlación débil.
- La mayoría de registros representan condiciones poco favorables de calidad del aire.

---

# Limitaciones

- El dataset no especifica todas las unidades de medida de las variables.
- Los datos provienen de Kaggle y presentan una estructura previamente organizada.
- Las correlaciones encontradas representan asociaciones y no causalidad.
- El análisis solo incluye cinco ciudades de India.
- No se incluyen variables meteorológicas o demográficas.

---

# Autores

Samuel Flores  
Santiago Becerra
