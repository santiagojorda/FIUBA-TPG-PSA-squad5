
def assert_exception_message(exception: Exception, response):
    response = response.json()
    expected_message = str(exception)
    print(response)
    assert response['detail'] == expected_message

def assert_fields_two_arr(arr1, arr2, field_name: str, first_index = False):
    if first_index == None:
        assert arr1[field_name] == arr2[field_name]   
    else:
        assert arr1[first_index][field_name] == arr2[first_index][field_name]   

def assert_fields_two_dics(dic1, dic2, field_name):
    assert dic1[field_name] == dic2[field_name]   

def assert_tickets(ticket_1, ticket_2):
    assert ticket_1.id == ticket_2.id
    assert ticket_1.product_id == ticket_2.product_id
    assert ticket_1.version_code == ticket_2.version_code
    assert ticket_1.title == ticket_2.title
    assert ticket_1.description == ticket_2.description
    assert str(ticket_1.opening_date) == str(ticket_2.opening_date)
    assert str(ticket_1.closing_date) == str(ticket_2.closing_date)
    assert ticket_1.status == ticket_2.status
    assert ticket_1.response == ticket_2.response
    assert ticket_1.playback_steps == ticket_2.playback_steps
    assert ticket_1.employee_id == ticket_2.employee_id
    assert ticket_1.client_id == ticket_2.client_id
    assert ticket_1.severity_id == ticket_2.severity_id