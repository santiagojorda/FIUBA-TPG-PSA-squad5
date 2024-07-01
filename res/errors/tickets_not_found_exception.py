
class Tickets_not_found_exception(Exception):
    def __init__(self, product_id, version_code):
        self.message = f"There is no tickets in version {version_code} of the product {product_id}"
        super().__init__(self.message)