Feature: Asignacion de severidad a ticket

    Scenario: Creación de ticket incidente correctamente
        Given se ingresaron datos de ticket incidente validos
        When se crea un ticket
        Then se crea el ticket y le informa al usuario que se hizo correctamente
    
    Scenario: No se ingresa severidad
        Given que se ingresan datos validos de un ticket incidente y no se ingresa severidad
        When se crea un ticket
        Then se informa que la severidad es invalido

    Scenario: Modificación de ticket incidente correctamente
        Given se selecciona un ticket incidente existente y se ingresan nuevos datos de ticket incidente validos
        When se modifica un ticket
        Then se modifica el ticket y le informa al usuario que se hizo correctamente

    Scenario: Se ingresa una severidad invalida
        Given se selecciona un ticket incidente existente y se ingresa una severidad invalida  
        When se modifica un ticket
        Then se informa que el tipo de severidad es invalida