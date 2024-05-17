#Formas de cintatenar en python

nombre="Miguel Delgado"
especialidad="Area de SW Multiplataforma"
carrera="Ingeneria en Gestion y desarrollo de SW"

#Primer forma
print("Mi nombre es "+nombre+" estoy en la especialidad de "+especialidad+" y estudio la carrera de "+carrera)

print("\n")

#Seguna Forma 
print("Mi nombre es ",nombre," estoy en la especialidad de ",especialidad," y estudio la carrera de ",carrera)

print("\n")

#Tercera forma y la mas comun
print(f"Mi nombre es ,{nombre}, estoy en la especialidad de ,{especialidad}, y estudio la carrera de ,{carrera}")

print("\n")

#Cuarta forma y la mas comun
print("Mi nombre es ,{}, estoy en la especialidad de ,{}, y estudio la carrera de ,{}",format(nombre,especialidad,carrera))

print("\n")