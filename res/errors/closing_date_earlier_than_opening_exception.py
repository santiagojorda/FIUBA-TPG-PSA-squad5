class Closing_date_earlier_than_opening_exception(Exception):
    def __init__(self, opening_date, closing_date):
        self.message = f"Closing date {closing_date} is earlier than opening date {opening_date}"
        super().__init__(self.message)