# En este archivo veremos las listas(arreglos) en python

lista1 = [10,20,30,40]
print(lista1)

lista2 = ['Miguel', 'Angel', 50 ,True, 8.5]
print(lista2)





# colocar un arreglo dentro de otro arreglo 
        #  0     1
lista3 = [100,[101,200,300,400]]

#imprimir de manera individual cada elemento

print(lista1[0])
print(lista1[1])
print(lista1[2])
print(lista1[3])

print("Esta es una impresion de la lista 3 que contiene una lista y se imprime el elemento 3 de esa lista anidada \n"+ str(lista3[1][3]))