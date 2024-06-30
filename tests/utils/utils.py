
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

