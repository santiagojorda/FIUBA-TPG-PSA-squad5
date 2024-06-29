from behave import *
from datetime import datetime
from services.tickets_service import Ticket_service
from routes.tickets_routes import PATH as ENDPOINT_TICKETS
from res.errors import Invalid_data_exception, No_result_exception, Version_code_not_exist_exception
from tests.features.utils.utils import assert_exception_message
from models.ticket import * 
from routes.tickets_routes import * 
from tests.features.utils.ticket_mock import *
from tests.features.utils.client_mock import *
from tests.features.utils.product_version_mock import *

ticket_service = Ticket_service()

def create_query_ticket(product_id, version_code):
    return Ticket(
        id = 1,
        product_id = product_id,
        version_code = version_code,
        title = MOCK_TICKET_TITLE,
        description = MOCK_TICKET_DESCRIPCION,
        client_id = MOCK_TICKET_CLIENT_ID,
        employee_id = MOCK_TICKET_EMPLOYEE_ID,
        ticket_type = QUERY_TICKET,
        response = MOCK_TICKET_RESPONSE,
        opening_date = MOCK_OPENING_DATE
    )

def modify_query_ticket(ticket, new_title=None, new_description=None, new_response=None, closing_date=None):
    if new_title:
        ticket.title = new_title
    if new_description:
        ticket.description = new_description
    if new_response:
        ticket.response = new_response
    if closing_date:
        ticket.closing_date = closing_date
    return ticket

@given("se Modifican datos de ticket consulta validos")
def modify_valid_query_ticket(context):
    existing_product_id, existing_version_code = create_version_and_product_1()
    context.original_ticket = create_query_ticket(existing_product_id, existing_version_code)
    context.original_ticket_id = context.original_ticket.id  # Guardar el ID del ticket original para futuras referencias
    ticket_service.create_ticket(context.original_ticket)
    context.modified_ticket = modify_query_ticket(context.original_ticket, new_title="Nuevo Título", new_description="Nueva Descripción", new_response="Nueva Respuesta", closing_date=date.today())

@when("se modifica un ticket")
def modify_ticket(context):
    opening_date = context.modified_ticket.opening_date
    closing_date = context.modified_ticket.closing_date
    if opening_date:
        opening_date = str(opening_date)
    if closing_date:
        closing_date = str(closing_date)

    context.response = context.client.put(f"{ENDPOINT_TICKETS}/{context.original_ticket.product_id}/{context.original_ticket.version_code}/{context.original_ticket_id}",
        json = {
            "id": context.original_ticket.id,
            "product_id": context.modified_ticket.product_id,
            "version_code": context.modified_ticket.version_code,
            "title": context.modified_ticket.title,
            'description': context.modified_ticket.description,
            'client_id': context.modified_ticket.client_id,
            'employee_id': context.modified_ticket.employee_id,
            'ticket_type': context.modified_ticket.ticket_type,
            'response': context.modified_ticket.response,
            'opening_date': opening_date,
            'closing_date': closing_date,
        }
    )

@then("se modifica el ticket y le informa al usuario que se hizo correctamente")
def check_ticket_is_modified_successfully(context):
    response = context.response.json()
    print(response)
    assert response['message'] == MESSAGE_TICKET_MODIFIED
