Feature: Modificación tickets consulta

    Scenario: Modificación de ticket consulta correcta
        Given existe un producto y una version asociado al mismo 
        And existe un ticket consulta
        And se ingresan nuevos datos validos de ticket consulta existente
        When se modifica un ticket
        Then se modifica el ticket
        And se informa que se hizo correctamente

    Scenario: Ticket no existe
        Given existe un producto y una version asociado al mismo 
        And existe un ticket consulta
        And se ingresan datos de moficacion de un ticket que no existe
        When se modifica un ticket
        Then se informa que el ticket no existe

    Scenario: Producto asociado no existe
        Given existe un producto y una version asociado al mismo 
        And existe un ticket consulta
        And se ingresan datos de moficacion de un ticket existente con un id de un producto que no existe
        When se modifica un ticket
        Then se informa que el producto asociado no existe

    Scenario: Codigo de version asociado no existe
        Given existe un producto y una version asociado al mismo 
        And existe un ticket consulta
        And se ingresan datos de moficacion de un ticket existente con una versio de un producto que no existe        
        When se modifica un ticket
        Then se informa que el codigo de version no esta asociado al producto 

    Scenario: Fecha de cierre es anterior a la fecha de ingreso
        Given existe un producto y una version asociado al mismo 
        And existe un ticket consulta
        And se ingresan datos de moficacion de un ticket existente con una fecha de cierre anterior a la fecha de ingreso        
        When se modifica un ticket
        Then se informa que la fecha de cierre es anterior a la de apertura

    Scenario: Se ingresa una cliente no existente
        Given existe un producto y una version asociado al mismo
        And existe un ticket consulta
        And se ingresan datos de moficacion de un ticket existente con un cliente que no existe  
        When se modifica un ticket
        Then se informa que el cliente no existe