from fastapi import FastAPI
from routes.support_routes import router as support_router

app = FastAPI()

app.include_router(support_router, prefix="/support") # prefix es opcional



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