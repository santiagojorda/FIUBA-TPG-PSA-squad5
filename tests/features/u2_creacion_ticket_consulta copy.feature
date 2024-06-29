# Feature: Creacion tickets consulta

#   Scenario: Creación de ticket consulta correctamente
#     Given se ingresaron datos de ticket consulta validos
#     When se crea un ticket
#     Then se crea el ticket y le informa al usuario que se hizo correctamente

#   Scenario: Producto asociado no existe
#     Given se ingresa un id de producto que no existe
#     When se crea un ticket
#     Then se informa que el producto asociado no existe

#   Scenario: Codigo de version asociado no existe
#     Given se ingresa un codigo de version que no esta asociado al id producto 
#     When se crea un ticket
#     Then se informa que el codigo de version no esta asociado al producto 

#   Scenario: No se ingresa titulo
#     Given no se ingresa titulo
#     When se crea un ticket
#     Then se informa que hay datos invalidos

#   Scenario: No se ingresa descripcion
#     Given no se ingresa descripcion
#     When se crea un ticket
#     Then se informa que hay datos invalidos

#   Scenario: No se ingresa tipo de ticket
#     Given no se ingresa descripcion
#     When se crea un ticket
#     Then se informa que hay datos invalidos

#   Scenario: No se ingresa fecha de apertura
#     Given no se ingresa fecha de apertura
#     When se crea un ticket
#     Then se informa que hay datos invalidos

#   Scenario: La fecha de cierre es anterior a la de apertura
#     Given se ingresa fecha de cierre es anterior a la de apertura
#     When se crea un ticket
#     Then se informa que hay datos invalidos

#   Scenario: El cliente seleccionado no existe
#     Given se ingresa un cliente que no existe
#     When se crea un ticket
#     Then se informa que el cliente no existe

#   # Scenario: El empleado seleccionado no existe
#   #   Given se ingresa un empleado responsable del ticket que no existe
#   #   When se crea un ticket
#   #   Then se informa que el empleado no existe

# # Escenario 3: Creación de ticket incidente fallida, sin el dato de severidad
# # Dado que se ingresan datos de tipo ticket incidente pero no incluye la severidad
# # Cuando quiero crear un ticket de tipo incidente
# # Entonces no se crea un ticket y se indica que no se ingreso la severidad

# # Escenario 4: Creación de ticket incidente fallida, sin pasos de preproducción (playback steps)
# # Dado que se ingresan datos de tipo ticket incidente pero no incluye los pasos de preproducción
# # Cuando quiero crear un ticket de tipo incidente
# # Entonces no se crea un ticket y se indica que no se ingresaron los pasos de preproducción

# # Escenario 6: Creación de ticket fallida, sin el dato el id de producto
# # Dado que se ingresan datos de tipo ticket pero no incluye el id de producto
# # Cuando quiero crear un ticket de cualquier tipo
# # Entonces no se crea un ticket y se indica que no se ingreso el id de producto

# # Escenario 7: Creación de ticket fallida, sin el dato el id de cliente
# # Dado que se ingresan datos de tipo ticket pero no incluye el id de cliente
# # Cuando quiero crear un ticket de cualquier tipo
# # Entonces no se crea un ticket y se indica que no se ingreso el id de cliente

# # Escenario 8: Creación de ticket fallida, sin el dato la versión de producto
# # Dado que se ingresan datos de tipo ticket pero no incluye la versión de producto
# # Cuando quiero crear un ticket de cualquier tipo
# # Entonces no se crea un ticket y se indica que no se ingreso la versión de producto

# # Escenario 9: Creación de ticket fallida, sin el dato de numero de empleado
# # Dado que se ingresan datos de tipo ticket pero no incluye el numero de empleado
# # Cuando quiero crear un ticket de cualquier tipo
# # Entonces no se crea un ticket y se indica que no se ingreso el numero de empleado

# # Escenario 10: Creación de ticket fallida, sin titulo
# # Dado que se ingresan datos de tipo ticket pero no incluye titulo
# # Cuando quiero crear un ticket de cualquier tipo
# # Entonces no se crea un ticket y se indica que no se ingreso titulo

# # Escenario 11: Creación de ticket fallida, sin descripción
# # Dado que se ingresan datos de tipo ticket pero no incluye descripción
# # Cuando quiero crear un ticket de cualquier tipo
# # Entonces no se crea un ticket y se indica que no se ingreso descripción

# # Escenario 12: Creación de ticket fallida, el día de finalización es anterior al día de inicio
# # Dado que se ingresan datos de tipo ticket pero el día de finalización es anterior al día de inicio
# # Cuando quiero crear un ticket de cualquier tipo
# # Entonces no se crea un ticket y se indica que el día de finalización es anterior al día de inicio