#El for es una estructura de control repetitiva o ciclica que funciona con iteraciones x veces de acuerdo a los valores numericos enteros que contenga 

#sintaxis:
# for variable in elemento_literable(list, range etc);
#bloqueo untrucciones

#Ejemplo 1 Crear un programa que imprima 5 veces el caracter @

for contador in range(1,6):
    print("@")


    
#Ejemplo 2 Crear un programa que imprima los numeros del 1 al 5 , los sume e imprima la suma al final 

suma=0
for contador in range(1,6):
    print(contador)
    suma+=contador
print(f"La suma es:{suma}")


#Ejemplo 3 crear un programa que solicite un numero entero y apartir de este numero genere e imprima la tabla de multiplicar correspondiente

numero=int(input("Ingrese un numero:"))

multi=0
for i in range(1,11):
    multi=numero*i
    print(f"{numero} x {i} = {multi}")
