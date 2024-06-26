# managment_tickets.py

from behave import given, when, then
from datetime import date
from models.ticket import TicketModel
from services.tickets_service import Ticket_service

ticket_service = Ticket_service()

@given('que tengo un producto con id "{product_id}" y versión "{version_code}"')
def set_product_and_version(context, product_id, version_code):
    context.product_id = int(product_id)
    context.version_code = version_code

@when('creo un nuevo ticket con los siguientes detalles:')
def create_new_ticket(context):
    details = context.table[0]
    ticket_data = TicketModel(
        product_id=context.product_id,
        version_code=context.version_code,
        title=details['title'],
        description=details['description'],
        status=int(details['status']),
        opening_date=date.fromisoformat(details['opening_date']),
        client_id=int(details['client_id']),
        employee_id=int(details['employee_id']) if details['employee_id'] else None,
        ticket_type=int(details['ticket_type'])
    )
    context.created_ticket_id = ticket_service.create_ticket(ticket_data)

@then('el sistema crea el ticket exitosamente')
def verify_ticket_created_successfully(context):
    assert context.created_ticket_id is not None, "Failed to create ticket"

@when('modifico el ticket con los siguientes detalles:')
def modify_ticket(context):
    details = context.table[0]
    ticket_data = TicketModel(
        id=int(details['ticket_id']),  # Suponiendo que 'ticket_id' es proporcionado en la tabla
        product_id=context.product_id,
        version_code=context.version_code,
        title=details['title'],
        description=details['description'],
        status=int(details['status']),
        opening_date=date.fromisoformat(details['opening_date']),
        client_id=int(details['client_id']),
        employee_id=int(details['employee_id']) if details['employee_id'] else None,
        ticket_type=int(details['ticket_type'])
    )
    ticket_service.update_ticket(ticket_data)

@then('el ticket se modifica exitosamente')
def verify_ticket_modified_successfully(context):
    ticket = ticket_service.get_ticket_by_id(context.created_ticket_id)
    assert ticket is not None, "Failed to retrieve modified ticket"
    # Asegurar que los campos modificados coincidan con los esperados

@when('elimino el ticket')
def delete_ticket(context):
    ticket_service.delete_ticket(context.created_ticket_id)

@then('el ticket se elimina correctamente')
def verify_ticket_deleted_successfully(context):
    ticket = ticket_service.get_ticket_by_id(context.created_ticket_id)
    assert ticket is None, "Ticket should have been deleted"

@when('busco el ticket por id')
def find_ticket_by_id(context):
    context.found_ticket = ticket_service.get_ticket_b
