from fastapi import APIRouter
from services.version_service import Version_service

PATH = "/versions"

router = APIRouter()
version_service = Version_service() 


# @router.get("/versions")
# async def get_versions():
#     versions = version_service.get_versions()
#     return {"versions": versions}

# @router.get("/product/version/")
# async def get_versions(product_id: int):
#     versions = version_service.get_versions_by_product_id(product_id)
#     return {"versions": versions}




# # Devuelve el producto con id con todas sus versiones
# @router.get("/{product_id}")
# async def index(product_id):
#     return {'mensaje': f"devuelve el producto con id {product_id}"}

# # Devuelve el producto con titulo con todas sus versiones
# @router.get("/title/{product_title}")
# async def index(product_title):
#     return {'mensaje': f"devuelve el producto con titulo {product_title}"}

# # devuelve la release note dependiendo el producto y la version
# @router.get("{product_id}/{version_id}")
# async def index(product_id, version_id):
#     return {'mensaje': f"devuelve la version con su realease note"}

