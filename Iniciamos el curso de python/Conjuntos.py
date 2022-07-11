# Un conjunto es una coleccion desordenada de elementos que soporta operaciones matematicas avanzadas
# Se pueden elimiar valores repetidos de una lista coviertiendolo a conjunto y ese conjunto convertirlo alista con la funcion list 

conjunto = {1,2,3,4}
print(conjunto)

conjunto.add(0)   # Agrega un elemento a el conjunto y tambien ya lo acomoda en orden ascendente 
print(conjunto)

lista = [7,7,7,7,7,2,3,4,5,6,1]
print(lista)
conjunto2 = set(lista)  #Convierte la lista en un conjunto y lo ordena 
conjunto2.add(8)
print(conjunto2)

lista=list(conjunto2) # la variable lista para comprobar que el conjunto ya es una lista 
print(lista)

# Para ahorrar lineas de codigo 
lista2 = [7,7,7,8,8,8,8,9,9,9,'hola']
lista3 = list(set(lista2)) # Convierto la lista en conjunto, elimina elementos repetidos y nuevamente se convierte en lista
print(lista3)

# verificar si hay un elemento en un conjunto 
pert = 3 in lista3 # si hay algun 3
print(pert)
perte = 3 not in lista3 #si no hay algun 3
print(perte)

pert = 'hola' in lista3 # si hay algun hola
print(pert)
perte = 'hola' not in lista3 #si no hay algun hola
print(perte) 

cadena = "Hola estamos evaluando conjuntos"
cadena = set (cadena)
print(cadena)