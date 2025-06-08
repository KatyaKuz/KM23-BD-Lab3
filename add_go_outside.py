from sqlalchemy.orm import Session
from weather_models import Wind
from sql_db_config import engine

with Session(engine) as session:
    winds = session.query(Wind).all()
    for w in winds:
        # Всі значення або 0, якщо None(перевіряємо навсяк випадок)
        wind_kph = w.wind_kph or 0
        wind_mph = w.wind_mph or 0
        gust_kph = w.wind_gust_kph or 0
        gust_mph = w.wind_gust_mph or 0

        # умови взято зі шкали Бофорта
        # - якщо швидкість вітру > 36 км/год або > 22.37 миль/год
        # - якщо пориви вітру > 50 км/год або > 31 миль/год
        if wind_kph > 36 or wind_mph > 22.37 or gust_kph > 50 or gust_mph > 31:
            w.go_outside = False
        else:
            w.go_outside = True
    session.commit()