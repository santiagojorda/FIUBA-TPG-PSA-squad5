from res.database import db

from models.severity import *
from res.errors import Severity_not_found_exception, Invalid_severity_exception

class Severity_service():

    def create_severity(self, response_time: int):
        if response_time <= 0:
            raise Invalid_severity_exception(f"Invalid response time {response_time}")
        db.create_severity(response_time)

    def validate_severity(self, severity_id: int):
        if not severity_id:
            raise Invalid_severity_exception(severity_id)
        
        severity_exist = db.get_severity(severity_id)
        
        if not severity_exist:
            raise Severity_not_found_exception(severity_id)
