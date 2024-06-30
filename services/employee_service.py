import requests

from res.errors import Employee_not_found_exception

ENDPOINT_EMPLOYEES = 'https://psa-project-microservice.onrender.com/workers'

class Employee_service():

    def get_employee(self, employee_id: int):
        response = requests.get(f"{ENDPOINT_EMPLOYEES}/{employee_id}")
        if response.status_code != 200:
            return False

        client = response.json()
        return client['id']
    
    def validate_employee(self, employee_id: int):
        client_exist = self.get_employee(employee_id)
        if not client_exist:
            raise Employee_not_found_exception(employee_id)
