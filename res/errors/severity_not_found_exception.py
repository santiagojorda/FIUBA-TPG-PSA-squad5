class Severity_not_found_exception(Exception):
    def __init__(self, severity_id):
        self.message = f"Severity id {severity_id} not found"
        super().__init__(self.message)