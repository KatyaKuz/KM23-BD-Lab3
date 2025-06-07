import pandas as pd
from datetime import datetime
from nogit_sql_db_config import engine, Session
from weather_models import Base, Weather, WindDirection

# Створює таблицю, якщо її нема
Base.metadata.create_all(engine)

df = pd.read_csv("data/GlobalWeatherRepository.csv")

#Фільтрує та готує дані
records = []
valid_dirs = set(item.value for item in WindDirection) # Створює множину усіх можливих значень напрямків вітру з WindDirection

for _, row in df.iterrows():
    if row['wind_direction'] not in valid_dirs:
        continue  # пропускає невалідні значення напряму вітру

    records.append(Weather(
        country        = row['country'],
        last_updated   = datetime.strptime(row['last_updated'], '%Y-%m-%d %H:%M').date(),
        sunrise        = datetime.strptime(row['sunrise'], '%H:%M %p').time(),
        wind_degree    = int(row['wind_degree']),
        wind_kph       = float(row['wind_kph']),
        wind_mph       = float(row['wind_mph']),
        wind_direction = WindDirection(row['wind_direction']),
        wind_gust_mph  = float(row['gust_mph']),
        wind_gust_kph  = float(row['gust_kph'])
    ))

#Зберігає в базу
session = Session()
session.add_all(records)
session.commit()
session.close()
