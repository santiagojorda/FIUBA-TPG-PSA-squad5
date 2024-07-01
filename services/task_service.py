from sqlalchemy.orm.exc import NoResultFound
from res.database import db
from typing import List
import requests

from res.errors import Data_not_exist_exception, No_result_exception
from services.tickets_service import Ticket_service
from models.task import TaskModel

ticket_service = Ticket_service()

ENDPOINT_PROJECT = 'https://psa-project-microservice.onrender.com/projects' # /{project_id}
ENDPOINT_TASK = 'https://psa-project-microservice.onrender.com/tasks' # /{project_id}/{task_id}

class Task_service():

    def get_tasks_by_ticket(self, product_id: int, version_code: str, ticket_id: int):
        ticket_service.validate_exist(product_id, version_code, ticket_id)

        tasks = db.get_tasks(ticket_id)
        arr_tasks = []
        for task in tasks:
            filtered_task = {
                "task_id": task.task_id,
                "project_id": task.project_id
            }
            arr_tasks.append(filtered_task)
        if not arr_tasks:
            return {}
        return arr_tasks
    

    def task_exist(self, project_id: int, task_id: int):
        response = requests.get(f"{ENDPOINT_TASK}/{project_id}/{task_id}")
        if response.status_code != 200:
            print(f"Error en la petición: {response.status_code}")
            return False
        
        task = response.json()
        print(task)
        if task['id'] == task_id:
            return True
        return False


    def project_exist(self, project_id: int):
        response = requests.get(f"{ENDPOINT_PROJECT}/{project_id}")
        if response.status_code != 200:
            print(f"Error en la petición: {response.status_code}")
            return False

        project = response.json()
        print(project)
        if project['id'] == project_id:
            return True
        return False

    def insert_tasks(self, product_id: int, version_code: int, ticket_id: int, tasks_data: List[TaskModel]):
        ticket_service.validate_exist(product_id, version_code, ticket_id)

        for data in tasks_data:            
            if not self.project_exist(data.project_id):
                raise Data_not_exist_exception(f"No existe project id {data.project_id}") 
            
            if not self.task_exist(data.project_id, data.task_id):
                raise Data_not_exist_exception(f"No existe tasks id {data.task_id} en el project id {data.project_id}") 

        is_inserted = db.insert_tasks(ticket_id, tasks_data)
        
        if not is_inserted:
            raise NoResultFound("There was an internal error to associate tasks to tickets")
        return is_inserted
