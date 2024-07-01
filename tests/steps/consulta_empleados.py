
from behave import *

from res.errors import Employee_not_found_exception
from utils.utils import assert_exception_message 

from services.employee_service import Employee_service

employee_service = Employee_service()

@then("se informa que el empleado no existe")
def check_client_not_exists(context):
    employee_id = context.requested_employee_id
    assert_exception_message(
        Employee_not_found_exception(employee_id),
        context.response
    )