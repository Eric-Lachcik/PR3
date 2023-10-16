import math


A = int(input("A: "))

if A <= 0:
    print("Error 404")
else:
    pot = A **2
    rz = math.sqrt(A) 
    print("La potencia es ", pot,"y la raiz cuadrada es", rz)