#4.-Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones


mi_lista = [1, 2, 3]
mi_cadena = "Hola, mundo!"
mi_entero = 42
mi_logico = True

def imprimir_tipo(variable):
    if isinstance(variable, list):
        print("La variable es una lista.")
    elif isinstance(variable, str):
        print("La variable es una cadena.")
    elif isinstance(variable, int):
        print("La variable es un entero.")
    elif isinstance(variable, bool):
        print("La variable es un booleano.")
    else:
        print("Tipo de variable desconocido.")

imprimir_tipo(mi_lista)
imprimir_tipo(mi_cadena)
imprimir_tipo(mi_entero)
imprimir_tipo(mi_logico)
