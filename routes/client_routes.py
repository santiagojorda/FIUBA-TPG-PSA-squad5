from fastapi import APIRouter, HTTPException
from services.client_service import Client_service
from res.errors.utils import raise_http_exception

PATH = "/clients"
CLIENT_TAG = 'Clients'

router = APIRouter()
client_service = Client_service() 

@router.get("/")
async def get_clients():
    try: 
        return client_service.get_clients()
    except Exception as e:
        raise_http_exception(str(e))

@router.get("/{client_id}")
async def get_client_by_id(client_id: int):
    try: 
        return client_service.get_client(client_id)
    except Exception as e:
        raise_http_exception(str(e))

