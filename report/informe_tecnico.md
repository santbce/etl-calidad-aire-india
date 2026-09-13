# Informe técnico

## ETL y análisis de la calidad del aire en India

**Integrante(s):** Escribir nombres  
**Curso:** Escribir nombre del curso  
**Fecha:** Escribir fecha  

---

## Resumen

Este proyecto desarrolla un proceso ETL para organizar y analizar datos de calidad del aire registrados en cinco ciudades de India entre 2015 y 2024.

El proceso comienza con la extracción de un archivo CSV obtenido de Kaggle. Posteriormente, los datos se validan y transforman utilizando Python y Pandas. Finalmente, la información se almacena en una base de datos SQLite y se organiza mediante un modelo dimensional tipo estrella.

El análisis incluye estadísticas descriptivas, distribución de categorías de calidad del aire, evolución anual del AQI, análisis de correlación y detección de valores extremos.

Los resultados muestran que la mayoría de los registros pertenece a categorías desfavorables de calidad del aire, especialmente `Very Poor` y `Severe`.

---

## 1. Introducción

La contaminación atmosférica es un problema ambiental que puede afectar la salud de las personas y la sostenibilidad de las ciudades. Por esta razón, es importante organizar y analizar los datos relacionados con los contaminantes presentes en el aire.

Este proyecto utiliza información de cinco ciudades de India para construir un flujo de procesamiento de datos que permita consultar, comparar y visualizar diferentes indicadores de calidad del aire.

El proyecto se desarrolla desde cero utilizando Python, Pandas, SQLite, SQL, Jupyter Notebook y GitHub.

---

## 2. Objetivos

### 2.1 Objetivo general

Construir un proceso ETL para almacenar y analizar información de calidad del aire de cinco ciudades de India entre 2015 y 2024.

### 2.2 Objetivos específicos

- Extraer los datos desde un archivo CSV.
- Validar la estructura, las fechas, los valores nulos y los duplicados.
- Transformar las fechas y crear variables temporales.
- Cargar la información en una base de datos SQLite.
- Diseñar un modelo dimensional tipo estrella.
- Consultar los datos mediante SQL.
- Construir visualizaciones a partir de la base de datos.
- Identificar patrones en el AQI y en los contaminantes atmosféricos.

---

## 3. Relación con los Objetivos de Desarrollo Sostenible

### ODS 3: Salud y bienestar

La contaminación del aire puede afectar la salud de las personas. El análisis del AQI permite identificar la frecuencia de diferentes niveles de calidad del aire y reconocer la presencia de condiciones desfavorables.

### ODS 11: Ciudades y comunidades sostenibles

Las ciudades sostenibles requieren información para monitorear sus condiciones ambientales. La comparación entre ciudades permite observar diferencias y patrones en la calidad del aire urbano.

---

## 4. Fuente y descripción de los datos

Los datos fueron obtenidos del siguiente dataset de Kaggle:

[AQI Air Quality Data India 2015–2024](https://www.kaggle.com/datasets/sathvikisikella/cleaned-air-quality-india)

Archivo utilizado:

```text
Air_quality_data.csv