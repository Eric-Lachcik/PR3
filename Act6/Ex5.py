max_value = 0
min_value = 0
suma = 0
i = 1

while True:
    B = int(input('Ingrese un número: '))
    
    if B == 0:
        break
    
    if i <= B and B != 0:
        max_value = B
        min_value = B
    else:
        if B > max_value:
            max_value = B
        if B < min_value:
            min_value = B
    
    i += 1
    suma += B

if i > 1:
    media = suma / (i - 1)
    print('El número máximo es:', max_value)
    print('El número mínimo es:', min_value)
    print('La media aritmética es:', media)
else:
    print('No se ingresaron números válidos.')
