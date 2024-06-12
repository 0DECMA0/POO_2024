#Los errores de ejecucion en un lenguaje de programacion se presentan cuando existen una anomalia o error dentro de la ejecucion del codigo lo cual provoca que se detenga la ejecucion del mismo con el contol  manejo de exepciones sera posible minimizar o evotar la interrupcion del programa debido a una exepcion

#Ejemplo 1 cuando una variable no se genera 

try:
    nombre=input("Introduce el nombre completo de una persona")
    if len(nombre)>0:
        nombre_usuario="El nombre completo del usuario es:" + nombre
    print(nombre_usuario)
except:
    print("Es necesario intoducir un nombre de usuario.... verifica por favor")


x=3+4
print("El valor de x es:" +str(0))



#Ejemplo 2 cuando se solicita un numero y se ingresa otra cosa

try:
    numero=int(input("Ingresa un numero entero"))
    if numero>0:
       print("Soy un numero entero positivo")
    elif numero==0:
        print("Soy un numero entero neutro")
    else:
        print("Soy un numero entero negativo")
except ValueError:
    print("Introduce un numero entero")

#Ejemplo 3 Cuando se generan multiples excepciones

try:
    numero=int(input("Introduce un numero: "))
    print("EL cudrado del numero es: "+str(numero+numero))
except ValueError :
    print("Intoduce un valor numerico entero")
except TypeError :
    print("Se debe convertir el numero a entero")
else: 
    print("No se presentaron errores de ejecucion")
finally:
    print("Termine la ejecucion")