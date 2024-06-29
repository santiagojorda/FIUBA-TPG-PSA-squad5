class Version_code_not_exist_exception(Exception):
    def __init__(self, product_id: int, version_code: str):
        self.message = f"There is no version {version_code} of the product {product_id}"
        super().__init__(self.message)