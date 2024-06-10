#Los errores de ejecucion en un lenguaje de programacion se presentan cuando existen una anomalia o error dentro de la ejecucion del codigo lo cual provoca que se detenga la ejecucion del mismo con el contol  manejo de exepciones sera posible minimizar o evotar la interrupcion del programa debido a una exepcion

#Ejemplo 1 cuando una variable no se genera 

nombre=input("Introduce el nombre completo de una persona")
if len(nombre)>0:
    nombre_usuario="El nombre completo del usuario es:" + nombre
    print(nombre_usuario)
else :
    print("No tienes nombre intentalo de nuevo")


