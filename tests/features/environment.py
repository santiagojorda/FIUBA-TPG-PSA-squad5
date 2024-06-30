from fastapi.testclient import TestClient
from res.database import db
from main import app
from services.tickets_service import Ticket_service
from utils.ticket_mock import create_query_ticket, create_incident_ticket
from utils.product_version_mock import create_version_and_product_1
from res.init_data.severities import init_data_severities
from services.severity_service import Severity_service

severity_service = Severity_service()
ticket_service = Ticket_service() 

def before_all(context):
    context.client = TestClient(app)

def before_scenario(context, scenario):
    db.create_all()

def after_scenario(context, scenario):
    db.drop_all()

def init_query_enviroment(context):
    existing_product_id, existing_version_code = create_version_and_product_1()
    context.original_ticket = create_query_ticket(existing_product_id, existing_version_code)
    context.original_ticket.id = ticket_service.create_ticket(context.original_ticket)

def init_incident_enviroment(context):
    init_severity_enviroment(context)
    existing_product_id, existing_version_code = create_version_and_product_1()
    context.original_ticket = create_incident_ticket(existing_product_id, existing_version_code)
    context.original_ticket.id = ticket_service.create_ticket(context.original_ticket)

def init_severity_enviroment(context):
    for response_time in init_data_severities:
        print(response_time)
        severity_service.create_severity(response_time)

    