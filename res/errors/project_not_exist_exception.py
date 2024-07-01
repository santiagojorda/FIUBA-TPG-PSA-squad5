class Project_not_exist_exception(Exception):
    def __init__(self, project_id):
        self.message = f"Project {project_id} not exist"
        super().__init__(self.message)