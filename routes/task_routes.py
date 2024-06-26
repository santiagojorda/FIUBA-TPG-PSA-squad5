from fastapi import APIRouter
from typing import List

from res.errors.utils import raise_http_exception
from services.task_service import Task_service
from models.task import TaskModel

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
        return {"message": "Successfully associated tasks"}
    except Exception as e:
        raise_http_exception(str(e))
