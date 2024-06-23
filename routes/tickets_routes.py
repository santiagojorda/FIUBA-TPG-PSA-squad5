from fastapi import APIRouter, HTTPException
from services.tickets_service import Ticket_service
from models.incident import IncidentModel
from models.query import QueryModel
from models.ticket import TicketModel

PATH = "/tickets"
TICKET_TAG = 'Tickets'

router = APIRouter()
ticket_service = Ticket_service() 


# # Devuelve un query ticket especifico
# @router.get("/q/{ticket_id}")
# async def get_query_ticket_by_id(ticket_id):
#     ticket = ticket_service.get_query_ticket(ticket_id)
#     if not ticket:
#         raise HTTPException(status_code=404, detail="Query ticket not found")
#     return {"ticket": ticket}

# Devuelve un incident ticket especifico
@router.get("/{ticket_id}")
async def get_ticket_by_id(ticket_id: int):
    ticket = ticket_service.get_ticket_by_id(ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Tickets ticket not found")
    return {"ticket": ticket}

@router.get("/{product_id}/{version_code}")
async def get_tickets_by_version_and_product(product_id: int, version_code: str):
    tickets = ticket_service.get_tickets(product_id, version_code)
    if not tickets:
        raise HTTPException(status_code=404, detail="Tickets not found")
    return {"tickets": tickets}






@router.post("/")
async def create_ticket(ticket: TicketModel):
    ticket = ticket_service.create_ticket(ticket)
    if not ticket:
        raise HTTPException(status_code=404, detail="Error al crear ticket")
    return {"message": "Ticket creado exitosamente"}

# @router.post("/q/")
# async def create_query_ticket(query: QueryModel):
#     ticket = ticket_service.create_query_ticket(query)
#     if not ticket:
#         raise HTTPException(status_code=404, detail="Error al crear query")
#     return {"message": "se creo exitosamente el query"}










# # Devuelve todos los tickets (no es necesario)
# @router.get("/")
# async def get_all_tickets():
#     return ticket_service.get_tickets()

# # Devuelve todos los ticket de una proyecto y todas sus versiones (no es neceasrio)
# @router.get("/{product_id}")
# async def get_all_tickets_of_product(product_id):
#     return {'mensaje': f"todos los ticket de un proyecto {product_id}"}

# # Devuelve todos los ticket de una version especifica de producto y version
# @router.get("/{product_id}/{version_id}")
# async def get_all_tickets_of_a_product_version(product_id, version_id):
#     return {'mensaje': f"todos los ticket de un proyecto: {product_id} y de su version {version_id}"}

# # crear nuyevo ticket tipo query
# # asdasdasd.com/tickets/query (POST) titulo descripcion  opening_date, closing_date, client
# @router.post("/q/")
# async def create_new_query_ticket():
#     ticket_service.create_ticket()
#     return {'mensaje': f"crear nuevo ticket"}

# # crear nuevo ticket tipo incident
# # asdasdasd.com/tickets/incident (POST) titulo descripcion opening_date, closing_date, client, sin_response, severity
# @router.post("/i/")
# async def create_new_incident_ticket():
#     return {'mensaje': f"crear nuevo ticket"}

# actualizar ticket tipo incident
# asdasdasd.com/tickets/incident (PATCH) titulo descripcion opening_date, closing_date, client, sin_response, severity
# @router.patch("/i/")
# async def update_incident_ticket():
#     return {'mensaje': f"actualizar ticket tipo incident"}

# # # actualizar ticket tipo query
# # # asdasdasd.com/tickets/query (PATCH) titulo descripcion  opening_date, closing_date, client
# @router.patch("/q/")
# async def update_query_ticket():
#     return {'mensaje': f"actualizar ticket tipo query"}

# # # borrar ticket
# @router.delete("/{ticket_id}")
# async def delete_ticket(ticket_id):
#      return {'mensaje': f"eliminar nuevo ticket de id: {ticket_id}"}

#{
# id_task
# id_proyect
# id_product
# id_version
# id_ticket
#}
# @router.post("/tasks")
# async def index():
#     return {"se enlazo una tarea con un ticket"}

# @router.delete("/tasks")
# async def index():
#     return {"se enlazo una tarea con un ticket"}

# @router.get("/proyect/{proyect_id}/{task_id}")
# async def index():
#     return {"se obtuvieron los tickets de una tarea de un proyecto"}

# @router.get("/proyect/{proyect_id}")
# async def index():
#     return {"se obtuvieron los tickets de un proyecto"}