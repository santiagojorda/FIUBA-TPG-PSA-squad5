from fastapi import APIRouter, HTTPException
from services.task_service import Task_service

PATH = "/tasks"
TASK_TAG = 'Task'

router = APIRouter()
task_service = Task_service() 

@router.get("/{product_id}/{version_code}/{ticket_id}")
async def get_tasks_by_ticket(product_id: int, version_code: str, ticket_id: int):
    tasks = task_service.get_tasks(ticket_id)
    if not tasks:
        raise HTTPException(status_code=500, detail="tasks not found")
    return {"tasks": tasks}

@router.put("/{product_id}/{version_code}/{ticket_id}")
async def get_tasks_by_ticket(product_id: int, version_code: str, ticket_id: int):
    tasks = task_service.get_tasks(ticket_id)
    if not tasks:
        raise HTTPException(status_code=500, detail="tasks not found")
    return {"tasks": tasks}


# @router.get("/")
# async def get_clients_by_id():
#     clients = client_service.get_clients()
#     if not clients:
#         raise HTTPException(status_code=404, detail="clients not found")
#     return {"clients": clients}