A = int(input("Introduce el dia:"))
B = int(input("Introduce el mes:"))

if 1 <= A <= 31:
         
            print("Dia correcto")
else:
         print("Dia incorrecto")
if 1 <=  B <= 12:           
     print("Mes correcto")     
else:
     print("Mes incorrecto")  
if 1 <= A <= 31 and 1 <=  B <= 12:
        print("La fecha introducida es el ", A , "de", B ,"del 2023")
