Feature: Modificación tickets incidente

    Scenario: Modificación de ticket incidente correctamente
        Given se selecciona un ticket incidente existente y se ingresan nuevos datos de ticket incidente validos
        When se modifica un ticket
        Then se modifica el ticket y le informa al usuario que se hizo correctamente

    Scenario: Producto asociado no existe
        Given se selecciona un ticket incidente existente y se ingresa un id de producto que no existe
        When se modifica un ticket
        Then se informa que el producto asociado no existe

    Scenario: Codigo de version asociado no existe
        Given se selecciona un ticket incidente existente y se ingresa un codigo de version que no esta asociado al id producto 
        When se modifica un ticket
        Then se informa que el codigo de version no esta asociado al producto 

    Scenario: Fecha de cierre es anterior a la fecha de ingreso
        Given se selecciona un ticket incidente existente y se ingresa una fecha de cierre anterior a la fecha de ingreso  
        When se modifica un ticket
        Then se informa que la fecha de cierre es anterior a la fecha de ingreso

    Scenario: Se ingresa un titulo invalido
        Given se selecciona un ticket incidente existente y se ingresa un titulo invalido  
        When se modifica un ticket
        Then se informa que el titulo es invalido

    Scenario: Se ingresa una descripcion invalida
        Given se selecciona un ticket incidente existente y se ingresa una descripcion invalida  
        When se modifica un ticket
        Then se informa que la descripcion es invalida

    Scenario: Se ingresa una cliente no existente
        Given se selecciona un ticket incidente existente y se ingresa un cliente que no existe
        When se modifica un ticket
        Then se informa que el cliente no existe

    Scenario: Se ingresa un empleado no existente
        Given se selecciona un ticket incidente existente y se ingresa un empleado que no existe  
        When se modifica un ticket
        Then se informa que el empleado no existe

    Scenario: Se ingresa un tipo de ticket invalido
        Given se selecciona un ticket incidente existente y se ingresa un tipo de ticket invalido  
        When se modifica un ticket
        Then se informa que el tipo de ticket es invalida

    Scenario: Se ingresa un tipo de ticket invalido
        Given se selecciona un ticket incidente existente y se ingresa un tipo de ticket invalido  
        When se modifica un ticket
        Then se informa que el tipo de ticket es invalida

    Scenario: Se ingresa una severidad invalida
        Given se selecciona un ticket incidente existente y se ingresa una severidad invalida  
        When se modifica un ticket
        Then se informa que el tipo de severidad es invalida

    Scenario: Se ingresa pasos de reproduccion invalido
        Given se selecciona un ticket incidente existente y se ingresan pasos de reproduccion invalidos  
        When se modifica un ticket
        Then se informa que los pasos de reproduccion son invalidos