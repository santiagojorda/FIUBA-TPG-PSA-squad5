from res.database import db

from models.version import Version

class Version_service():

    def __init__(self):
        self.db = db

    def get_version(self, version_code: int):
        return self.db.get_session().query(Version).filter(Version.version_code == version_code).first()

    def get_versions(self):
        return self.db.get_session().query(Version).all()

    def get_versions_by_product_id(self, product_id: int):
        return self.db.get_session().query(Version).filter(Version.product_id == product_id).all()    
    
    def get_version_by_product_id(self, product_id: int, version_code: str):
        return self.db.get_session().query(Version).filter(Version.product_id == product_id, Version.version_code == version_code).first()    