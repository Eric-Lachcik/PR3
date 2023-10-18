
A = input("Escriba la contraseña:")
D = 2
if A == "Eureka":
        print("Contraseña correcta")
else:
        while D > 0 and A != "Eureka":
                print("Contraseña incorrecta")
                D = D - 1
                A = input("Intente lo otra vez:")
                if A == "Eureka":
                        print("Contraseña correcta")
        if D == 0 and A != "Eureka":
                print("Contraseña incorrecta,reincia para continuar")
#Ahora si puedo hacer la contraseña en 20 intentos si quiero