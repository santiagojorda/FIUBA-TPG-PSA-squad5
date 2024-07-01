from behave import *

from services.task_service import Task_service
from routes.task_routes import PATH as ENDPOINT_TASKS
from models.task import TaskModel
from res.errors import Task_not_exist_exception, Project_not_exist_exception
from tests.utils.task_mock import *
from tests.utils.ticket_mock import *
from tests.utils.utils import *

task_service = Task_service()

# --- Given


@given("se ingresan tareas existentes asociadas a un proyecto existente")
def tasks_exists(context):
    context.tasks = [
        {"task_id": MOCK_TASK_1, "project_id": MOCK_PROJECT_1},
        {"task_id": MOCK_TASK_2, "project_id": MOCK_PROJECT_1}
    ]

@given("se ingresa una tarea que no existente asociadas a un proyecto existente")
def tasks_exists(context):
    context.tasks = [
        {"task_id": MOCK_TASK_NOT_EXIST, "project_id": MOCK_PROJECT_1},
        {"task_id": MOCK_TASK_2, "project_id": MOCK_PROJECT_1}
    ]

@given("se ingresa una tarea asociada a un proyecto que no existe")
def tasks_exists(context):
    context.tasks = [
        {"task_id": MOCK_TASK_1, "project_id": MOCK_PROJECT_NOT_EXIST},
        {"task_id": MOCK_TASK_2, "project_id": MOCK_PROJECT_1}
    ]

    

@given("se ingresa un ticket no existente")
def tasks_exists(context):
    context.original_ticket.id = MOCK_TICKET_ID_NOT_EXIST

# --- When


@when("se asocia tareas a ticket")
def assiate_tasks(context):
        
    context.response = context.client.put(
        f"{ENDPOINT_TASKS}/{context.product_id}/{context.version_code}/{context.original_ticket.id}",
        json = context.tasks
    ) 

# --- Then

@then("las tareas se asignan correctamente")
def check_ticket_is_modified_successfully(context):
    requested_tasks = task_service.get_tasks_by_ticket(
        context.product_id,
        context.version_code,
        context.original_ticket.id
    )
    assert_tasks(requested_tasks[0], context.tasks[0])
    assert_tasks(requested_tasks[1], context.tasks[1])

@then("se informa que la tarea no existe")
def check_ticket_not_exist(context):
    print(context.tasks[0])
    assert_exception_message(
        Task_not_exist_exception(
            context.tasks[0]['project_id'],
            context.tasks[0]['task_id']
        ),
        context.response
    )

@then("se informa que el proyecto no existe")
def check_ticket_not_exist(context):
    print(context.tasks[0])
    assert_exception_message(
        Project_not_exist_exception(
            context.tasks[0]['project_id']
        ),
        context.response
    )
