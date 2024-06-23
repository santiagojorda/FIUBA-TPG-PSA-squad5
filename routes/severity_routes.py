from fastapi import APIRouter, HTTPException
from services.severity_service import Severity_service

PATH = "/severitys"
SEVERITY_TAG = "Severity"

router = APIRouter()
severity_service = Severity_service() 

# Devuelve todos los severityos
@router.get("/severity")
async def get_severities():
    severitys = severity_service.get_severitys()
    return {"severities": severitys}

# Devuelve un severityo buscado por su ID
@router.get("/severity/{severity_id}")
async def get_severity(severity_id: int):
    severity = severity_service.get_severity(severity_id)
    if not severity:
        raise HTTPException(status_code=404, detail="severity not found")
    return {"severity": severity}


