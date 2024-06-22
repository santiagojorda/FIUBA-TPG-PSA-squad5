from fastapi import APIRouter
from services.product_service import Product_service


PATH = "/products"

router = APIRouter()
product_service = Product_service() 

# Devuelve todos los productos y todas sus versiones
@router.get("/")
async def index():
    return {'mensaje': 'todos los productos'}

# Devuelve todos los productos
@router.get("/products")
async def get_products():
    products = product_service.get_products()
    return {"products": products}

# Devuelve un producto buscado por su ID
@router.get("/products/{product_id}")
async def get_product(product_id: int):
    product = product_service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"product": product}


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
