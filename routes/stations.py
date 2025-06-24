from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.station import Station

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def list_stations(db: Session = Depends(get_db)):
    return db.query(Station).all()

@router.post("/")
def create_station(station: Station, db: Session = Depends(get_db)):
    db.add(station)
    db.commit()
    db.refresh(station)
    return station
