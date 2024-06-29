from behave import *

from services.tickets_service import Ticket_service
from routes.tickets_routes import PATH as ENDPOINT_TICKETS
from res.errors import Product_not_exist_exception, Invalid_data_exception, Version_code_not_exist_exception
from tests.features.utils.utils import assert_exception_message
from models.ticket import * 
from routes.tickets_routes import * 
from tests.features.utils.ticket_mock import *
from tests.features.utils.client_mock import *
from tests.features.utils.product_version_mock import *
from res.database import db

ticket_service = Ticket_service()

def create_query_ticket(product_id, version_code):
    return Ticket(
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

# --- Escenario 1

@given("se ingresaron datos de ticket consulta validos")
def create_valid_query_ticket(context):
    existing_product_id, existing_version_code = create_version_and_product_1() 
    context.expected_ticket = create_query_ticket(existing_product_id, existing_version_code)


@when("se crea un ticket")
def create_ticket(context):
    opening_date = context.expected_ticket.opening_date
    closing_date = context.expected_ticket.closing_date
    if opening_date:
        opening_date = str(opening_date)
    
    if closing_date:
        closing_date = str(closing_date)

    context.response = context.client.post(ENDPOINT_TICKETS,
        json = {
            "product_id": context.expected_ticket.product_id,
            "version_code": context.expected_ticket.version_code,
            "title": context.expected_ticket.title,
            'description': context.expected_ticket.description,
            'client_id': context.expected_ticket.client_id,
            'employee_id': context.expected_ticket.employee_id,
            'ticket_type': context.expected_ticket.ticket_type,
            'response': context.expected_ticket.response,
            'opening_date': opening_date,
            'closing_date': closing_date,
        }
    )

@then("se crea el ticket y le informa al usuario que se hizo correctamente")
def check_ticket_is_create_succesfully(context):
    response = context.response.json()
    print(response)
    assert response['message'] == MESSAGE_TICKET_CREATED


# --- Escenario 2

@given("se ingresa un id de producto que no existe")
def create_query_but_product_not_exist(context):
    existing_product_id, existing_version_code = create_version_and_product_1()
    context.expected_ticket = create_query_ticket(MOCK_PRODUCT_ID_2, existing_version_code)

@then("se informa que el producto asociado no existe")
def check_product_id_not_exist(context):
    
    assert_exception_message(
        Product_not_exist_exception(context.expected_ticket.product_id),
        context.response
    )


# --- Escenario 3

@given("se ingresa un codigo de version que no esta asociado al id producto")
def create_query_but_product_not_exist(context):
    existing_product_id, existing_version_code = create_version_and_product_1() 
    context.expected_ticket = create_query_ticket(existing_product_id, MOCK_RELEASE_NOTE_2)

@then("se informa que el codigo de version no esta asociado al producto")
def check_product_id_not_exist(context):
    
    assert_exception_message(
        Version_code_not_exist_exception(
            context.expected_ticket.product_id,
            context.expected_ticket.version_code
        ),
        context.response
    )

# --- Escenario 4

@given("no se ingresa titulo")
def create_query_without_title(context):
    existing_product_id, existing_version_code = create_version_and_product_1() 
    context.expected_ticket = create_query_ticket(existing_product_id, existing_version_code)
    context.expected_ticket.title = None

@then("se informa que hay datos invalidos")
def check_title_is_invalid(context):
    
    assert_exception_message(
        Invalid_data_exception(),
        context.response
    )

# --- Escenario 5

@given("no se ingresa descripcion")
def create_query_without_description(context):
    existing_product_id, existing_version_code = create_version_and_product_1() 
    context.expected_ticket = create_query_ticket(existing_product_id, existing_version_code)
    context.expected_ticket.description = None

# --- Escenario 6

@given("no se ingresa tipo de ticket")
def create_query_without_ticket_type(context):
    existing_product_id, existing_version_code = create_version_and_product_1() 
    context.expected_ticket = create_query_ticket(existing_product_id, existing_version_code)
    context.expected_ticket.ticket_type = None

# --- Escenario 7

@given("no se ingresa fecha de apertura")
def create_query_without_opening_date(context):
    existing_product_id, existing_version_code = create_version_and_product_1() 
    context.expected_ticket = create_query_ticket(existing_product_id, existing_version_code)
    context.expected_ticket.opening_date = None

# --- Escenario 8

@given("se ingresa fecha de cierre es anterior a la de apertura")
def create_query_closing_time_earlier_than_existing(context):
    existing_product_id, existing_version_code = create_version_and_product_1() 
    context.expected_ticket = create_query_ticket(existing_product_id, existing_version_code)
    context.expected_ticket.opening_date = MOCK_OPENING_DATE
    context.expected_ticket.closing_date = MOCK_CLOSING_DATE_EARLIER_THAN_OPENING

# --- Escenario 9

@given("se ingresa un cliente que no existe")
def create_query_client_not_exist(context):
    existing_product_id, existing_version_code = create_version_and_product_1() 
    context.expected_ticket = create_query_ticket(existing_product_id, existing_version_code)
    context.expected_ticket.client_id = MOCK_CLIENT_ID_NOT_EXIST
    context.requested_client_id = context.expected_ticket.client_id # para el given de clientes
