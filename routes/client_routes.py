from fastapi import APIRouter, HTTPException
from services.client_service import Client_service


PATH = "/clients"
CLIENT_TAG = 'Clients'

router = APIRouter()
client_service = Client_service() 

@router.get("/{client_id}")
async def get_client_by_id(client_id: int):
    client = client_service.get_client(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="client not found")
    return {"client": client}


@router.get("/")
async def get_clients_by_id():
    clients = client_service.get_clients()
    if not clients:
        raise HTTPException(status_code=404, detail="clients not found")
    return {"clients": clients}