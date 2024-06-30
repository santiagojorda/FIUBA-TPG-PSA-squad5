class Invalid_date_exception(Exception):
    def __init__(self, date):
        self.message = f"Invalid date {date}"
        super().__init__(self.message)