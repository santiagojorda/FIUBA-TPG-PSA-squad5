from behave import *

from services.tickets_service import Ticket_service
from routes.tickets_routes import PATH as ENDPOINT_TICKETS
from res.errors import Tickets_not_found_exception, Invalid_severity_exception, \
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


# --- Given

@given("existen varios tickets incidente")
def create_valid_query_ticket(context):
    context.original_ticket_1 = create_incident_ticket(
        context.product_id, 
        context.version_code
    )
    context.original_ticket_1.id = ticket_service.create_ticket(context.original_ticket_1)

    context.original_ticket_2 = create_incident_ticket(
        context.product_id, 
        context.version_code
    )
    context.original_ticket_2.id = ticket_service.create_ticket(context.original_ticket_2)

    context.original_ticket_3 = create_incident_ticket(
        context.product_id, 
        context.version_code
    )
    context.original_ticket_3.id = ticket_service.create_ticket(context.original_ticket_3)

@given("existen varios tickets consulta")
def create_valid_query_ticket(context):
    context.original_ticket_1 = create_query_ticket(
        context.product_id, 
        context.version_code
    )
    context.original_ticket_1.id = ticket_service.create_ticket(context.original_ticket_1)

    context.original_ticket_2 = create_query_ticket(
        context.product_id, 
        context.version_code
    )
    context.original_ticket_2.id = ticket_service.create_ticket(context.original_ticket_2)

    context.original_ticket_3 = create_query_ticket(
        context.product_id, 
        context.version_code
    )
    context.original_ticket_3.id = ticket_service.create_ticket(context.original_ticket_3)


@given("ingresan id producto no existente")
def create_valid_query_ticket(context):
    context.product_id = MOCK_PRODUCT_ID_2
    context.version_code = MOCK_VERSION_CODE_2

@given("no existen tickets incidentes asociados")
def create_valid_query_ticket(context):
    pass

@given("no existen tickets consulta asociados")
def create_valid_query_ticket(context):
    pass

@given("ingresa id producto no existente y un codigo de version")
def create_valid_query_ticket(context):
    context.product_id = MOCK_PRODUCT_ID_2
    context.version_code = MOCK_VERSION_CODE_2

# --- When

@when("se consulta por tickets")
def get_versiones_of_product(context):
    context.expected_product_id = context.product_id
    context.expected_version_code = context.version_code
    context.response = context.client.get(f"{ENDPOINT_TICKETS}/{context.expected_product_id}/{context.expected_version_code}")


# --- Then

@then("se obtiene listado de todos los tickets asociados a ese producto y esa version")
def check_ticket_is_modified_successfully(context):
    response = context.response.json()
    print(response)

    assert_ticket_response(response[0], context.original_ticket_1)
    assert_ticket_response(response[1], context.original_ticket_2)
    assert_ticket_response(response[2], context.original_ticket_3)

@then("se informa que no tiene tickets asociados")
def check_products_no_exists(context):
    assert_exception_message(
        Tickets_not_found_exception(
            context.expected_product_id, 
            context.expected_version_code
        ),
        context.response
    )
