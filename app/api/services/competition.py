from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.api.models.competition import Competition
from app.api.schemas.participant import CompetitionBase
import logging

def create_competition(db: Session, competition: CompetitionBase):
    try:
        new_competition = Competition(**competition.model_dump())
        db.add(new_competition)
        db.commit()
        db.refresh(new_competition)
        return new_competition
    except Exception as e:
        logging.error(f"Error al introducir los datos: {e}")
        raise HTTPException(status_code=500, detail="Error al introducir los datos.")

def modify_competition(db: Session, competition: CompetitionBase):
    try:
        db.query(Competition).filter(Competition.competition_name == competition.competition_name).update(competition.model_dump())
        db.commit()
        return db.query(Competition).filter(Competition.competition_name == competition.competition_name).first()
    except Exception as e:
        logging.error(f"Error al modificar los datos: {e}")
        raise HTTPException(status_code=500, detail="Error al modificar los datos.")

def get_all_competitions(db: Session):
    return db.query(Competition).all()

def get_competition_by_url_path(db: Session, url_path: str):
    return db.query(Competition).filter(Competition.url_path == url_path).first()

def competitions_active(db: Session):
    return db.query(Competition).filter(Competition.active == True).all()