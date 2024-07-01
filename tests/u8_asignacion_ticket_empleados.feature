Feature: Asigncion de empleados a tickets

  Scenario: se asigna empleado a un ticket consulta correctamente
    Given que se ingresaron datos de ticket consulta validos
    When se crea un ticket
    Then se crea el ticket y le informa al usuario que se hizo correctamente

  Scenario: se asigna empleado a un ticket incidente correctamente
    Given que se ingresaron datos de ticket incidente validos
    When se crea un ticket
    Then se crea el ticket y le informa al usuario que se hizo correctamente

  Scenario: Empleado no existe al crear ticket consulta
    Given que se ingresan datos validos de un ticket consulta con un empleado que no existe
    When se crea un ticket
    Then se informa que el empleado no existe

  Scenario: Empleado no existe al crear ticket consulta
    Given que se ingresan datos validos de un ticket consulta y un empleado que no existente
    When se crea un ticket
    Then se informa que el empleado no existe
