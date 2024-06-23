from res.database import db
from models.product import Product

class Product_service():
    
    def get_product(self, product_id: int):
        # return db.get_product
        pass
    
    def get_products(self):
        return db.get_products()
