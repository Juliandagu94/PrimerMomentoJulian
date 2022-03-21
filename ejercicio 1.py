contador = 1
multiplo_2 = 0
multiplo_3 = 0

while (contador <= 5):
    numero = int (input('digite un numero entero: '))
    if (numero % 2 == 0):
        multiplo_2 += 1
    elif(numero % 3==0):
        multiplo_3 += 1
    contador +=1

print(f'los numero que ingreso que son multiplos de 2 son: {multiplo_2}')
print(f'los numero que ingreso que son multiplos de 3 son: {multiplo_3}')
