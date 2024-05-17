#Convertir los tipos de datos

#Nota: solo es posile en una cocatenacion concatena entre tipo de datos iguales

texto="Soy una cadena"
numero=23


print(texto+" Y soy una cadena 2")
print(numero+34)

#Convertir un tipo de dato int a str
numero_str=str(numero)
print(texto+ numero_str)

#Como se debe de usar comunmente 
print(texto+""+str(numero))

#Convertit un STR a INT

n1=33
suma=int('23')+n1
print("suma:"+str(suma))

#Convertit un float a int
n1=33
n2=int(33.99)

suma=n1+n2
print(suma)

#cONVERTIR UN INT A FLOAT

n1=3
n2=4

suma=float(n1+n2)

print(f"La suma es: {suma}")
