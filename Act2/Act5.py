A = int(input("Introduzca un numero para calcular su factorial:"))


def factorial(A):
    if A == 0 or A == 1:
                resultado=1
                
    elif A>1:
            resultado=A*factorial(A-1)
            
    return resultado
ress=factorial(A)
print("El factorial de tu numero es", ress)