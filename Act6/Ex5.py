maximo = 0
minimo = 0
suma = 0
i = 1

while True:
    B = int(input('Ingrese un numero: '))
    
    if B == 0:
        break
    
    if i <= B and B != 0:
        maximo = B
        minimo = B
    else:
        if B > maximo:
            maximo = B
        if B < minimo:
            minimo = B
    
    i += 1
    suma += B

if i > 1:
    media = suma / (i - 1)
    print('El numero maximo es:', maximo)
    print('El numero minimo es:', minimo)
    print('La media aritmetica es:', media)
else:
    print('No se ingresaron numeros validos.')
