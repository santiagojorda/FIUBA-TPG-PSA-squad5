from fastapi import APIRouter
from models.ticket import Ticket
from services.tickets_services import TicketService
from res.database import db

TICKETS_PATH = "/tickets"

router = APIRouter()

ticketService = TicketService() 

@router.get("/")
async def index():
    return ticketService.get_tickets()

# Devuelve todos los tickets
@router.get("/tickets")
async def index():
    return {'mensaje': 'todos los tickets'}

# Devuelve todos los ticket de una proyecto
@router.get("/tickets/{proyect_id}")
async def index():
    return {'mensaje': 'todos los ticket de un proyecto'}

# Devuelve todos los ticket de una version especifica de proyecto
@router.get("/tickets/{proyect_id}/{versin_id}")
async def index():
    return {'mensaje': 'todos los ticket de una version'}

# Devuelve un ticket especifico
@router.get("/tickets/{proyect_id}/{version_id}/{ticket_id}")
async def index():
    return {'mensaje': 'un ticket en especifico'}