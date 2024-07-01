class Invalid_status_exception(Exception):
    def __init__(self, status):
        self.message = f"Invalid status {status}"
        super().__init__(self.message)