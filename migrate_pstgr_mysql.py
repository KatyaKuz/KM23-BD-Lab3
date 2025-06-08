from sqlalchemy.orm import sessionmaker
from weather_models import Base, Weather, Wind
from sql_db_config import pg_engine, mysql_engine

# Створення сесій
PostgresSession = sessionmaker(bind=pg_engine)
MySQLSession = sessionmaker(bind=mysql_engine)

pg_session = PostgresSession()
mysql_session = MySQLSession()

# Міграція Weather
pg_weather_data = pg_session.query(Weather).all()

weather_id_map = {}

for weather in pg_weather_data:
    new_weather = Weather(
        id=weather.id,
        country=weather.country,
        last_updated=weather.last_updated,
        sunrise=weather.sunrise
    )
    mysql_session.add(new_weather)
    mysql_session.flush()
    weather_id_map[weather.id] = new_weather.id

mysql_session.commit()

#Міграція Wind
pg_wind_data = pg_session.query(Wind).all()

for wind in pg_wind_data:
    new_wind = Wind(
        id=wind.id,
        weather_id=weather_id_map[wind.weather_id],
        wind_degree=wind.wind_degree,
        wind_kph=wind.wind_kph,
        wind_mph=wind.wind_mph,
        wind_direction=wind.wind_direction,
        wind_gust_kph=wind.wind_gust_kph,
        wind_gust_mph=wind.wind_gust_mph,
        go_outside=wind.go_outside
    )
    mysql_session.add(new_wind)


mysql_session.commit()

print("Успішно перенесли дані Wind та Weather з PostgreSQL у MySQL.")

# Закриває сесії
pg_session.close()
mysql_session.close()

