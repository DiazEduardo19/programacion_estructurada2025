
import agenda

agenda_contactos = []

opcion = True
while opcion:
    agenda.borrar_pantalla()
    print("\n\t...:::🛠️📅 Sistema de Gestión de Agenda de Contacto 📅🛠️:::...\n")
    print("1️⃣ Agregar contacto")
    print("2️⃣ Mostrar todos los contactos")
    print("3️⃣ Buscar contacto por nombre")
    print("4️⃣ SALIR")

    opcion_input = input("\n🙏 Elige una opción (1-4): ").strip()

    match opcion_input:
        case "1":
            agenda.agregar_contacto(agenda_contactos)
            agenda.esperar_tecla()
        case "2":
            agenda.mostrar_contactos(agenda_contactos)
            agenda.esperar_tecla()
        case "3":
            agenda.buscar_contacto(agenda_contactos)
            agenda.esperar_tecla()
        case "4":
            print("👍 Acabaste de usar la agenda. ¡Hasta luego! 👍")
            opcion = False
        case _:
            print("❌ Opción no válida, vuelva a intentarlo ❌")
            agenda.esperar_tecla()
