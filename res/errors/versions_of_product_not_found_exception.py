class Versions_product_not_found_exception(Exception):
    def __init__(self, product_id: int):
        self.message = f"Versions of product {product_id} not found"
        super().__init__(self.message)