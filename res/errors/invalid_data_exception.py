class Invalid_data_exception(Exception):

    def __init__(self):
        self.message = f"There is invalid data"
        super().__init__(self.message)