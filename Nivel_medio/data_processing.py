import pandas as pd
from sqlalchemy import create_engine
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
def process_data():
    '''
    Procesa los datos en la tabla weather_data y los normaliza en una nueva tabla weather_data_normalized.
    '''
    df = pd.read_sql_table("weather_data", engine)
    df["date"] = pd.to_datetime(df["dt"], unit="s")
    df["temp"] = df["temp"] - 273.15
    df = df[["city", "date", "temp", "humidity"]]
    df.to_sql("weather_data_normalized", engine, if_exists="replace", index=False)
process_data()