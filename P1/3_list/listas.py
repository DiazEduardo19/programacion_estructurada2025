import os
#Ejemplo 1 crear una lista de numeros e impirmir el contenido

numeros=[5,10,15,20,25,30]

#1er forma

print(numeros)

#2da forma valor

for i in numeros:
    print(i)

#3er forma indices

for i in range(0,len(numeros)):
    print(numeros[i])


#Ejemplo 2 crear una lista de palabras y posteriormente buscar la coincidencia de una palabra

os.system("clear")

palabras=["Hola","Lalin","Que paso","Tartas"]
palabras[0]="Hola"
palabras[1]="Lalin"
palabras[2]="Que paso"
palabras[3]="Tartas"


palabra_buscar=input("Dame la palabra a buscar")

#1er forma
if palabra_buscar in palabras:
    print("se encontro la palabra")
else:
    print("No encontro la palabra")


#2da forma
encontro=False
for i in palabras:
    if i==palabra_buscar:
        print("se encontro la palabra")
        econtro=True
        
if encontro:
    print("No ecnontro la palabra")
else:
   print("No encontro la palabra")

#3er forma
encontro=False
for i in range(0,len(numeros)):
    if palabras[i]==palabra_buscar:
        encontro=True
        
if encontro:
    print("No ecnontro la palabra")
else:
    print("No encontro la palabra")

#Ejemplo 3 añadir elementos a una lista}

numeros=[]
opc="si"
while opc=="si":
    numero=float(input("Dame un numero entero o decimal"))
    numeros.append(numero)
    opc=input("Deseas solicitar otro numero (si/no)").lower()

print(numeros)


#Ejemplo 4 crear una multidimensional (matriz que almacene el nombre y telefono de 4 personas )


agenda=[
    ["Carlos","6181234567"],
    ["Alberto","668202092"],
    ["Marin","67758584849"]
    ]

for r in agenda:
    print(r)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])

valores=""
for r in range(0,3):
    for c in range(0,2):
        valores+=f"[{agenda[r][c]}],"
    valores+=f"\n"
print(valores)



















