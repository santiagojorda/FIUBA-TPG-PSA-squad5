from behave import *

from services.tickets_service import Ticket_service
from routes.tickets_routes import PATH as ENDPOINT_TICKETS
from res.errors import Product_not_exist_exception, Invalid_data_exception, Version_code_not_exist_exception
from tests.utils.utils import assert_exception_message
from models.ticket import * 
from routes.tickets_routes import * 
from tests.utils.ticket_mock import *
from tests.utils.client_mock import *
from tests.utils.product_version_mock import *
from tests.environment import init_incident_enviroment, init_query_enviroment

# ticket_service = Ticket_service()

#-- Escenario 1

@given("se ingreso un id de un ticket existente")
def create_valid_query_ticket(context):
    init_query_enviroment(context)

@when("se elimina un ticket")
def eliminar_ticket(context):
    context.response = context.client.delete(f"{ENDPOINT_TICKETS}/{context.original_ticket.product_id}/{context.original_ticket.version_code}/{context.original_ticket.id}")

@then('se elimina el ticket y le informa al usuario que se hizo correctamente')
def step_impl(context):
    response = context.response.json()
    assert response['message'] == MESSAGE_TICKET_DELETED  # Verificar el mensaje de confirmación


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
        assert response['message'] == "Ticket deleted successfully"  # Verificar el mensaje de confirmación
    elif response.status_code == 404:
        ticket_id = context.ticket_id  # Asegúrate de tener el ticket_id en el contexto
        response = response.json()
        assert response['detail'] == f"Ticket with id {ticket_id} not found"  # Verificar el mensaje de error
