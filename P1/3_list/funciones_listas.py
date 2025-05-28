"""  

 List (Array)
 son colleciones o conjunto de datos/valores bajo 
 un mismo nombre, para acceder a los valores se
 hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.


"""

import os 
os.system("clear")

#Funciones más comunes en las listas

paises=["México","Brasil","España","Canada"]

numeros=[23,12,100,34]

#Ordenar ascendentemente
print(numeros)
numeros.sort()
print(numeros)
print(paises)
paises.sort()
print(paises)

#Añadir o Ingresar o Insertar elementos a una lista

#1er forma
print(paises)
paises.append("Honduras")
#2da forma
paises.insert(1,"Honduras")
print(paises)

#Eliminar o Borrar o Quitar elementos a una lista
#1er forma con el indice
paises.pop(1)
print(paises)
#2da forma con el valor 
paises.remove("Honduras")
print(paises)

#buscar un elemento dentro de la lista
#1er forma
resp="Brasil" in paises
if resp:
    print("Si enconcontre el pais")
else:     
    print("No enconcontre el pais")


#2da forma
for i in range(0,len(paises)):
     if paises[i]=="Brasil":
        print("Si enconcontre el pais")
     else:
        print("No enconcontre el pais")        

#cuantas veces aparece un elemento dentro de la lista

#numeros=[23,12,100,34]

print(f"Este numero 12 aparece: {numeros.count(12)} vez o veces")

numeros.append(12)
print(f"Este numero 12 aparece: {numeros.count(12)} vez o veces")

#Identificar o conocer el indice de un valor 

#paises=["México","Brasil","España","Canada"]

indice=paises.index("España")
print(indice)
paises.pop(indice)
print(paises)

#Recorrer los valores de la lista 
#1er forma con los valores
for i in paises:
    print(i)

#2da forma con los indices
for i in range(0,len(paises)):
    print(f"El valor {i} es: {paises[i]}")    

#Unir contenido de listas
#paises=["México","Brasil","Canada"]
#numeros=[23,12,100,34,12]

print(paises)
print(numeros)
paises.extend(numeros)
print(paises)

#Es hora de colocar mas codigo






