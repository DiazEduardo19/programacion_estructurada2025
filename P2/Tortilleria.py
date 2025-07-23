import csv
from datetime import datetime

PRODUCTOS = {
    1: {"nombre": "Tortilla de maíz", "precio": 20.0},   # precio por kilo
    2: {"nombre": "Tortilla de harina", "precio": 25.0},
            }

ARCHIVO_VENTAS = "ventas.csv"

def mostrar_productos():
    print("\n---📂 PRODUCTOS DISPONIBLES 📂---")
    for pid, prod in PRODUCTOS.items():
        print(f"{pid}. {prod['nombre']} - ${prod['precio']} por kilo")

def registrar_venta():
    mostrar_productos()
    try:
        producto_id = int(input("📝 Seleccione el número del producto: 📝"))
        if producto_id not in PRODUCTOS:
            print("❌Producto no válido.❌")
            return

        kilos = float(input("📝 Ingrese la cantidad en kilos: 📝"))
        if kilos <= 0:
            print("❌Cantidad no válida.❌")
            return

        producto = PRODUCTOS[producto_id]
        total = kilos * producto["precio"]
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(ARCHIVO_VENTAS, mode='a', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([fecha, producto["nombre"], kilos, producto["precio"], total])

        print(f"✅Venta registrada: {kilos} kg de {producto['nombre']} - Total: ${total:.2f}✅")
    except ValueError:
        print("❌Entrada no válida.❌")

def mostrar_ventas():
    print("\n---🕒 HISTORIAL DE VENTAS 🕒---")
    try:
        with open(ARCHIVO_VENTAS, mode='r') as archivo:
            lector = csv.reader(archivo)
            total_general = 0
            for fila in lector:
                fecha, producto, kilos, precio_unitario, total = fila
                print(f"{fecha} - {producto}: {kilos} kg a ${precio_unitario}/kg = ${total}")
                total_general += float(total)
            print(f"\nTotal vendido: ${total_general:.2f}")
    except FileNotFoundError:
        print("❌No hay ventas registradas aún.❌")

def menu():
    while True:
        print("\n===🎉🎉 SISTEMA DE VENTAS - TORTILLERÍA 🎉🎉===")
        print("1.📂 Registrar venta 📂")
        print("2.🔍 Mostrar historial de ventas 🔍")
        print("3.📛 Salir 📛")


        opcion = input("📝 Seleccione una opción: 📝")
        if opcion == '1':
            registrar_venta()
        elif opcion == '2':
            mostrar_ventas()
        elif opcion == '3':
            print("🎉Gracias por usar el sistema.🎉")
            break
        else:
            print("❌Opción no válida.❌")

if __name__ == "__main__":
    menu()




    