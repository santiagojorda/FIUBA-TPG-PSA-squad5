from fastapi import APIRouter, HTTPException
from services.incident_service import Incident_service


router = APIRouter()
incident_service = Incident_service() 

PATH = "/incident"

# Devuelve todos las querys
@router.get("/")
async def get_Query():
    querys = incident_service.get_Incidents()
    return {"querys": querys}

# Devuelve un query buscado por id de ticket
@router.get("/incident/{severity_id}")
async def get_Query(Ticket_id: int):
    querys = incident_service.get_Incident(Ticket_id)
    if not querys:
        raise HTTPException(status_code=404, detail="incident not found")
    return {"querys": querys}



