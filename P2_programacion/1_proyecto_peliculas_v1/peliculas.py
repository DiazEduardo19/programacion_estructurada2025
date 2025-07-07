peliculas=[]

def borrarPantalla():
    import os
    os.system("clear")

def esperarTecla():
    input("\n\t\t...🕒 Oprima cualquier tecla para continuar 🕒...")

def agregarPeliculas():
    borrarPantalla()
    print("\n\t.::💾 Agregar Peliculas 💾::. \n")
    peliculas.append(input("ingresa el nombre ").upper().strip()) #Upper convierte en mayusculas y strip quita espacios para que no falle el codigo
    print("\n\t\t:::✅ ¡LA OPERACION SE REALIZO CON EXITO ✅:::")

def modificarPeliculas():
    borrarPantalla()
    print("\n\t\t.:: 🔄 Modificar Películas 🔄 ::.\n")
    pelicula_modificar = input("Ingrese el nombre de la película que desea modificar: ").upper().strip()

    if pelicula_modificar not in peliculas:
        print("\n\t\t ❌ ¡La película no se encuentra en el sistema! ❌")
        return

    indices = [i for i, p in enumerate(peliculas) if p == pelicula_modificar]

    print(f"\nSe encontró(n) {len(indices)} coincidencia(s) para: {pelicula_modificar}")
    for i, index in enumerate(indices):
        print(f"{i + 1}. Posición {index + 1} - {peliculas[index]}")

    try:
        seleccion = int(input("Seleccione el número de la película que desea modificar: ")) - 1
        if seleccion < 0 or seleccion >= len(indices):
            print("\n\t❌ Selección inválida.")
            return
    except ValueError:
        print("\n\t❌ Entrada no válida. Debe ingresar un número.")
        return

    nuevo_nombre = input("Ingrese el nuevo nombre de la película: ").upper().strip()
    peliculas[indices[seleccion]] = nuevo_nombre
    print("\n\t\t:::✅ ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO ✅:::")


def consultarPeliculas():
    borrarPantalla()
    print("\n\t\t.::🔍 Consultar o Mostrar las Peliculas 🔍::. \n")
    if len(peliculas)>0:
        for i in range (0,len(peliculas)):
            print(f"\t{i+1}: {peliculas[i]}")
    else:
        print("\n\t.::❌ No hay pelicilas en el Sistema de momento ❌::.")

def vaciarPelicula():

    borrarPantalla()
    print("\n\t\t.:: Vaciar o quitar las peliculas ::. \n")
    resp=input("⚠️Deseas quitar TODAS las peliculas del sistema (Si/No)⚠️").lower().strip()
    if resp=="si":
        peliculas.clear
        print("\n\t\t:::✅ ¡LA OPERACION SE REALIZO CON EXITO ✅:::")

def buscarPeliculas():
    borrarPantalla()
    print("\n\t.::🔍 Buscar Peliculas 🔍::.\n")
    pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar:").upper().strip()
    encontro=0
    if not(pelicula_buscar in peliculas):
        print("\n\t\t ❌ ¡No se encuentra la pelicula! ❌")
    else:
        for i in range(0,len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                print(f"La pelicula {pelicula_buscar} si la tenemos y esta en la casilla {i+1}")
                encontro+=1
            print(f"\nTenemos {encontro} peliculas(s) con este titulo")
            print("\n\t\t:::✅ ¡LA OPERACION SE REALIZO CON EXITO ✅:::")
        
def eliminarPeliculas():
    borrarPantalla()
    print("\n\t.::📛 Borrar peliculas 📛::.\n")
    pelicula_buscar=input("Ingrese el nombre de la pelicula a borrar:").upper().strip()
    encontro=0
    if not(pelicula_buscar in peliculas):
        print("\n\t\t ❌ ¡No se encuentra la pelicula! ❌")
    else:
        resp="si"
        while pelicula_buscar in peliculas and resp=="si":
            resp=input("⚠️¿Deseas borrar la pelicula del sistema? (Si/No) ⚠️")
            if resp=="si":
                posicion=peliculas.index(pelicula_buscar)
                print(f"\n⚠️ La pelicula que se borro es:{pelicula_buscar} y esta en la casilla: {posicion+1} ⚠️")
                peliculas.remove(pelicula_buscar)
                encontro+=1
                print("\n\t\t:::✅ ¡LA OPERACION SE REALIZO CON EXITO ✅:::")
            
            print(f"\n\tSe borro {encontro} peliculas(s) con este titulo")
def vaciarPeliculas():
    borrarPantalla()
    print("\n\t\t.:: ⚠️ Vaciar o quitar todas las películas ⚠️ ::. \n")
    resp = input("⚠️ ¿Deseas quitar TODAS las películas del sistema? (Si/No): ").lower().strip()
    if resp == "si":
        peliculas.clear()
        print("\n\t\t:::✅ ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO ✅:::")
    else:
        print("\n\t\t:::❌ Operación cancelada por el usuario ❌:::")
    