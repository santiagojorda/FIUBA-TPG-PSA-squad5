from res.database import db

from models.query import Query

class Query_service():

    def get_query(self, Ticket_id: int):
        return db.filter(Query.ticket_id == Ticket_id).first()
    
    def get_querys(self):
        return db.get_session().query(Query).all()
