
# list(Array)
# Son coleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico
# Nota sus valores si son modificables

# las lista es una coleccion ordenada y modificale permite miembros duplicados



# #Ejemplo 1 crear una lista de numeros e imprimir el contenido 

# numero=[23,34]
# print(numero)

# #Recorrer la lista con for 
# for i in numero:
#     print(i)

# #Recorrer la lista con un ciclo while 

# #Ejemplo 2 crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 

# palabras=["","Hola","Como","Estas","Ok"]
# palabra_a_buscar=input("Ingresa la palabra a buscar: ")
# indice = 0
# encontrado = False
# while indice < len(palabras):
#     if palabras[indice] == palabra_a_buscar:
#         print(f"Palabra '{palabra_a_buscar}' encontrada en el índice {indice}.")
#         encontrado = True
#         break  
#     indice += 1

# if not encontrado:
#     print(f"Palabra '{palabra_a_buscar}' no encontrada en la lista.")




# numeros=[23,34]
# print(numeros)


# for i in numeros:
#     print(i)


# i=0
# tamanio=len (numeros)
# print (tamanio) 
# i=0
# while i<=len(numeros)-1:
#     print(numeros[i]) 
#     i+=1
 

# palabras=["hola,saludos, america, azul"] 
# palabras_buscar=input("Ingresa una palabra a buscar :")

# for i in palabras:
#   if i==palabras_buscar:
#      print(f"se encontro la palabra a buscar en la posicion {palabras.index}")



# numeros[23,34,23]
# print(numeros)

# #agregar un elemento
# numeros.append(100)
# print(numeros)
# numeros.insert(3,200)
# print(numeros)

# #eliminar un elemento
# numeros.remove(100) # indicar el elemento a borrar 
# print(numeros)
# numeros.pop(2) #indicar la posicion del elemento a borrar
# print(numeros)

# i=0
# while i<len(palabras):
#     if palabras[i]==palabra_a_buscar:
#         print("a")
#Ejemplo 4 crar una lista multilnea(Matriz) para agregar los nombres y numeros telefonicos
# agenda=[
#     ["Carlos",61812344567] ,
#     ["Leo",6671234576],
#     ["Sebastian",6182341234],
#     ["Pedro",61712345678],
# ]

# print(agenda)

# for i in agenda:
#     print(f"{agenda.index(i)+1}{i}")
import os

from desde_otro_lado import *

def mostrar_menu():
    os.system("cls")
    print("\nMenu de opciones:")
    print("1.- Agregar pelicula")
    print("2.- Eliminar pelicula")
    print("3.- Consultar peliculas")
    print("4.- Actualizar peliculas")
    print("5.- Salir")

peliculas = []
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        agregar_pelicula(peliculas)
    elif opcion == '2':
        eliminar_pelicula(peliculas)
    elif opcion == '3':
        consultar_peliculas(peliculas)
    elif opcion == '4':
        actualizar_peliculas(peliculas)
    elif opcion == '5':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")
