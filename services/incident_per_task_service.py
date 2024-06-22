from res.database import db

from models.incident_per_task import Incident_per_task

class Incident_per_task_service():

    def __init__(self):
        self.db = db

    def get_incident_per_task(self, Ticket_id: int):
        return self.db.get_session().query(Incident_per_task).filter(Incident_per_task.ticket_id == Ticket_id).first()
    
    def get_incident_per_tasks(self):
        return self.db.get_session().query(Incident_per_task).all()
