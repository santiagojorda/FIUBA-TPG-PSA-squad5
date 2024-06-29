from behave import *

from services.product_version_service import Version_service
from res.database import db 
from routes.product_version_routes import PATH as ENDPOINT_PRODUCT
from res.errors import Products_not_found_exception
from utils import assert_exception_message

version_service = Version_service()

# --- Escenario 1

@given("que existen productos")
def created_products(context):
    context.product_title1 = "product1" 
    context.product_title2 = "product2" 
    db.create_product(context.product_title1)
    db.create_product(context.product_title2)

@when("se consulta por productos")
def send_get_products(context):
    context.response = context.client.get(ENDPOINT_PRODUCT)

@then("se obtienen listado con los datos productos")
def check_products_exists(context):
    products = context.response.json()

    expected_title1 = context.product_title1
    expected_title2 = context.product_title2

    assert products[0]["title"] == expected_title1
    assert products[1]["title"] == expected_title2

# --- Escenario 2

@given("que no existen productos")
def no_create_products(context):
    pass

@then("el sistema informa que no hay productos")
def check_products_no_exists(context):
    response = context.response
    assert response.status_code == 500

    assert_exception_message(
        Products_not_found_exception(),
        context.response
    )
