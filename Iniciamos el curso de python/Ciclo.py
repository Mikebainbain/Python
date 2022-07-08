# ciclo for  while , do-while en phyton

var = 0

while var < 100:
    print("Sigue asi, sigue  esforzandote")
    var += 1



#
lista = [10,20,30,'Hola',True]

for i in lista:
    print(i)

# tambien se pueden hacer operaciones para los valores dentro de esa misma lista ejemplo elevar a al cuadrado y se puede dejar en una sola linea todo

lista2 = [10,20,30]
nuevalista = [i**2 for i in lista2]

for i in nuevalista:
    print(i)