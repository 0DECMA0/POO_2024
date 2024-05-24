# Hacer un programa que solicite numeros indefinidamente hasta que se introduzca el 111 y salir del programa1


print("Ingrese números. Para salir, introduzca 111.")

while True:
    numero = int(input("Ingrese un número: "))
    if numero == 111:
        print("¡Saliendo del programa!")
        break
    