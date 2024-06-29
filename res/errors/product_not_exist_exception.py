class Product_not_exist_exception(Exception):
    def __init__(self, product_id: int):
        self.message = f"Product {product_id} not exist"
        super().__init__(self.message)