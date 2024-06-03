
"""opcion=True
while opcion:
    print("\n \t Calculadora basica, \n Escoge una opcion \n 1-Suma \n 2-Resta \n 3-Multiplicacion \n 4-Divicion \n 5-Salir")
    opcion=input("\t Elige una opcion").upper()
    
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
        n1=int(input("Numero #1:"))
        n2=int(input("Numero #2:"))
        print(f"{n1}+{n2}={n1+n2}")
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        n1=int(input("Numero #1:"))
        n2=int(input("Numero #2:"))
        print(f"{n1}-{n2}={n1-n2}")
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
        n1=int(input("Numero #1:"))
        n2=int(input("Numero #2:"))
        print(f"{n1}*{n2}={n1*n2}")
    elif opcion=="4" or opcion=="/" or opcion=="DIVICION":
        n1=int(input("Numero #1:"))
        n2=int(input("Numero #2:"))
        print(f"{n1}/{n2}={n1/n2}")
    else
        print("Gracias , Terminaste la ejecucion del programa") 

def solicitarNumero():
    global n1,n2
    n1=int(input("Numero #1:"))
    n2=int(input("Numero #2:"))
    return n1,n2

def operacionAritmetica(num1,num2,opcion):
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
        return f"{n1}+{n2}={n1+n2}"
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        return f"{n1}-{n2}={n1-n2}"
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
        return f"{n1}*{n2}={n1*n2}"
    elif opcion=="4" or opcion=="/" or opcion=="DIVICION":
        return f"{n1}/{n2}={n1/n2}"
    else:
        opcion=False
        return "Gracias , Terminaste la ejecucion del programa"
opcion1=True
while opcion1:
    print("\n \t Calculadora basica, \n Escoge una opcion \n 1-Suma \n 2-Resta \n 3-Multiplicacion \n 4-Divicion \n 5-Salir")
    opcion1=input("\t Elige una opcion").upper()
    solicitarNumero()
    print(operacionAritmetica(n1,n2,opcion))
"""
def solicitarNumeros():
  global n1,n2  
  n1=int(input("Numero #1: "))
  n2=int(input("Numero #2: "))


def operacionAritmetica(num1,num2,opcion):  
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
      return f"{n1}+{n2}={n1+n2}"
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
     return f"{n1}-{n2}={n1-n2}"
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
     return f"{n1}*{n2}={n1*n2}"
    elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
     return f"{n1}/{n2}={n1/n2}"  
    
opcion=True    
while opcion :
 print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- SALIR ")
 opcion=input("\t Elige una opción: ").upper()
 if opcion !=5:
   solicitarNumeros()
   print(operacionAritmetica(n1,n2,opcion))
else:
  opcion=True    
  print("Terminaste la ejecucion del SW")


   
