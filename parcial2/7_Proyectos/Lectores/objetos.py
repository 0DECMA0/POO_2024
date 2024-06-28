from clases import * 

print(f"Nombre del estudiante: {estudiante1.getNombre()}, Carrera: {estudiante1.getCarrera()}, Matrícula: {estudiante1.getMatricula()}")
print(f"Nombre del docente: {docente1.getNombre()}, Modalidad: {docente1.getModalidad()}, Número de Empleado: {docente1.getNumEmpleado()}")

# Llamar a los métodos
estudiante1.reserva("Libro de Matemáticas")
estudiante1.entregar("Libro de Matemáticas")


docente1.reserva("Proyector")
docente1.entregar("Proyector")
