from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.api.models.participant import Participant
from app.api.schemas.participant import ParticipantBase

def create_participant(db: Session, participant: ParticipantBase):
    try:
        new_participant = Participant(**participant.model_dump())
        db.add(new_participant)
        db.commit()
        db.refresh(new_participant)
        return new_participant
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al introducir los datos.")

def get_all_participants(db: Session):
    return db.query(Participant).all()

def get_participants_by_competition_name(db: Session, competition_name: str):
    return db.query(Participant).filter(Participant.competition_name == competition_name).all()