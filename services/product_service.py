from res.database import db

class Product_service():
    
    def get_products(self):
        return db.get_products()
