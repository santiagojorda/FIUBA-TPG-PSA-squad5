import requests

from res.errors import No_result_exception, Data_not_exist_exception, External_microservice_exception, Client_not_found_exception

ENDPOINT_CLIENTS = 'https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/754f50e8-20d8-4223-bbdc-56d50131d0ae/clientes-psa/1.0.0/m/api/clientes'

ERROR_CLIENT_SERVER_MESSAGE = "We cannot connect to client-server"

class Client_service():

    def get_clients(self):
        response = requests.get(ENDPOINT_CLIENTS)
        if response.status_code != 200:
            raise External_microservice_exception(ERROR_CLIENT_SERVER_MESSAGE)

        return response.json()

    def get_client(self, client_id: int):
        response = requests.get(ENDPOINT_CLIENTS)
        if response.status_code != 200:
            raise External_microservice_exception(ERROR_CLIENT_SERVER_MESSAGE)

        data = response.json()

        try: 
            client = next(item for item in data if item['id'] == client_id)
            if client['id'] != client_id:
                raise
            return client
        except: 
            raise Client_not_found_exception(client_id)
        

    def validate_client(self, client_id: int):
        client_exist = self.get_client(client_id)
        if not client_exist:
            raise Client_not_found_exception(client_id)
