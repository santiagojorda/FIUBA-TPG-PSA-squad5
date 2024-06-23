from fastapi import APIRouter, HTTPException
from services.tickets_service import Ticket_service

PATH = "/tickets"
TICKET_TAG = 'Tickets'

router = APIRouter()
ticket_service = Ticket_service() 


# Devuelve todos los tickets (no es necesario)
@router.get("/")
async def get_all_tickets():
    return ticket_service.get_tickets()

# Devuelve todos los ticket de una proyecto y todas sus versiones (no es neceasrio)
@router.get("/{product_id}")
async def get_all_tickets_of_product(product_id):
    return {'mensaje': f"todos los ticket de un proyecto {product_id}"}

# Devuelve todos los ticket de una version especifica de producto y version
@router.get("/{product_id}/{version_id}")
async def get_all_tickets_of_a_product_version(product_id, version_id):
    return {'mensaje': f"todos los ticket de un proyecto: {product_id} y de su version {version_id}"}

# Devuelve un ticket especifico
@router.get("/{ticket_id}")
async def get_ticket_by_id(ticket_id):
    return {'mensaje': 'un ticket en especifico'}

# # crear nuyevo ticket tipo query
# # asdasdasd.com/tickets/query (POST) titulo descripcion  opening_date, closing_date, client
@router.post("/q/")
async def create_new_query_ticket():
    return {'mensaje': f"crear nuevo ticket"}

# # crear nuevo ticket tipo incident
# # asdasdasd.com/tickets/incident (POST) titulo descripcion opening_date, closing_date, client, sin_response, severity
@router.post("/i/")
async def create_new_incident_ticket():
    return {'mensaje': f"crear nuevo ticket"}

# actualizar ticket tipo incident
# asdasdasd.com/tickets/incident (PATCH) titulo descripcion opening_date, closing_date, client, sin_response, severity
@router.patch("/i/")
async def update_incident_ticket():
    return {'mensaje': f"actualizar ticket tipo incident"}

# # actualizar ticket tipo query
# # asdasdasd.com/tickets/query (PATCH) titulo descripcion  opening_date, closing_date, client
@router.patch("/q/")
async def update_query_ticket():
    return {'mensaje': f"actualizar ticket tipo query"}

# # borrar ticket
@router.delete("/{ticket_id}")
async def delete_ticket(ticket_id):
     return {'mensaje': f"eliminar nuevo ticket de id: {ticket_id}"}

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