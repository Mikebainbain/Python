# definicion de funciones en python 



def sumar():
    num1 = int(input("Ingresa el primer numero \n"))
    num2 = int(input("Ingresa el segundo numero \n"))

    resultado = num1 + num2
    print("El numero es \n"+str(resultado))

sumar()


# con argumentos 

def restar(num3,num4):
    resta = num3 - num4
    return resta

for i in range(2):
    num3 = int(input("iNGRESA EL PRIMER NUMERO \n"))
    num4 = int(input("INGRESA EL SEGUNDO NUMERO \n"))
    resultado = restar(num3,num4)
    print("El resultado de la resta es "+ str(resultado))

# Para ahorrar lineas d ecodigo podemos hacer de la siguiente forma 

"""""""""
for i in range(2):
    num3 = int(input("iNGRESA EL PRIMER NUMERO \n"))
    num4 = int(input("INGRESA EL SEGUNDO NUMERO \n"))
    print("El resultado de la resta es "+ str(restar(num3,num4)))

"""""""""