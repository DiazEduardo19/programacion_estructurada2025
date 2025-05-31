def main(num):
    numero = 2  # Número fijo como indica la restricción
    if numero > 0:  # Estructura selectiva: if
        imprimir_tabla(numero)
    else:
        print("El número debe ser positivo.")

def imprimir_tabla(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):  # Estructura iterativa: for
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
