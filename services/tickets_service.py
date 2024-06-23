from models.ticket import Ticket
from res.database import db

class Ticket_service():

    def get_ticket(self, ticket_id: int):
        ticket = Ticket(title="hola")
        return db.get_ticket(ticket_id)
        return db.query(Ticket).filter(Ticket.ID_ticket == ticket_id).first()

    def get_tickets(self):
        return db.get_all_tickets()




#def create_ticket(cliente: schemas.ClienteCreate):
#    db_cliente = models.Cliente(nombre=cliente.nombre, email=cliente.email)
#    db.add(db_cliente)
#    db.commit()
#    db.refresh(db_cliente)
#    return db_cliente