# Programa para averiguar si un numero es par o imprar y si es positivo o negativo

numero =int(input("Ingresa un numero\n"))

if numero%2 == 0:
    if numero > 0:
        print("El numero es par, por lo tanto divisible entre 2 tambien el numero es positivo ")
    else:
        print("El numero es par pero es negativo")
else:
    if numero >0:
        print("el numero es impar, no divisible entre 2  tambien el numero es positivo")
    else:
        print("El numeroes impar y es negativo")
