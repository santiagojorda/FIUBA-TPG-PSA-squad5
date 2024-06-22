from res.database import db

class Version_service():

    def __init__(self):
        self.db = db

    # def get_version(self, version_id: int):
    #     return self.db.get_session().query(Version).filter(Version.id_version == version_id).first()

    # def get_versions(self):
    #     return self.db.get_session().query(Version).all()

    # def get_versions_by_product_id(self, product_id: int):
    #     return self.db.get_session().query(Version).filter(Version.id_product == product_id).all()    