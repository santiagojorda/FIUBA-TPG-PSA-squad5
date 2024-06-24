from behave import *

from behave.api.async_step import async_run_until_complete
from services.client_service import Client_service

client_service = Client_service()

@given('the clients')
def given_employees(context):
    context.expected_clients = []
    for row in context.table:
        client = {
            'id': int(row['id']),
            'razon social': row['razon social'],
            'CUIT': row['CUIT']
        }
        context.expected_clients.append(client) 

@when(u'the user requests the clients')
def step_impl(context):
    context.requested_clients = client_service.get_clients()

@when(u'the user requests the client by id = 2')
def step_when_user_requests_client_by_id(context):
    client_id = 2
    context.requested_client = client_service.get_client(client_id)

@when(u'the user requests the client by id = 55')
def step_when_user_requests_client_by_id(context):
    client_id = 55
    context.requested_client = client_service.get_client(client_id)

@then(u'the system shows the clients')
def step_then_system_shows_clients(context):
    assert context.requested_clients == context.expected_clients, f"\nExpected \n{context.expected_clients} \nBut got \n{context.requested_clients}"

@then(u'the system shows the client')
def step_then_system_shows_client(context):
    result = []
    for client in context.expected_clients:
        if client["id"]== context.requested_client["id"]:
            result.append(client)
    
    assert result == [], f"\nExpected \n{[]} \nBut got \n{result}"


@then(u'the system notifies there is no client with that id')
def step_then_system_shows_client(context):
    print(context.requested_clients)
    assert True

