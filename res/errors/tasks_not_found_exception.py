class Tasks_not_found_exception(Exception):
    def __init__(self, product_id, version_code, ticket_id):
        self.message = f"No taks assoiated to ticket {ticket_id} in version {version_code} of product {product_id}"
        super().__init__(self.message)