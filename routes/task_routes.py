from fastapi import APIRouter, HTTPException
from services.task_service import Task_service

PATH = "/tasks"
TASK_TAG = 'Task'

router = APIRouter()
task_service = Task_service() 

@router.get("/{client_id}")
async def get_tasks_by_ticket(ticket_id: int):
    tasks = task_service.get_tasks(ticket_id)
    if not tasks:
        raise HTTPException(status_code=404, detail="tasks not found")
    return {"tasks": tasks}

@router.post("/{proyect_id}")
async def get_tasks_by_ticket(ticket_id: int):
    tasks = task_service.get_tasks(ticket_id)
    if not tasks:
        raise HTTPException(status_code=404, detail="tasks not found")
    return {"tasks": tasks}


# @router.get("/")
# async def get_clients_by_id():
#     clients = client_service.get_clients()
#     if not clients:
#         raise HTTPException(status_code=404, detail="clients not found")
#     return {"clients": clients}