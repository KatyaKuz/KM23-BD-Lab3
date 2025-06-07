import pandas as pd

df = pd.read_csv("data/GlobalWeatherRepository.csv")
print(df.head())

# Вивід унікальних напрямків вітру для 1 етапу
print(df["wind_direction"].dropna().unique())
