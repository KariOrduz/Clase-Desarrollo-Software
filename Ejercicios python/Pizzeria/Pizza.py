class Topping:
    def __init__(self, nombre, precio, costo):
        self.nombre = nombre
        self.precio = precio
        self.costo = costo

class MasaBase:
    def __init__(self, tamaño, costo, sabor):
        self.tamaño = tamaño
        self.costo = costo
        self.sabor = sabor

    def descripcion(self):
        return "La masa base " + self.sabor + ", tiene un tamaño de " + str(self.tamaño) + " cms."

class Pizza(MasaBase):
    def __init__(self, tamaño, costoMB, sabor, nombre, precioVenta, toppings = []):
        super().__init__(tamaño, costoMB, sabor)

        self.nombre = nombre
        self.precio = precioVenta
        self.toppings = toppings
        self.costoFinal() #Calcula el costo final de la pizza

    def costoFinal(self):
        for topping in self.toppings:
            self.costo += topping.costo

    def utilidadBruta(self):
        #precio de venta - costo de pizza
        return self.precio - self.costo

    


#Toppings
tomate = Topping("Tomate", 100, 50)
queso = Topping("Queso", 400, 100)
salami = Topping("Salami", 800, 200)

#Pizza
pizzaSalami = Pizza(15, 500, "Integral", "Pizza de Salami Integral", 8000, [tomate, queso, salami])


print(pizzaSalami.costoFinal())
print(pizzaSalami.utilidadBruta())