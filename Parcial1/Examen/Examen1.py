#Examen 24/05/24

solicitud=0
nomb_tra=(input("¿Nombre del Trabajador?"))
hor_tra=float(input("¿Horas Trabajadas?"))
dias_tra=int(input("¿Dias Trabajados?"))
suel_hor=(int(input("¿Sueldo por Hora?")))
respuesta=(input("¿Desea Otra Capturar?"))
solicitud
if respuesta == 'si':
    nomb_tra=(input("¿Nombre del Trabajador?"))
    hor_tra=float(input("¿Horas Trabajadas?"))
    dias_tra=int(input("¿Dias Trabajados?"))
    suel_hor=(int(input("¿Sueldo por Hora?")))
    respuesta=(input("¿Desea Otra Capturar?"))
    solicitud+1

if respuesta== 'no':
    sueldo_sem=hor_tra*dias_tra*suel_hor
    sueldo_men=sueldo_sem*4
if sueldo_men <=10000:
    cat='A'
if sueldo_men >10000 <15000:
    cat='B'
if sueldo_men > 15000:
    cat='Sin categoria'
sueldo_to=sueldo_men*solicitud

print("Tu sueldo semanal es:",sueldo_sem,)
print(("Tu sueldo mensual es:",sueldo_men,"Eres obrero tipo:",cat))
print("El total de trabajadores es:",solicitud,"El total de todos los sueldo es:",sueldo_to)