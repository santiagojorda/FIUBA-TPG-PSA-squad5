from pydantic import BaseModel

class TaskModel(BaseModel):
    task_id: int
    project_id: int