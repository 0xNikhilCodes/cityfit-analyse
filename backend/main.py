from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from database import SessionLocal, engine
from models import Base, SavedProfile
from schemas import PreferenceInput, SaveProfile
from clustering import recommend_city

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {
        "message": "CityFit Analyse API Running"
    }


@app.post("/recommend")
def recommend(preferences: PreferenceInput):

    user_data = {
        "cost": preferences.cost,
        "safety": preferences.safety,
        "internet": preferences.internet,
        "climate": preferences.climate,
        "nightlife": preferences.nightlife
    }

    result = recommend_city(user_data)

    return {
        "recommended_cities": result
    }


@app.post("/save-profile")
def save_profile(profile: SaveProfile, db: Session = Depends(get_db)):

    new_profile = SavedProfile(
        username=profile.username,
        cost=profile.cost,
        safety=profile.safety,
        internet=profile.internet,
        climate=profile.climate,
        nightlife=profile.nightlife
    )

    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)

    return {
        "message": "Profile saved successfully"
    }


@app.get("/profiles")
def get_profiles(db: Session = Depends(get_db)):

    profiles = db.query(SavedProfile).all()

    return profiles