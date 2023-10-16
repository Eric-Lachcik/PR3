
A = input("Escriba la contraseña:")
D = 2


if A == "Eureka":
        print("Contraseña correcta")
else:
        while D > 0:
                print("Contraseña incorrecta")
                D = D - 1
                A = input("Intente lo otra vez:")
        if D == 0:
                print("Contraseña incorrecta,reincia para continuar")
 #Este Eureka si que podria hacerlo 20 veces       