from fastapi import APIRouter, HTTPException
from services.severity_service import Severity_service

PATH = "/severitys"
SEVERITY_TAGS = "Severity"
router = APIRouter()
severity_service = Severity_service() 


# Devuelve todos los severityos
@router.get("/severitys", tags=[SEVERITY_TAGS])
async def get_severitys():
    severitys = severity_service.get_severitys()
    return {"severitys": severitys}

# Devuelve un severityo buscado por su ID
@router.get("/severitys/{severity_id}", tags=[SEVERITY_TAGS])
async def get_severity(severity_id: int):
    severity = severity_service.get_severity(severity_id)
    if not severity:
        raise HTTPException(status_code=404, detail="severity not found")
    return {"severity": severity}

@router.get("/severitys/{severity_id}/v/{version_id}", tags=[SEVERITY_TAGS])
async def get_severitys():
    severitys = severity_service.get_severitys()
    return {"severitys": severitys}


