Feature: Asignacion de tareas a ticket

    Scenario: Se obtiene un tareas correctamente
      Given se ingresan tareas asociados a un proyecto y existe un ticket asociado a una version y un producto
      When se asocia tareas a ticket
      Then las tareas se asignan correctamente

    Scenario: No existen tareas
      Given se ingresan tareas que no existen y existe un ticket asociado a una version y un producto
      When se asocia tareas a ticket
      Then se informa que no pudo asociarse correctamente

    # Scenario: Se obtiene un cliente por id correctamente
    #   Given que existen clientes y se ingreso un cliente existente
    #   When se consulta por un cliente
    #   Then se obtienen los datos del cliente

    # Scenario: Cliente no existe
    #   Given que existen clientes y se ingreso un cliente no existente
    #   When se consulta por un cliente
    #   Then se informa que el cliente no existe