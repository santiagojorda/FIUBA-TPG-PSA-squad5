class Client_not_found_exception(Exception):
    def __init__(self, client_id: int):
        self.message = f"Client {client_id} not found"
        super().__init__(self.message)