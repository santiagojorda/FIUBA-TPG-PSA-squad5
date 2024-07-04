Feature: Asigncion de empleados a tickets

    Scenario: Se asigna empleado a un ticket consulta correctamente
        Given existe un producto y una version asociado al mismo
        And se ingresan datos de ticket consulta validos
        When se crea un ticket
        Then se crea el ticket
        And se informa que se creo correctamente

    Scenario: Se asigna empleado a un ticket incidente correctamente
        Given existe un producto y una version asociado al mismo
        And existen severidades
        And se ingresan datos de ticket incidente validos
        When se crea un ticket
        Then se crea el ticket
        And se informa que se creo correctamente

    Scenario: Empleado no existe al asignar ticket consulta
        Given existe un producto y una version asociado al mismo
        And se ingresan datos de ticket consulta validos
        And se ingresa un empleado que no existe
        When se crea un ticket
        Then se informa que el empleado no existe

    Scenario: Empleado no existe al asignar ticket incidente
        Given existe un producto y una version asociado al mismo
        And existen severidades
        And se ingresan datos de ticket incidente validos
        And se ingresa un empleado que no existe
        When se crea un ticket
        Then se informa que el empleado no existe

    Scenario: Modificación de ticket incidente correcta
        Given existe un producto y una version asociado al mismo 
        And existen severidades
        And existe un ticket incidente
        And se ingresan nuevos datos validos de ticket incidente existente
        When se modifica un ticket
        Then se modifica el ticket
        And se informa que se hizo correctamente
    
    Scenario: Modificación de ticket consulta correcta
        Given existe un producto y una version asociado al mismo 
        And existe un ticket consulta
        And se ingresan nuevos datos validos de ticket consulta existente
        When se modifica un ticket
        Then se modifica el ticket
        And se informa que se hizo correctamente

    Scenario: En un ticket incidente se cambia la asignacion de empleado a uno no existente de un ticket consulta        
        Given existe un producto y una version asociado al mismo
        And existen severidades 
        And existe un ticket incidente
        And se ingresan datos de moficacion de un ticket existente con un empleado que no existe
        When se modifica un ticket
        Then se informa que el empleado no existe

    Scenario: En un ticket consulta se cambia la asignacion de empleado a uno no existente de un ticket consulta        
        Given existe un producto y una version asociado al mismo
        And existe un ticket consulta
        And se ingresan datos de moficacion de un ticket existente con un empleado que no existe
        When se modifica un ticket
        Then se informa que el empleado no existe