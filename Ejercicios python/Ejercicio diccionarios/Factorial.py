def factorial(x):
    #Objetivo: Retornan el factorial de un numero
    fact = x
    while x > 1:
        x -= 1
        fact *= x
    return fact

def y(x):
    
    return (x**2+5)/(2*factorial(x))

def factorial(x):
    if x == 1:
        return x
    elif x == 0:
        return 1
    elif x < 1:
        return "No existe el factorial de números negativos"
    else:
        return x*factorial(x-1)

print(y(4))
