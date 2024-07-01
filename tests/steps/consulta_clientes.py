from behave import *

from services.client_service import Client_service
from routes.client_routes import PATH as ENDPOINT_CLIENTS
from res.errors import Client_not_found_exception
from tests.utils.utils import assert_exception_message, assert_fields_two_dics, assert_fields_two_arr
from tests.utils.client_mock import initialize_clients

client_service = Client_service()


# --- Given

@given("que existen clientes")
def clients_exists(context):
    context.expected_clients = initialize_clients()

@given("se ingreso un cliente existente")
def clients_exists(context):
    context.requested_client_id = 1
    
@given("se ingreso un cliente no existente")
def client_not_exist(context):
    context.requested_client_id = 9999

# --- When

@when("se consulta por clientes")
def get_clients(context):
    context.response = context.client.get(ENDPOINT_CLIENTS)

@when("se consulta por un cliente")
def get_client(context):
    context.response = context.client.get(f"{ENDPOINT_CLIENTS}/{context.requested_client_id}")


# --- Then

@then("se obtienen listado con los clientes con todos sus datos")
def check_clients_exists(context):
    clients = context.response.json()
    expected_clients = context.expected_clients
    for i in range(0,3):
        assert_fields_two_arr(clients, expected_clients, 'id', i)
        assert_fields_two_arr(clients, expected_clients, 'razon social', i)
        assert_fields_two_arr(clients, expected_clients, 'CUIT', i)


@then("se obtienen los datos del cliente")
def check_client_exists(context):
    clients = context.response.json()
    expected_client = context.expected_clients
    print(type(clients))
    print(type(expected_client))
    assert_fields_two_dics(clients, expected_client[0], 'id')
    assert_fields_two_dics(clients, expected_client[0], 'razon social')
    assert_fields_two_dics(clients, expected_client[0], 'CUIT')



@then("se informa que el cliente no existe")
def check_client_not_exists(context):
    client_id = context.requested_client_id
    assert_exception_message(
        Client_not_found_exception(client_id),
        context.response
    )




# # --- Escenario 2

# @given("que existen clientes y se ingreso un cliente existente")
# def client_exist(context):

#     context.requested_client_id = 1
#     context.expected_clients = initialize_clients()

# @when("se consulta por un cliente")
# def get_client(context):
#     context.response = context.client.get(f"{ENDPOINT_CLIENTS}/{context.requested_client_id}")

# @then("se obtienen los datos del cliente")
# def check_client_exists(context):
#     clients = context.response.json()
#     expected_client = context.expected_clients
#     print(type(clients))
#     print(type(expected_client))
#     assert_fields_two_dics(clients, expected_client[0], 'id')
#     assert_fields_two_dics(clients, expected_client[0], 'razon social')
#     assert_fields_two_dics(clients, expected_client[0], 'CUIT')

# # --- Escenario 3

# @given("que existen clientes y se ingreso un cliente no existente")
# def client_not_exist(context):
#     context.requested_client_id = 9999
#     context.expected_clients = initialize_clients()

# @then("se informa que el cliente no existe")
# def check_client_not_exists(context):
#     client_id = context.requested_client_id
#     assert_exception_message(
#         Client_not_found_exception(client_id),
#         context.response
#     )