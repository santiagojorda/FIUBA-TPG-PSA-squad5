Feature: Getting tickets

    Scenario: Getting tickets successful
        Given Tickets obtaining data
          | product_id | version_code |
          | 1          | 1.1.0        |
        When gets tickets of a version and product
        Then the tickets should be retrieved successfully

    Scenario: Getting tickets failed, version_code is empty
        Given Tickets obtaining data
          | product_id |
          | 1          |
        When gets tickets of a version and product
        Then the tickets retrieval would be failed

    Scenario: Getting tickets failed, product_id is empty
        Given Tickets obtaining data
          | version_code |
          | 2.2.0        |
        When gets tickets of a version and product
        Then the tickets retrieval would be failed

    Scenario: Getting tickets failed, product_id or version_code doesn't exist
        Given Tickets obtaining data
          | product_id  | version_code |
          | 14          | 2.2.4        |
        When gets tickets of a version and product
        Then the tickets retrieval would be failed

    Scenario: Getting a ticket successful
        Given Tickets obtaining data
          | product_id | version_code | ticket_id |
          | 1          | 1.1.0        | 1         |
        When get an specific ticket
        Then the ticket should be retrieved successfully
    
    Scenario: Getting a ticket failed, version_code is empty
        Given Tickets obtaining data
          | product_id |
          | 1          |
        When gets tickets of a version and product
        Then the ticket retrieval would be failed

    Scenario: Getting a ticket failed, product_id is empty
        Given Tickets obtaining data
          | version_code |
          | 2.2.0        |
        When gets tickets of a version and product
        Then the ticket retrieval would be failed

    Scenario: Getting a ticket failed, product_id or version_code doesn't exist
        Given Tickets obtaining data
          | product_id  | version_code |
          | 14          | 2.2.4        |
        When gets tickets of a version and product
        Then the ticket retrieval would be failed