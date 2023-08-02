import pandas as pd
import matplotlib.pyplot as plt
 # Ruta del archivo CSV que se generó anteriormente
file_path = "Nivel_Inicial/data_analytics/openweather/tiempodiario_20230726.csv"  # Reemplaza con la ruta correcta
 # Leer el archivo CSV y cargar los datos en un DataFrame
df = pd.read_csv(file_path)
 # Graficar una columna específica (por ejemplo, temperatura)
plt.plot(df['Fecha'], df['Temperatura'])
plt.xlabel('Fecha')
plt.ylabel('Temperatura')
plt.title('Variación de temperatura')
plt.xticks(rotation=45)  # Rotar las etiquetas del eje x para mayor legibilidad
plt.show()