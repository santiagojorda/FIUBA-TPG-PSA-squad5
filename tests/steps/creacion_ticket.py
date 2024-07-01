from behave import *

from services.tickets_service import Ticket_service
from routes.tickets_routes import PATH as ENDPOINT_TICKETS
from res.errors import Product_not_exist_exception, Invalid_severity_exception, \
    Invalid_playback_steps_exception, Severity_not_found_exception, Invalid_ticket_type_exception, \
    Closing_date_earlier_than_opening_exception ,Invalid_title_exception, \
    Invalid_description_exception, Version_code_not_exist_exception, \
    Invalid_status_exception
from tests.utils.utils import assert_exception_message
from models.ticket import * 
from routes.tickets_routes import * 
from tests.utils.ticket_mock import *
from tests.utils.utils import *
from tests.utils.severity_mock import *
from tests.utils.client_mock import *
from tests.utils.product_version_mock import *
from tests.environment  import init_severity_enviroment

ticket_service = Ticket_service()


# --- GIVEN 

@given("existen severidades")
def create_valid_query_ticket(context):
    init_severity_enviroment()

@given("existe un producto y una version asociado al mismo")
def create_valid_query_ticket(context):
    product_id, version_code = create_version_and_product_1() 
    context.product_id = product_id
    context.version_code = version_code

@given("se ingresan datos de ticket consulta validos")
def create_valid_query_ticket(context):
    context.original_ticket = create_query_ticket(
        context.product_id, 
        context.version_code
    )

@given("se ingresan datos de ticket incidente validos")
def create_valid_query_ticket(context):
    context.original_ticket = create_incident_ticket(
        context.product_id, 
        context.version_code
    )

@given("se ingresa un id de producto que no existe")
def create_query_but_product_not_exist(context):
    context.original_ticket.product_id = MOCK_PRODUCT_ID_2

@given("se ingresa un codigo de version que no esta asociado al id producto")
def create_query_but_product_not_exist(context):
    context.original_ticket.version_code = MOCK_RELEASE_NOTE_2

@given("no se ingresa titulo")
def create_query_without_title(context):
    context.original_ticket.title = None

@given("no se ingresa descripcion")
def create_query_without_description(context):
    context.original_ticket.description = None

@given("no se ingresa tipo de ticket")
def create_query_without_ticket_type(context):
    context.original_ticket.ticket_type = None

@given("la fecha de cierre es anterior a la de apertura")
def create_query_closing_time_earlier_than_existing(context):
    context.original_ticket.opening_date = MOCK_OPENING_DATE
    context.original_ticket.closing_date = MOCK_CLOSING_DATE_EARLIER_THAN_OPENING

@given("se ingresa un cliente que no existe")
def create_query_client_not_exist(context):
    context.original_ticket.client_id = MOCK_CLIENT_ID_NOT_EXIST
    context.requested_client_id = context.original_ticket.client_id

@given("se ingresa un empleado que no existe")
def create_query_employee_not_exist(context):
    context.original_ticket.employee_id = MOCK_EMPLOYEE_ID_NOT_EXIST
    context.requested_employee_id = context.original_ticket.employee_id

@given("no se ingresa severidad")
def create_query_employee_not_exist(context):
    context.original_ticket.severity_id = None

@given("se ingresa severidad no existente")
def create_query_employee_not_exist(context):
    context.original_ticket.severity_id = MOCK_SEVERITY_NOT_EXIST

@given("no se ingresa pasos de reproduccion")
def create_query_employee_not_exist(context):
    context.original_ticket.playback_steps = None

    
@given("no se ingresa estado de ticket")
def create_query_employee_not_exist(context):
    context.original_ticket.status = None

@given("se ingresa estado no valido")
def create_query_employee_not_exist(context):
    context.original_ticket.status = MOCK_STATUS_NOT_EXIST


# --- WHEN

@when("se crea un ticket")
def create_ticket(context):
    opening_date = context.original_ticket.opening_date
    closing_date = context.original_ticket.closing_date
    if opening_date:
        opening_date = str(opening_date)
    
    if closing_date:
        closing_date = str(closing_date)

    context.response = context.client.post(ENDPOINT_TICKETS,
        json = {
            "product_id": context.original_ticket.product_id,
            "version_code": context.original_ticket.version_code,
            "title": context.original_ticket.title,
            'description': context.original_ticket.description,
            'client_id': context.original_ticket.client_id,
            'employee_id': context.original_ticket.employee_id,
            'ticket_type': context.original_ticket.ticket_type,
            'response': context.original_ticket.response,
            'severity_id': context.original_ticket.severity_id,
            'opening_date': opening_date,
            'status': context.original_ticket.status,
            'closing_date': closing_date,
            'playback_steps': context.original_ticket.playback_steps
        }
    )

    context.error_ticket = context.original_ticket

# --- THEN

@then("se crea el ticket")
def check_ticket_is_create_succesfully(context):
    response = context.response.json()
    original_ticket = context.original_ticket
    original_ticket.id = response['ticket_id']

    requested_ticket = ticket_service.get_ticket(
        original_ticket.product_id,
        original_ticket.version_code,
        original_ticket.id
    )
    assert_tickets(requested_ticket, original_ticket)

@then("se informa que se creo correctamente")
def check_ticket_is_create_succesfully(context):
    response = context.response.json()
    assert response['message'] == MESSAGE_TICKET_CREATED

@then("se informa que el producto asociado no existe")
def check_product_id_not_exist(context):
    assert_exception_message(
        Product_not_exist_exception(context.error_ticket.product_id),
        context.response
    )

@then("se informa que el codigo de version no esta asociado al producto")
def check_product_id_not_exist(context):
    assert_exception_message(
        Version_code_not_exist_exception(
            context.error_ticket.product_id,
            context.error_ticket.version_code
        ),
        context.response
    )

@then("se informa que titulo es invalido")
def check_title_is_invalid(context):
    assert_exception_message(
        Invalid_title_exception(context.error_ticket.title),
        context.response
    )

@then("se informa que descripcion es invalida")
def check_description_is_invalid(context):
    assert_exception_message(
        Invalid_description_exception(context.error_ticket.description),
        context.response
    )

@then("se informa que el tipo de ticket es invalido")
def check_ticket_type_invalid(context):
    
    assert_exception_message(
        Invalid_ticket_type_exception(context.error_ticket.ticket_type),
        context.response
    )

@then("se informa que la fecha de cierre es anterior a la de apertura")
def check_closing_date_is_invalid(context):
    assert_exception_message(
        Closing_date_earlier_than_opening_exception(
            context.error_ticket.opening_date,
            context.error_ticket.closing_date
        ),
        context.response
    )

@then("se informa que la severidad es invalida")
def check_severity_is_invalid(context):
    
    assert_exception_message(
        Invalid_severity_exception(context.error_ticket.severity_id),
        context.response
    )

@then("se informa que la severidad no existe")
def check_severity_not_found(context):
    assert_exception_message(
        Severity_not_found_exception(context.error_ticket.severity_id),
        context.response
    )


@then("se informa que los pasos de reproduccion son invalidos")
def check_playback_steps_are_invalid(context):
    assert_exception_message(
        Invalid_playback_steps_exception(context.error_ticket.playback_steps),
        context.response
    )

@then("se informa que el estado de ticket es invalido")
def check_severity_is_invalid(context):
    
    assert_exception_message(
        Invalid_status_exception(context.error_ticket.status),
        context.response
    )


















# @given("se ingresaron datos de ticket incidente validos")
# def create_valid_query_ticket(context):
#     existing_product_id, existing_version_code = create_version_and_product_1() 
#     init_severity_enviroment()
#     context.expected_ticket = create_incident_ticket(existing_product_id, existing_version_code)


# @then("se informa que hay datos invalidos")
# def check_title_is_invalid(context):
#     assert_exception_message(
#         Invalid_data_exception(
#             context.expected_ticket.title
#         ),
#         context.response
#     )

# @given("no se ingresa tipo de ticket")
# def create_query_without_ticket_type(context):
#     existing_product_id, existing_version_code = create_version_and_product_1() 
#     context.expected_ticket = create_query_ticket(existing_product_id, existing_version_code)
#     context.expected_ticket.ticket_type = None

# @given("no se ingresa fecha de apertura")
# def create_query_without_opening_date(context):
#     existing_product_id, existing_version_code = create_version_and_product_1() 
#     context.expected_ticket = create_query_ticket(existing_product_id, existing_version_code)
#     context.expected_ticket.opening_date = None



# @given("se ingresan datos validos de un ticket consulta y un empleado que no existente")
# def create_query_employee_not_exist(context):
#     existing_product_id, existing_version_code = create_version_and_product_1() 
#     context.requested_employee_id = 999999
#     context.expected_ticket = create_query_ticket(
#         existing_product_id,
#         existing_version_code,
#         employee_id = context.requested_employee_id
#     )