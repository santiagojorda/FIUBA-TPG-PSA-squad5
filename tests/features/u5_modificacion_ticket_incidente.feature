Feature: Modificación tickets incidente

   Scenario: Modificación de ticket incidente correctamente
       Given se selecciona un ticket incidente existente y se ingresan nuevos datos de ticket incidente validos
       When se modifica un ticket
       Then se modifica el ticket y le informa al usuario que se hizo correctamente
