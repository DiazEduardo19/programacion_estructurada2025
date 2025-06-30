#dict u objeto para al,acenar los atrivutos( nombre, categoria, clasificacion, genero, idioma)

#pelicula=¨{
#      "nombre",
#      "categoria":"",
#     "clasificacion":"",
#        "genero":"",
#        "idioma":""
#}

pelicula = {}

def borra_pantalla():
    import os
    os.system("cls")


def esperarTecla():
    input("\n\t🕒 ... Oprime una tecla para continuar...")


def crear_peliculas():
    borra_pantalla()
    print("\n\t🎬 .:: Crear Películas ::.\n")
    pelicula["nombre"] = input("📝 Ingrese el nombre: ").upper().strip()
    pelicula.update({"categoria": input("📝 Ingrese la categoría: ").upper().strip()})
    pelicula.update({"clasificacion": input("📝 Ingrese la clasificación: ").upper().strip()})
    pelicula.update({"genero": input("📝 Ingrese el género: ").upper().strip()})
    pelicula.update({"idioma": input("📝 Ingrese el idioma: ").upper().strip()})
    print("\n\t✅ .:: ¡La operación se realizó con éxito! ::.")
    esperarTecla()


def mostrarPeliculas():
    borra_pantalla()
    print("\n\t🔍 .:: Consultar la Película ::.\n")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t📌 {i.capitalize()}: {pelicula[i]}")
    else:
        print("\t❌ .:: No hay películas en el sistema. ::.")
    esperarTecla()


def borrar_peliculas():
    borra_pantalla()
    print("\n\t📛 .:: Borrar TODAS las Películas ::.\n")
    resp = input("⚠️ ¿Deseas quitar o borrar todas las películas del sistema? (Si/No): ").lower()
    if resp == "si":
        pelicula.clear()
        print("\n\t✅ .:: ¡La operación se realizó con éxito! ::.")
    else:
        print("\n\t🔄 .:: Operación cancelada por el usuario. ::.")
    esperarTecla()


def agreagarCaracteristicaPeliculas():
    borra_pantalla()
    print("\n\t🆕 .:: Agregar Característica a Películas ::.\n")
    atributo = input("📝 Ingrese la nueva característica de la película: ").lower().strip()
    valor = input(f"📝 Ingrese el valor de la característica '{atributo}': ").upper().strip()
    pelicula[atributo] = valor
    print("\n\t✅ .:: ¡La operación se realizó con éxito! ::.")
    esperarTecla()


def modificarCaracteristcaPeliculas():
    borra_pantalla()
    print("\n\t🔄 .:: Modificar Características de la Película ::.\n")
    if len(pelicula) > 0:
        print("\n\t📋 Valores actuales:\n")
        for i in pelicula:
            print(f"\t📌 {i.capitalize()}: {pelicula[i]}")
            resp = input(f"\t📝 ¿Deseas cambiar el valor de '{i}'? (Si/No): ").lower()
            if resp == "si":
                nuevo_valor = input("\t🔁 Ingresa el nuevo valor: ").upper().strip()
                pelicula[i] = nuevo_valor
                print("\n\t✅ ¡Cambio realizado con éxito!")
    else:
        print("\t❌ ..:: No hay películas en el sistema. ::..")
    esperarTecla()


def borrarCaracteristicaPeliculas():
    borra_pantalla()
    print("\n\t📛 .:: Borrar Características de la Película ::.\n")
    if len(pelicula) > 0:
        print("\n\t📋 Características actuales:\n")
        for i in pelicula:
            print(f"\t📌 {i.capitalize()}: {pelicula[i]}")
        atributo = input("\n📝 Ingrese el nombre de la característica a borrar: ").lower().strip()
        if atributo in pelicula:
            del pelicula[atributo]
            print(f"\n\t✅ La característica '{atributo}' se ha borrado con éxito.")
        else:
            print(f"\n\t❌ La característica '{atributo}' no existe en la película.")
    else:
        print("\t❌ No hay características para borrar.")
    esperarTecla()





#def consultarPeliculas():
    #borra_pantalla()
    #print("\n\t.:: Consultar o Mostrar  Películas ::\n")
    #if len(peliculas) > 0:
    #    for i in range(0, len(peliculas)):
    #        print(f"{i+1}. {peliculas[i]}")
    #else:
    #    print("\n\t.::No hay películas registradas.")

#def vaciarPeliculas():
   # borra_pantalla()
    #print("\n\t.:: Vaciar o quitar TODAS las   Películas::.\n ")
    #resp = input("¿Deseas quitar TODOS las peliculas del sistema? (si/no): ").lower().strip()
    #if resp == "si":
    #    peliculas.clear()
    #    print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::\n")

#def buscar_Peliculas():
   # borra_pantalla()
    #print("\n\t.:: Buscar Películas ::\n")
    #pelicula_buscar = input("Ingrese el nombre de la película a buscar: ").upper().strip()
    #encontro=0
    #if not  (pelicula_buscar in peliculas):
    #    print("\n\t.::¡No se encuentra la película!.\n")
    #else:
     #   for i in range(0, len(peliculas)):
      #      if pelicula_buscar  == peliculas[i]:
       #        print(f"\nLa película '{pelicula_buscar}' si tenemos y esta en la casilla {i+1} ")
        #    encontro+=1
       # print(f"\n\t.::¡Se encontraron {encontro} con este titulo!.\n")
        #print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::\n")       


#def eliminar_pelicula():
 #   borra_pantalla()
  #  print("\n\t.:: Borrar  Película ::\n")
   # pelicula_buscar=input("Ingrese el nombre de la pelicula a borrar: ").upper().strip()
   # encontro=0
   # if not (pelicula_buscar in peliculas):
    #    print("\n\t\t.::¡No se encuentra la película!.")
    #   resp="si"
     #   while pelicula_buscar in peliculas:
      ###       print(f"\n\La película '{pelicula_buscar} y estaba en la casilla {posicion+1}.")