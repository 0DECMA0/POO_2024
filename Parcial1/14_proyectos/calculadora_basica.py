
# opcion=True
# while opcion:
#     print("\n \t Calculadora basica, \n Escoge una opcion \n 1-Suma \n 2-Resta \n 3-Multiplicacion \n 4-Divicion \n 5-Salir")
#     opcion=input("\t Elige una opcion").upper()
    
#     if opcion=="1" or opcion=="+" or opcion=="SUMA":
#         n1=int(input("Numero #1:"))
#         n2=int(input("Numero #2:"))
#         print(f"{n1}+{n2}={n1+n2}")
#     elif opcion=="2" or opcion=="-" or opcion=="RESTA":
#         n1=int(input("Numero #1:"))
#         n2=int(input("Numero #2:"))
#         print(f"{n1}-{n2}={n1-n2}")
#     elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
#         n1=int(input("Numero #1:"))
#         n2=int(input("Numero #2:"))
#         print(f"{n1}*{n2}={n1*n2}")
#     elif opcion=="4" or opcion=="/" or opcion=="DIVICION":
#         n1=int(input("Numero #1:"))
#         n2=int(input("Numero #2:"))
#         print(f"{n1}/{n2}={n1/n2}")
#     else
#         print("Gracias , Terminaste la ejecucion del programa") 

# def solicitarNumero():
#     global n1,n2
#     n1=int(input("Numero #1:"))
#     n2=int(input("Numero #2:"))
#     return n1,n2

# def operacionAritmetica(num1,num2,opcion):
#     if opcion=="1" or opcion=="+" or opcion=="SUMA":
#         return f"{n1}+{n2}={n1+n2}"
#     elif opcion=="2" or opcion=="-" or opcion=="RESTA":
#         return f"{n1}-{n2}={n1-n2}"
#     elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
#         return f"{n1}*{n2}={n1*n2}"
#     elif opcion=="4" or opcion=="/" or opcion=="DIVICION":
#         return f"{n1}/{n2}={n1/n2}"
#     else:
#         opcion=False
#         return "Gracias , Terminaste la ejecucion del programa"
# opcion1=True
# while opcion1:
#     print("\n \t Calculadora basica, \n Escoge una opcion \n 1-Suma \n 2-Resta \n 3-Multiplicacion \n 4-Divicion \n 5-Salir")
#     opcion1=input("\t Elige una opcion").upper()
#     solicitarNumero()
#     print(operacionAritmetica(n1,n2,opcion))

# import os
# def solicitarNumeros():
#   global n1,n2  
#   n1=int(input("Numero #1: "))
#   n2=int(input("Numero #2: "))


# def operacionAritmetica(num1,num2,opcion):  
#     if opcion=="1" or opcion=="+" or opcion=="SUMA":
#       return f"{n1}+{n2}={n1+n2}"
#     elif opcion=="2" or opcion=="-" or opcion=="RESTA":
#      return f"{n1}-{n2}={n1-n2}"
#     elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
#      return f"{n1}*{n2}={n1*n2}"
#     elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
#      return f"{n1}/{n2}={n1/n2}"  
# os.system("clear")
# opcion=True    
# while opcion :
#  print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- SALIR ")
#  opcion=input("\t Elige una opción: ").upper()
#  if opcion !="5":
#    solicitarNumeros()
#    print(operacionAritmetica(n1,n2,opcion))
# else:
#   opcion=False
#   print("Terminaste la ejecucion del SW")



# import os
# from Otras_Funciones import esperarYContinuar,operacionAritmetica
# #from Otras_Funciones import * "Te taes todos los archivos"

# def solicitarNumeros():
#     global n1, n2  
#     n1 = int(input("Numero #1: "))
#     n2 = int(input("Numero #2: "))


# def operacionAritmetica(num1, num2, opcion):  
#     if opcion == "1" or opcion == "+" or opcion == "SUMA":
#         return f"{n1} + {n2} = {n1 + n2}"
#     elif opcion == "2" or opcion == "-" or opcion == "RESTA":
#         return f"{n1} - {n2} = {n1 - n2}"
#     elif opcion == "3" or opcion == "*" or opcion == "MULTIPLICACION":
#         return f"{n1} * {n2} = {n1 * n2}"
#     elif opcion == "4" or opcion == "/" or opcion == "DIVISION":
#         return f"{n1} / {n2} = {n1 / n2}"

# def esperarYContinuar():
#     input("\nPresiona Enter para continuar...")

# opcion = True    
# while opcion:
#     os.system("clear")
#     print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- SALIR ")
#     opcion = input("\t Elige una opción: ").upper()
#     if opcion != "5":
        
#         n1,n2=solicitarNumeros()
#         print(operacionAritmetica(n1 ,n2 ,opcion))
#         esperarYContinuar()
#     else:
#         opcion = False
#         print("Terminaste la ejecucion del SW")

   

import os
import math  # Import the math module for square root function

def solicitarNumeros():
    global n1, n2  
    n1 = float(input("Numero #1: "))  # Changed int to float to handle decimal division
    n2 = float(input("Numero #2: "))  # Changed int to float to handle decimal division
    return n1, n2

def operacionAritmetica(n1, n2, opcion):  
    if opcion == "1" or opcion == "+" or opcion == "SUMA":
        return f"{n1} + {n2} = {n1 + n2}"
    elif opcion == "2" or opcion == "-" or opcion == "RESTA":
        return f"{n1} - {n2} = {n1 - n2}"
    elif opcion == "3" or opcion == "*" or opcion == "MULTIPLICACION":
        return f"{n1} * {n2} = {n1 * n2}"
    elif opcion == "4" or opcion == "/" or opcion == "DIVISION":
        if n2 == 0:
            return "No se puede dividir por cero."
        else:
            return f"{n1} / {n2} = {n1 / n2}"
    elif opcion == "5" or opcion == "POTENCIA":
        return f"{n1} ^ {n2} = {n1 ** n2}"
    elif opcion == "6" or opcion == "RAIZ":
        if n1 < 0:
            return "No se puede calcular la raíz cuadrada de un número negativo."
        else:
            return f"Raíz cuadrada de {n1} = {math.sqrt(n1)}"
    elif opcion == "7" or opcion.upper() == "SALIR":
        return "Salir"
    else:
        return "Opción no válida"

opcion = True
while opcion:
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
    print("\n\t..:: CALCULADORA BÁSICA ::..\n 1.- Suma \n 2.- Resta\n 3.- Multiplicación\n 4.- División\n 5.- Potencia\n 6.- Raíz Cuadrada\n 7.- SALIR") 
    opcion = input("\tElige una opción: ").strip().upper()

    if opcion in ["1", "2", "3", "4", "5", "6"]:
        solicitarNumeros()
        print(operacionAritmetica(n1, n2, opcion))
        input("Presiona Enter para continuar...")
    elif opcion == "7" or opcion.upper() == "SALIR":
        print("Terminaste la ejecución del programa.")
        opcion = False
    else:
        print("Opción no válida. Introduce un número del 1 al 7.")
        input("Presiona Enter para continuar...")


import os
import math

def solicitarNumeros():
    global n1, n2  
    n1 = float(input("Numero #1: "))  
    n2 = float(input("Numero #2: ")) 
    return n1, n2

def operacionAritmetica(n1, n2, opcion):  
    if opcion == "1" or opcion == "+" or opcion == "SUMA":
        return f"{n1} + {n2} = {n1 + n2}"
    elif opcion == "2" or opcion == "-" or opcion == "RESTA":
        return f"{n1} - {n2} = {n1 - n2}"
    elif opcion == "3" or opcion == "*" or opcion == "MULTIPLICACION":
        return f"{n1} * {n2} = {n1 * n2}"
    elif opcion == "4" or opcion == "/" or opcion == "DIVISION":
        if n2 == 0:
            return "No se puede dividir por cero."
        else:
            return f"{n1} / {n2} = {n1 / n2}"
    elif opcion == "5" or opcion == "POTENCIA":
        return f"{n1} ^ {n2} = {n1 ** n2}"
    elif opcion == "6" or opcion == "RAIZ":
        if n1 < 0:
            return "No se puede calcular la raíz cuadrada de un número negativo."
        else:
            return f"Raíz cuadrada de {n1} = {math.sqrt(n1)}"
    elif opcion == "7" or opcion.upper() == "SALIR":
        return "Salir"
    else:
        return "Opción no válida"

opcion = True
while opcion:
    os.system('cls' if os.name == 'nt' else 'clear')  
    print("\n\t..:: CALCULADORA BÁSICA ::..\n 1.- Suma \n 2.- Resta\n 3.- Multiplicación\n 4.- División\n 5.- Potencia\n 6.- Raíz Cuadrada\n 7.- SALIR") 
    opcion = input("\tElige una opción: ").strip().upper()

    if opcion in ["1", "2", "3", "4", "5", "6"]:
        solicitarNumeros()
        print(operacionAritmetica(n1, n2, opcion))
        input("Presiona Enter para continuar...")
    elif opcion == "7" or opcion.upper() == "SALIR":
        print("Terminaste la ejecución del programa.")
        opcion = False
    else:
        print("Opción no válida. Introduce un número del 1 al 7.")
        input("Presiona Enter para continuar...")