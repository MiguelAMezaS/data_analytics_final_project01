import requests
import pandas as pd
from sqlalchemy import create_engine
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

BASE_URL = "https://api.openweathermap.org/data/2.5/onecall/timemachine?"
API_KEY = "tu_api_key"
CITIES = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao"]
DAYS = 5

def download_data(city):
    '''
    Descarga los datos meteorológicos de la ciudad especificada.
    Args:
        city (str): Nombre de la ciudad.
    Returns:
        data (dict): Datos descargados en forma de diccionario.
    '''
    url = f"{BASE_URL}q={city}&dt=1623081600&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data["hourly"]

def process_data(data, city):
    '''
    Procesa los datos descargados y los normaliza en un DataFrame.
    Args:
        data (dict): Datos descargados en forma de diccionario.
        city (str): Nombre de la ciudad.
    Returns:
        df (pandas.DataFrame): Datos normalizados en forma de DataFrame.
    '''
    df = pd.DataFrame(data)
    df["city"] = city
    df = df[["city", "dt", "temp", "humidity"]]
    return df

def update_database(df):
    '''
    Actualiza la base de datos con los nuevos datos.
    Args:
        df (pandas.DataFrame): Datos a ser actualizados en la base de datos.
    '''
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    df.to_sql("weather_data", engine, if_exists="append", index=False)

def main():
    '''
    Función principal que descarga los datos, los procesa y actualiza la base de datos para cada ciudad.
    '''
    for city in CITIES:
        data = download_data(city)
        df = process_data(data, city)
        update_database(df)

if __name__ == "__main__":
    main()