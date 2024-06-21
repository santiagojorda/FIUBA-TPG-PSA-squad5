from fastapi import APIRouter
from services.version_service import version_service  # Asegúrate de importar correctamente

PATH = "/versions"

router = APIRouter()
# Usa version_service en minúscula aquí para coincidir con la importación
version_service = version_service() 

# Devuelve todas las versiones
@router.get("/")
async def get_versions():
    versions = version_service.get_versions()
    return {"versions": versions}

# Devuelve una versión buscada por su ID
@router.get("/{version_id}")
async def get_version(version_id: int):
    version = version_service.get_version(version_id)
    if not version:
        raise HTTPException(status_code=404, detail="Version not found")
    return {"version": version}

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


# asdasdasd.com/products/                        -> todos los productos y todas sus versiones
# asdasdasd.com/products/123123                  -> producto
# asdasdasd.com/product_service/title/carlos     -> product
# asdasdasd.com/products/1242/23.0.4 -> string   -> product + version
