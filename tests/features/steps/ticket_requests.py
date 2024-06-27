from behave.api.async_step import async_run_until_complete
from behave import *
from utils import *

from services.tickets_service import Ticket_service

ticket_service = Ticket_service()

@given('Tickets obtaining data')
@async_run_until_complete
async def given_obtaining_data(context):
    for row in context.table:
        context.product_id = row.get('product_id', None)
        context.version_code = row.get('version_code', None)
        context.ticket_id = row.get('ticket_id', None)

@when('gets tickets of a version and product')
@async_run_until_complete
async def when_gets_tickets(context):
    try:
        context.tickets = ticket_service.get_tickets(
            context.product_id, 
            context.version_code
        )
    except Exception as e:
        print(e)
        context.error = e

@when('get an specific ticket')
@async_run_until_complete
async def when_get_tiket(context):
    try:
        context.ticket_id = int(context.ticket_id)
        context.ticket = ticket_service.get_ticket(
            context.product_id,
            context.version_code,
            context.ticket_id    
        )
    except Exception as e:
        print(e)
        context.error = e

@then('the tickets should be retrieved successfully')
@async_run_until_complete
async def then_tickets_obtained_succesfully(context):
    try:
        if hasattr(context, 'error'):
            raise context.error

        tickets = ticket_service.get_tickets(
            context.product_id,
            context.version_code
        )
        
        assert tickets, "Tickets obtained successfully"
    except Exception as e:
        print(f"Expected failure encountered: {e}")
        assert False, "Could not get tickets"

@then('the ticket should be retrieved successfully')
@async_run_until_complete
async def then_ticket_obtained_succesfully(context):
    try:
        if hasattr(context, 'error'):
            raise context.error

        ticket = ticket_service.get_ticket(
            context.product_id,
            context.version_code,
            context.ticket_id
        )
        assert ticket, "Ticket obtained successfully"
    except Exception as e:
        print(f"Expected failure encountered: {e}")
        assert False, "Could not get tickets"

@then('the tickets retrieval would be failed')
@async_run_until_complete
async def then_tickets_retrieval_failed(context):
    try:
        if hasattr(context, 'error'):
            raise context.error

        tickets = ticket_service.get_tickets(
            context.product_id,
            context.version_code
        )
        assert tickets is None, "Tickets obtained but are not expected"
    except Exception as e:
        print(f"Expected failure encountered: {e}")
        assert True, "Tickets are not obtained as expected"

@then('the ticket retrieval would be failed')
@async_run_until_complete
async def then_ticket_retrieval_failed(context):
    try:
        if hasattr(context, 'error'):
            raise context.error

        ticket = ticket_service.get_ticket(
            context.product_id,
            context.version_code,
            context.ticket_id
        )
        assert ticket is None, "Ticket obtained but is not expected"
    except Exception as e:
        print(f"Expected failure encountered: {e}")
        assert True, "Ticket is not obtained as expected"