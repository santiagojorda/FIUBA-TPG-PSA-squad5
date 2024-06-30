from res.database import db

from models.severity import *
from res.errors import No_result_exception, Invalid_data_exception

class Severity_service():

    def create_severity(self, response_time: int):
        print(f"response_time create {response_time}")
        if response_time <= 0:
            raise Invalid_data_exception(f"Invalid response time {response_time}")
        db.create_severity(response_time)

    def validate_severity(self, severity_id: int):
        print(f"severity id {severity_id}")
        severity_exist = db.get_severity(severity_id)
        print(f"severity {severity_exist}")
        if not severity_exist:
            raise No_result_exception("Severity id {severity_id} not found")
