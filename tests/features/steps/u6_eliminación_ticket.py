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

# ticket_service = Ticket_service()

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
#-- Escenario 1

@given("se ingreso un id de un ticket valido")
def create_valid_query_ticket(context):

    existing_product_id, existing_version_code = create_version_and_product_1() 
    context.expected_ticket = create_query_ticket(existing_product_id, existing_version_code)
    context.original_ticket_id = context.expected_ticket.id  # Guardar el ID del ticket original para futuras referencias
    ticket_service.create_ticket(context.expected_ticket)

@when("se Elimina un ticket")
def eliminar_ticket(context):
    
    context.response = context.client.delete(f"{context.expected_ticket}/{context.expected_ticket.product_id}/{context.expected_ticket.version_code}/{context.expected_ticket.id}")


# @then('se Elimina el ticket y le informa al usuario que se hizo correctamente')
# def step_impl(context):
#     response = context.response
#     assert response.json()['message'] == MESSAGE_TICKET_DELETED  # Verificar el mensaje de confirmación

@given("se ingresa un id producto existente, un código de versión existente y que esta asociado al producto ingresado y un id de ticket que no esta asociado a los mismos.")
def create_valid_query_ticket(context):
    existing_product_id, existing_version_code = create_version_and_product_1() 
    context.expected_ticket = create_query_ticket(existing_product_id, existing_version_code)
    ticket_service.create_ticket(context.expected_ticket)

@when("se Elimina un ticket no asociado al producto y version")
def eliminar_ticket(context):
    context.response = context.client.delete(f"{ENDPOINT_TICKETS}/{context.expected_ticket.product_id}/{context.expected_ticket.version_code}/{2}")

@then('se Elimina el ticket y le  informa que el ticket no existe')
def step_impl(context):
    response = context.response
    if response.status_code == 200:
        assert response.json()['message'] == "Ticket deleted successfully"  # Verificar el mensaje de confirmación
    elif response.status_code == 404:
        ticket_id = context.ticket_id  # Asegúrate de tener el ticket_id en el contexto
        assert response.json()['detail'] == f"Ticket with id {ticket_id} not found"  # Verificar el mensaje de error
