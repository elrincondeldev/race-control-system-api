from fastapi import APIRouter, Depends, Request, Response, HTTPException, Query
from sqlalchemy.orm import Session
from app.api.schemas import participant
from app.api.services import competition as competition_service
from app.db.database import get_db
from typing import List, Optional
from authx import AuthX, RequestToken, AuthXConfig

router = APIRouter()

config = AuthXConfig(
    JWT_ALGORITHM="HS256",
    JWT_SECRET_KEY="SECRET_KEY",
    JWT_TOKEN_LOCATION=["headers"],
)

auth = AuthX(config=config)

async def get_current_user(token: RequestToken = Depends(auth.get_access_token_from_request)) -> str:
    try:
        # Verifica el token (aquí se puede ajustar según tus necesidades)
        auth.verify_token(token=token)
        return token  # O puedes devolver el `uid` u otro identificador del usuario
    except Exception as e:
        raise HTTPException(status_code=401, detail={"message": str(e)})

@router.post("/create-competition", response_model=participant.CompetitionBase)
def create_competition(    
    competition: participant.CompetitionBase,  # No envuelto en una clave
    db: Session = Depends(get_db), 
    current_user: str = Depends(get_current_user)):
    return competition_service.create_competition(db, competition)

@router.post("/modify-competition", response_model=participant.CompetitionBase)
def modify_competition(request: Request, competition: participant.CompetitionBase, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return competition_service.modify_competition(db, competition)

@router.get("/get-all-competitions", response_model=List[participant.CompetitionBase])
async def get_all_competitions(
    request: Request, 
    db: Session = Depends(get_db), 
    current_user: str = Depends(get_current_user)
):
    return competition_service.get_all_competitions(db)

@router.get("/get-competition-by-url-path", response_model=participant.CompetitionRespond)
def get_competition_by_url_path(url_path: str, db: Session = Depends(get_db)):
    return competition_service.get_competition_by_url_path(db, url_path)

@router.get("/competitions-active", response_model=List[participant.CompetitionBase])
def competitions_active(db: Session = Depends(get_db)):
    return competition_service.competitions_active(db)