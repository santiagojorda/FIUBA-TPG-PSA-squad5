from behave import *

from services.product_version_service import Version_service
from res.database import db 
from routes.product_version_routes import PATH as ENDPOINT_PRODUCT
from res.errors import Versions_product_not_found_exception, Product_not_exist_exception
from tests.features.utils.product_version_mock import MOCK_PRODUCT_TITLE_1, MOCK_VERSION_CODE_1, MOCK_VERSION_CODE_2, MOCK_RELEASE_NOTE_1, MOCK_RELEASE_NOTE_2
from tests.features.utils.utils import assert_exception_message

version_service = Version_service()

# --- Escenario 1

@given("que existe un producto y tiene asociado versiones")
def create_product_and_versions(context):
    context.product_title1 = MOCK_PRODUCT_TITLE_1
    context.expected_product_id = db.create_product(context.product_title1)

    db.create_version(
        context.expected_product_id,
        MOCK_VERSION_CODE_1,
        MOCK_RELEASE_NOTE_1
    )

    db.create_version(
        context.expected_product_id,
        MOCK_VERSION_CODE_2,
        MOCK_RELEASE_NOTE_2
    )


@when("se consulta las versiones del producto")
def get_versiones_of_product(context):
    context.response = context.client.get(
        f"{ENDPOINT_PRODUCT}/{context.expected_product_id}/versions"
    )

@then("se obtienen listado con los datos versiones del producto")
def check_versiones_exists(context):
    versions = context.response.json()

    assert versions[0]["product_id"] == context.expected_product_id
    assert versions[0]["version_code"] == MOCK_VERSION_CODE_1
    assert versions[0]["release_notes"] == MOCK_RELEASE_NOTE_1

    assert versions[1]["product_id"] == context.expected_product_id
    assert versions[1]["version_code"] == MOCK_VERSION_CODE_2
    assert versions[1]["release_notes"] == MOCK_RELEASE_NOTE_2

# --- Escenario 1

@given("que existe un producto y no tienen asociados versiones")
def create_product_without_version(context):
    context.expected_product_id = db.create_product(MOCK_PRODUCT_TITLE_1)


@then("el sistema informa que el producto no posee versiones")
def check_versiones_not_exists(context):
    product_id = context.expected_product_id
    assert_exception_message(
        Versions_product_not_found_exception(product_id),
        context.response
    )

# --- Escenario 1

@given("que no existe un producto")
def create_nothing(context):
    context.expected_product_id = 0  
    pass

@then("el sistema informa que el producto existe")
def check_versiones_not_exists(context):
    product_id = context.expected_product_id
    assert_exception_message(
        Product_not_exist_exception(product_id),
        context.response
    )
    
