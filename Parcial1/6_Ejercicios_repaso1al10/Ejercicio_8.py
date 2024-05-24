#Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?

print("Ingresa el porcentaje :")
porcentaje = float(input())
print("Ingresa el número:")
numero = float(input())
resultado = (porcentaje / 100) * numero
print(f"{porcentaje}% de {numero} es {resultado}")
