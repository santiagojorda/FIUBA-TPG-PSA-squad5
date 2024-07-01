from behave import *
from datetime import datetime
from services.tickets_service import Ticket_service
from routes.tickets_routes import PATH as ENDPOINT_TICKETS
from res.errors import Invalid_data_exception, No_result_exception, Ticket_not_found_exception
from tests.utils.utils import assert_exception_message
from models.ticket import * 
from routes.tickets_routes import * 
from tests.utils.ticket_mock import *
from tests.utils.client_mock import *
from tests.utils.product_version_mock import *
from tests.utils.severity_mock import * 
from tests.utils.utils import assert_tickets
from tests.environment import init_incident_enviroment, init_query_enviroment  

ticket_service = Ticket_service()


def create_ticket(context):
    context.original_ticket.id = ticket_service.create_ticket(context.original_ticket)
    context.modified_ticket = context.original_ticket

# --- Given

@given("existe un ticket consulta")
def create_valid_query_ticket(context):
    context.original_ticket = create_query_ticket(
        context.product_id, 
        context.version_code
    )
    create_ticket(context)


@given("existe un ticket incidente")
def create_valid_incident_ticket(context):
    context.original_ticket = create_incident_ticket(
        context.product_id, 
        context.version_code
    )
    create_ticket(context)

@given("se ingresan nuevos datos validos de ticket consulta existente")
def modify_query_ticket(context):
    context.modified_ticket = context.original_ticket
    context.modified_ticket.new_title = MOCK_TICKET_TITLE_2
    context.modified_ticket.new_description = MOCK_TICKET_DESCRIPCION_2
    context.modified_ticket.response = MOCK_TICKET_RESPONSE_2
    context.modified_ticket.closing_date = MOCK_CLOSING_DATE
    context.modified_ticket.employee_id = MOCK_TICKET_EMPLOYEE_ID_2
    context.modified_ticket.client_id = MOCK_TICKET_CLIENT_ID_2

@given("se ingresan nuevos datos validos de ticket incidente existente")
def modify_incident_ticket(context):
    context.modified_ticket = context.original_ticket
    context.modified_ticket.new_title = MOCK_TICKET_TITLE_2
    context.modified_ticket.new_description = MOCK_TICKET_DESCRIPCION_2
    context.modified_ticket.closing_date = MOCK_CLOSING_DATE
    context.modified_ticket.employee_id = MOCK_TICKET_EMPLOYEE_ID_2
    context.modified_ticket.client_id = MOCK_TICKET_CLIENT_ID_2
    context.modified_ticket.severity_id = MOCK_SEVERITY_ID_2
    context.modified_ticket.playback_steps = MOCK_PLAYBACK_STEPS_2
    context.modified_ticket.duration = MOCK_DURATION_2


@given("se ingresan datos de moficacion de un ticket que no existe")
def modify_invalid_product_id_ticket(context):
    context.modified_ticket.id = MOCK_TICKET_ID_NOT_EXIST

@given("se ingresan datos de moficacion de un ticket existente con un id de un producto que no existe")
def modify_invalid_product_id_ticket(context):
    context.modified_ticket.product_id = MOCK_PRODUCT_ID_2

@given("se ingresan datos de moficacion de un ticket existente con una versio de un producto que no existe")
def modify_invalid_version_code_ticket(context):
    context.modified_ticket.version_code = MOCK_VERSION_CODE_2

@given("se ingresan datos de moficacion de un ticket existente con una fecha de cierre anterior a la fecha de ingreso")
def modify_invalid_closing_date_ticket(context):
    context.modified_ticket.closing_date = MOCK_CLOSING_DATE_EARLIER_THAN_OPENING

@given("se ingresan datos de moficacion de un ticket existente con una severidad que no existe")
def modify_invalid_closing_date_ticket(context):
    context.modified_ticket.severity_id = MOCK_SEVERITY_NOT_EXIST

@given("se selecciona un ticket incidente existente y se ingresa un tipo de ticket invalido")
def modify_invalid_closing_date_ticket(context):
    context.modified_ticket.ticket_type = MOCK_TICKET_TYPE_INVALID

@given("se ingresan datos de moficacion de un ticket existente con un cliente que no existe")
def modify_invalid_client_ticket(context):
    context.modified_ticket.client_id = MOCK_CLIENT_ID_NOT_EXIST
    context.requested_client_id = context.modified_ticket.client_id

@given("se ingresan datos de moficacion de un ticket existente con un empleado que no existe")
def modify_invalid_employee_ticket(context):
    context.modified_ticket.employee_id = MOCK_EMPLOYEE_ID_NOT_EXIST
    context.requested_employee_id = MOCK_EMPLOYEE_ID_NOT_EXIST

# --- When

@when("se modifica un ticket")
def modify_ticket(context):
    opening_date = context.modified_ticket.opening_date
    closing_date = context.modified_ticket.closing_date
    if opening_date:
        context.modified_ticket.opening_date = str(opening_date)
    if closing_date:
        context.modified_ticket.closing_date = str(closing_date)

    context.response = context.client.put(f"{ENDPOINT_TICKETS}/{context.modified_ticket.product_id}/{context.modified_ticket.version_code}/{context.modified_ticket.id}",
        json = {
            "id": context.modified_ticket.id,
            "product_id": context.modified_ticket.product_id,
            "version_code": context.modified_ticket.version_code,
            "title": context.modified_ticket.title,
            'description': context.modified_ticket.description,
            'client_id': context.modified_ticket.client_id,
            'employee_id': context.modified_ticket.employee_id,
            'ticket_type': context.modified_ticket.ticket_type,
            'response': context.modified_ticket.response,
            'status': context.modified_ticket.status,
            'opening_date': context.modified_ticket.opening_date,
            'closing_date': context.modified_ticket.closing_date,
            'playback_steps': context.modified_ticket.playback_steps,
            'severity_id': context.modified_ticket.severity_id,
        }
    ) 

    context.error_ticket = context.original_ticket


# --- Then

@then("se modifica el ticket")
def check_ticket_is_modified_successfully(context):
    requested_ticket = ticket_service.get_ticket(
        context.modified_ticket.product_id,
        context.original_ticket.version_code,
        context.original_ticket.id
    )
    modified_ticket = context.modified_ticket

    assert_tickets(requested_ticket, modified_ticket)

@then("se informa que se hizo correctamente")
def check_ticket_is_modified_successfully(context):
    response = context.response.json()
    assert response['message'] == MESSAGE_TICKET_MODIFIED


@then("se informa que el ticket no existe")
def check_ticket_not_exist(context):
    assert_exception_message(
        Ticket_not_found_exception(
            context.error_ticket.product_id,
            context.error_ticket.version_code,
            context.error_ticket.id
        ),
        context.response
    )
