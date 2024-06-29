from fastapi import APIRouter, HTTPException

from res.errors.utils import raise_http_exception
from services.tickets_service import Ticket_service
from models.ticket import TicketModel

PATH = "/tickets"
TICKET_TAG = 'Tickets'

router = APIRouter()
ticket_service = Ticket_service() 

@router.get("/{product_id}/{version_code}/{ticket_id}")
async def get_ticket_by_id(product_id: int, version_code: str, ticket_id: int):
    try:
        return ticket_service.get_ticket(product_id, version_code, ticket_id)
    except Exception as e:
        raise_http_exception(str(e))

@router.get("/{product_id}/{version_code}")
async def get_tickets_by_version_and_product(product_id: int, version_code: str):
    try:
        return ticket_service.get_tickets(product_id, version_code)
    except Exception as e:
        raise_http_exception(str(e))

@router.post("/")
async def create_ticket(ticket: TicketModel):
    try:
        ticket = ticket_service.create_ticket(ticket)
        return {"message": "Ticket created successfully"}
    except Exception as e:
        raise_http_exception(str(e))

@router.put("/{product_id}/{version_code}/{ticket_id}")
async def modify_ticket(product_id: int, version_code: str, ticket_id: int, ticket: TicketModel):
    try:
        ticket.id = ticket_id
        ticket = ticket_service.modify_ticket(product_id, version_code, ticket)
        return {"message": "Ticket modified successfully"}
    except Exception as e:
        raise_http_exception(str(e))

@router.delete("/{product_id}/{version_code}/{ticket_id}")
async def delete_ticket(product_id: int, version_code: str, ticket_id: int):
    try:
        ticket_service.delete_ticket(product_id, version_code, ticket_id)
        return {"message": "Ticket deleted successfully"}
    except Exception as e:
        raise_http_exception(str(e))
