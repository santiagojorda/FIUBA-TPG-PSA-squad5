from fastapi import APIRouter, HTTPException
from services.version_service import Version_service  # Asegúrate de importar correctamente

PATH = "/versions"
router = APIRouter()

version_service = Version_service() 
router = APIRouter()

# todas las versiones existentes 
@router.get("/versions")
async def get_versions():
    versions = version_service.get_versions()
    return {"versions": versions}

# 
@router.get("/versions/Product/{product_id}")
async def get_versions(product_id: int):
    versions = version_service.get_versions_by_product_id(product_id)
    return {"versions": versions}