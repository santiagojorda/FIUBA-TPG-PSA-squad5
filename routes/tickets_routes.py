from fastapi import APIRouter
from .. import models
from res.database import SessionLocal, engine

router = APIRouter()

models.Base.metadata.create_all(bind=engine)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def index():
    return {'mensaje': 'squad5'}

