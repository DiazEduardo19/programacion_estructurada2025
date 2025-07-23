"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
import os
os.system("clear")

paises=["Mexico","Brasil","Canada"]
print(paises)
print(paises[1])

paises={"Mexico","Brasil","España","Canada"}
print(paises)

#Funciones u opercaciones
for i in paises:
    print(i)

paises.add("Mexico")
print(paises)

paises.pop()
print(paises)

paises.remove("Mexico")
print(paises)

#Ejemplo crear un programa que solicite los email de los alumnos de la UTD almacenar 
#en una lista y posteriormente mostrar en pantalla los emails sin duplicados

correos=[]
resp="si"

while resp=="si":
  correos.append(input("Ingrese un email de la UTD:"))
  resp=input("Deseas poner otro correo? (si/no)").lower()

correos_set=set(correos)
emails=list(correos_set)
print(correos_set)




































