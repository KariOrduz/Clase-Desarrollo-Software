class Calculadora:
    def suma(self, x=0, y=0, z=0):
        return x+y+z
    
    def mult(self, **kwargs):
        #kwargs --> Operador que convierte los argumentos de entrada, especificados por el usuario, en un diccionario
        print(kwargs)

    def div(self, *args):
        #args --> Operador que convierte los argumentos de entrafa en una lista
        args = [*args]
        print(args)

calc = Calculadora()
calc.mult(x = 5, y = 6)

calc.div(3, 4, 5)