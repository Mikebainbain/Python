"""
En este archivo elaboramos un 
    -input que solicita datos al usuario final  almacenando el valor que teclee en una variable 
    -los saltos de linea
    -Python interpreta los los valores como tipo de dato string por lo que es necesario hacer su conversion al hacer la operacion
    -Asi como en otros lenguajes no es posible concatenar numeros con letras por lo que los numeros se convierten en string
         para concatenar es de la siguiente forma: print("El resultado de la multiplicacion es: \n"+ str(operacion))

"""
var=input("Por favor ingresa un valor \n")

operacion = int(var)+10

print("El resultado de la multiplicacion es: \n"+ str(operacion))

