import pandas as pd

# Ruta del archivo CSV que se generó anteriormente
file_path = "Nivel_Inicial/data_analytics/openweather/tiempodiario_20230726.csv"  # Reemplaza con la ruta correcta

# Leer el archivo CSV y cargar los datos en un DataFrame
df = pd.read_csv(file_path)

# Mostrar las primeras filas del DataFrame de forma legible
pd.set_option('display.max_rows', None)  # Muestra todas las filas del DataFrame
pd.set_option('display.max_columns', None)  # Muestra todas las columnas del DataFrame
print(df)