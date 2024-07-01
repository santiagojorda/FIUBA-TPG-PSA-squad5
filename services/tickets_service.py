from models.ticket import TicketModel, INCIDENT_TICKET, QUERY_TICKET, STATUS_CLOSED, STATUS_NEW_TICKET
from res.errors import Invalid_status_exception, Ticket_not_found_exception, Invalid_ticket_type_exception, Invalid_playback_steps_exception, No_result_exception, Closing_date_earlier_than_opening_exception, Invalid_description_exception, Invalid_title_exception
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
            raise Ticket_not_found_exception(product_id, version_code, ticket_id)
        return ticket

    def get_tickets(self, product_id: int, version_code: str):
        version_service.validate_version(product_id, version_code)

        tickets = db.get_tickets(product_id, version_code)
        if not tickets:
            raise No_result_exception("Tickets not found")
        return tickets
    
    def validate_exist(self, product_id: int, version_code: int, ticket_id: int):
        try: 
            self.get_ticket(product_id, version_code, ticket_id)
            return True
        except:
            return False
         
    def validate_ticket_type(self, ticket_type: int):
        if ticket_type is None or not ticket_type in [QUERY_TICKET, INCIDENT_TICKET]:
            raise Invalid_ticket_type_exception(ticket_type)

    def validate_ticket_title(self, ticket_title: str):
        if self.is_valid_string(ticket_title):
            raise Invalid_title_exception(ticket_title)
        
    def validate_ticket_playback_steps(self, playback_steps: str):
        if self.is_valid_string(playback_steps):
            raise Invalid_playback_steps_exception(playback_steps)
        
    def validate_ticket_description(self, description: str):
        if self.is_valid_string(description):
            raise Invalid_description_exception(description)
        
    def validate_dates(self, opening_date: str, closing_date: str):
        if closing_date and opening_date and closing_date < date.today():
            if closing_date < opening_date:
                raise Closing_date_earlier_than_opening_exception(opening_date, closing_date)

    def is_valid_status(self, status: int):
        print(status >= STATUS_NEW_TICKET and status <= STATUS_CLOSED)
        return status >= STATUS_NEW_TICKET and status <= STATUS_CLOSED

    def validate_status(self, status: int):
        if status is None or not self.is_valid_status(status):
            raise Invalid_status_exception(status)

    def validate_ticket(self, ticket_data: TicketModel):
        version_service.validate_version(ticket_data.product_id, ticket_data.version_code)
        client_service.validate_client(ticket_data.client_id)
        employee_service.validate_employee(ticket_data.employee_id)
        self.validate_ticket_type(ticket_data.ticket_type)
        self.validate_ticket_title(ticket_data.title)
        self.validate_ticket_description(ticket_data.description)   
        self.validate_dates(ticket_data.opening_date, ticket_data.closing_date)
        self.validate_status(ticket_data.status)

        if ticket_data.ticket_type == INCIDENT_TICKET:
            severity_service.validate_severity(ticket_data.severity_id)
            self.validate_ticket_playback_steps(ticket_data.playback_steps)


    def create_ticket(self, ticket_data: TicketModel):
        self.validate_ticket(ticket_data)

        return db.create_ticket(ticket_data)
        
    def modify_ticket(self, product_id: int, version_code: int, new_ticket: TicketModel):
        self.validate_modification(product_id, version_code, new_ticket)

        ticket = db.modify_ticket(new_ticket)
        if not ticket:
            raise No_result_exception(f"The modification could not be completed.")
        return ticket
    
    def delete_ticket(self, product_id: int, version_code: str, ticket_id: int):
        if not self.validate_exist(product_id, version_code, ticket_id):
            raise Ticket_not_found_exception(product_id, version_code, ticket_id)
        
        id_deleted = db.delete_ticket(ticket_id)
        if not id_deleted:
            raise Ticket_not_found_exception(product_id, version_code, ticket_id)
        return id_deleted
    
    def is_valid_string(self, string: str):
        return string is None or len(string) <= 0

    def validate_modification(self, product_id: int, version_code: int, new_ticket: TicketModel):
        version_service.validate_version(product_id, version_code)

        old_ticket = self.get_ticket(product_id, version_code, new_ticket.id)
        
        if old_ticket.title and self.is_valid_string(new_ticket.title):
            raise Invalid_title_exception(new_ticket.title)
        
        if old_ticket.description and self.is_valid_string(new_ticket.description):
            raise Invalid_description_exception(new_ticket.description)
        
        if new_ticket.ticket_type:
            self.validate_ticket_type(new_ticket.ticket_type)
        
        if new_ticket.client_id:
            client_service.validate_client(new_ticket.client_id)
        
        if new_ticket.employee_id:
            employee_service.validate_employee(new_ticket.employee_id)

        if new_ticket.status:
            self.validate_status(new_ticket.status)
        
        if new_ticket.closing_date:
            print(type(old_ticket.opening_date))
            print(type(new_ticket.closing_date))
            self.validate_dates(old_ticket.opening_date, new_ticket.closing_date)
        
        self.validate_dates(new_ticket.opening_date, new_ticket.closing_date)
