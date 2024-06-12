#2.- Escribir un programa  que añada valores a una lista mientras que su longitud sea menor a 120, y luego mostrar la lista: Usar un while y for


lista_while = []
contador = 0

while len(lista_while) < 120:
    lista_while.append(contador)
    contador += 1

print("Lista generada con bucle while:")
print(lista_while)



lista_for = []

for i in range(120):
    lista_for.append(i)

print("\nLista generada con bucle for:")
print(lista_for)
