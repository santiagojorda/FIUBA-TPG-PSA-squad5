from res.database import db

from models.query import Query

class Query_service():

    def __init__(self):
        self.db = db

    def get_Query(self, Ticket_id: int):
        return self.db.get_session().query(Query).filter(Query.ticket_id == Ticket_id).first()
    
    def get_Querys(self):
        return self.db.get_session().query(Query).all()
