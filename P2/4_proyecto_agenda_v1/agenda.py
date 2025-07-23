

def borrar_pantalla():
    import os
    os.system("cls")

def esperar_tecla():
    input("\n\t🕒 ... Oprime una tecla para continuar... 🕒")

def agregar_contacto(agenda_contactos):
    nombre = input("👤 Ingresa el nombre del contacto: ").strip()
    telefono = input("📞 Ingresa el número de teléfono: ").strip()
    email = input("📧 Ingresa el correo electrónico: ").strip()

    contacto = {
        'nombre': nombre,
        'telefono': telefono,
        'email': email
    }

    agenda_contactos.append(contacto)
    print("✅ Contacto agregado correctamente.")

def mostrar_contactos(agenda_contactos):
    if not agenda_contactos:
        print("📭 No hay contactos en la agenda.")
        return

    print("\n📋 Lista de contactos:")
    for i, contacto in enumerate(agenda_contactos, 1):
        print(f"\n🔹 Contacto {i}:")
        print(f"   Nombre: {contacto['nombre']}")
        print(f"   Teléfono: {contacto['telefono']}")
        print(f"   Email: {contacto['email']}")

def buscar_contacto(agenda_contactos):
    nombre_buscado = input("🔍 Ingresa el nombre a buscar: ").strip().lower()

    encontrados = [
        contacto for contacto in agenda_contactos
        if contacto['nombre'].lower() == nombre_buscado
    ]

    if encontrados:
        print("👀 Contacto(s) encontrado(s):")
        for contacto in encontrados:
            print(f"\n   Nombre: {contacto['nombre']}")
            print(f"   Teléfono: {contacto['telefono']}")
            print(f"   Email: {contacto['email']}")
    else:
        print("❌ No se encontró ningún contacto con ese nombre.")
