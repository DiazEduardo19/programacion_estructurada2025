"""
Crear un programa que calcule e imprima la tabla de multlipicar del 2

Restricciones:
1-Sin estructuras de control
2-Sin funciones

"""
#Version 1

num=int(input("Dime un numero de la tabla de multlipicar:"))
m=num*1
print(f"{num}x1={m}")
m=num*2
print(f"{num}x2={m}")
m=num*3
print(f"{num}x3={m}")
m=num*4
print(f"{num}x4={m}")
m=num*5
print(f"{num}x5={m}")
m=num*6
print(f"{num}x6={m}")
m=num*7
print(f"{num}x7={m}")
m=num*8
print(f"{num}x8={m}")
m=num*9
print(f"{num}x9={m}")
m=num*10
print(f"{num}x10={m}")

#version 2
"""
Crear un programa que calcule e imprima la tabla de multlipicar del 2

Restricciones:
1-Con estructuras de control
2-Sin funciones

"""
num=int(input("Dime un numero de la tabla de multlipicar:"))
for i in range(1,11,1):
    m=num*i
    print(f"{num}x{i}={m}")

#version 3
"""
Crear un programa que calcule e imprima la tabla de multlipicar del 2

Restricciones:
1-Con estructuras de control
2-Con funciones

"""
def solicitarDatos(num):
    for i in range(1,11,1):
        m=num*i
    print(f"{num}x{i}={m}")
def main():
    numero = 2  
    if numero > 0:
        solicitarDatos(num)
    else:
        print("El número debe ser positivo.")
