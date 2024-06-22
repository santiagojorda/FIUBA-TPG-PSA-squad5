from res.database import db

class Ticket_service():

    def __init__(self):
        self.db = db

    # def get_ticket(self, ticket_id: int):
    #     # ticket = Ticket(title: "hola")
    #     return self.db.get_session().query(Ticket).filter(Ticket.ID_ticket == ticket_id).first()

    # def get_tickets(self):
    #     pass
        # return self.db.query(Ticket).all()

# def create_ticket(db: Session, cliente: schemas.ClienteCreate):
#     db_cliente = models.Cliente(nombre=cliente.nombre, email=cliente.email)
#     db.add(db_cliente)
#     db.commit()
#     db.refresh(db_cliente)
#     return db_cliente