correos=[]
resp="si"

while resp=="si":
  correos.append(input("Dime los correos de la UTD para hacer una lista:"))
  resp=input("Deseas poner otro correo? (si/no)").lower()

print(correos)
