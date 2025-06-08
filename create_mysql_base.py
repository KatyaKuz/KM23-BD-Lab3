from sql_db_config import mysql_engine
from weather_models import Base

Base.metadata.create_all(mysql_engine)
print("Таблиці створені в MySQL.") #Викоується -> все добре