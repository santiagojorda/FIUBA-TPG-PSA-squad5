from fastapi import APIRouter, HTTPException
from services.incident_per_task_service import Incident_per_task_service


router = APIRouter()
incident_per_task_service = Incident_per_task_service() 

PATH = "/incident_per_task"
INCIDENTS_PER_TASK_TAG = 'Incidents per task'
# Devuelve todos las querys
@router.get("/")
async def get_Query():
    incident_per_task = (incident_per_task_service).get_incident_per_tasks()
    return {"incident per task": incident_per_task}

# Devuelve un query buscado por id de ticket
@router.get("/incident/{severity_id}")
async def get_Query(Ticket_id: int):
    incident_per_task = incident_per_task_service.get_incident_per_task(Ticket_id)
    if not incident_per_task:
        raise HTTPException(status_code=404, detail="incident per stask not found")
    return {"incident per task": incident_per_task}



