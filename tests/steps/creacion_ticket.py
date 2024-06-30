from behave import *

from services.tickets_service import Ticket_service
from routes.tickets_routes import PATH as ENDPOINT_TICKETS
from res.errors import Product_not_exist_exception, Invalid_ticket_type_exception,  Date_invalid_exception, Closing_date_earlier_than_opening_exception ,Invalid_title_exception, Invalid_description_exception, Invalid_data_exception, Version_code_not_exist_exception
from tests.utils.utils import assert_exception_message
from models.ticket import * 
from routes.tickets_routes import * 
from tests.utils.ticket_mock import *
from tests.utils.client_mock import *
from tests.utils.product_version_mock import *
from tests.environment  import init_severity_enviroment

ticket_service = Ticket_service()

@given("se ingresaron datos de ticket consulta validos")
def create_valid_query_ticket(context):
    existing_product_id, existing_version_code = create_version_and_product_1() 
    context.expected_ticket = create_query_ticket(existing_product_id, existing_version_code)

@given("se ingresaron datos de ticket incidente validos")
def create_valid_query_ticket(context):
    existing_product_id, existing_version_code = create_version_and_product_1() 
    init_severity_enviroment()
    context.expected_ticket = create_incident_ticket(existing_product_id, existing_version_code)

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
            'severity_id': context.expected_ticket.severity_id,
            'opening_date': opening_date,
            'closing_date': closing_date,
            'playback_steps': context.expected_ticket.playback_steps
        }
    )

@then("se crea el ticket y le informa al usuario que se hizo correctamente")
def check_ticket_is_create_succesfully(context):
    response = context.response.json()
    print("response")
    print(response)
    assert response['message'] == MESSAGE_TICKET_CREATED


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

@given("no se ingresa titulo")
def create_query_without_title(context):
    existing_product_id, existing_version_code = create_version_and_product_1() 
    context.expected_ticket = create_query_ticket(existing_product_id, existing_version_code)
    context.expected_ticket.title = None

@then("se informa que hay datos invalidos")
def check_title_is_invalid(context):
    assert_exception_message(
        Invalid_data_exception(
            context.expected_ticket.title
        ),
        context.response
    )

@then("se informa que no hay titulo")
def check_title_is_invalid(context):
    assert_exception_message(
        Invalid_title_exception(context.expected_ticket.title),
        context.response
    )


@then("se informa que no hay descripcion")
def check_description_is_invalid(context):
    assert_exception_message(
        Invalid_description_exception(context.expected_ticket.description),
        context.response
    )


@then("se informa que la fecha de cierre es anterior a la de apertura")
def check_closing_date_is_invalid(context):
    
    assert_exception_message(
        Closing_date_earlier_than_opening_exception(
            context.expected_ticket.opening_date,
            context.expected_ticket.closing_date
        ),
        context.response
    )

@then("se informa que el tipo de ticket es invalido")
def check_ticket_type_invalid(context):
    
    assert_exception_message(
        Invalid_ticket_type_exception(context.expected_ticket.ticket_type),
        context.response
    )


@then("se informa la fecha ingresada de apertura es invalida")
def check_date_invalid(context):
    assert_exception_message(
        Date_invalid_exception(context.expected_ticket.opening_date),
        context.response
    )

@given("no se ingresa descripcion")
def create_query_without_description(context):
    existing_product_id, existing_version_code = create_version_and_product_1() 
    context.expected_ticket = create_query_ticket(existing_product_id, existing_version_code)
    context.expected_ticket.description = None

@given("no se ingresa tipo de ticket")
def create_query_without_ticket_type(context):
    existing_product_id, existing_version_code = create_version_and_product_1() 
    context.expected_ticket = create_query_ticket(existing_product_id, existing_version_code)
    context.expected_ticket.ticket_type = None

@given("no se ingresa fecha de apertura")
def create_query_without_opening_date(context):
    existing_product_id, existing_version_code = create_version_and_product_1() 
    context.expected_ticket = create_query_ticket(existing_product_id, existing_version_code)
    context.expected_ticket.opening_date = None

@given("se ingresa fecha de cierre es anterior a la de apertura")
def create_query_closing_time_earlier_than_existing(context):
    existing_product_id, existing_version_code = create_version_and_product_1() 
    context.expected_ticket = create_query_ticket(existing_product_id, existing_version_code)
    context.expected_ticket.opening_date = MOCK_OPENING_DATE
    context.expected_ticket.closing_date = MOCK_CLOSING_DATE_EARLIER_THAN_OPENING

@given("se ingresan datos validos de un ticket consulta con un cliente que no existe")
def create_query_client_not_exist(context):
    existing_product_id, existing_version_code = create_version_and_product_1() 
    context.expected_ticket = create_query_ticket(existing_product_id, existing_version_code)
    context.expected_ticket.client_id = MOCK_CLIENT_ID_NOT_EXIST
    context.requested_client_id = context.expected_ticket.client_id # para el given de clientes

@given("se ingresan datos validos de un ticket consulta con un empleado que no existe")
def create_query_employee_not_exist(context):
    existing_product_id, existing_version_code = create_version_and_product_1() 
    context.requested_employee_id = 999999
    context.expected_ticket = create_query_ticket(
        existing_product_id,
        existing_version_code,
        employee_id = context.requested_employee_id
    )


@given("se ingresan datos validos de un ticket consulta y un empleado que no existente")
def create_query_employee_not_exist(context):
    existing_product_id, existing_version_code = create_version_and_product_1() 
    context.requested_employee_id = 999999
    context.expected_ticket = create_query_ticket(
        existing_product_id,
        existing_version_code,
        employee_id = context.requested_employee_id
    )