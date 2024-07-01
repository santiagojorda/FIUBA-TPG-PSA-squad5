Feature: Cierre ticket

    Scenario: Cierre de ticket consulta correctamente
        Given existe un producto y una version asociado al mismo 
        And existe un ticket consulta
        And se ingresan datos de moficacion de un ticket existente con un estado de ticket cerrado       
        When se modifica un ticket
        Then se modifica el ticket
        Then se informa que se hizo correctamente

        Scenario: Cierre de ticket incidente correctamente   
        Given existe un producto y una version asociado al mismo
        And existen severidades 
        And existe un ticket incidente
        And se ingresan datos de moficacion de un ticket existente con un estado de ticket cerrado       
        When se modifica un ticket
        Then se modifica el ticket
        And se informa que se hizo correctamente

     Scenario: Estado de ticket incidente invalido
        Given existe un producto y una version asociado al mismo 
        And existen severidades 
        And existe un ticket incidente
        And se ingresan datos de moficacion de un ticket existente con estado invalido
        When se modifica un ticket
        Then se informa que el estado de ticket es invalido

     Scenario: Estado de ticket consulta invalido
        Given existe un producto y una version asociado al mismo 
        And existe un ticket consulta
        And se ingresan datos de moficacion de un ticket existente con estado invalido
        When se modifica un ticket
        Then se informa que el estado de ticket es invalido