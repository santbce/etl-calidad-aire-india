PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS fact_air_quality;
DROP TABLE IF EXISTS dim_city;
DROP TABLE IF EXISTS dim_date;
DROP TABLE IF EXISTS dim_aqi;

CREATE TABLE dim_city (
    city_id INTEGER PRIMARY KEY,
    city_name TEXT NOT NULL UNIQUE
);

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    full_datetime TEXT NOT NULL UNIQUE,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL,
    quarter INTEGER NOT NULL,
    day_of_week TEXT NOT NULL
);

CREATE TABLE dim_aqi (
    aqi_id INTEGER PRIMARY KEY,
    aqi_bucket TEXT NOT NULL UNIQUE
);

CREATE TABLE fact_air_quality (
    measurement_id INTEGER PRIMARY KEY,
    city_id INTEGER NOT NULL,
    date_id INTEGER NOT NULL,
    aqi_id INTEGER NOT NULL,
    datetime TEXT NOT NULL,
    pm25 REAL,
    pm10 REAL,
    no_value REAL,
    no2 REAL,
    nox REAL,
    nh3 REAL,
    co REAL,
    so2 REAL,
    o3 REAL,
    aqi REAL,

    FOREIGN KEY (city_id) REFERENCES dim_city(city_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id),
    FOREIGN KEY (aqi_id) REFERENCES dim_aqi(aqi_id)
);