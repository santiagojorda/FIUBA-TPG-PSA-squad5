# my_fastapi_app/crud/cliente_crud.py
from sqlalchemy.orm import Session
from .. import models, schemas

def get_ticket(db: Session, ticket_id: int):
    return db.query(models.Ticket).filter(models.Ticket.ID_ticket == ticket_id).first()

def get_tickets(db: Session):
    return db.query(models.Ticket).all()

# def create_ticket(db: Session, cliente: schemas.ClienteCreate):
#     db_cliente = models.Cliente(nombre=cliente.nombre, email=cliente.email)
#     db.add(db_cliente)
#     db.commit()
#     db.refresh(db_cliente)
#     return db_cliente