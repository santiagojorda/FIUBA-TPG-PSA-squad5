import requests

from res.errors import Invalid_data_exception

class Client_service():

    ENDPOINT_CLIENTS = 'https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/754f50e8-20d8-4223-bbdc-56d50131d0ae/clientes-psa/1.0.0/m/api/clientes'

    def get_clients(self):
        url_clientes = self.ENDPOINT_CLIENTS

        response = requests.get(url_clientes)
        if response.status_code != 200:
            print(f"Error en la petición: {response.status_code}")

        data_clients = response.json()
        
        return data_clients 

    def get_client(self, client_id: int):
        url_clientes = self.ENDPOINT_CLIENTS

        data = ''
        response = requests.get(url_clientes)
        if response.status_code != 200:
            raise Invalid_data_exception(f"There is no client with id {client_id}")

        data = response.json()
        client = next(item for item in data if item['id'] == client_id)
        return client 