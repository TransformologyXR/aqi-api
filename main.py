from fastapi import FastAPI
from app.routes import stations, readings

app = FastAPI(title="AQI API")

app.include_router(stations.router, prefix="/stations", tags=["Stations"])
app.include_router(readings.router, prefix="/readings", tags=["Readings"])