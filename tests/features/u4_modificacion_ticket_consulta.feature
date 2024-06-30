Feature: Modificación tickets consulta

   Scenario: Modificación de ticket consulta correctamente
       Given se selecciona un ticket consulta existente y se ingresan nuevos datos de ticket consulta validos
       When se modifica un ticket
       Then se modifica el ticket y le informa al usuario que se hizo correctamente
