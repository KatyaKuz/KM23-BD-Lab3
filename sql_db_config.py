from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

username = 'postgres'
password = 'your_password'
host = 'localhost'
database = 'lab3-weather-db'

engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}/{database}')
Session = sessionmaker(bind=engine)
