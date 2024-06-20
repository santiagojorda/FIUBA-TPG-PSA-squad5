from fastapi import APIRouter
from models.ticket import Ticket
from services.tickets_services import TicketService
from res.database import db

TICKETS_PATH = "/tickets"

router = APIRouter()

ticketService = TicketService() 

# Devuelve todos los tickets
@router.get("/")
async def index():
    return {'mensaje': 'todos los tickets'}
    # return ticketService.get_tickets()

# Devuelve todos los ticket de una proyecto
@router.get("/{proyect_id}")
async def index(proyect_id):
    return {'mensaje': f"todos los ticket de un proyecto {proyect_id}"}

# Devuelve todos los ticket de una version especifica de proyecto
@router.get("/{proyect_id}/{version_id}")
async def index(proyect_id, version_id):
    return {'mensaje': f"todos los ticket de un proyecto: {proyect_id} y de su version {version_id}"}

# Devuelve un ticket especifico
@router.get("/{proyect_id}/{version_id}/{ticket_id}")
async def index():
    return {'mensaje': 'un ticket en especifico'}