from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.api.schemas import participant
from app.api.services import participant as participant_service
from app.db.database import get_db
from typing import List
from authx import AuthX, RequestToken, AuthXConfig

router = APIRouter()

# Si `authx` ya está configurado en otro archivo, puedes importarlo o definirlo aquí
config = AuthXConfig(
    JWT_ALGORITHM="HS256",
    JWT_SECRET_KEY="SECRET_KEY",
    JWT_TOKEN_LOCATION=["headers"],
)

auth = AuthX(config=config)

# Dependencia para autenticar el token
async def get_current_user(token: RequestToken = Depends(auth.get_access_token_from_request)) -> str:
    try:
        # Verifica el token (aquí se puede ajustar según tus necesidades)
        auth.verify_token(token=token)
        return token  # O puedes devolver el `uid` u otro identificador del usuario
    except Exception as e:
        raise HTTPException(status_code=401, detail={"message": str(e)})

@router.post("/register-participant", response_model=participant.ParticipantBase)
def register_participant(participant: participant.ParticipantBase, db: Session = Depends(get_db)):
    return participant_service.create_participant(db, participant)

@router.get("/get-all-participants", response_model=List[participant.ParticipantBase])
async def get_all_participants(
    request: Request, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return participant_service.get_all_participants(db)

@router.get("/get-participants-by-competition-name", response_model=List[participant.ParticipantResponse])
async def get_participants_by_competition_name(
    competition_name: str, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)  # Agrega la dependencia de autenticación
):
    return participant_service.get_participants_by_competition_name(db, competition_name)
