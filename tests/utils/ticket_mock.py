from datetime import date, timedelta
from models.ticket import *
from models.severity import *

MOCK_TICKET_TITLE_1 = 'esto es un titulo'
MOCK_TICKET_TITLE_2 = 'esto es otro titulo'
MOCK_TICKET_DESCRIPCION_1 = 'esto es una descripcion'
MOCK_TICKET_DESCRIPCION_2 = 'esto es otra descripcion'
MOCK_TICKET_CLIENT_ID_1 = 1
MOCK_TICKET_CLIENT_ID_2 = 2
MOCK_TICKET_EMPLOYEE_ID_1 = 1
MOCK_TICKET_EMPLOYEE_ID_2 = 2
MOCK_TICKET_ = 1
MOCK_TICKET_RESPONSE_1 = 'esto es una respuesta'
MOCK_TICKET_RESPONSE_2 = 'esto es otra respuesta'
MOCK_OPENING_DATE = date.today()
MOCK_CLOSING_DATE = MOCK_OPENING_DATE + timedelta(days=1)
MOCK_CLOSING_DATE_EARLIER_THAN_OPENING = date.today() - timedelta(days=5)
MOCK_PLAYBACK_STEPS_1 = 'esto es una playback step'
MOCK_PLAYBACK_STEPS_2 = 'esto es otra playback step'
MOCK_SEVERITY_ID_1 = 1
MOCK_SEVERITY_ID_2 = 2
MOCK_DURATION_1 = 1
MOCK_DURATION_2 = 2
MOCK_EMPLOYEE_ID_NOT_EXIST = 999999
MOCK_TICKET_ID_NOT_EXIST = 999999
MOCK_TICKET_TYPE_INVALID = 99999
MOCK_STATUS_NOT_EXIST = 99999

def create_query_ticket(product_id: int, 
                        version_code: int,
                        employee_id = None
                        ):
    return Ticket(
        product_id = product_id,
        version_code = version_code,
        title = MOCK_TICKET_TITLE_1,
        description = MOCK_TICKET_DESCRIPCION_1,
        client_id = MOCK_TICKET_CLIENT_ID_1,
        employee_id = employee_id or MOCK_TICKET_EMPLOYEE_ID_1,
        ticket_type = QUERY_TICKET,
        status = STATUS_NEW_TICKET,
        response = MOCK_TICKET_RESPONSE_1,
        opening_date = MOCK_OPENING_DATE
    )

def create_incident_ticket(
                            product_id: int,
                            version_code: int,
                            employee_id: int = None
                            ):
    
    return Ticket(
        product_id = product_id,
        version_code = version_code,
        title = MOCK_TICKET_TITLE_1,
        description = MOCK_TICKET_DESCRIPCION_1,
        client_id = MOCK_TICKET_CLIENT_ID_1,
        employee_id = employee_id or MOCK_TICKET_EMPLOYEE_ID_1,
        ticket_type = INCIDENT_TICKET,
        status = STATUS_NEW_TICKET,
        opening_date = MOCK_OPENING_DATE,
        severity_id = MOCK_SEVERITY_ID_1,
        playback_steps = MOCK_PLAYBACK_STEPS_1,
        duration = MOCK_DURATION_1
    )
