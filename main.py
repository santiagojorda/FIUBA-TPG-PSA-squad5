from fastapi import FastAPI
from routes.tickets_routes import router as tickets_router

app = FastAPI()

app.include_router(tickets_router, prefix="/tickets") # prefix es opcional



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