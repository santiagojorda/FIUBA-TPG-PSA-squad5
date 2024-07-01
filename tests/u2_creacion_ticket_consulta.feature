Feature: Creacion tickets consulta

  Scenario: Creación de ticket consulta correctamente
    Given existe un producto y una version asociado al mismo 
    And se ingresan datos de ticket consulta validos
    When se crea un ticket
    Then se crea el ticket 
    And se informa que se creo correctamente

  Scenario: Producto asociado no existe
    Given existe un producto y una version asociado al mismo 
    And se ingresan datos de ticket consulta validos
    And se ingresa un id de producto que no existe
    When se crea un ticket
    Then se informa que el producto asociado no existe

  Scenario: Codigo de version asociado no existe
    Given existe un producto y una version asociado al mismo 
    And se ingresan datos de ticket consulta validos
    And se ingresa un codigo de version que no esta asociado al id producto 
    When se crea un ticket
    Then se informa que el codigo de version no esta asociado al producto 

  Scenario: Titulo invalido
    Given existe un producto y una version asociado al mismo 
    And se ingresan datos de ticket consulta validos
    And no se ingresa titulo
    When se crea un ticket
    Then se informa que titulo es invalido

  Scenario: Descripcion invalido
    Given existe un producto y una version asociado al mismo 
    And se ingresan datos de ticket consulta validos  
    And no se ingresa descripcion
    When se crea un ticket
    Then se informa que descripcion es invalida

  Scenario: Tipo de ticket invalido
    Given existe un producto y una version asociado al mismo 
    And se ingresan datos de ticket consulta validos  
    And no se ingresa tipo de ticket
    When se crea un ticket
    Then se informa que el tipo de ticket es invalido

  Scenario: El cliente seleccionado no existe
    Given existe un producto y una version asociado al mismo 
    And se ingresan datos de ticket consulta validos  
    And se ingresa un cliente que no existe
    When se crea un ticket
    Then se informa que el cliente no existe
