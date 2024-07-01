class Employee_not_found_exception(Exception):
    def __init__(self, employee_id):
        self.message = f"Employee {employee_id} not found"
        super().__init__(self.message)