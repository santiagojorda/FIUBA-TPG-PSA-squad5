class Task_not_exist_exception(Exception):
    def __init__(self, project_id, task_id):
        self.message = f"Task {task_id} not exist in project {project_id}"
        super().__init__(self.message)