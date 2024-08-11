from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class ParticipantBase(BaseModel):
    category: str
    driver_name: str
    driver_lastname: str
    driver_nif: str
    driver_phone: str
    driver_birthdate: str
    driver_email: str
    driver_team: str

class CompetitionBase(BaseModel):
    competition_name: str
    inscription_price: str
    categories: List[str]
    active: bool
    date: str
    regulation_url: str

class ParticipantResponse(BaseModel):
    id: int
    category: str
    driver_name: str
    driver_lastname: str
    driver_nif: str
    driver_phone: str
    driver_birthdate: str
    driver_email: str
    driver_team: str

class CompetitionRespond(BaseModel):
    id: int
    competition_name: str
    inscription_price: str
    categories: List[str]
    active: bool
    date: str
    regulation_url: str

class UserBase(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    is_active: bool