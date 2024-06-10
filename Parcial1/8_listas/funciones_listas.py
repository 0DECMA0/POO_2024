paise=["Mexico","USA","Brasil","Japon"]
numero=[23,100,3.1416,0.100]
varios=["Hola",True,100,10.22]

#Ordenar la lista 

print(paise)
paise.sort() #Funcion para ordenarlos de manera decendente 
print(paise) 

print(numero)
numero.sort() #No se puede hacer listas de varios 
print(numero) 

#Agregar elementos a la lista
print(numero)
numero.insert(len(numero),100)
print(numero)
numero.append(100)

#Eliminar elementos a la lista
print(numero)
numero.pop(2) #Las funciones pop tienen que ser enteros
print(numero)
numero.remove(100) #Remove elimina todos los vales que tenga asignados

#Buscar dento de una lista
encontrar="Brasil" in paise
print(encontrar) 

#Dar la vuelta
print(varios)
varios.reverse()
print(varios)

#Unir listas 
print(paise)
paise.extend(numero)
print(paise)

#Vaciar una lista
print(varios)
varios.clear()
print(varios
      )

