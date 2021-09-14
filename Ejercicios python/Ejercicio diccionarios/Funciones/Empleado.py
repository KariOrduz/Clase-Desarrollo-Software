class Empleado:
    #ATRIBUTOS
    mombre = ""
    edad = 0
    cargo = ""
    salario = 0

    #METODOS
    def __init__(self, nombre, edad, cargo, salario):
        #Inicializador de atributos
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo
        self.salario = salario

    def asenso(self, cargo, salario):
        self.cargo = cargo
        self.salario = salario
        
    def imprimir (self):
        print(self.nombre + " tiene " + str(self.edad) + " años. Tiene el cargo de " + self.cargo + " y gana $" + str(self.salario))

Pedro = Empleado("Pedro Pérez", 30, "Administrador", 2000000)
Pedro.asenso("Gerente", 5000000)
Pedro.imprimir()        