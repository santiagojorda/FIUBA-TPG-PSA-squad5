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
from tests.features.utils.utils import assert_fields_two_dics

ticket_service = Ticket_service()

def init_query_enviroment(context):
    existing_product_id, existing_version_code = create_version_and_product_1()
    context.original_ticket = create_query_ticket(existing_product_id, existing_version_code)
    context.original_ticket.id = ticket_service.create_ticket(context.original_ticket)

def init_incident_enviroment(context):
    existing_product_id, existing_version_code = create_version_and_product_1()
    context.original_ticket = create_incident_ticket(existing_product_id, existing_version_code)
    context.original_ticket.id = ticket_service.create_ticket(context.original_ticket)

# --- Escenario 1

@given("se selecciona un ticket consulta existente y se ingresan nuevos datos de ticket consulta validos")
def modify_valid_query_ticket(context):

    init_query_enviroment(context)

    context.original_ticket.new_title = MOCK_TICKET_TITLE_2
    context.original_ticket.new_description = MOCK_TICKET_DESCRIPCION_2
    context.original_ticket.response = MOCK_TICKET_RESPONSE_2
    context.original_ticket.closing_date = MOCK_CLOSING_DATE


@when("se modifica un ticket")
def modify_ticket(context):
    opening_date = context.original_ticket.opening_date
    closing_date = context.original_ticket.closing_date
    if opening_date:
        context.original_ticket.opening_date = str(opening_date)
    if closing_date:
        context.original_ticket.closing_date = str(closing_date)

    context.response = context.client.put(f"{ENDPOINT_TICKETS}/{context.original_ticket.product_id}/{context.original_ticket.version_code}/{context.original_ticket.id}",
        json = {
            "id": context.original_ticket.id,
            "product_id": context.original_ticket.product_id,
            "version_code": context.original_ticket.version_code,
            "title": context.original_ticket.title,
            'description': context.original_ticket.description,
            'client_id': context.original_ticket.client_id,
            'employee_id': context.original_ticket.employee_id,
            'ticket_type': context.original_ticket.ticket_type,
            'response': context.original_ticket.response,
            'status': context.original_ticket.status,
            'opening_date': context.original_ticket.opening_date,
            'closing_date': context.original_ticket.closing_date,
        }
    ) 

@then("se modifica el ticket y le informa al usuario que se hizo correctamente")
def check_ticket_is_modified_successfully(context):
    response = context.response.json()
    print(response)
    assert response['message'] == MESSAGE_TICKET_MODIFIED
    requested_ticket = ticket_service.get_ticket(
        context.original_ticket.product_id,
        context.original_ticket.version_code,
        context.original_ticket.id
    )
    original_ticket = context.original_ticket
    modified_ticket = context.modified_ticket
    assert requested_ticket.id == original_ticket.id
    assert requested_ticket.product_id == original_ticket.product_id
    assert requested_ticket.version_code == original_ticket.version_code
    assert requested_ticket.title == original_ticket.title
    assert requested_ticket.description == original_ticket.description
    # assert requested_ticket.opening_date == original_ticket.opening_date
    # assert requested_ticket.closing_date == original_ticket.closing_date
    assert requested_ticket.status == original_ticket.status
    assert requested_ticket.response == original_ticket.response
    assert requested_ticket.playback_steps == modified_ticket.playback_steps
    assert requested_ticket.employee_id == original_ticket.employee_id
    assert requested_ticket.client_id == original_ticket.client_id
    assert requested_ticket.severity_id == original_ticket.severity_id
    # assert_fields_two_dics(requested_ticket, original_ticket, 'id')


#--- Escenario 2

# @given("se selecciona un ticket incidente existente y se ingresan nuevos datos de ticket incidente validos")
# def modify_valid_query_ticket(context):
#     init_query_enviroment(context)
#     context.modified_ticket = context.original_ticket 
#     context.original_ticket.new_title = MOCK_TICKET_TITLE_2
#     context.original_ticket.new_description = MOCK_TICKET_DESCRIPCION_2
#     context.original_ticket.client_id = MOCK_TICKET_CLIENT_ID_2
#     context.original_ticket.employee_id = MOCK_TICKET_CLIENT_ID_2
#     context.original_ticket.playback_steps = MOCK_PLAYBACK_STEPS_2
#     context.original_ticket.severity_id = MOCK_SEVERITY_ID_2
#     context.original_ticket.duration = MOCK_DURATION_2
#     context.original_ticket.closing_date = MOCK_CLOSING_DATE
