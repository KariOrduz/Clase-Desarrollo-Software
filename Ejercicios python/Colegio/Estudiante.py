class Estudiante:
    def __init__(self, nombre, edad, grado, promedio =0.0):
        #Inicializar atributos
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self._promedio = promedio

    def promedio(self, notas):
        self._promedio = sum(notas)/len(notas)
        return self._promedio

Jose = Estudiante("Jose Miguel", 14, 8)
Anna = Estudiante("Ana María", 12, 10)

print(Jose.promedio([4, 5, 3]))
print(Anna.promedio([2, 3, 1]))