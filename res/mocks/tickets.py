from models.ticket import * 
from datetime import date

# Mock data para tickets
mock_tickets = [
    {
        'title': "Email Application Crashing",
        'description': "Email Application crash when attempting to access",
        'client_id': 1,
        'version_code': '1.1.0',
        'ticket_type': INCIDENT_TICKET,
        'status': STATUS_NEW_TICKET,
        'employee_id': 1,
        'product_id': 1,
        'playback_steps': """Open the email application by clicking on the application icon on the desktop or from the start menu.\nObserve that the application begins to load but crashes within a few seconds.""",
        'severity_id': 2,
        'response': None,
        'closing_date': None,
    },
    {
        'title': "Profile Image",
        'description': "Im wondering to change image of my profile",
        'client_id': 1,
        'version_code': '1.1.0',
        'ticket_type': QUERY_TICKET,
        'status': STATUS_CLOSED,
        'employee_id': 1,
        'closing_date': date.today(),
        'product_id': 1,
        'playback_steps': None,
        'severity_id': None,
        'response': """Once logged in, locate your profile icon or name, usually found at the top right corner of the page.\nClick on your profile icon or name to open a dropdown menu.\nSelect "Settings" or "Profile" from the dropdown menu."""
    },
    {
        'title': "Request for Professor's Email Address",
        'description': "Im wondering to get the email of professor to send a message",
        'client_id': 1,
        'version_code': '2.2.0',
        'ticket_type': QUERY_TICKET,
        'status': STATUS_NEW_TICKET,
        'employee_id': 1,
        'product_id': 2,
        'closing_date': None,
        'playback_steps': None,
        'severity_id': None,
        'response': """Navigate to the "Faculty" or "Staff Directory" section.\nUse the search function to find the professor by name or department.\nThe directory listing usually includes contact details such as email addresses."""
    }
]
