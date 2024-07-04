Feature: Consulta de versiones

    Scenario: Se obtienen todas las versiones de un producto correctamente
        Given existe un producto
        And existen versiones asociadas al producto
        When se consulta las versiones de un producto
        Then se obtienen listado con los datos versiones del producto

    Scenario: Un producto no tiene versiones
        Given no existe producto
        When se consulta las versiones de un producto
        Then se informa que el producto no existe
