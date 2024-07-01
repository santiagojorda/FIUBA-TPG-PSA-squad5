from behave import *

from services.product_version_service import Version_service
from res.database import db 
from routes.product_version_routes import PATH as ENDPOINT_PRODUCT
from res.errors import Versions_product_not_found_exception, Product_not_exist_exception
from tests.utils.product_version_mock import *
from tests.utils.utils import *

# version_service = Version_service()


# # --- Given

@given("existe un producto")
def create_product_and_versions(context):
    context.expected_product_id = create_mock_product_1()

@given("no existe producto")
def create_product_and_versions(context):
    context.expected_product_id = MOCK_PRODUCT_ID_1

@given("existen versiones asociadas al producto")
def create_product_and_versions(context):
    context.expected_version_code_1 = create_mock_version_of_product_1(context.expected_product_id)
    create_mock_version_of_product_2(context.expected_product_id)
    print(context.expected_version_code_1)

# # -- When

@when("se consulta las versiones de un producto")
def get_versiones_of_product(context):
    context.response = context.client.get(f"{ENDPOINT_PRODUCT}/{context.expected_product_id}/versions")

# # --- Then

@then("se obtienen listado con los datos versiones del producto")
def check_versiones_exists(context):
    requested_versions = context.response.json()
    assert requested_versions[0]["product_id"] == context.expected_product_id
    assert requested_versions[0]["version_code"] == MOCK_VERSION_CODE_1
    assert requested_versions[0]["release_notes"] == MOCK_RELEASE_NOTE_1

    assert requested_versions[1]["product_id"] == context.expected_product_id
    assert requested_versions[1]["version_code"] == MOCK_VERSION_CODE_2
    assert requested_versions[1]["release_notes"] == MOCK_RELEASE_NOTE_2


@then("se obtienen los datos de la version del producto")
def check_versiones_exists(context):
    requested_versions = context.response.json()
    print(requested_versions)
    assert requested_versions["product_id"] == context.expected_product_id
    assert requested_versions["version_code"] == MOCK_VERSION_CODE_1
    assert requested_versions["release_notes"] == MOCK_RELEASE_NOTE_1


@then("se informa que el producto no existe")
def check_versiones_exists(context):
    assert_exception_message(
        Product_not_exist_exception(
            context.expected_product_id
        ),
        context.response
    )

















# # @when("se consulta las versiones del producto")
# # def get_versiones_of_product(context):
# #     context.response = context.client.get(
# #         f"{ENDPOINT_PRODUCT}/{context.expected_product_id}/versions"
# #     )

# # @then("se obtienen listado con los datos versiones del producto")
# # def check_versiones_exists(context):
# #     versions = context.response.json()

# #     assert versions[0]["product_id"] == context.expected_product_id
# #     assert versions[0]["version_code"] == MOCK_VERSION_CODE_1
# #     assert versions[0]["release_notes"] == MOCK_RELEASE_NOTE_1

# #     assert versions[1]["product_id"] == context.expected_product_id
# #     assert versions[1]["version_code"] == MOCK_VERSION_CODE_2
# #     assert versions[1]["release_notes"] == MOCK_RELEASE_NOTE_2

# # # --- Escenario 1

# # @given("que existe un producto y no tienen asociados versiones")
# # def create_product_without_version(context):
# #     context.expected_product_id = db.create_product(MOCK_PRODUCT_TITLE_1)


# # @then("el sistema informa que el producto no posee versiones")
# # def check_versiones_not_exists(context):
# #     product_id = context.expected_product_id
# #     assert_exception_message(
# #         Versions_product_not_found_exception(product_id),
# #         context.response
# #     )

# # # --- Escenario 1

# # @given("que no existe un producto")
# # def create_nothing(context):
# #     context.expected_product_id = 0  
# #     pass

# # @then("el sistema informa que el producto existe")
# # def check_versiones_not_exists(context):
# #     product_id = context.expected_product_id
# #     assert_exception_message(
# #         Product_not_exist_exception(product_id),
# #         context.response
# #     )
    
