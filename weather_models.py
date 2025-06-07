from sqlalchemy.orm import declarative_base
from sqlalchemy import (Column, Integer, Float, String, Date, Time, Enum )
import enum

Base = declarative_base()

class WindDirection(enum.Enum):
    N = "N"
    NNE = "NNE"
    NE = "NE"
    ENE = "ENE"
    E = "E"
    ESE = "ESE"
    SE = "SE"
    SSE = "SSE"
    S = "S"
    SSW = "SSW"
    SW = "SW"
    WSW = "WSW"
    W = "W"
    WNW = "WNW"
    NW = "NW"
    NNW = "NNW"

class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True)
    country = Column(String, nullable=False) # текст
    last_updated = Column(Date) # дата
    sunrise = Column(Time) # час

    wind_degree = Column(Integer)# ціле
    wind_kph = Column(Float)# дробне
    wind_mph = Column(Float)
    wind_direction = Column(Enum(WindDirection))# enum
    wind_gust_mph = Column(Float)
    wind_gust_kph = Column(Float)
