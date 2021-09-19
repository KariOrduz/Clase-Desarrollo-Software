class Persona:
    def __init__(self, nombre = "", edad = 0 ):
        self.nombre = nombre
        self.edad = edad

    def descripcion(self):
        return self.nombre + ", " + str(self.edad)

class Usuario(Persona):
    def __init__(self,nombre, edad ,usuario = "", contraseña = ""):
        super().__init__(nombre, edad)
        self.usuario = usuario
        self.contraseña = contraseña

    def cambiarContra(self, nuevaContra):
        self.contraseña = nuevaContra

    def descripcion(self):
        return super().descripcion() + ", " + self.usuario + ", " + self.contraseña
        #return self.usuario + ", " + self.contraseña

juan = Usuario("Juan", 38, "jun", "123456")
print(juan.nombre)

u1 = Usuario("Pedro", 20, "pepe", "123")
print(u1.descripcion())