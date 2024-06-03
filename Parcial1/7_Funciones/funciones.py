""" Una funcion es un conjunto de instrucciones agrupadas bajo un nombre en particular como un prohtama mas pequeño que cumple una funcion especifica la funcion se puede reutilizar con el simple hecho de invocarla es decir mandarla llamar

intaxis:
 def nombredeMifuncion(parametros):
 bloque o conjunto de instrucciones

nombredeMifuncion(parametros=)

Las funciones pueden ser de 4 tipos 
1,- Funcion que no recibe parametros y no regresa Valor
2,- Funcion que no recibe parametros y regresa Valor
3,- Funcion que recibe parametros y no regresa Valor
4,- Funcion que  recibe parametros y regresa Valor

Temas a ver: funciones, lista, set, duplas y diccionarios
"""

#Crear una funcion para imprimir nombre de personas 
# 1,- Funcion que no recibe parametros y no regresa Valor
def solicitarNombre():
    nombre=input("Ingresa el nombre comleto:")

solicitarNombre()

#Ejemplo 2 Suma dos numeros
def suma():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")

suma()

#Ejemplo 3 sumar dos numeros
#2,- Funcion que no recibe parametros y regresa Valor

def suma():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    return suma

print(f"La suma es: {suma}")

#Ejemplo  4 suma dos numeros
#3,- Funcion que recibe parametros y no regresa Valor

def suma(n1,n2):
    suma=n1+n2
    print(f"La suma es: {suma}")
    
n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))    
suma(n1,n2)



#Ejemplo  5 suma dos numeros
#4,- Funcion que recibe parametros y regresa Valor

def suma(n1,n2):
    suma=n1+n2
    return suma

n1=int(input("Numero #1: "))
n2=int(input("Numero #2: ")) 
resultado_suma=suma(n1,n2)   
print(f"La suma es: {resultado_suma}")


#Ejemplo 6 Crear un programa que solicite a tarves de una funcion la siguiente informacion:
#Nombre del paciente , Edad, Estatura, Tipo de sangre , Utilizar los 4 tipo de funciones









