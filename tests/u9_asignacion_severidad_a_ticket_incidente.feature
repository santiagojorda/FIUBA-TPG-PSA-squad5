Feature: Asignacion de severidad a ticket

    Scenario: Creación de ticket incidente correctamente
        Given existe un producto y una version asociado al mismo
        And existen severidades
        And se ingresan datos de ticket incidente validos
        When se crea un ticket
        Then se crea el ticket
        And se informa que se creo correctamente

    Scenario: Sin severidad 
        Given existe un producto y una version asociado al mismo 
        And existen severidades
        And se ingresan datos de ticket incidente validos  
        And no se ingresa severidad 
        When se crea un ticket
        Then se informa que la severidad es invalida

    Scenario: Severidad invalida
        Given existe un producto y una version asociado al mismo 
        And existen severidades
        And se ingresan datos de ticket incidente validos  
        And se ingresa severidad no existente
        When se crea un ticket
        Then se informa que la severidad no existe
        
    Scenario: Se ingresa una severidad invalida
        Given existe un producto y una version asociado al mismo
        And existen severidades 
        And existe un ticket incidente
        And se ingresan datos de moficacion de un ticket existente con una severidad que no existe  
        When se modifica un ticket
        Then se informa que la severidad no existe