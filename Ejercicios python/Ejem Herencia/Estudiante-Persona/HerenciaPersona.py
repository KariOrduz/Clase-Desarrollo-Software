class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def descripcion(self):
        return self.nombre + " " + self.apellido

class Estudiante(Persona):
    def __init__(self, nombre, apellido, IDEstudiantil, promedio = 0.0):
        #Inicializa el contructor de la clase 'Persona'
        super().__init__(nombre, apellido)

        print(self.nombre)
        print(super().descripcion())

Juan = Estudiante("Juan", "Plata", 2020202)
