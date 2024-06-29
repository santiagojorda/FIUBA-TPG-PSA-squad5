from datetime import date, timedelta

MOCK_TICKET_TITLE = 'esto es un titulo'
MOCK_TICKET_DESCRIPCION = 'esto es una descripcion'
MOCK_TICKET_CLIENT_ID = 1
MOCK_TICKET_EMPLOYEE_ID = 1
MOCK_TICKET_ = 1
MOCK_TICKET_RESPONSE = 'esto es una respuesta'
MOCK_OPENING_DATE = date.today()
MOCK_CLOSING_DATE = MOCK_OPENING_DATE + timedelta(days=1)
MOCK_CLOSING_DATE_EARLIER_THAN_OPENING = date.today() - timedelta(days=5)