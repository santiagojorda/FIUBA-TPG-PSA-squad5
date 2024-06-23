from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes.tickets_routes import PATH as TICKETS_PATH, TICKET_TAG, router as tickets_router
from routes.product_version_routes import PATH as PRODUCT_PATH, PRODUCT_TAG, router as product_versions_router
from routes.severity_routes import PATH as SEVERITY_PATH, SEVERITY_TAG, router as severity_router
from routes.client_routes import PATH as CLIENT_PATH, CLIENT_TAG, router as client_router
from routes.task_routes import PATH as TASK_PATH, TASK_TAG, router as tasks_router
# from routes.query_routes import PATH as QUERY_PATH, router as query_router
# from routes.incident_routes import PATH as INCIDENT_PATH, router as incident_router
# from routes.incident_per_task_routes import PATH as INCIDENT_PER_TASK_PATH, router as incident_per_task_router
from res.database import *

app = FastAPI(title="PSA - Support")

app = FastAPI()

db_support = Database(SQLALCHEMY_DATABASE_URL)

app.include_router(tickets_router, prefix=TICKETS_PATH, tags=[TICKET_TAG]) # prefix es opcional
app.include_router(product_versions_router, prefix=PRODUCT_PATH, tags=[PRODUCT_TAG]) # prefix es opcional
app.include_router(severity_router, prefix=SEVERITY_PATH, tags=[SEVERITY_TAG]) # prefix es opcional
app.include_router(client_router, prefix=CLIENT_PATH, tags=[CLIENT_TAG]) # prefix es opcional
app.include_router(tasks_router, prefix=TASK_PATH, tags=[TASK_TAG]) # prefix es opcional

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://psa-support-microservice.onrender.com",
        "http://psa-support-microservice.onrender.com",
        "http://localhost:8000",
        "https://localhost:8000",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    print("APP START")
    uvicorn.run(app, host="0.0.0.0", port=8000, loop="asyncio")

# app.include_router(incident_router, prefix=INCIDENT_PATH, tags=[INCIDENT_PATH]) # prefix es opcional
# app.include_router(query_router, prefix=QUERY_PATH, tags=[QUERY_PATH]) # prefix es opcional
# app.include_router(incident_per_task_router, prefix=INCIDENT_PER_TASK_PATH, tags=[INCIDENT_PER_TASK_PATH]) # prefix es opcional

# @asynccontextmanager
# async def startup(app: FastAPI):
#     await db.load_default()
#     yield


# app = FastAPI(lifespan=startup, title="PSA - Manager de Proyectos")
# app.include_router(projects.router, prefix="/projects", tags=["projects"])
# app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
# app.include_router(workers.router, prefix="/workers", tags=["workers"])
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "https://psa-project-microservice.onrender.com",
#         "http://psa-project-microservice.onrender.com",
#         "http://localhost:8000",
#         "https://localhost:8000",
#         "*"
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

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