import requests

from models.ticket import TicketModel, INCIDENT_TICKET, QUERY_TICKET
from res.errors import Invalid_data_exception, No_result_exception
from services.product_version_service import Version_service
from services.severity_service import Severity_service
from res.database import db

version_service = Version_service()
severity_service = Severity_service()

class Ticket_service():

    def get_ticket(self, product_id: int, version_code: int, ticket_id: int):
        version_service.validate_version(product_id, version_code)

        ticket = db.get_ticket(ticket_id)
        if ticket is None or ticket_id != ticket.id:
            raise No_result_exception(f"There is no ticket id {ticket_id} in version {version_code} of the product {product_id}")
        return ticket

    def get_tickets(self, product_id: int, version_code: str):
        version_service.validate_version(product_id, version_code)

        tickets = db.get_tickets(product_id, version_code)
        if not tickets:
            raise No_result_exception("Tickets not found")
        return tickets
    
    def validate_ticket(self, product_id: int, version_code: int, ticket_id: int):
        self.get_ticket(product_id, version_code, ticket_id)

    # VER MANEJO DE ERRORES
    def create_ticket(self, ticket_data: TicketModel):

        if ticket_data.title == "" or ticket_data.title == " ":
            raise Invalid_data_exception(f"Title cannot be empty")
        if ticket_data.description == "" or ticket_data.description == " ":
            raise Invalid_data_exception(f"Description cannot be empty")
        
        if ticket_data.closing_date:
            if ticket_data.closing_date < ticket_data.opening_date:
                raise Invalid_data_exception(f"Closing date cannot be earlier than opening date")
        
        # if not employee_service.exist(ticket_data.employee_id):
        #     raise Invalid_data_exception(f"Employee {ticket_data.employee_id} doesn't exist")

        version_service.validate_version(ticket_data.product_id, ticket_data.version_code)

        if not ticket_data.ticket_type in [QUERY_TICKET, INCIDENT_TICKET]:
            raise Invalid_data_exception(f"Ticket type is invalid")
        
        if ticket_data.ticket_type == INCIDENT_TICKET:
            if ticket_data.playback_steps == "" or ticket_data.playback_steps == " ":
                raise Invalid_data_exception(f"Playback steps cannot be empty")

            if not severity_service.exists(ticket_data.severity_id):
                raise Invalid_data_exception(f"Severity is not valid")

        ticket_id = db.create_ticket(ticket_data)
        return ticket_id
        
    def modify_ticket(self, product_id: int, version_code: int, new_ticket: TicketModel):
        ticket = self.get_ticket(product_id, version_code, new_ticket.id)
        if new_ticket.closing_date:
            if new_ticket.closing_date < ticket.opening_date:
                raise Invalid_data_exception(f"Closing date cannot be earlier than opening date")

        ticket = db.modify_ticket(ticket)
        if not ticket:
            raise No_result_exception(f"The modification could not be completed.")
        return ticket
    
    def delete_ticket(self, product_id: int, version_code: str, ticket_id: int):
        self.validate_ticket(product_id, version_code, ticket_id)

        id_deleted = db.delete_ticket(ticket_id)
        if not id_deleted:
            raise No_result_exception(f"There is no ticket id {ticket_id}")
        return id_deleted