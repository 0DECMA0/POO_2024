#Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

print("Ingresa el primer número:")
numero1 = int(input())

print("Ingresa el segundo número:")
numero2 = int(input())

print(f"Números impares entre {numero1} y {numero2}:")

if numero1 < numero2:
    for num in range(numero1 + 1, numero2):
        if num % 2 != 0:
            print(num)
elif numero1 > numero2:
    for num in range(numero2 + 1, numero1):
        if num % 2 != 0:
            print(num)
else:
    print("Los números son iguales, no hay números entre ellos.")


