from sqlalchemy import String, Boolean, Integer, Column, DATE, Text, UniqueConstraint
from app.db.database import Base
from datetime import datetime

class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    driver_name = Column(String)
    driver_lastname = Column(String)
    driver_nif = Column(String)
    driver_phone = Column(String)
    driver_birthdate = Column(String)
    driver_email = Column(String)
    driver_team = Column(String)
    created_at = Column(DATE, default=datetime.now)

    def serialize(self):
        return {
            "id": self.id,
            "category": self.category,
            "driver_name": self.driver_name,
            "driver_lastname": self.driver_lastname,
            "driver_nif": self.driver_nif,
            "driver_phone": self.driver_phone,
            "driver_birthdate": self.driver_birthdate,
            "driver_email": self.driver_email,
            "driver_team": self.driver_team,
            "created_at": self.created_at.isoformat()
        }
