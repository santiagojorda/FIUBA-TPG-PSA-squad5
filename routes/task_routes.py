from fastapi import APIRouter
from typing import List

from res.errors.utils import raise_http_exception
from services.task_service import Task_service
from models.task import TaskModel

PATH = "/tasks"
TASK_TAG = 'Task'

router = APIRouter()
task_service = Task_service() 

MESSAGE_SUCCESSFULLY_ASSOCIATED_TASK = 'Successfully associated tasks'

@router.get("/{product_id}/{version_code}/{ticket_id}")
async def get_tasks(product_id: int, version_code: str, ticket_id: int):
    try:
        return task_service.get_tasks_by_ticket(product_id, version_code, ticket_id)
    except Exception as e:
        print(str(e))
        raise_http_exception(str(e))

@router.put("/{product_id}/{version_code}/{ticket_id}")
async def insert_tasks(product_id: int, version_code: str, ticket_id: int, tasks_data: List[TaskModel]):
    print(tasks_data)
    try:
        print(tasks_data)
        task_service.insert_tasks(product_id, version_code, ticket_id, tasks_data)
        return {"message": MESSAGE_SUCCESSFULLY_ASSOCIATED_TASK}
    except Exception as e:
        print(str(e))
        raise_http_exception(str(e))
