from fastapi import FastAPI
from routes.tickets_routes import PATH as TICKETS_PATH, router as tickets_router
from routes.product_routes import PATH as PRODUCT_PATH, router as product_router
from routes.version_routes import PATH as VERSION_PATH, router as version_router
from routes.severity_routes import PATH as SEVERITY_PATH, router as severity_router
from routes.query_routes import PATH as QUERY_PATH, router as query_router
from routes.incident_routes import PATH as INCIDENT_PATH, router as incident_router
from routes.incident_per_task_routes import PATH as INCIDENT_PER_TASK_PATH, router as incident_per_task_router
from res.database import *

app = FastAPI()

db_support = Database(SQLALCHEMY_DATABASE_URL)

app.include_router(tickets_router, prefix=TICKETS_PATH) # prefix es opcional
app.include_router(product_router, prefix=PRODUCT_PATH) # prefix es opcional
app.include_router(version_router, prefix=VERSION_PATH) # prefix es opcional
app.include_router(severity_router, prefix=SEVERITY_PATH) # prefix es opcional
app.include_router(incident_router, prefix=INCIDENT_PATH) # prefix es opcional
app.include_router(query_router, prefix=QUERY_PATH) # prefix es opcional
app.include_router(incident_per_task_router, prefix=INCIDENT_PER_TASK_PATH) # prefix es opcional

# from pydantic import BaseModel
# from typing import Optional
# class Tarea(BaseModel):
#     nombre: str # sirve para sincronizar los tipso de datos especificados en la clase
#     detalles: Optional[str]

# creamos la ruta con el decorador @ arriba de la funcion
# @app.get("/")
# def index():
#     return {'mensaje': 'squad5'}


# @app.get("/tareas/{id}")
# def mostrar_tarea(id: int):
#     return {'tarea': id}

# @app.post("/tarea")
# def insertar_tarea(tarea: Tarea):
#     return {'mensaje': f"tarea {tarea.nombre} insertado"}