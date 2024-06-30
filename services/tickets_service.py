from models.ticket import TicketModel, INCIDENT_TICKET, QUERY_TICKET
from res.errors import Invalid_data_exception, Invalid_date_exception, Invalid_ticket_type_exception, Invalid_playback_steps_exception, No_result_exception, Closing_date_earlier_than_opening_exception, Invalid_description_exception, Invalid_title_exception
from services.product_version_service import Version_service
from services.severity_service import Severity_service
from services.client_service import Client_service
from services.employee_service import Employee_service
from res.database import db
from datetime import date


version_service = Version_service()
severity_service = Severity_service()
client_service = Client_service()
employee_service = Employee_service()

class Ticket_service():

    def get_ticket(self, product_id: int, version_code: str, ticket_id: int):
        version_service.validate_version(product_id, version_code)
        ticket = db.get_ticket(ticket_id)
        if ticket is None or ticket_id != ticket.id:
            print('no hay ticket')
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

    def validate_ticket_type(self, ticket_type: int):
        if ticket_type is None or not ticket_type in [QUERY_TICKET, INCIDENT_TICKET]:
            raise Invalid_ticket_type_exception(ticket_type)

    def validate_ticket_title(self, ticket_title: str):
        if ticket_title is None or len(ticket_title) <= 0:
            raise Invalid_title_exception(ticket_title)
        
    def validate_ticket_playback_steps(self, playback_steps: str):
        if playback_steps is None or len(playback_steps) <= 0:
            raise Invalid_playback_steps_exception(playback_steps)
        
    def validate_ticket_description(self, description: str):
        if description is None or len(description) <= 0:
            raise Invalid_description_exception(description)
        
    def validate_dates(self, opening_date: str, closing_date: str):
        # if not opening_date:
        #     raise Invalid_date_exception(opening_date)
        if closing_date and opening_date and closing_date > date.today():
            print(closing_date)
            print(opening_date)
            if closing_date < opening_date:
                raise Closing_date_earlier_than_opening_exception(opening_date, closing_date)

    def validate_ticket(self, ticket_data: TicketModel):
        version_service.validate_version(ticket_data.product_id, ticket_data.version_code)
        client_service.validate_client(ticket_data.client_id)
        employee_service.validate_employee(ticket_data.employee_id)
        self.validate_ticket_type(ticket_data.ticket_type)
        self.validate_ticket_title(ticket_data.title)
        self.validate_ticket_description(ticket_data.description)   
        self.validate_dates(ticket_data.opening_date, ticket_data.closing_date)


        if ticket_data.ticket_type == INCIDENT_TICKET:
            severity_service.validate_severity(ticket_data.severity_id)
            self.validate_ticket_playback_steps(ticket_data.playback_steps)


    def create_ticket(self, ticket_data: TicketModel):
        
        self.validate_ticket(ticket_data)

        return db.create_ticket(ticket_data)
        
    def modify_ticket(self, product_id: int, version_code: int, new_ticket: TicketModel):
        print(new_ticket)
        ticket = self.get_ticket(product_id, version_code, new_ticket.id)
        self.validate_dates(new_ticket.opening_date, new_ticket.closing_date)
        print(ticket)
        ticket = db.modify_ticket(new_ticket)
        if not ticket:
            raise No_result_exception(f"The modification could not be completed.")
        return ticket
    
    def delete_ticket(self, product_id: int, version_code: str, ticket_id: int):
        id_deleted = db.delete_ticket(ticket_id)
        if not id_deleted:
            raise No_result_exception(f"There is no ticket id {ticket_id}")
        return id_deleted