
class Products_not_found_exception(Exception):
    def __init__(self):
        self.message = "El producto no fue encontrado."
        super().__init__(self.message)