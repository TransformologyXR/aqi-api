from sqlalchemy import Column, Integer, String
from app.database import Base

class Station(Base):
    __tablename__ = "aqi_stations"
    station_id = Column(Integer, primary_key=True, index=True)
    station_name = Column(String, unique=True, nullable=False)
