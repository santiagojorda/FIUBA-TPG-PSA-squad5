Feature: Incident Ticket creation

    Scenario: Incident Ticket creation succesful
        Given Ticket creation data
          | product_id | version_code | title      | description      | client_id | employee_id | ticket_type | severity_id | playback_steps      |
          | 1          | 2.2.0        | mock_title | mock_description | 1         | 1           | 1           | 1           | mock_playback_steps |
        When create a new ticket
        Then the ticket should be created successfully

    Scenario: Incident Ticket creation failed, creation data without title
        Given Ticket creation data
          | product_id | version_code | description      | client_id | employee_id | ticket_type | severity_id | playback_steps      |
          | 1          | 2.2.0        | mock_description | 1         | 1           | 1           | 1           | mock_playback_steps |
        When create a new ticket
        Then the creation would be failed

    Scenario: Incident Ticket creation failed, creation data without description
        Given Ticket creation data
          | product_id | version_code | title      | client_id | employee_id | ticket_type | severity_id | playback_steps      |
          | 1          | 2.2.0        | mock_title | 1         | 1           | 1           | 1           | mock_playback_steps |
        When create a new ticket
        Then the creation would be failed

    Scenario: Incident Ticket creation failed, creation data without severity
        Given Ticket creation data
          | product_id | version_code | title      | description      | client_id | employee_id | ticket_type | playback_steps      |
          | 1          | 2.2.0        | mock_title | mock_description | 1         | 1           | 1           | mock_playback_steps |
        When create a new ticket
        Then the creation would be failed
 
    Scenario: Incident Ticket creation failed, creation data without ticket_type
        Given Ticket creation data
          | product_id | version_code | title      | description      | client_id | employee_id | severity_id | playback_steps      |
          | 1          | 2.2.0        | mock_title | mock_description | 1         | 1           | 1           | mock_playback_steps |
        When create a new ticket
        Then the creation would be failed
        
    Scenario: Incident Ticket creation failed, creation data without playback_steps
        Given Ticket creation data
          | product_id | version_code | title      | description      | client_id | employee_id | ticket_type | severity_id |
          | 1          | 2.2.0        | mock_title | mock_description | 1         | 1           | 1           | 1           |
        When create a new ticket
        Then the creation would be failed
        
    Scenario: Incident Ticket creation failed, creation data without employee_id
        Given Ticket creation data
          | product_id | version_code | title      | description      | client_id | ticket_type | severity_id | playback_steps      |
          | 1          | 2.2.0        | mock_title | mock_description | 1         | 1           | 1           | mock_playback_steps |
        When create a new ticket
        Then the creation would be failed

    Scenario: Incident Ticket creation failed, creation data without client_id
        Given Ticket creation data
          | product_id | version_code | title      | description      | employee_id | ticket_type | severity_id | playback_steps      |
          | 1          | 2.2.0        | mock_title | mock_description | 1           | 1           | 1           | mock_playback_steps |
        When create a new ticket
        Then the creation would be failed

    Scenario: Incident Ticket creation failed, creation data without product_id
        Given Ticket creation data
          | version_code | title      | description      | client_id | employee_id | ticket_type | severity_id | playback_steps      |
          | 2.2.0        | mock_title | mock_description | 1         | 1           | 1           | 1           | mock_playback_steps |
        When create a new ticket
        Then the creation would be failed

    Scenario: Incident Ticket creation failed, creation data without version_code
        Given Ticket creation data
          | product_id | title      | description      | client_id | employee_id | ticket_type | severity_id | playback_steps      |
          | 1          | mock_title | mock_description | 1         | 1           | 1           | 1           | mock_playback_steps |
        When create a new ticket
        Then the creation would be failed