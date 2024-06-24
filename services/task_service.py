from res.database import db

class Task_service():

    def get_tasks(self, product_id: int, version_code: str, ticket_id: int):
        tasks = db.get_tasks(self, ticket_id)
        transformed_array = [{'task_id': item['task_id'], 'project_id': item['project_id']} for item in tasks]
        return transformed_array