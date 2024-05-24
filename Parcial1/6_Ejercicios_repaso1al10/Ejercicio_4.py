#Solicitar 2 numeros al usuario
# y realizar todas las operaciones
# basicas de una calculadora (+,-,*,/)
# y mostrar por pantalla el resultado
 
print("Ingresa el primer numero")
num1=float(input())

print("Ingresa el segundo numero")
num2=float(input())

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 

print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division}")
