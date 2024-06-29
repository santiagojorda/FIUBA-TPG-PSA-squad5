from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn

from routes.tickets_routes import PATH as TICKETS_PATH, TICKET_TAG, router as tickets_router
from routes.product_version_routes import PATH as PRODUCT_PATH, PRODUCT_TAG, router as product_versions_router
from routes.client_routes import PATH as CLIENT_PATH, CLIENT_TAG, router as client_router
from routes.task_routes import PATH as TASK_PATH, TASK_TAG, router as tasks_router
from res.database import *

db_support = Database(SQLALCHEMY_DATABASE_URL)

app = FastAPI(title="PSA - Support")
app = FastAPI()

app.include_router(tickets_router, prefix=TICKETS_PATH, tags=[TICKET_TAG])
app.include_router(product_versions_router, prefix=PRODUCT_PATH, tags=[PRODUCT_TAG])
app.include_router(client_router, prefix=CLIENT_PATH, tags=[CLIENT_TAG])
app.include_router(tasks_router, prefix=TASK_PATH, tags=[TASK_TAG])

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

@app.get("/")
async def read_root():
    return {"message": "Bienvenido al microservicio de Soporte - SLA"}

if __name__ == "__main__":
    print("APP START")
    uvicorn.run(app, host="0.0.0.0", port=8000, loop="asyncio")


