# Feature: Gestión de Tickets

#   Background: 
#     Given que tengo un producto con id "1" y versión "2.2.0"
#     | title          | description                    | status | opening_date | client_id | employee_id | ticket_type |
#     | "Nuevo Ticket" | "Descripción del nuevo ticket" | 0      | 2024-06-27 | 1         | None        |             |

#   Scenario: Crear un nuevo ticket
#     Given los detalles del nuevo ticket
#     | title          | description                    | status | opening_date | client_id | employee_id | ticket_type |
#     | "Nuevo Ticket" | "Descripción del nuevo ticket" | 0      | 2024-06-27 | 1         | None        | QUERY_TICKET |
#     When creo un nuevo ticket
#     Then el sistema crea el ticket exitosamente

#   Scenario: Crear un nuevo ticket con campos opcionales
#     Given que tengo un producto con id "2" y versión "1.1.0"
#       | title               | description                          | status | opening_date | client_id | employee_id | ticket_type  |
#       | "Ticket Opcional"   | "Descripción del ticket opcional"     | 0      | 2024-06-27   | 2         | None        | QUERY_TICKET |
#     When creo un nuevo ticket con campos opcionales
#       | severity_id | playback_steps                                                                                                          |
#       | 2           | "Paso 1: Abrir la aplicación\nPaso 2: Reproducir el error\nPaso 3: Observar el mensaje de error"                             |
#     Then el sistema crea el ticket con campos opcionales exitosamente


#   Scenario: Crear un nuevo ticket con campos obligatorios faltantes
#     Given que tengo un producto con id "2" y versión "1.1.0"
#     When intento crear un nuevo ticket con campos obligatorios faltantes
#       | title            | description                        | status | opening_date | client_id | ticket_type  |
#       | "Ticket Incompleto" | "Descripción del ticket incompleto" | 0      | 2024-06-28   | 1         | QUERY_TICKET |
#     Then el sistema no crea el ticket y muestra un mensaje de error adecuado
