from pathlib import Path
import sqlite3
import pandas as pd


def extract(ruta_csv):
    """Extrae los datos desde el archivo CSV."""
    datos = pd.read_csv(ruta_csv)

    print(
        f"Extracción completada: "
        f"{datos.shape[0]} filas y {datos.shape[1]} columnas"
    )

    return datos


def transform(datos):
    """Transforma los datos y crea variables derivadas de fecha."""
    datos_transformados = datos.copy()

    datos_transformados["Datetime"] = pd.to_datetime(
        datos_transformados["Datetime"],
        errors="coerce"
    )

    if datos_transformados["Datetime"].isna().any():
        raise ValueError("El dataset contiene fechas inválidas.")

    datos_transformados["Year"] = (
        datos_transformados["Datetime"].dt.year
    )

    datos_transformados["Month"] = (
        datos_transformados["Datetime"].dt.month
    )

    datos_transformados["Day"] = (
        datos_transformados["Datetime"].dt.day
    )

    datos_transformados["Quarter"] = (
        datos_transformados["Datetime"].dt.quarter
    )

    datos_transformados["Day_of_Week"] = (
        datos_transformados["Datetime"].dt.day_name()
    )

    print(
        f"Transformación completada: "
        f"{datos_transformados.shape[0]} filas y "
        f"{datos_transformados.shape[1]} columnas"
    )

    return datos_transformados


def load(datos, ruta_db, nombre_tabla="air_quality"):
    """Carga los datos transformados en una base de datos SQLite."""
    ruta_db.parent.mkdir(parents=True, exist_ok=True)

    conexion = sqlite3.connect(ruta_db)

    try:
        datos.to_sql(
            nombre_tabla,
            conexion,
            if_exists="replace",
            index=False
        )

        conexion.commit()

    finally:
        conexion.close()

    print(
        f"Carga completada: tabla '{nombre_tabla}' "
        f"en {ruta_db}"
    )


if __name__ == "__main__":
    raiz = Path(__file__).resolve().parents[1]

    ruta_csv = (
        raiz
        / "data"
        / "raw"
        / "Air_quality_data.csv"
    )

    ruta_db = (
        raiz
        / "database"
        / "air_quality.db"
    )

    datos_extraidos = extract(ruta_csv)

    datos_transformados = transform(
        datos_extraidos
    )

    load(
        datos_transformados,
        ruta_db
    )