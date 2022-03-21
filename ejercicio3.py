#menu de opciones

opcion=1 
i = 1 
numeros = []

print('Menu principal')
print("1. Digite 5 numeros enteros: ")
print("2. Sumar los 2 numeros ingresados: ")
print("3. Agregar un nuevo numero : ")
print("4. Salir")



while(opcion !=4):
    opcion=int(input("Bienvenido, Digita una opción : "))
    if(opcion ==1):
        while (i <=5):
            numero = int(input('Digite un numero entero: ' ))
            numeros.append(numero)
            print(numeros)
            i +=1
    elif(opcion == 2):
       suma =sum(numeros)
       print(f'EL resultado de la suma es : {suma}')
    elif(opcion == 3):
       numero = int(input('Digite un numero nuevo: '))
       numeros.append(numero)
       print(numeros)
    elif(opcion == 4):
        print("Saliendo del menu principal")
    else:
        print("Digite un opcion valida")
        break 

else:
    print("Saliste del programa")
