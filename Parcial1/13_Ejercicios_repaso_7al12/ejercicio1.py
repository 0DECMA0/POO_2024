# 1.-Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado

lista_numeros = [5, 12, 3, 7, 9, 14, 1, 8]

print("Lista:")
for numero in lista_numeros:
    print(numero)

def lista_a_string(lista):
    return ','.join(map(str, lista))

resultado = lista_a_string(lista_numeros)
print(f"Lista como string: {resultado}")

lista_ordenada = sorted(lista_numeros)
print("\nLista ordenada:")
print(lista_ordenada)

longitud = len(lista_numeros)
print("\nLongitud de la lista:")
print(longitud)

elemento_a_buscar = int(input("\nIntroduzca el número a buscar: "))

if elemento_a_buscar in lista_numeros:
    print(f"El número {elemento_a_buscar} Se encuentra en la lista.")
else:
    print(f"El número {elemento_a_buscar} NO se encuentra en la lista.")
