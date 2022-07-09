# funciones tuple() y list()
lista = [10,20,30,40,50]
tupla = ('Hola' ,10, 'San')
lista2 = [1,2,3,'FaFa']

print("lista antes de la conversion \n"+ str(lista))

print("tupla antes de la conversion \n"+ str(tupla))


var1 = tuple(lista)

var2 = list(tupla)

print("lista despues de la conversion \n"+ str(var1))
print("tupla despues de la conversion \n"+ str(var2))

"""""""""

funciones para listas


"""""""""
lista.append(15) # Agrega el valor 15 en la lista
print(lista)
lista.insert(2,7) # inserta el valor 10 en la posicion 2
print(lista)
lista.remove(15) # Remueve el valor 15
print(lista)
lista.pop(0) # elimina el valor de una posicion
print(lista)
var3 = lista.count(30) # Cuenta cuantas veces se repite un valor dentro de la lista 
print("Hay "+str(var3)+" treinta en la lista")
lista.extend(lista2) # Une la lista 1 con la lista 2 
print(lista)
var4 = lista.copy() # Copia los valores de una lista a otra 
print(var4)
#lista.clear() # remueve todos los valores de una lista 
