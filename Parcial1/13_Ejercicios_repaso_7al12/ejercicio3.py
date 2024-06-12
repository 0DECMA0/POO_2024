# 3.-Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#  palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#  el contenido de la lista en mayusculas

def lista_vacia(lista):
    return len(lista) == 0

def llenar_lista(lista):
    while True:
        palabra = input("Ingrese una palabra o frase (o presione Enter para terminar): ")
        if palabra:
            lista.append(palabra)
        else:
            break

def imprimir_en_mayusculas(lista):
    for palabra in lista:
        print(palabra.upper())


mi_lista = []

if lista_vacia(mi_lista):
    print("La lista está vacía.")
    llenar_lista(mi_lista)

print("Contenido de la lista en mayúsculas:")
imprimir_en_mayusculas(mi_lista)
