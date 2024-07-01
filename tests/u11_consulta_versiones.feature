Feature: Consulta de versiones

  Scenario: Se obtienen todas las versiones de un producto correctamente
    Given que existe un producto y tiene asociado versiones
    When se consulta las versiones del producto
    Then se obtienen listado con los datos versiones del producto

  Scenario: Un producto no tiene versiones
    Given que existe un producto y no tienen asociados versiones
    When se consulta las versiones del producto
    Then el sistema informa que el producto no posee versiones

  Scenario: El produco no existe
    Given que no existe un producto
    When se consulta las versiones del producto
    Then el sistema informa que el producto existe
