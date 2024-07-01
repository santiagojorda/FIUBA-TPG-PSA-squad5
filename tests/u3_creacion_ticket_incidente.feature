Feature: Creacion tickets incidente

  Scenario: Creación de ticket incidente correctamente
    Given existe un producto y una version asociado al mismo
    And existen severidades
    And se ingresan datos de ticket incidente validos
    When se crea un ticket
    Then se crea el ticket
    And se informa que se creo correctamente

  Scenario: Producto asociado no existe
    Given existe un producto y una version asociado al mismo 
    And existen severidades
    And se ingresan datos de ticket incidente validos
    And se ingresa un id de producto que no existe
    When se crea un ticket
    Then se informa que el producto asociado no existe

  Scenario: Codigo de version asociado no existe
    Given existe un producto y una version asociado al mismo 
    And existen severidades
    And se ingresan datos de ticket incidente validos
    And se ingresa un codigo de version que no esta asociado al id producto 
    When se crea un ticket
    Then se informa que el codigo de version no esta asociado al producto 

  Scenario: Titulo invalido
    Given existe un producto y una version asociado al mismo 
    And existen severidades
    And se ingresan datos de ticket incidente validos
    And no se ingresa titulo
    When se crea un ticket
    Then se informa que titulo es invalido

  Scenario: Descripcion invalido
    Given existe un producto y una version asociado al mismo 
    And existen severidades
    And se ingresan datos de ticket incidente validos  
    And no se ingresa descripcion
    When se crea un ticket
    Then se informa que descripcion es invalida

  Scenario: Tipo de ticket invalido
    Given existe un producto y una version asociado al mismo 
    And existen severidades
    And se ingresan datos de ticket incidente validos  
    And no se ingresa tipo de ticket
    When se crea un ticket
    Then se informa que el tipo de ticket es invalido

  Scenario: Sin estado
    Given existe un producto y una version asociado al mismo 
    And existen severidades
    And se ingresan datos de ticket incidente validos  
    And se ingresa estado no valido
    When se crea un ticket
    Then se informa que el estado de ticket es invalido

  Scenario: Estado de ticket invalido
    Given existe un producto y una version asociado al mismo 
    And existen severidades
    And se ingresan datos de ticket incidente validos  
    And no se ingresa estado de ticket
    When se crea un ticket
    Then se informa que el estado de ticket es invalido

  Scenario: La fecha de cierre es anterior a la de apertura
    Given existe un producto y una version asociado al mismo 
    And existen severidades
    And se ingresan datos de ticket incidente validos  
    And la fecha de cierre es anterior a la de apertura
    When se crea un ticket
    Then se informa que la fecha de cierre es anterior a la de apertura

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

  Scenario: Pasos de reproduccion invalidos
    Given existe un producto y una version asociado al mismo 
    And existen severidades
    And se ingresan datos de ticket incidente validos  
    And no se ingresa pasos de reproduccion
    When se crea un ticket
    Then se informa que los pasos de reproduccion son invalidos
