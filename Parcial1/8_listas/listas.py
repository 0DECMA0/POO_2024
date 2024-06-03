"""
list(Array)
Son coleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico
Nota sus valores si son modificables

las lista es una coleccion ordenada y modificale permite miembros duplicados

"""

#Ejemplo 1 crear una lista de numeros e imprimir el contenido 

numero=[23,34]
print(numero)

#Recorrer la lista con for 
for i in numero:
    print(i)

#Recorrer la lista con un ciclo while 

#Ejemplo 2 crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 

palabras=["","Hola","Como","Estas","Ok"]
palabra_a_buscar=input("Ingresa la palabra a buscar: ")
indice = 0
encontrado = False
while indice < len(palabras):
    if palabras[indice] == palabra_a_buscar:
        print(f"Palabra '{palabra_a_buscar}' encontrada en el índice {indice}.")
        encontrado = True
        break  
    indice += 1

if not encontrado:
    print(f"Palabra '{palabra_a_buscar}' no encontrada en la lista.")
