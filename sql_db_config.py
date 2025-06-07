from sqlalchemy import create_engine

username = 'postgres'
password = 'your_password'
host = 'localhost'
database = 'lab3-weather-db'

engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}/{database}')
