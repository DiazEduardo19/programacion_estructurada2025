#Proyecto1
#Crear un proyecto que permita gestionar (administrar) peliculas; colocar un menu de opciones para agregar,
#borrar, modificar, consultar, buscar y vaciar peliculas
#Notas:
#1.-Utilizar funciones y mandar llamar desde otro archivo
#2.-Utilizar una lista para almacenar los nombres de las peliculas

import peliculas

opcion=True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t.:::🎉 CINEPOLIS CLON 🎉:::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Agregar 💾 \n\t\t 2.- Eliminar ❌ \n\t\t 3.- Actualizar 🔄\n\t\t 4.- Consultar 🔍\n\t\t 5.- Buscar 🔍\n\t\t 6.- Vaciar ⚠️\n\t\t 7.-📛 SALIR 📛")
    opcion=input("\n\t\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.eliminarPeliculas()
            peliculas.esperarTecla()
            print(".:: Eliminar Peliculas ::.") 
            input("Oprima cualquier tecla para continuar ...") 
        case "3":
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()
            print(".:: Modificar Peliculas ::.") 
            input("Oprima cualquier tecla para continuar ...")    
        case "4":
            peliculas.consultarPeliculas() 
            peliculas.esperarTecla()
        case "5": 
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        case "6": 
            peliculas.vaciarPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion=False
            peliculas
            print("\n\tTerminaste la ejecucion del SW")
        case _: 
            opcion=True
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")

