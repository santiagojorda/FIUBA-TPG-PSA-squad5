Feature: Asignacion de tareas a ticket

    Scenario: Se asocia correctamente
        Given existe un producto y una version asociado al mismo 
        And existe un ticket consulta
        And se ingresan tareas existentes asociadas a un proyecto existente
        When se asocia tareas a ticket
        Then las tareas se asignan correctamente

    Scenario: Se asocia una tarea que no existe        
        Given existe un producto y una version asociado al mismo 
        And existe un ticket consulta
        And se ingresa una tarea que no existente asociadas a un proyecto existente
        When se asocia tareas a ticket
        Then se informa que la tarea no existe 

    Scenario: Se asocia una tarea de un proyecto que no existe        
        Given existe un producto y una version asociado al mismo 
        And existe un ticket consulta
        And se ingresa una tarea asociada a un proyecto que no existe
        When se asocia tareas a ticket
        Then se informa que el proyecto no existe 

