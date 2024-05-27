contador=0
rep='si'
while rep =='si' :
    peso=int(input("Ingresa tu Peso"))
    estatura=float(input("Ingresa tu Estatura"))
    imca= round(float(peso/(estatura*estatura)),2)
    rep=input("Deseas repetir")
    contador+contador

if imca <18.5:
    ps="Peso inferior al normal"
if imca >18.5 <25 :
    ps="Peso Normal"
if imca >24.9 <30:
    ps="Peso superior al normal"
if imca >30:
    ps="Obesidad"
print(ps,contador)


