Feature: Gestión de Tickets

  Background: 
    Given que tengo un producto con id "1" y versión "2.2.0"
    | title          | description                    | status | opening_date | client_id | employee_id | ticket_type |
    | "Nuevo Ticket" | "Descripción del nuevo ticket" | 0      | 2024-06-27 | 1         | None        |             |

  Scenario: Crear un nuevo ticket
    Given los detalles del nuevo ticket
    | title          | description                    | status | opening_date | client_id | employee_id | ticket_type |
    | "Nuevo Ticket" | "Descripción del nuevo ticket" | 0      | 2024-06-27 | 1         | None        | QUERY_TICKET |
    When creo un nuevo ticket
    Then el sistema crea el ticket exitosamente

  Scenario: Modificar un ticket existente
    Given que tengo un ticket con id "3"
    When modifico el ticket con los siguientes detalles
    | title               | description                         | status | opening_date | client_id | employee_id | ticket_type |
    | "Ticket Modificado" | "Descripción modificada del ticket" | 1      | 2024-06-28 | 1         | 2           | INCIDENT_TICKET |
    Then el ticket se modifica exitosamente


