from pathlib import Path
import sqlite3
import pandas as pd


def leer_datos_base(conexion):
    """Lee la tabla plana creada durante la fase ETL."""
    datos = pd.read_sql_query(
        "SELECT * FROM air_quality",
        conexion
    )

    datos["Datetime"] = pd.to_datetime(
        datos["Datetime"],
        errors="coerce"
    )

    if datos["Datetime"].isna().any():
        raise ValueError("Existen fechas inválidas en la tabla air_quality.")

    datos["datetime_key"] = datos["Datetime"].dt.strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    return datos


def construir_dimensiones(datos):
    """Construye las dimensiones del modelo estrella."""

    dim_city = (
        datos[["City"]]
        .drop_duplicates()
        .sort_values("City")
        .reset_index(drop=True)
    )

    dim_city.insert(
        0,
        "city_id",
        range(1, len(dim_city) + 1)
    )

    dim_city = dim_city.rename(
        columns={"City": "city_name"}
    )

    dim_date = (
        datos[
            [
                "datetime_key",
                "Year",
                "Month",
                "Day",
                "Quarter",
                "Day_of_Week",
            ]
        ]
        .drop_duplicates(subset=["datetime_key"])
        .sort_values("datetime_key")
        .reset_index(drop=True)
    )

    dim_date.insert(
        0,
        "date_id",
        range(1, len(dim_date) + 1)
    )

    dim_date = dim_date.rename(
        columns={
            "datetime_key": "full_datetime",
            "Year": "year",
            "Month": "month",
            "Day": "day",
            "Quarter": "quarter",
            "Day_of_Week": "day_of_week",
        }
    )

    dim_aqi = (
        datos[["AQI_Bucket"]]
        .drop_duplicates()
        .sort_values("AQI_Bucket")
        .reset_index(drop=True)
    )

    dim_aqi.insert(
        0,
        "aqi_id",
        range(1, len(dim_aqi) + 1)
    )

    dim_aqi = dim_aqi.rename(
        columns={"AQI_Bucket": "aqi_bucket"}
    )

    return dim_city, dim_date, dim_aqi


def construir_tabla_hechos(
    datos,
    dim_city,
    dim_date,
    dim_aqi
):
    """Relaciona las dimensiones y construye la tabla de hechos."""

    hechos = (
        datos
        .merge(
            dim_city,
            left_on="City",
            right_on="city_name",
            how="left",
            validate="many_to_one"
        )
        .merge(
            dim_date[["date_id", "full_datetime"]],
            left_on="datetime_key",
            right_on="full_datetime",
            how="left",
            validate="many_to_one"
        )
        .merge(
            dim_aqi,
            left_on="AQI_Bucket",
            right_on="aqi_bucket",
            how="left",
            validate="many_to_one"
        )
    )

    columnas_clave = [
        "city_id",
        "date_id",
        "aqi_id",
    ]

    if hechos[columnas_clave].isna().any().any():
        raise ValueError(
            "Hay registros sin correspondencia en alguna dimensión."
        )

    hechos = hechos.rename(
        columns={
            "datetime_key": "datetime",
            "PM2.5": "pm25",
            "PM10": "pm10",
            "NO": "no_value",
            "NO2": "no2",
            "NOx": "nox",
            "NH3": "nh3",
            "CO": "co",
            "SO2": "so2",
            "O3": "o3",
            "AQI": "aqi",
        }
    )

    hechos.insert(
        0,
        "measurement_id",
        range(1, len(hechos) + 1)
    )

    columnas_finales = [
        "measurement_id",
        "city_id",
        "date_id",
        "aqi_id",
        "datetime",
        "pm25",
        "pm10",
        "no_value",
        "no2",
        "nox",
        "nh3",
        "co",
        "so2",
        "o3",
        "aqi",
    ]

    return hechos[columnas_finales]


def cargar_tablas(
    conexion,
    dim_city,
    dim_date,
    dim_aqi,
    hechos
):
    """Carga las dimensiones y la tabla de hechos en SQLite."""

    conexion.execute("DELETE FROM fact_air_quality")
    conexion.execute("DELETE FROM dim_city")
    conexion.execute("DELETE FROM dim_date")
    conexion.execute("DELETE FROM dim_aqi")

    dim_city.to_sql(
        "dim_city",
        conexion,
        if_exists="append",
        index=False
    )

    dim_date.to_sql(
        "dim_date",
        conexion,
        if_exists="append",
        index=False
    )

    dim_aqi.to_sql(
        "dim_aqi",
        conexion,
        if_exists="append",
        index=False
    )

    hechos.to_sql(
        "fact_air_quality",
        conexion,
        if_exists="append",
        index=False
    )

    conexion.commit()


if __name__ == "__main__":
    raiz = Path(__file__).resolve().parents[1]
    ruta_db = raiz / "database" / "air_quality.db"
    ruta_schema = raiz / "sql" / "schema.sql"

    conexion = sqlite3.connect(ruta_db)
    conexion.execute("PRAGMA foreign_keys = ON")

    # Garantiza que el esquema exista antes de cargar los datos.
    conexion.executescript(
        ruta_schema.read_text(encoding="utf-8")
    )

    datos = leer_datos_base(conexion)

    dim_city, dim_date, dim_aqi = construir_dimensiones(
        datos
    )

    hechos = construir_tabla_hechos(
        datos,
        dim_city,
        dim_date,
        dim_aqi
    )

    cargar_tablas(
        conexion,
        dim_city,
        dim_date,
        dim_aqi,
        hechos
    )

    print(f"dim_city: {len(dim_city)} registros")
    print(f"dim_date: {len(dim_date)} registros")
    print(f"dim_aqi: {len(dim_aqi)} registros")
    print(f"fact_air_quality: {len(hechos)} registros")

    conexion.close()