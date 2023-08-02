from datetime import datetime
from dotenv import load_dotenv
import os
import requests
import pandas as pd
from pandas import json_normalize
import json

load_dotenv()
api_key = os.getenv('API_KEY')

# Definir la URL base de la API
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# Lista de ciudades y coordenadas
cityList = ["London", "New York", "Cordoba", "Taipei", "Buenos Aires", "Mexico DF", "Dublin", "Tilfis", "Bogota", "Tokio"]
coordList = ["lat=31&lon=64", "lat=40&lon=-73", "lat=-31&lon=-64", "lat=25&lon=64", "lat=-34&lon=-58", "lat=19&lon=-99", "lat=53&lon=6", "lat=41&lon=44", "lat=4&lon=74", "lat=35&lon=139"]

# Obtener los datos del clima para cada ciudad
for city, coord in zip(cityList, coordList):

    # Obtener la fecha actual
    now = datetime.now()
    date = now.strftime("%Y%m%d")

    # Construir la URL de la solicitud HTTP
    url = f"{BASE_URL}?q={city}&{coord}&appid=api_key"

    # Hacer la solicitud HTTP y obtener la respuesta en formato JSON
    response = requests.get(url)
    data = response.json()

    # Convertir los datos JSON a un DataFrame de pandas
    df = json_normalize(data)
    #print(df)

    # Definir la ruta de almacenamiento del archivo CSV
    file_path = f"Nivel_Inicial/data_analytics/openweather/tiempodiario_{date}.csv"
    
    # Guardar el DataFrame como archivo CSV localmente
    df.to_csv(file_path, index=False)