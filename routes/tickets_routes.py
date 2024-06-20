from fastapi import APIRouter
from services.tickets_service import Ticket_service

PATH = "/tickets"

router = APIRouter()
ticketService = Ticket_service() 

# un ticket puede ser consulta o incidente

# Devuelve todos los tickets (no es necesario)
@router.get("/")
async def index():
    return {'mensaje': 'todos los tickets'}

# Devuelve todos los ticket de una proyecto y todas sus versiones (no es neceasrio)
@router.get("/{proyect_id}")
async def index(proyect_id):
    return {'mensaje': f"todos los ticket de un proyecto {proyect_id}"}

# Devuelve todos los ticket de una version especifica de producto y version
@router.get("/{proyect_id}/{version_id}")
async def index(proyect_id, version_id):
    return {'mensaje': f"todos los ticket de un proyecto: {proyect_id} y de su version {version_id}"}

# Devuelve un ticket especifico
@router.get("/{proyect_id}/{version_id}/{ticket_id}")
async def index():
    return {'mensaje': 'un ticket en especifico'}



# @router.post("/")
# async def index(proyect_id, version_id):
#     return {'mensaje': f"todos los ticket de un proyecto: {proyect_id} y de su version {version_id}"}

# # Devuelve el tiempo de respuesta dependiendo la severidad -> s1 s2 s3 s4
# @router.get("/response_time/{severidad}")
# async def index(severidad):
#     return {'mensaje': f"tiempo correspondiente a la severidad"}


# crear nuyevo ticket tipo query
# asdasdasd.com/tickets/query (POST) titulo descripcion  opening_date, closing_date, client
@router.post("/query")
async def index():
    return {'mensaje': f"crear nuevo ticket"}

# crear nuevo ticket tipo incident
# asdasdasd.com/tickets/incident (POST) titulo descripcion opening_date, closing_date, client, sin_response, severity
@router.post("/incident")
async def index():
    return {'mensaje': f"crear nuevo ticket"}

# actualizar ticket tipo incident
# asdasdasd.com/tickets/incident (PATCH) titulo descripcion opening_date, closing_date, client, sin_response, severity
@router.patch("/incident")
async def index():
    return {'mensaje': f"actualizar ticket tipo incident"}

# actualizar ticket tipo query
# asdasdasd.com/tickets/query (PATCH) titulo descripcion  opening_date, closing_date, client
@router.patch("/query")
async def index():
    return {'mensaje': f"actualizar ticket tipo query"}

# borrar ticket
@router.delete("/{ticket_id}")
async def index(ticket_id):
    return {'mensaje': f"eliminar nuevo ticket de id: {ticket_id}"}


#{
# id_task
# id_proyect
# id_product
# id_version
# id_ticket
#}
@router.post("/tasks")
async def index():
    return {"se enlazo una tarea con un ticket"}

@router.delete("/tasks")
async def index():
    return {"se enlazo una tarea con un ticket"}

@router.get("/proyect/{proyect_id}/{task_id}")
async def index():
    return {"se obtuvieron los tickets de una tarea de un proyecto"}

@router.get("/proyect/{proyect_id}")
async def index():
    return {"se obtuvieron los tickets de un proyecto"}