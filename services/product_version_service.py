from sqlalchemy.orm.exc import NoResultFound

from res.errors import Data_not_exist_exception, Invalid_data_exception, No_result_exception
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
            raise NoResultFound("Products not found")
        return products
    
    def get_version(self, version_code: int):
        return db.get_version(version_code)

    def get_versions_by_product_id(self, product_id: int):
        if not self.product_exist(product_id):
            raise Data_not_exist_exception(f"Product id {product_id} doesn't exist")
        
        versions = db.get_versions_by_product_id(product_id)
        if not versions:
            raise No_result_exception(f"Versions of product {product_id} not found")
        return versions
    
    def get_version(self, product_id: int, version_code: str):
        if not version_code: 
            raise Invalid_data_exception("Version code is invalid")
        
        if not self.product_exist(product_id):
            raise Data_not_exist_exception("Product id doesn't exist")
        
        version = db.get_version_by_product_id(product_id, version_code)
        return version
    
    def validate_version(self, product_id: int, version_code: str):
        if not self.get_version(product_id, version_code):
            raise Data_not_exist_exception(f"There is no version {version_code} of the product {product_id}")