from sqlalchemy import Column, Integer, String, Float
from database import Base

class SavedProfile(Base):
    __tablename__ = "saved_profiles"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    cost = Column(Float)
    safety = Column(Float)
    internet = Column(Float)
    climate = Column(Float)
    nightlife = Column(Float)