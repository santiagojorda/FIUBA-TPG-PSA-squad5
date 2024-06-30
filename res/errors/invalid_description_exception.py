class Invalid_description_exception(Exception):
    def __init__(self, description):
        self.message = f"Invalid description {description}"
        super().__init__(self.message)