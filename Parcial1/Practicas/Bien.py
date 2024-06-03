
#1 suma=n(n+1)2

na=int(input("¿Cuanto vale N?"))
suma=na*(na+1)/2
print("Tu suma es de los primeros numeros enteros des 1 hasta10",str(na),("es"), str(suma))

#2 Saca tu masa corporal


peso=int(input("Ingresa tu Peso"))
estatura=float(input("Ingresa tu Estatura"))

imc= round(float(peso/(estatura*estatura)),2)

print("Tu Masa Corporal es",imc)

#3 Cociente y resto
n = input("Introduce el dividendo (entero): ")
m = input("Introduce el divisor (entero): ")
print(n + " entre " +  m + " da un cociente " + str(int(n) // int(m)) + " y un resto " + str(int(n) % int(m)))