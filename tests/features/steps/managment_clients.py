from behave import *
from services.client_service import Client_service

client_service = Client_service()

@given('the clients')
def given_clients(context):
    context.expected_clients = []
    for row in context.table:
        client = {
            'id': int(row['id']),
            'razon social': row['razon social'],
            'CUIT': row['CUIT']
        }
        context.expected_clients.append(client)

@when(u'the user requests the clients')
def step_user_requests_clients(context):
    context.requested_clients = client_service.get_clients()

@when(u'the user requests the client by id = 2')
def step_user_requests_client_by_id_2(context):
    client_id = 2
    context.requested_client = client_service.get_client(client_id)

@when(u'the user requests the client by id = 55')
def step_user_requests_client_by_id_55(context):
    client_id = 55
    context.requested_client = client_service.get_client(client_id)

@then(u'the system shows the clients')
def step_system_shows_clients(context):
    assert context.requested_clients == context.expected_clients, f"\nExpected \n{context.expected_clients} \nBut got \n{context.requested_clients}"

@then(u'the system shows the client')
def step_system_shows_client(context):
    expected_client = None
    for client in context.expected_clients:
        if client["id"] == context.requested_client["id"]:
            expected_client = client
            break
    
    assert expected_client is not None, f"Expected client with ID {context.requested_client['id']} not found in expected clients."

@then(u'the system notifies there is no client with that id')
def step_system_notifies_no_client(context):
    assert context.requested_client is None, f"Expected no client with ID 55, but found client: {context.requested_client}"
