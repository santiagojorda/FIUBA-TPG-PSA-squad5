from sqlalchemy.orm.exc import NoResultFound

from res.errors import Version_code_not_exist_exception, Product_not_exist_exception, Invalid_data_exception, Versions_product_not_found_exception, Products_not_found_exception
from res.database import db

class Version_service():

    def product_exist(self, product_id: int):
        product = db.get_product_by_id(product_id)
        if not product:
            return False
        return True

    def get_products(self):
        products = db.get_products()
        if not products:
            raise Products_not_found_exception()
        return products
    
    def get_version(self, version_code: int):
        return db.get_version(version_code)

    def get_versions_by_product_id(self, product_id: int):
        if not self.product_exist(product_id):
            raise Product_not_exist_exception(product_id)
        
        versions = db.get_versions_by_product_id(product_id)
        if not versions:
            raise Versions_product_not_found_exception(product_id)
        return versions
    
    def get_version(self, product_id: int, version_code: str):
        if not version_code: 
            return False
        
        if not self.product_exist(product_id):
            raise Product_not_exist_exception(product_id)
        
        version = db.get_version_by_product_id(product_id, version_code)
        return version
    
    def validate_version(self, product_id: int, version_code: str):
        if not self.get_version(product_id, version_code):
            raise Version_code_not_exist_exception(product_id, version_code)