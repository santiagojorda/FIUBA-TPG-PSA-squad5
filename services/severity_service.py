from res.database import db

from models.severity import *
from res.errors import Severity_not_found_exception, Invalid_data_exception

class Severity_service():

    def create_severity(self, response_time: int):
        if response_time <= 0:
            raise Invalid_data_exception(f"Invalid response time {response_time}")
        db.create_severity(response_time)

    def validate_severity(self, severity_id: int):
        print(f"severity id {severity_id}")
        severity_exist = db.get_severity(severity_id)
        print(f"severity {severity_exist}")
        if not severity_exist:
            raise Severity_not_found_exception(severity_id)
