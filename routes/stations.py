from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_stations():
    return [{"station_id": 1, "station_name": "Deira Union Square"}]

@router.post("/")
def create_station():
    return {"message": "Station created"}