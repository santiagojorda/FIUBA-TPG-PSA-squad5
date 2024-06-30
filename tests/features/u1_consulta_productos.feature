Feature: Consulta de productos

    Scenario: Se obtienen todos los productos correctamente
      Given que existen productos
      When se consulta por productos
      Then se obtienen listado con los datos productos

    Scenario: No hay productos
      Given que no existen productos
      When se consulta por productos
      Then el sistema informa que no hay productos