import mysql.connector
from mysql.connector import Error

#Disct u objeto para almacenar los atributos (nombre,categoria,clasificacion,genero,idioma)  y sus valores 

# pelicula={
#            "nombre":"",
#            "categoria":"",
#            "clasificacion":"",
#            "genero":"",
#            "idioma":""
#          }

pelicula={}

def borrar_pantalla():
  import os  
  os.system("clear")

def esperarTecla():
  input("\n\t\t... Oprima cualquier tecla para continuar ...")  

def conectar():
  try:
    conexion=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_peliculas"  
      )
    return conexion
  except Error as e:
    print(f"El error que se presento es: {e}")
    return None

def crearPeliculas():
  borrar_pantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: Crear Películas ::. \n")
    pelicula["nombre"]=input("Ingresa el nombre: ").upper().strip()
    #pelicula.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
    pelicula.update({"categoria":input("Ingresa la categoría: ").upper().strip()})
    pelicula.update({"clasificacion":input("Ingresa la clasificación: ").upper().strip()})
    pelicula.update({"genero":input("Ingresa el genero: ").upper().strip()})
    pelicula.update({"idioma":input("Ingresa el idioma: ").upper().strip()})
    
    ####### BD
    cursor=conexionBD.cursor()
    sql="insert into peliculas (nombre,categoria,clasificacion,genero,idioma) value (%s,%s,%s,%s,%s)"
    val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"])
    cursor.execute(sql,val)
    conexionBD.commit()
    print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON EXÍTO! :::")

def mostrarPeliculas():
  borrar_pantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: Mostrar las Películas ::. \n")
    cursor=conexionBD.cursor()
    sql="select * from peliculas"
    cursor.execute(sql)
    registros=cursor.fetchall()
    if registros:
      print("Mostrar las Peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for pelis in registros:
        print(f"{pelis[0]:<10}{pelis[1]:<15}{pelis[2]:<15}{pelis[3]:<15}{pelis[4]:<15}{pelis[5]:<15}")
      print(f"-"*80)  
    else:
      print("\t .:: No hay peliculas en el sistema ::..")   

def buscarPeliculas():
  borrar_pantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: Buscar Películas ::. \n")
    nombre=input("Ingresa el nombre de la pelicula a buscar: ").upper().strip()
    cursor=conexionBD.cursor()
    sql="select * from peliculas where nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
    if registros:
      print("Mostrar las Peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for pelis in registros:
        print(f"{pelis[0]:<10}{pelis[1]:<15}{pelis[2]:<15}{pelis[3]:<15}{pelis[4]:<15}{pelis[5]:<15}")
      print(f"-"*80)  
    else:
      print("\t .:: peliculas no encontradas en el sistema ::..")

def borrar_peliculas():
  borrar_pantalla()
  conexionBD=conectar()
  if conexionBD!=None:
    print("\n\t.:: Borrar Películas ::. \n")
    nombre=input("Ingresa el nombre de la pelicula a borrar: ").upper().strip()
    cursor=conexionBD.cursor()
    sql="select * from peliculas where nombre=%s"
    val=(nombre,)
    cursor.execute(sql,val)
    registros=cursor.fetchall()
    if registros:
      print("Mostrar las Peliculas")
      print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
      print(f"-"*80)
      for pelis in registros:
        print(f"{pelis[0]:<10}{pelis[1]:<15}{pelis[2]:<15}{pelis[3]:<15}{pelis[4]:<15}{pelis[5]:<15}")
      print(f"-"*80) 
      resp=input(f"¿Deseas borrar la pelicula {nombre}? (Si/No): ").lower().strip()
      if resp=="si":
        sql="delete from peliculas where nombre = %s"
        val=(nombre,)
        cursor.execute(sql,val)
        conexionBD.commit()
        print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON EXÍTO! :::")
    else:
      print("\t .:: peliculas no encontradas en el sistema ::..")
    borrar_pantalla()
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