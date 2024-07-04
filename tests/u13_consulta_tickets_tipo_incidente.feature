Feature: Consulta tickets tipo incidente

    Scenario: Se obtienen todos los tickets tipo incidente correctamente
        Given existe un producto y una version asociado al mismo 
        And existen severidades
        And existen varios tickets incidente
        When se consulta por tickets
        Then se obtiene listado de todos los tickets asociados a ese producto y esa version 

    Scenario: No existen tickets
        Given existe un producto y una version asociado al mismo
        And no existen tickets incidentes asociados
        When se consulta por tickets
        Then se informa que no tiene tickets asociados
        
    Scenario: No existe producto
        Given ingresa id producto no existente y un codigo de version
        When se consulta por tickets
        Then se informa que el producto no existe
