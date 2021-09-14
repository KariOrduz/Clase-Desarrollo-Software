class Persona :
    #Atributos
    nombre = ""
    edad = 0
    estatura = 0

    '''def Informacion(self, nombre, edad, estatura):       
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
         #self en python == this en java
Jhon = Persona()

Jhon.Informacion ("Jhon Alexander Pérez", 20, 1.78)'''

    def __init__(self, nombre, edad,  estatura):            #Costructor de lo atributos
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
Mario = Persona("Mario Pérez", 20, 1.78)

print(Mario.nombre, Mario.edad)
