from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.main.database import SessionLocal
from app.models.reading import Reading

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def list_readings(db: Session = Depends(get_db)):
    return db.query(Reading).all()

@router.post("/")
def create_reading(reading: Reading, db: Session = Depends(get_db)):
    db.add(reading)
    db.commit()
    db.refresh(reading)
    return reading
