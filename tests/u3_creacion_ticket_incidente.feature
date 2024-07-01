Feature: Creacion tickets incidente

  Scenario: Creación de ticket incidente correctamente
    Given se ingresaron datos de ticket incidente validos
    When se crea un ticket
    Then se crea el ticket y le informa al usuario que se hizo correctamente

  Scenario: Producto asociado no existe
    Given que se ingresan datos validos de un ticket incidente y se ingresa un id de producto que no existe
    When se crea un ticket
    Then se informa que el producto asociado no existe

  Scenario: Codigo de version asociado no existe
    Given que se ingresan datos validos de un ticket incidente y se ingresa un codigo de version que no esta asociado al id producto 
    When se crea un ticket
    Then se informa que el codigo de version no esta asociado al producto 

  Scenario: No se ingresa titulo
    Given que se ingresan datos validos de un ticket incidente y no se ingresa titulo
    When se crea un ticket
    Then se informa que no hay titulo

  Scenario: No se ingresa descripcion
    Given que se ingresan datos validos de un ticket incidente y no se ingresa descripcion
    When se crea un ticket
    Then se informa que no hay descripcion

  Scenario: No se ingresa tipo de ticket
    Given que se ingresan datos validos de un ticket incidente y no se ingresa tipo de ticket
    When se crea un ticket
    Then se informa que el tipo de ticket es invalido

  Scenario: No se ingresa fecha de apertura
    Given que se ingresan datos validos de un ticket incidente y no se ingresa fecha de apertura
    When se crea un ticket
    Then se informa la fecha ingresada de apertura es invalida

  Scenario: La fecha de cierre es anterior a la de apertura
    Given que se ingresan datos validos de un ticket incidente y la fecha de cierre es anterior a la de apertura
    When se crea un ticket
    Then se informa que la fecha de cierre es anterior a la de apertura

  Scenario: El cliente seleccionado no existe
    Given que se ingresan datos validos de un ticket incidente con un cliente que no existe
    When se crea un ticket
    Then se informa que el cliente no existe

  Scenario: El empleado seleccionado no existe
    Given que se ingresan datos validos de un ticket incidente con un empleado que no existe
    When se crea un ticket
    Then se informa que el empleado no existe

  Scenario: No se ingresa severidad
    Given que se ingresan datos validos de un ticket incidente y no se ingresa severidad
    When se crea un ticket
    Then se informa que la severidad es invalido

  Scenario: No se ingresa pasos de reproduccion
    Given que se ingresan datos validos de un ticket incidente y no se ingresa pasos de reproduccion
    When se crea un ticket
    Then se informa que los pasos de reproduccion son invalido