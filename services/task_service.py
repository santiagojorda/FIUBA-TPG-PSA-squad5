from res.database import db
from models.task import TaskModel
from typing import List
class Task_service():

    def get_tasks_by_ticket(self, product_id: int, version_code: str, ticket_id: int):
        tasks = db.get_tasks(ticket_id)
        arr_tasks = []
        for task in tasks:
            filtered_task = {
                "task_id": task.task_id,
                "project_id": task.project_id
            }
            arr_tasks.append(filtered_task)
        return arr_tasks
    

    def insert_tasks(self, product_id: int, version_code: int, ticket_id: int, tasks_data: List[TaskModel]):
        is_inserted = db.insert_tasks(product_id, version_code, ticket_id, tasks_data)
        return is_inserted
        # db.insert_task(product_id, version_code, ticket_id, task_item)
