Feature: Eliminación de tickets

    Scenario: Eliminación de ticket consulta correctamente
        Given existe un producto y una version asociado al mismo 
        And existe un ticket consulta
        And se ingresa un id producto, un codigo version existente y id de un ticket existente
        When se elimina un ticket
        Then se elimina el ticket
        And se le informa que se elimino correctamente

    Scenario: Eliminación de ticket incidente correctamente
        Given existe un producto y una version asociado al mismo 
        And existen severidades
        And existe un ticket incidente
        And se ingresa un id producto, un codigo version existente y id de un ticket existente
        When se elimina un ticket
        Then se elimina el ticket
        And se le informa que se elimino correctamente

    Scenario: Eliminación de ticket fallida, ticket no existe
        Given existe un producto y una version asociado al mismo 
        And existe un ticket consulta
        And se ingresa un id producto, un codigo version existente y id de un ticket no existente
        When se elimina un ticket
        Then se elimina el ticket
        And se informa que el ticket no existe

