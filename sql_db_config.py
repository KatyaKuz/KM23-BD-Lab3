from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

host = 'localhost'

# PostgreSQL
username_pst = 'postgres'
password_pst = 'your_password'
database_pst = 'lab3-weather-db'

pg_engine = create_engine(f'postgresql+psycopg2://{username_pst}:{password_pst}@{host}/{database_pst}')
PGSession = sessionmaker(bind=pg_engine)

# MySQL
username_mysql = 'root'
password_mysql = 'your_password'
database_mysql = 'lab3_weather_mysql'

mysql_engine = create_engine(f'mysql+pymysql://{username_mysql}:{password_mysql}@{host}:3306/{database_mysql}')
MySQLSession = sessionmaker(bind=mysql_engine)

DB_TYPE = "postgresql"  # або "mysql" або "postgresql"

if DB_TYPE == "postgresql":
    Session = PGSession
elif DB_TYPE == "mysql":
    Session = MySQLSession
