import os
#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
os.system("clear")

numeros=[23,45,8,24]

#1er forma
print(numeros)

#2da forma valor

for i in numeros:
    print(i)

#3er forma indices

for i in range(0,len(numeros)):
    print(numeros[i])  
    



#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 

os.system("clear")

# palabras=["hola","casa","jupiter","sol"]
# palabra_buscar=input("Dame la palabra a buscar: ")

# #1er forma
# if palabra_buscar in palabras:
#     print("Se encontro la palabra")
# else:
#     print("No encontro la palabra")     

# #2da forma
# encontro=False
# for i in palabras:
#    if i==palabra_buscar:
#        encontro=True

# if encontro:
#     print("Se encontro la palabra")
# else:
#     print("No encontro la palabra")     

# #3er forma
# encontro=False
# for i in range(0,len(numeros)):
#    if palabras[i]==palabra_buscar:
#        encontro=True

# if encontro:
#     print("Se encontro la palabra")
# else:
#     print("No encontro la palabra")     












#Ejemplo 3 Añadir elementos a la lista

numeros=[]
opc="si"
while opc=="si":
    numeros.append(float(input("Dame un numero entero o decimal: ")))
    opc=input("¿Deseas solicitar otro numero (si/no)").lower()

print(numeros)



#Ejemplo 4 Crear una lista multidimensional (matriz) que almacene el nombre y telefono de 4 personas

agenda=[
        ["Carlos","6181234567"],
        ["Alberto","6671234567"],
        ["Martin","6785678923"]
       ]
