class Invalid_title_exception(Exception):
    def __init__(self, title):
        self.message = f"Invalid title {title}"
        super().__init__(self.message)