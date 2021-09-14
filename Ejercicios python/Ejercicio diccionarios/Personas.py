producto = {
    'Martillo' : 1000,
    'Destornillador' : 5000,
    'Arandelas' : 100,
    'Tuercas' : 50,
    'Pernos' : 200,
}


personas = {
    'Julian Florez' : {"Tipo documento" : "C.C.", "Número" : "1.098.880.330"},
    'Oscar Giraldo' : {"Tipo documento" : "T.I.", "Número" : "1.100.880.330"},
    'Andrea Juarez' : {"Tipo documento" : "C.C.", "Número" : "1.098.870.330"},
    'Jorge Ivan López' : {"Tipo documento" : "C.C.", "Número" : "1.098.860.331"},
    'Javier Florez' : {"Tipo documento" : "T.I.", "Número" : "1.098.880.000"},
    'Sara López' : {"Tipo documento" : "C.C.", "Número" : "1.098.980.330"},
}

#Ejemplo
#¿Quién es mayor y quién es menor de edad?

for persona in personas:
    #key = persona
    #print(persona, personas[persona]["Tipo documento"])
    if personas[persona]["Tipo documento"] == "C.C.":
        print (persona + " es mayor de edad")
    else:
        print(persona + " es menor de edad")
        