class TicketNotFoundException(Exception):
    def __init__(self, ticket_id: int):
        self.message = f"Ticket with id {ticket_id} not found"
        super().__init__(self.message)
