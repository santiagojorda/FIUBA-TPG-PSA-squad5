from fastapi import APIRouter, HTTPException

from services.tickets_service import Ticket_service
from models.ticket import TicketModel

PATH = "/tickets"
TICKET_TAG = 'Tickets'

router = APIRouter()
ticket_service = Ticket_service() 

@router.get("/{product_id}/{version_code}/{ticket_id}")
async def get_ticket_by_id(product_id: int, version_code: str, ticket_id: int):
    ticket = ticket_service.get_ticket(ticket_id)
    if not ticket:
        raise HTTPException(status_code=500, detail="Tickets ticket not found")
    return ticket

@router.get("/{product_id}/{version_code}")
async def get_tickets_by_version_and_product(product_id: int, version_code: str):
    tickets = ticket_service.get_tickets(product_id, version_code)
    if not tickets:
        raise HTTPException(status_code=500, detail="Tickets not found")
    return tickets

@router.post("/")
async def create_ticket(ticket: TicketModel):
    ticket = ticket_service.create_ticket(ticket)
    if not ticket:
        raise HTTPException(status_code=500, detail="Error al crear ticket")
    return {"message": "Ticket creado exitosamente"}

@router.put("/{product_id}/{version_code}/{ticket_id}")
async def modify_ticket(product_id: int, version_code: str, ticket_id: int, ticket: TicketModel):
    ticket.id = ticket_id
    ticket = ticket_service.modify_ticket(ticket)
    if not ticket:
        raise HTTPException(status_code=500, detail="Error al modificar ticket")
    return {"message": "Ticket modificado exitosamente"}

@router.delete("/{product_id}/{version_code}/{ticket_id}")
async def delete_ticket(product_id: int, version_code: str, ticket_id: int):
    is_deleted = ticket_service.delete_ticket(ticket_id)
    if not is_deleted:
        raise HTTPException(status_code=500, detail="Error al eliminar ticket")
    return {"message": "Ticket eliminado exitosamente"}
