

#listas=[
#            ["Ruben",10.0,10.0,10.0],
#            ["Diana",10.0,9.8,8.0],
#            ["Jose",5.0,6.0,7.0]
#        ]

def borrarPantalla():
    import os  
    os.system("clear")

def esperarTecla():
    input("🕒 Oprima cualquier tecla para continuar...")  

def menu_principal():
    print("🎓 .:: Sistema de Gestión de Calificaciones ::. 🎓")
    print("📝 1.- Agregar 📂")
    print("📋 2.- Mostrar 🔍")
    print("📊 3.- Calcular Promedios 💯")
    print("🚪 4.- SALIR")
    opcion = input("👤 Elige una opción (1-4): ")
    return opcion

def agregar_calificaciones(lista):
    borrarPantalla()
    print("📝 Agregar Calificaciones")
    nombre = input("👤 Nombre del Alumno: ").upper().strip()
    calificaciones = []
    for i in range(1, 4):
        continua = True
        while continua:
            try:
                cal = float(input(f"🧮 Calificación {i}: "))
                if 0 <= cal < 11:
                    calificaciones.append(cal)
                    continua = False
                else:
                    print("⚠️ Ingresa un número válido entre 0 y 10.")
            except ValueError:
                print("❌ Ingresa un valor numérico.")
    lista.append([nombre] + calificaciones)
    print("✅ Acción realizada con éxito 🎉")

def mostrar_calificaciones(lista):
    borrarPantalla()
    print("📋 Mostrar Calificaciones")
    if len(lista) > 0:
        print(f"{'👤 Nombre':<15}{'📘 Calf. 1':<10}{'📙 Calf. 2':<10}{'📗 Calf. 3':<10}")
        print(f"{'-'*40}")
        for fila in lista:
            print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
        print(f"{'-'*40}")  
        cuantos = len(lista)
        print(f"👥 Son {cuantos} alumnos registrados")
    else:
        print("⚠️ No hay calificaciones registradas en el sistema.")    

def calcular_promedios(lista):
    borrarPantalla()
    print("📊 .:: PROMEDIOS ::. ")
    if len(lista) > 0:
        print(f"{'👤 Alumno':<15}{'📈 Promedio':<10}")
        print(f"{'-'*30}")
        promedio_grupal = 0
        for fila in lista:
            nombre = fila[0]
            promedio = sum(fila[1:]) / 3
            print(f"{nombre:<15}{promedio:.2f}")  
            promedio_grupal += promedio 
        print(f"{'-'*30}")
        promedio_grupal = promedio_grupal / len(lista)
        print(f"📊 El promedio grupal es: {promedio_grupal:.2f}")
    else:
        print("⚠️ No hay calificaciones registradas en el sistema.")     

def buscar_calificaciones(lista):
    borrarPantalla()
    print("Buscar Calificaciones")
    nombre = input("Nombre del Alumno a buscar: ").upper().strip()
    encontrado = False
    for fila in lista:
        if fila[0] == nombre:
            print(f"\nCalificaciones de {nombre}:")
            print(f"Calf. 1: {fila[1]}")
            print(f"Calf. 2: {fila[2]}")
            print(f"Calf. 3: {fila[3]}")
            encontrado = True
            break
    if not encontrado:
        print(f"No se encontró al alumno '{nombre}' en el sistema.")
    esperarTecla()