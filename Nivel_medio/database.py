from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
Base = declarative_base()
class WeatherData(Base):
    '''
    Clase que representa la estructura de la tabla weather_data en la base de datos.
    '''
    __tablename__ = "weather_data"
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String)
    dt = Column(Integer)
    temp = Column(Float)
    humidity = Column(Integer)
Base.metadata.create_all(engine)