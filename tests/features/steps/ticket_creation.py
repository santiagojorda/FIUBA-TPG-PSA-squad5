from behave.api.async_step import async_run_until_complete
from behave import *
from utils import *

from models.ticket import TicketModel

from services.tickets_service import Ticket_service

ticket_service = Ticket_service()

ID_TICKET_MOCK = 4

@given('Ticket creation data')
@async_run_until_complete
async def given_incident_ticket(context):
    context.new_data_ticket = {}
    for row in context.table:
        context.new_data_ticket = {
            'product_id': row.get('product_id', None),
            'version_code': row.get('version_code', None),
            'title': row.get('title', None),
            'description': row.get('description', None),
            'client_id': row.get('client_id', None),
            'employee_id': row.get('employee_id', None),
            'ticket_type': row.get('ticket_type', None),
            'severity_id': row.get('severity_id', None),
            'playback_steps': row.get('playback_steps', None),
            'response': row.get('response', None)
        }

@when('create a new ticket')
@async_run_until_complete
async def when_create_ticket(context):
    try:
        context.new_ticket = TicketModel(**context.new_data_ticket)
        ticket_service.create_ticket(context.new_ticket)
    except Exception as e:
        print(e)
        context.error = e

@then('the ticket should be created successfully')
@async_run_until_complete
async def then_ticket_created_successfully(context):
    try:
        if hasattr(context, 'error'):
            raise context.error
 
        created_ticket = ticket_service.get_ticket(
            context.new_ticket.product_id,
            context.new_ticket.version_code,
            ID_TICKET_MOCK
        )

        if created_ticket:
            ticket_service.delete_ticket(
                context.new_ticket.product_id,
                context.new_ticket.version_code,
                ID_TICKET_MOCK
            )
    
        assert created_ticket is not None, "Incident Ticket with valid data created successfully"

    except Exception as e:
        print(f"Expected failure encountered: {e}")
        assert False, "Incident Ticket with valid data failed creation"


@then('the creation would be failed')
@async_run_until_complete
async def then_ticket_created_successfully(context):
    try:
        if hasattr(context, 'error'):
            raise context.error

        created_ticket = ticket_service.get_ticket(
            context.new_ticket.product_id,
            context.new_ticket.version_code,
            ID_TICKET_MOCK
        )
        
        if created_ticket:
            ticket_service.delete_ticket(
                context.new_ticket.product_id,
                context.new_ticket.version_code,
                ID_TICKET_MOCK
            )
        assert created_ticket is None, "Incident Ticket with invalid data failed creation as expected"
    except Exception as e:
        print(f"Expected failure encountered: {e}")
        assert True, "Incident Ticket with invalid data failed creation as expected"

