from fastapi import APIRouter
from services.task_service import Task_service
from res.errors.utils import raise_http_exception
from models.task import TaskModel
from typing import List
PATH = "/tasks"
TASK_TAG = 'Task'

router = APIRouter()
task_service = Task_service() 

@router.get("/{product_id}/{version_code}/{ticket_id}")
async def get_tasks(product_id: int, version_code: str, ticket_id: int):
    try:
        return task_service.get_tasks_by_ticket(product_id, version_code, ticket_id)
    except Exception as e:
        raise_http_exception(str(e))

@router.put("/{product_id}/{version_code}/{ticket_id}")
async def insert_tasks(product_id: int, version_code: str, ticket_id: int, tasks_data: List[TaskModel]):
    try:
        task_service.insert_tasks(product_id, version_code, ticket_id, tasks_data)
        return {"message": "Tareas asociadas con exito"}
    except Exception as e:
        raise_http_exception(str(e))


# @router.get("/")
# async def get_clients_by_id():
#     clients = client_service.get_clients()
#     if not clients:
#         raise HTTPException(status_code=404, detail="clients not found")
#     return {"clients": clients}