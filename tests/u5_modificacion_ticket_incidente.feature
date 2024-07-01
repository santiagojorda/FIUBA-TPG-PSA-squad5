Feature: Modificación tickets incidente

    Scenario: Modificación de ticket incidente correcta
        Given existe un producto y una version asociado al mismo 
        And existen severidades
        And existe un ticket incidente
        And se ingresan nuevos datos validos de ticket incidente existente
        When se modifica un ticket
        Then se modifica el ticket
        And se informa que se hizo correctamente

    Scenario: Producto asociado no existe
        Given existe un producto y una version asociado al mismo 
        And existen severidades
        And existe un ticket incidente
        And se ingresan datos de moficacion de un ticket existente con un id de un producto que no existe
        When se modifica un ticket
        Then se informa que el producto asociado no existe

    Scenario: Codigo de version asociado no existe
        Given existe un producto y una version asociado al mismo
        And existen severidades 
        And existe un ticket incidente
        And se ingresan datos de moficacion de un ticket existente con una versio de un producto que no existe        
        When se modifica un ticket
        Then se informa que el codigo de version no esta asociado al producto 

    Scenario: Fecha de cierre es anterior a la fecha de ingreso
        Given existe un producto y una version asociado al mismo
        And existen severidades 
        And existe un ticket incidente
        And se ingresan datos de moficacion de un ticket existente con una fecha de cierre anterior a la fecha de ingreso        
        When se modifica un ticket
        Then se informa que la fecha de cierre es anterior a la de apertura

    Scenario: Se ingresa una cliente no existente
        Given existe un producto y una version asociado al mismo
        And existen severidades 
        And existe un ticket incidente
        And se ingresan datos de moficacion de un ticket existente con un cliente que no existe  
        When se modifica un ticket
        Then se informa que el cliente no existe

    Scenario: Se ingresa una cliente no existente
        Given existe un producto y una version asociado al mismo
        And existen severidades 
        And existe un ticket incidente
        And se ingresan datos de moficacion de un ticket existente con un cliente que no existe  
        When se modifica un ticket
        Then se informa que el cliente no existe

    Scenario: Se ingresa un tipo de ticket invalido
        Given existe un producto y una version asociado al mismo
        And existen severidades 
        And existe un ticket incidente
        Given se selecciona un ticket incidente existente y se ingresa un tipo de ticket invalido  
        When se modifica un ticket
        Then se informa que el tipo de ticket es invalido

     Scenario: Se ingresa una severidad invalida
        Given existe un producto y una version asociado al mismo
        And existen severidades 
        And existe un ticket incidente
        And se ingresan datos de moficacion de un ticket existente con una severidad que no existe  
        When se modifica un ticket
        Then se informa que la severidad no existe

     Scenario: Estado de ticket incidente invalido
        Given existe un producto y una version asociado al mismo 
        And existen severidades 
        And existe un ticket incidente
        And se ingresan datos de moficacion de un ticket existente con estado invalido
        When se modifica un ticket
        Then se informa que el estado de ticket es invalido