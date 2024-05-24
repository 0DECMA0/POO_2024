#Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron

aprobados = 0
no_aprobados = 0

for i in range(1, 16):
    calificacion = float(input(f"Ingrese la calificación del alumno {i}: "))
    if calificacion >= 80:
        aprobados += 1
    else:
        no_aprobados += 1

print(f"\nAlumnos que aprobaron: {aprobados}")
print(f"Alumnos que no aprobaron: {no_aprobados}")