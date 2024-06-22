from fastapi import APIRouter, HTTPException
from services.query_service import Query_service


router = APIRouter()
query_service = Query_service() 

PATH = "/query"

# Devuelve todos las querys
@router.get("/")
async def get_Query():
    querys = query_service.get_Querys()
    return {"querys": querys}

# Devuelve un query buscado por id de ticket
@router.get("/query/{ticket_id}")
async def get_Query(Ticket_id: int):
    querys = query_service.get_Query(Ticket_id)
    if not querys:
        raise HTTPException(status_code=404, detail="querys not found")
    return {"querys": querys}



