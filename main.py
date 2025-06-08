from sql_db_config import Session
from weather_models import Weather, Wind
from sqlalchemy.orm import joinedload

def main():
    session = Session()

    country = input("Введіть країну: ").strip()
    date = input("Введіть дату (у форматі YYYY-MM-DD): ").strip()

    # Знайти погоду з вітром за країною та датою
    weather = session.query(Weather).\
        options(joinedload(Weather.wind)).\
        filter(Weather.country == country, Weather.last_updated == date).first()

    if not weather:
        print("Дані не знайдено. Спробуйте іншу країну або дату.")
        session.close()
        return

    print("\nІнформація про вітер")
    print(f"\nКраїна: {weather.country}")
    print(f"Дата: {weather.last_updated}")
    print(f"Схід сонця: {weather.sunrise}")

    if weather.wind:
        w = weather.wind
        print("\nДані про вітер:")
        print(f"Напрям: {w.wind_direction.value}")
        print(f"Кут (градуси): {w.wind_degree}")
        print(f"Швидкість (км/год): {w.wind_kph}")
        print(f"Швидкість (миль/год): {w.wind_mph}")
        print(f"Пориви (км/год): {w.wind_gust_kph}")
        print(f"Пориви (миль/год): {w.wind_gust_mph}")

        # Висновок
        can_go_outside = "так" if w.go_outside else "ні"
        print(f"\nЧи варто виходити на вулицю? {can_go_outside}")
    else:
        print("\nДані про вітер відсутні.")

    session.close()

if __name__ == "__main__":
    main()

