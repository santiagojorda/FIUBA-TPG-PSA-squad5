class Invalid_severity_exception(Exception):
    def __init__(self, severity_id):
        self.message = f"Invalid severity {severity_id}"
        super().__init__(self.message)