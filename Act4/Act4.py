A = input("A: ")
B = input("B: ")
C = input("C: ")

mayor = 0

if A > B and A > C:
    mayor = A
else:
    if B > C:
        mayor = B
    else:
        mayor = C
    

print("El numero mayor es ",mayor)
