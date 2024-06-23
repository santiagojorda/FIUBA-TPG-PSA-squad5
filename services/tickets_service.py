from datetime import date
from res.database import db

import requests

from models.ticket import Ticket
from models.query import Query
from models.incident import Incident

class Ticket_service():

    def get_query_ticket(self, ticket_id: int):
        print("GET QUERY")
        query = db.get_query_ticket(ticket_id)
        ticket = db.get_ticket(ticket_id)
        
        ticket.response = query.response
        return ticket
    
    def get_incident_ticket(self, ticket_id: int):
        print("GET INCIDENT")

        ticket = db.get_ticket(ticket_id)
        incident = db.get_incident_ticket(ticket_id)
        severity = db.get_severity(incident.severity_id)

        # ticket.pop('client_id')
        ticket.client = self.get_client(ticket.client_id)
        ticket.severity = severity
        ticket.playback_steps = incident.playback_steps
        ticket.duration = incident.duration
        return ticket

    def get_tickets(self):
        return db.get_all_tickets()

    def get_client(self, client_id: int):
        url_clientes = 'https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/754f50e8-20d8-4223-bbdc-56d50131d0ae/clientes-psa/1.0.0/m/api/clientes'

        data = ''
        response = requests.get(url_clientes)
        if response.status_code != 200:
            print(f"Error en la petición: {response.status_code}")

        data = response.json()
        client = next(item for item in data if item['id'] == client_id)
        return client 
        # if not client:
        #     return {'text': 'no existe cliente'}

    # def create_ticket(ticket_data):

    #     # MOCK
    #     ticket_data = Ticket(
    #         title = 'se rompio algo',
    #         description = 'esto es una descripcion de todo el problema',
    #         client_id = 1,
    #         employee_id = 4,
    #         product_id = 0,
    #         opening_date = date.today(),
    #         version_code = '2.2.0',
    #         state = 'estado 1',
    #         duration = 24,
    #         playback_steps = 'estos son los pasos a seguir',
    #         severity_id = 2
    #     )

    #     ticket = Ticket(
    #         title = ticket_data.title,
    #         description = ticket_data.description,
    #         client_id = ticket_data.client_id,
    #         employee_id = ticket_data.employee_id,
    #         product_id = ticket_data.product_id,
    #         version_code = ticket_data.version_code,
    #         opening_date = ticket_data.opening_date,
    #     )

    #     ticket_id = db.create_ticket(ticket)

    #     incident = Incident(
    #         ticket_id = ticket_id,
    #         client_id = ticket_data.client_id,
    #         product_id = ticket_data.product_id,
    #         version_code = ticket_data.version_code,
    #         duration = ticket_data.duration,
    #         playback_steps = ticket_data.playback_steps,
    #         severity_id = ticket_data.severity
    #     )

    #     db.create_incident(incident)

        # ticket_data = Ticket(
        #     title = 'se rompio algo',
        #     description = 'esto es una descripcion de todo el problema',
        #     client_id = 1,
        #     employee_id = 4,
        #     id_product = 0,
        #     version_code = '2.2.0'
        # )
        # url_clientes = 'https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/754f50e8-20d8-4223-bbdc-56d50131d0ae/clientes-psa/1.0.0/m/api/clientes'

        # data = ''
        # response = requests.get(url_clientes)
        # if response.status_code != 200:
        #     print(f"Error en la petición: {response.status_code}")

        # data = response.json()
        # client_exists = any(item['id'] == ticket_data['client_id'] for item in data)

        # if not client_exists:
        #     return {'text': 'no existe cliente'}
        
        # ticket = Ticket(ticket_data)
        # db.add(db_cliente)
        # db.commit()
        # db.refresh(db_cliente)
        # return db_cliente

    def create_incident_ticket(ticket_data):

        ticket_id = db.create_ticket(ticket_data)

        ticket_data.id = ticket_id
        db.create_incident_ticket(ticket_data)

