#Proyecto3
#Crear un proyecto que permita gestionar (administrar) calificaciones, colocar un menu de opciones para agregar, mostrar y calcular promedios de las calificaciones de los alumnos

#Notas: 
#1.-utiliza  funciones y mandar a llamar desde otro archivo 
#2.- Utilizar dict  para almacenar  los siguentes atrivutos (nombre, categoria, clasificacion, genero,idioama de la película, )

import calificaciones

def main():

    opcion=True
    datos = []
    while opcion:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
        calificaciones.borrar_pantalla()
        opcion=calificaciones.menu_pricpal()

    match opcion:
        case "1":
            calificaciones.agrearCalificaciones(datos)
            calificaciones.esperarTecla()
        case "2":
            calificaciones.mostrarCalificaciones(datos)
            calificaciones.esperarTecla() 
        case "3":
           calificaciones.calcularPromedios(datos)   
           calificaciones.esperarTecla()
        case "4":
           opcion=False
           calificaciones.borra_pantalla() 
           print("Terminaste la ejecucion del SW")
        
        case _:
            opcion=True 
            input("Opción invalida vuelva a intentarlo ... por favor")
            return 

if __name__ == "__main__":
    main()


