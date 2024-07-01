Feature: Asignacion de tareas a ticket

    Scenario: Se asocia correctamente
        Given se ingresan tareas asociados a un proyecto y existe un ticket asociado a una version y un producto
        When se asocia tareas a ticket
        Then las tareas se asignan correctamente

    Scenario: No existen tareas
        Given se ingresan tareas que no existen y existe un ticket asociado a una version y un producto
        When se asocia tareas a ticket
        Then se informa que no pudo asociarse correctamente

