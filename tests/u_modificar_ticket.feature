Feature: Modificación tickets consulta

   Scenario: Modificación de ticket consulta correctamente
       Given se selecciona un ticket consulta existente y se ingresan nuevos datos de ticket consulta validos
       When se modifica un ticket
       Then se modifica el ticket y le informa al usuario que se hizo correctamente

#    Scenario: Fecha de cierre es anterior a la fecha de ingreso
#        Given se selecciona un ticket existente y se ingresa una fecha de cierre anterior a la fecha de ingreso  
#        When se modifica un ticket
#        Then se informa que la fecha de cierre es anterior a la fecha de ingreso

#    Scenario: Se ingresa un titulo invalido
#        Given se selecciona un ticket existente y se ingresa un titulo invalido  
#        When se modifica un ticket
#        Then se informa que el titulo es invalido

#    Scenario: Se ingresa una descripcion invalida
#        Given se selecciona un ticket existente y se ingresa una descripcion invalida  
#        When se modifica un ticket
#        Then se informa que la descripcion es invalida

#    Scenario: Se ingresa una cliente no existente
#        Given se selecciona un ticket existente y se ingresa una cliente invalido  
#        When se modifica un ticket
#        Then se informa que el cliente no existe