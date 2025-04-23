import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/CAChemE/curso-python-datos/master/data/weather_data.csv"
df = pd.read_csv(url)

#pasar los datos fecha de string a datatime
df['fecha'] = pd.to_datetime(df['fecha'])
print("\nTipo de dato de la columna 'fecha':", df['fecha'].dtype)

##limpiar datos con values y 0
df.replace('Varias', pd.NA, inplace = True)  
df = df.replace(0, pd.NA)  
df.dropna(inplace = True) 
df.info()
df.dropna()

print(df.shape)
# La temperatura media del período registrado.
temperatura_media = df['tmed'].mean()
print(f"\nTemperatura media del período: {temperatura_media:.2f} °C")

# La temperatura máxima y la fecha en la que ocurrió.
max_temp = df['tmax'].max()
fecha_max_temp = df['fecha'][df['tmax'] == max_temp].iloc[0]
print(f"Temperatura máxima: {max_temp:.2f} °C, ocurrida el: {fecha_max_temp.strftime('%Y-%m-%d')}")

# La temperatura mínima y la fecha en la que ocurrió.
min_temp = df['tmin'].min()
fecha_min_temp = df['fecha'][df['tmin'] == min_temp].iloc[0]
print(f"Temperatura mínima: {min_temp:.2f} °C, ocurrida el: {fecha_min_temp.strftime('%Y-%m-%d')}")

# El rango de temperatura (máxima - mínima).
rango_temp = max_temp - min_temp
print(f"Rango de temperatura: {rango_temp:.2f} °C")


# grafica de líneas que muestre la evolución de la temperatura máxima y mínima a lo largo del tiempo.
plt.figure(figsize=(12, 6))
plt.plot(df['fecha'], df['tmax'], label='Temperatura Máxima', color='red')
plt.plot(df['fecha'], df['tmin'], label='Temperatura Mínima', color='blue')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.title('Evolución de la Temperatura Máxima y Mínima a lo largo del Tiempo')
plt.legend()
plt.grid(True)
plt.show()

# Un boxplot de la temperatura media.
plt.figure(figsize=(8, 6))
sns.boxplot(y=df['tmed'])
plt.ylim(10, 20)
plt.title('Distribución de la Temperatura Media')
plt.grid(True)
plt.show()

# diagrma de calor de las variables climáticas
numeric_df = df[['altitud', 'prec', 'presMax', 'presMin', 'racha', 'sol', 'tmax', 'tmed', 'tmin', 'velmedia']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_df, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de Correlaciones entre Variables Climáticas Relevantes')
plt.show()

# diagrama de las cuatro varibles 
sns.pairplot(df[['tmax','tmed', 'tmin', 'presMin', 'presMax']])
plt.suptitle('Diagrama de Dispersión entre Tmax, Tmin, Precipitación y Velocidad Media', y=1.02)
plt.show()
