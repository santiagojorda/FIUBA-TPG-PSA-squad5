from res.database import db

from models.severity import Severity

class Severity_service():

    def __init__(self):
        self.db = db

    def get_severity(self, severity_id: int):
        return self.db.get_session().query(Severity).filter(Severity.id_severity == severity_id).first()
    
    def get_severitys(self):
        return self.db.get_session().query(Severity).all()
