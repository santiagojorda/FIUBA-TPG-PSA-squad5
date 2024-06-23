from fastapi import APIRouter, HTTPException
from services.product_service import Product_service
from services.version_service import Version_service

PATH = "/products"
PRODUCT_TAG = 'Products'

router = APIRouter()
product_service = Product_service() 
version_service = Version_service() 

# Devuelve todos los productos
@router.get("/", tags=[PRODUCT_TAG])
async def get_products():
    products = product_service.get_products()
    return {"products": products}

# Devuelve un producto buscado por su ID
@router.get("/{product_id}", tags=[PRODUCT_TAG])
async def get_product(product_id: int):
    product = product_service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"product": product}

# Devuelve el producto y su version
@router.get("/{product_id}/v/{version_id}", tags=[PRODUCT_TAG])
async def get_version_of_a_product(product_id, version_id):
    version = version_service.get_version_by_product_id(product_id, version_id)
    if not version:
        raise HTTPException(status_code=404, detail="Version not found")
    return {"version": version}


# Devuelve el producto con id con todas sus versiones
@router.get("/{product_id}/v/", tags=[PRODUCT_TAG])
async def get_versions_of_a_product(product_id):
    versions = version_service.get_versions_by_product_id(product_id)
    if not versions:
        raise HTTPException(status_code=404, detail="Versions not found")
    return {"versions": versions}

# Devuelve el producto con titulo con todas sus versiones
@router.get("/title/{product_title}", tags=[PRODUCT_TAG])
async def index(product_title):
    return {'mensaje': f"devuelve el producto con titulo {product_title}"}

# devuelve la release note dependiendo el producto y la version
@router.get("{product_id}/{version_id}", tags=[PRODUCT_TAG])
async def index(product_id, version_id):
    return {'mensaje': f"devuelve la version con su realease note"}


# asdasdasd.com/products/                        -> todos los productos y todas sus versiones
# asdasdasd.com/products/123123                  -> producto
# asdasdasd.com/product_service/title/carlos     -> product
# asdasdasd.com/products/1242/23.0.4 -> string   -> product + version
