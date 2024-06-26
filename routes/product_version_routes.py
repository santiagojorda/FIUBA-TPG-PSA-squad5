from fastapi import APIRouter
from res.errors.utils import raise_http_exception
from services.product_version_service import Version_service

PATH = "/products"
PRODUCT_TAG = 'Products and versions'

router = APIRouter()
version_service = Version_service() 

@router.get("/")
async def get_all_products():
    try: 
        return version_service.get_products()
    except Exception as e:
        raise_http_exception(str(e))

@router.get("/{product_id}/versions/")
async def get_all_versions_of_a_product(product_id):
    try:
        return version_service.get_versions_by_product_id(product_id)
    except Exception as e: 
        raise_http_exception(str(e))

