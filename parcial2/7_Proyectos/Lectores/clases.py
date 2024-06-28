class Lectores:
    def __init__(self, nombre: str, direccion: str, telefono: int):
        self._nombre = nombre
        self._direccion = direccion
        self._telefono = telefono

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre: str):
        self._nombre = nombre

    def getDireccion(self):
        return self._direccion

    def setDireccion(self, direccion: str):
        self._direccion = direccion

    def getTelefono(self):
        return self._telefono

    def setTelefono(self, telefono: int):
        self._telefono = telefono

    def reserva(self, item: str):
        print(f"{self._nombre} ha reservado {item}.")

    def entregar(self, item: str):
        print(f"{self._nombre} ha entregado {item}.")

class Estudiantes(Lectores):
    def __init__(self, nombre: str, direccion: str, telefono: int, carrera: str, matricula: int):
        super().__init__(nombre, direccion, telefono)
        self._carrera = carrera
        self._matricula = matricula

    def getCarrera(self):
        return self._carrera

    def setCarrera(self, carrera: str):
        self._carrera = carrera

    def getMatricula(self):
        return self._matricula

    def setMatricula(self, matricula: int):
        self._matricula = matricula

    def reserva(self, item: str):
        super().reserva(item)
        print(f"Estudiante con matrícula {self._matricula} ha reservado {item}.")

    def entregar(self, item: str):
        super().entregar(item)
        print(f"Estudiante con matrícula {self._matricula} ha entregado {item}.")

class Docentes(Lectores):
    def __init__(self, nombre: str, direccion: str, telefono: int, modalidad: str, num_empleado: int):
        super().__init__(nombre, direccion, telefono)
        self._modalidad = modalidad
        self._num_empleado = num_empleado

    def getModalidad(self):
        return self._modalidad

    def setModalidad(self, modalidad: str):
        self._modalidad = modalidad

    def getNumEmpleado(self):
        return self._num_empleado

    def setNumEmpleado(self, num_empleado: int):
        self._num_empleado = num_empleado

    def reserva(self, item: str):
        super().reserva(item)
        print(f"Docente con número de empleado {self._num_empleado} ha reservado {item}.")

    def entregar(self, item: str):
        super().entregar(item)
        print(f"Docente con número de empleado {self._num_empleado} ha entregado {item}.")


estudiante1 = Estudiantes("Ana Torres Guzman", "Col.centro 1500 ote", 618123456, "Meca", 2335678)
docente1 = Docentes("Daniel Fuentes Loera", "Fracc.D.Arrieta 1400 nte", 6183335678, "TI", 123)
