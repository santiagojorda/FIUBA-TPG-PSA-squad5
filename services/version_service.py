from res.database import db

class Version_service():

    def get_version(self, version_code: int):
        return db.get_version(version_code)

    def get_versions_by_product_id(self, product_id: int):
        return db.get_versions_by_product_id(product_id)
    
    def get_version_by_product_id(self, product_id: int, version_code: str):
        return db.get_version_by_product_id(product_id, version_code)