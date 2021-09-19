#%matplotlib inline
from math import pi
#import matplotlib.pyplot as plt

#-------------POLIMORFISMO------------
#cLASE PADRE
class FiguraGeometrica:
    dimensiones = []
    ubicacionEspacial = [0,0]
    #fig, ax = plt.subplots()

    def Area(self):
        return None

    def Perimetro(self):
        return None

#CLASES HIJAS
class Circulo (FiguraGeometrica):
    def __init__(self, radio, ubicacion =[0,0]):
        self.dimensiones.append(radio)
        self.ubicacionEspacial = ubicacion

    def Area(self):
        return pi*self.dimensiones[0]**2

    def Perimetro(self):
        return 2*pi*self.dimensiones[0]

class Rectangulo (FiguraGeometrica):
    def __init__(self, b, h, ubicacion=[0,0]):
        self.dimensiones.append(b)
        self.dimensiones.append(h)
        self.ubicacionEspacial = ubicacion

    def Area(self):
        return self.dimensiones[0]*self.dimensiones[1]

    def Perimetro(self):
        return 2*(self.dimensiones[0]+self.dimensiones[1])

#-----------CREACION DE FIGURAS----------
cir1 = Circulo(0.2)
cir2 = Circulo(0.4, [0.6,0])
rec1 = Rectangulo(3,4)

print("Círculo de radio " + str(cir1.dimensiones[0]) + " tiene un área de " + str(cir1.Area()))
print("Rectángulo de " + str(rec1.dimensiones[0]) + " de base por " + str(rec1.dimensiones[1]) + " de altura tiene un área de " + str(rec1.Area()))
