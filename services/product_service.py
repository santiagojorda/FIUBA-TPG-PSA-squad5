from res.database import db
from models.product import Product

class Product_service():

    def __init__(self):
        self.db = db

    def get_product(self, product_id: int):
        return self.db.get_session().query(Product).filter(Product.id == product_id).first()
    
    def get_products(self):
        return self.db.get_session().query(Product).all()
