
A = input("Escriba la contraseña:")

if A == "Eureka":
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta faltan 2 intentos")
    B = input("Escriba la contraseña:")
    if B == "Eureka":
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta falta un intento")
        C = input("Escriba la contraseña:")
        if C == "Eureka":
            print("Contraseña incorrecta")
        else:
            print("Contraseña incorrecta, reinicie para volver a intentar")