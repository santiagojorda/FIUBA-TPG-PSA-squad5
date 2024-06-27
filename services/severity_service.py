from res.database import db

from models.severity import *
from res.errors import No_result_exception

class Severity_service():

    def get_severity(self, severity_id: int):
        return db.get_session().query(Severity).filter(Severity.id_severity == severity_id).first()
    
    def get_severitys(self):
        return db.get_session().query(Severity).all()

    def validate_severity(self, severity_id: int):
        severity_exist = db.get_severity(severity_id)
        if severity_exist is None:
            raise No_result_exception("Severity id {severity_id} not found")
