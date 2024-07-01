
class Ticket_not_found_exception(Exception):
    def __init__(self, product_id, version_code, ticket_id):
        self.message = f"There is no ticket id {ticket_id} in version {version_code} of the product {product_id}"
        super().__init__(self.message)