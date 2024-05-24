#Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for


#while
print("Cuadrados de los 60 primeros números :")
i = 1
while i <= 60:
    print(f"{i}^2 = {i * i}")
    i += 1

#for
print("\nCuadrados de los 60 primeros números:")
for i in range(1, 61):
    print(f"{i}^2 = {i * i}")
    