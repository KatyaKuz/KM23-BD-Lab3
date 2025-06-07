from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import (Column, Integer, Float, String, Date, Time, Enum, ForeignKey )
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

    wind = relationship("Wind", back_populates="weather", uselist=False)

class Wind(Base):
    __tablename__ = 'wind'
    
    id = Column(Integer, primary_key=True)
    weather_id = Column(Integer, ForeignKey('weather.id'), nullable=False)  # зовнішній ключ weather_id

    wind_degree = Column(Integer)# ціле
    wind_kph = Column(Float)# дробне
    wind_mph = Column(Float)
    wind_direction = Column(Enum(WindDirection))# enum
    wind_gust_mph = Column(Float)
    wind_gust_kph = Column(Float)

    weather = relationship("Weather", back_populates="wind")
