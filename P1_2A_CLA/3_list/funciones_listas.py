"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""

import os 
os.system("clear")

#Funciones más comunes en las listas

paises=["México","Brasil","España","Canada"]

numeros=[23,12,100,34]

varios=["Hola",True,33,3.12]

#ordenar las listas

print(numeros)
print(paises)
print(varios)

numeros.sort()
print(numeros)
paises.sort()
print(paises)

#Agregar o insertar o añadir un elemento a la lista
#1er forma paises=["México","Brasil","España","Canada"]
print(paises)
paises.append("Honduras")
print(paises)

#2da forma 
paises.insert(1,"Honduras")
print(paises)

#Eliminar o borrar o suprimir un elemento a la lista
#1er forma
paises.sort()
print(paises)
paises.pop(4)
print(paises)

#2da forma 
paises.remove("Honduras")
print(paises)


#buscar un elemento dentro de una lista
#paises=["México","Brasil","España","Canada"]

print("Brasil" in paises)

#Contar el numero veces que un elemento esta dentro de una lista
#numeros=[23,12,100,34]
print(numeros)
print(numeros.count(12))
numeros.insert(1,12)
print(numeros)
print(numeros.count(101))

#Dar la vuelta a los elementos de una lista
print(paises)
print(numeros)
paises.reverse()
numeros.reverse()
print(numeros)
print(paises)

#Conocer el indice o la posicion de un valor de la lista 
posicion=paises.index("España")

#Unir el contenido de 2 o mas listas en una sola
#numeros=[100,34,23,12,12]
numeros2=[300,500,100]

print(numeros)
print(numeros2)
numeros.extend(numeros2)
print(numeros)

paises.extend(numeros2)
print(paises)

