A = int(input("Introduce el dia:"))
B = int(input("Introduce el mes:"))

if 1 <= A <= 31:
        if A > 0: 
            print("Dia correcto")
        else:
         print("Dia incorrecto")
        if 1 <=  B <= 12:
            if B > 0:
                 print("Mes correcto")
                 print("La es fecha introducida es ",A , "del",B ,"del 2023")
            else:
                 print("Mes incorrecto")
        else:("Mes incorrecto")
else:
     print("Dia incorrecto")