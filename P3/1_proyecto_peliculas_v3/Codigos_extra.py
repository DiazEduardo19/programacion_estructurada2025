peliculas=[]
respuesta="si"
while respuesta=="si":
    peliculas.append(input("Bienvenido a al catalogo de peliculas añade cuantas quieras:"))
    respuesta=input("Deseas agregar otra pelicula:").lower()
print(peliculas)
