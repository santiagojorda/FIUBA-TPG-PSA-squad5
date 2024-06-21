# my_fastapi_app/crud/cliente_crud.py
from sqlalchemy.orm import Session
from models.version import Version
from res.database import db

class version_service:

    def __init__(self):
        self.db = db

    def get_version(self, version_id: int):
        return self.db.get_session().query(Version).filter(Version.id_version == version_id).first()

    def get_versions(self):
        return self.db.get_session().query(Version).all()