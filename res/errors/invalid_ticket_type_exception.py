class Invalid_ticket_type_exception(Exception):
    def __init__(self, ticket_type):
        self.message = f"Invalid ticket type {ticket_type}"
        super().__init__(self.message)