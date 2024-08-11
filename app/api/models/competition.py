from sqlalchemy import String, Boolean, Integer, Column, DATE, Text, ARRAY
from app.db.database import Base
from datetime import datetime

class Competition(Base):
    __tablename__ = "competition"

    id = Column(Integer, primary_key=True, index=True)
    competition_name = Column(String)
    categories = Column(ARRAY(String))
    date = Column(String)
    inscription_price = Column(String)
    active = Column(Boolean)
    regulation_url = Column(String)

def serialize(self):
    return {
        "id": self.id,
        "competition_name": self.competition_name,
        "categories": self.categories,
        "date": self.date,
        "inscription_price": self.inscription_price,
        "active": self.active,
        "regulation_url": self.regulation
    }