class Colegio:
    estudiantes = []
    def __init__(self, nombre, ubicacion, estudiantes=[]):
        #Inicializar atributos
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.estudiantes = []

    def removerEstudiante(self, estudiante):
        self.estudiantes.remove(estudiante)

    def añadirEstudiante(self, estudiante):
        self.estudiantes.append(estudiante)

#CREACION DE COLEGIOS
SanPedro = Colegio("San Pedro", "Cll 45 - Bucaramanga")
LaPresentacion = Colegio("La Presentacion", "Cll 54 - Bucaramanga")


