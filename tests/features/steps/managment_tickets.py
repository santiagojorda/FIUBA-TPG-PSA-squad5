from datetime import datetime

# Función para convertir cadena a fecha
def str_to_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError as e:
        raise ValueError(f'Formato de fecha incorrecto para {date_str}. Debe ser YYYY-MM-DD.') from e

# Resto del código de pasos
from behave import given, when, then
from services.tickets_service import Ticket_service
from models.ticket import TicketModel, INCIDENT_TICKET, QUERY_TICKET

ticket_service = Ticket_service()

@given('que tengo un producto con id "{product_id}" y versión "{version_code}"')
def given_producto_y_version(context, product_id, version_code):
    context.product_id = int(product_id)
    context.version_code = version_code

@given('los detalles del nuevo ticket')
def given_nuevo_ticket(context):
    for row in context.table:
        context.new_ticket = TicketModel(
            product_id=context.product_id,
            version_code=context.version_code,
            title=row['title'],
            description=row['description'],
            status=int(row['status']),
            opening_date=str_to_date(row['opening_date']),
            client_id=int(row['client_id']),
            employee_id=None if row['employee_id'] == 'None' else int(row['employee_id']),
            ticket_type=QUERY_TICKET if row['ticket_type'] == 'QUERY_TICKET' else INCIDENT_TICKET
        )

@when('creo un nuevo ticket')
def when_creo_nuevo_ticket(context):
    context.creation_response = ticket_service.create_ticket(context.new_ticket)

@then('el sistema crea el ticket exitosamente')
def then_ticket_creado_exitosamente(context):
    assert context.creation_response, "El ticket no fue creado exitosamente"


@when('creo un nuevo ticket con campos opcionales')
def when_creo_nuevo_ticket_opcional(context):
    for row in context.table:
        context.new_ticket.severity_id = int(row['severity_id'])
        context.new_ticket.playback_steps = row['playback_steps']

    context.creation_response = ticket_service.create_ticket(context.new_ticket)

@then('el sistema crea el ticket con campos opcionales exitosamente')
def then_ticket_creado_con_campos_opcionales(context):
    assert context.creation_response, "El ticket con campos opcionales no fue creado exitosamente"
    assert context.new_ticket.severity_id == int(context.table.rows[0]['severity_id']), \
        f"El severity_id del ticket creado ({context.new_ticket.severity_id}) no coincide con el esperado ({int(context.table.rows[0]['severity_id'])})"
    assert context.new_ticket.playback_steps == context.table.rows[0]['playback_steps'], \
        f"Los pasos de reproducción del ticket creado ({context.new_ticket.playback_steps}) no coinciden con los esperados ({context.table.rows[0]['playback_steps']})"

@when('intento crear un nuevo ticket con campos obligatorios faltantes')
def when_intento_crear_ticket_incompleto(context):
    # Define un ticket con campos obligatorios faltantes
    context.incomplete_ticket = TicketModel(
        product_id=context.product_id,
        version_code=context.version_code,
        title=None,  # Campo obligatorio faltante
        description="Descripción del ticket incompleto",
        status=0,
        opening_date=str_to_date("2024-06-28"),
        client_id=1,
        ticket_type=QUERY_TICKET
    )
    # Intenta crear el ticket incompleto
    try:
        context.creation_response = ticket_service.create_ticket(context.incomplete_ticket)
    except Exception as e:
        context.error_message = str(e)

@then('el sistema no crea el ticket y muestra un mensaje de error adecuado')
def then_ticket_no_creado_con_campos_faltantes(context):
    assert not context.creation_response, "Se creó un ticket con campos faltantes"
    assert context.error_message, "No se mostró un mensaje de error adecuado"


# # managment_tickets.py

# from behave import given, when, then
# from datetime import date
# from models.ticket import TicketModel
# from services.tickets_service import Ticket_service

# ticket_service = Ticket_service()

# @given('que tengo un producto con id "{product_id}" y versión "{version_code}"')
# def set_product_and_version(context, product_id, version_code):
#     context.product_id = int(product_id)
#     context.version_code = version_code

# @when('creo un nuevo ticket con los siguientes detalles:')
# def create_new_ticket(context):
#     details = context.table[0]
#     ticket_data = TicketModel(
#         product_id=context.product_id,
#         version_code=context.version_code,
#         title=details['title'],
#         description=details['description'],
#         status=int(details['status']),
#         opening_date=date.fromisoformat(details['opening_date']),
#         client_id=int(details['client_id']),
#         employee_id=int(details['employee_id']) if details['employee_id'] else None,
#         ticket_type=int(details['ticket_type'])
#     )
#     context.created_ticket_id = ticket_service.create_ticket(ticket_data)

# @then('el sistema crea el ticket exitosamente')
# def verify_ticket_created_successfully(context):
#     assert context.created_ticket_id is not None, "Failed to create ticket"

# @when('modifico el ticket con los siguientes detalles:')
# def modify_ticket(context):
#     details = context.table[0]
#     ticket_data = TicketModel(
#         id=int(details['ticket_id']),  # Suponiendo que 'ticket_id' es proporcionado en la tabla
#         product_id=context.product_id,
#         version_code=context.version_code,
#         title=details['title'],
#         description=details['description'],
#         status=int(details['status']),
#         opening_date=date.fromisoformat(details['opening_date']),
#         client_id=int(details['client_id']),
#         employee_id=int(details['employee_id']) if details['employee_id'] else None,
#         ticket_type=int(details['ticket_type'])
#     )
#     ticket_service.update_ticket(ticket_data)

# @then('el ticket se modifica exitosamente')
# def verify_ticket_modified_successfully(context):
#     ticket = ticket_service.get_ticket_by_id(context.created_ticket_id)
#     assert ticket is not None, "Failed to retrieve modified ticket"
#     # Asegurar que los campos modificados coincidan con los esperados

# @when('elimino el ticket')
# def delete_ticket(context):
#     ticket_service.delete_ticket(context.created_ticket_id)

# @then('el ticket se elimina correctamente')
# def verify_ticket_deleted_successfully(context):
#     ticket = ticket_service.get_ticket_by_id(context.created_ticket_id)
#     assert ticket is None, "Ticket should have been deleted"

# @when('busco el ticket por id')
# def find_ticket_by_id(context):
#     context.found_ticket = ticket_service.get_ticket_b
