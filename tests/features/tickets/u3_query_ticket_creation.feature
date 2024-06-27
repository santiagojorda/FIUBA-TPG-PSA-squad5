Feature: Query Ticket creation

    Scenario: Query Ticket creation succesful
        Given Ticket creation data
          | product_id | version_code | title      | description      | client_id | employee_id | ticket_type | response      | 
          | 1          | 2.2.0        | mock_title | mock_description | 1         | 1           | 0           | mock_response |
        When create a new ticket
        Then the ticket should be created successfully

    Scenario: Query Ticket creation failed, data without response
        Given Ticket creation data
          | product_id | version_code | title      | description      | client_id | employee_id | ticket_type | 
          | 1          | 2.2.0        | mock_title | mock_description | 1         | 1           | 0           |
        When create a new ticket
        Then the ticket should be created successfully

    Scenario: Query Ticket creation failed, creation data without title
        Given Ticket creation data
          | product_id | version_code | description      | client_id | employee_id | ticket_type | response      |
          | 1          | 2.2.0        | mock_description | 1         | 1           | 0           | mock_response |
        When create a new ticket
        Then the creation would be failed

    Scenario: Query Ticket creation failed, creation data without description
        Given Ticket creation data
          | product_id | version_code | title      | client_id | employee_id | ticket_type | response      |
          | 1          | 2.2.0        | mock_title | 1         | 1           | 0           | mock_response |
        When create a new ticket
        Then the creation would be failed

    Scenario: Query Ticket creation failed, creation data without ticket_type
        Given Ticket creation data
          | product_id | version_code | title      | description      | client_id | employee_id | response      |
          | 1          | 2.2.0        | mock_title | mock_description | 1         | 1           | mock_response |
        When create a new ticket
        Then the creation would be failed
        
    Scenario: Query Ticket creation failed, creation data without employee_id
        Given Ticket creation data
          | product_id | version_code | title      | description      | client_id | ticket_type | response      |
          | 1          | 2.2.0        | mock_title | mock_description | 1         | 0           | mock_response |
        When create a new ticket
        Then the creation would be failed

    Scenario: Query Ticket creation failed, creation data without client_id
        Given Ticket creation data
          | product_id | version_code | title      | description      | employee_id | ticket_type | response      |
          | 1          | 2.2.0        | mock_title | mock_description | 1           | 0           | mock_response |
        When create a new ticket
        Then the creation would be failed

    Scenario: Query Ticket creation failed, creation data without product_id
        Given Ticket creation data
          | version_code | title      | description      | client_id | employee_id | ticket_type | response      |
          | 2.2.0        | mock_title | mock_description | 1         | 1           | 0           | mock_response |
        When create a new ticket
        Then the creation would be failed

    Scenario: Query Ticket creation failed, creation data without version_code
        Given Ticket creation data
          | product_id | title      | description      | client_id | employee_id | ticket_type | response      |
          | 1          | mock_title | mock_description | 1         | 1           | 0           | mock_response |
        When create a new ticket
        Then the creation would be failed