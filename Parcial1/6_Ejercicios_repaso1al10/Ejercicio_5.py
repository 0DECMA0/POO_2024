#Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario

print("Ingresa el primer número:")
numero1 = int(input())

print("Ingresa el segundo número:")
numero2 = int(input())

if numero1 < numero2:
    for num in range(numero1 + 1, numero2):
        print(num)
elif numero1 > numero2:
    for num in range(numero2 + 1, numero1):
        print(num)
else:
    print("Los números son iguales, no hay números entre ellos.")

print(f"Números entre {numero1} y {numero2}:")
