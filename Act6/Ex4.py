print("Introduce una secuencia de numeros:")

A = int(input(""))
x = 1
suma = 0

while x <= A:
    print("Ingresa el siguiente el numero", x)
    n = int(input(""))
    suma = suma + n
    x = x + 1

media = suma/A
print("La media aritmetica es", media)