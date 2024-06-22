from res.database import db

from models.incident import Incident

class Incident_service():

    def __init__(self):
        self.db = db

    def get_Incident(self, Ticket_id: int):
        return self.db.get_session().query(Incident).filter(Incident.ticket_id == Ticket_id).first()
    
    def get_Incidents(self):
        return self.db.get_session().query(Incident).all()
