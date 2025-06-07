from sqlalchemy.orm import Session
from weather_models import Weather, Wind, WindDirection
from sql_db_config import engine

session = Session(bind=engine)

weathers = session.query(Weather).all()

for w in weathers:
    if w.wind_degree is not None or w.wind_kph is not None or w.wind_mph is not None:
        wind_row = Wind(
            weather_id=w.id,
            wind_degree=w.wind_degree,
            wind_kph=w.wind_kph,
            wind_mph=w.wind_mph,
            wind_direction=WindDirection(w.wind_direction) if w.wind_direction else None,
            wind_gust_kph=w.wind_gust_kph,
            wind_gust_mph=w.wind_gust_mph,
        )
        session.add(wind_row)

session.commit()
session.close()
