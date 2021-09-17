```
import math 
class Circulo:
  radio = 0

  def __init__(self, radio):
    self.radio = radio

  def area(self):
    a = math.pi * self.radio ** 2
    print("Area= " + str(a))

  def perimetro(self):
    p = 2 * math.pi * self.radio
    print("Perimetro= " + str(p))

calcular = Circulo(6)
calcular.area()
calcular.perimetro()
```
