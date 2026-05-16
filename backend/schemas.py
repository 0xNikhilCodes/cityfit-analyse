from pydantic import BaseModel

class PreferenceInput(BaseModel):
    cost: float
    safety: float
    internet: float
    climate: float
    nightlife: float

class SaveProfile(BaseModel):
    username: str
    cost: float
    safety: float
    internet: float
    climate: float
    nightlife: float