from fastapi import FastAPI
from routes import stations, readings

app = FastAPI()

app.include_router(stations.router, prefix="/stations", tags=["Stations"])
app.include_router(readings.router, prefix="/readings", tags=["Readings"])
