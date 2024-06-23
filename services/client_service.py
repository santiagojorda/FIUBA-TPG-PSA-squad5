import requests

class Client_service():

    def get_clients(self):
        url_clientes = 'https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/754f50e8-20d8-4223-bbdc-56d50131d0ae/clientes-psa/1.0.0/m/api/clientes'

        data = ''
        response = requests.get(url_clientes)
        if response.status_code != 200:
            print(f"Error en la petición: {response.status_code}")

        data_clients = response.json()
        
        return data_clients 

    def get_client(self, client_id: int):
        url_clientes = 'https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/754f50e8-20d8-4223-bbdc-56d50131d0ae/clientes-psa/1.0.0/m/api/clientes'

        data = ''
        response = requests.get(url_clientes)
        if response.status_code != 200:
            print(f"Error en la petición: {response.status_code}")

        data = response.json()
        client = next(item for item in data if item['id'] == client_id)
        return client 