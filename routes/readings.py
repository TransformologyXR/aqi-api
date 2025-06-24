from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/")
def list_readings():
    return [{"reading_id": 1, "station_id": 1, "reading_datetime": datetime.now().isoformat()}]

@router.post("/")
def create_reading():
    return {"message": "Reading created"}