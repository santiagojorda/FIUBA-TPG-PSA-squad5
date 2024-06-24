from datetime import date
from res.database import db

import requests

from models.ticket import TicketModel

class Ticket_service():

    def get_ticket(self, ticket_id: int):
        ticket = db.get_ticket(ticket_id)
        if not ticket:
            return False 
        return ticket

    # VER MANEJO DE ERRORES
    def create_ticket(self, ticket_data: TicketModel):
        ticket_id = db.create_ticket(ticket_data)
        # db.create_incident_ticket(ticket_data, ticket_id)
        return ticket_id

    def get_tickets(self, product_id: int, version_code: str):
        tickets = db.get_tickets(product_id, version_code)
        return tickets
    
    def modify_ticket(self, ticket: TicketModel):
        ticket = db.modify_ticket(ticket)
        return ticket
    
    def delete_ticket(self, ticket_id: TicketModel):
        is_deleted = db.delete_ticket(ticket_id)
        return is_deleted





        
    









    # def get_query_ticket(self, ticket_id: int):
    #     print("GET QUERY")
    #     query = db.get_query_ticket(ticket_id)
    #     ticket = db.get_ticket(ticket_id)
        
    #     ticket.response = query.response
    #     return ticket
    
    # def get_incident_ticket(self, ticket_id: int):
    #     print("GET INCIDENT")

    #     ticket = db.get_ticket(ticket_id)
    #     incident = db.get_incident_ticket(ticket_id)
    #     severity = db.get_severity(incident.severity_id)

    #     # ticket.pop('client_id')
    #     ticket.client = self.get_client(ticket.client_id)
    #     ticket.severity = severity
    #     ticket.playback_steps = incident.playback_steps
    #     ticket.duration = incident.duration
    #     return ticket

    # def get_tickets(self):
    #     return db.get_all_tickets()

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


    # def create_query_ticket(self, ticket_data: QueryModel):

    #     ticket_id = db.create_ticket(ticket_data)
    #     db.create_query_ticket(ticket_data, ticket_id)
    #     return True