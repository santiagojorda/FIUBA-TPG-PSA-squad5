Feature: Request clients

    Scenario: succesful request of clients
        Given the clients
        | id      | razon social  | CUIT          |
        | 1       | FIUBA         | 20-12345678-2 |
        | 2       | FSOC          | 20-12345678-5 |
        | 3       | Macro         | 20-12345678-3 |
        When the user requests the clients
        Then the system shows the clients
        | id      | razon social  | CUIT          |
        | 1       | FIUBA         | 20-12345678-2 |
        | 2       | FSOC          | 20-12345678-5 |
        | 3       | Macro         | 20-12345678-3 |

    Scenario: succesful request client by id
        Given the clients
        | id      | razon social  | CUIT          |
        | 2       | FSOC          | 20-12345678-5 |
        When the user requests the client by id = 2
        Then the system shows the client
        | id | razon social | CUIT          |
        | 2  | FSOC         | 20-12345678-5 |

    Scenario: failed request client by id
        Given the clients
        | id      | razon social  | CUIT          |
        | 2       | FSOC          | 20-12345678-5 |
        When the user requests the client by id = 55
        Then the system notifies there is no client with that id