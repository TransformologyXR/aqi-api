from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from database import SessionLocal
from models.reading import Reading
from typing import Optional
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def list_readings(
    station_id: Optional[int] = Query(None),
    start_datetime: Optional[datetime] = Query(None),
    end_datetime: Optional[datetime] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Reading)

    if station_id:
        query = query.filter(Reading.station_id == station_id)
    if start_datetime:
        query = query.filter(Reading.reading_datetime >= start_datetime)
    if end_datetime:
        query = query.filter(Reading.reading_datetime <= end_datetime)

    return query.all()


