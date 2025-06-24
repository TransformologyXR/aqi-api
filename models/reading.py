from sqlalchemy import Column, Integer, Numeric, String, DateTime, ForeignKey
from database import Base

class Reading(Base):
    __tablename__ = "aqi_readings"
    reading_id = Column(Integer, primary_key=True, index=True)
    station_id = Column(Integer, ForeignKey("aqi_stations.station_id"), nullable=False)
    reading_datetime = Column(DateTime, nullable=False)
    no2 = Column(Numeric)
    nox = Column(Numeric)
    co = Column(Numeric)
    so2 = Column(Numeric)
    o3 = Column(Numeric)
    no = Column(Numeric)
    itemp = Column(Numeric)
    temp = Column(Numeric)
    rh = Column(Numeric)
    aqi = Column(Numeric)
    aqi_status = Column(String)
