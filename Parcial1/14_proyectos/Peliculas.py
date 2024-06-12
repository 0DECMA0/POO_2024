import os
import time
from desde_otro_lado import *

def mostrar_menu():
    os.system("cls")
    print("\nMenu de opciones:")
    print("1.- Agregar pelicula")
    print("2.- Eliminar pelicula")
    print("3.- Consultar peliculas")
    print("4.- Actualizar peliculas")
    print("5.- Vaciar peliculas")
    print("6.- Salir")

peliculas = []
while True:
    time.sleep(2)
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
        vaciar_peliculas(peliculas)
    elif opcion == '6':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")

