agenda_contactos = {
    "RUBEN": ["6181234567", "ruben@gmail.com"],
    "DANIEL": ["6181234568", "daniel@gmail.com"],
    "XIMENA": ["6181234569", "xime@gmail.com"],
}

def borrarPantalla():  
    import os
    os.system("cls")

def esperarTecla():  
    input("🔄 Oprima cualquier tecla para continuar 🔄 ")

def menu_principal():  
    print("📝 ..::: Sistema de Gestión de Agenda de Contactos :::... 📝\n")
    print("1️⃣\tAgregar contacto")
    print("2️⃣\tMostrar todos los contactos")
    print("3️⃣\tBuscar un contacto por el nombre")
    print("4️⃣\tModificar un contacto")
    print("5️⃣\tEliminar un contacto")
    print("6️⃣\tSALIR\n")
    opcion = input("😎 Elige una opción (1-6): ")
    return opcion

def agregar_contacto(agenda):
    borrarPantalla()
    print("➕ Agregar Contactos")
    nombre = input("📛 Ingresa el nombre: ").upper().strip()
    if nombre in agenda:
        print("⚠️ El contacto ya existe")
    else:
        tel = input("📞 Ingresa el teléfono: ").strip()
        email = input("✉️ Ingresa el email: ").upper().strip()
        agenda[nombre] = [tel, email]
        print("✅ Acción realizada con éxito")

def mostrar_contacto(agenda):
    borrarPantalla()
    print("📋 Mostrar todos los contactos")
    if not agenda:
        print("😔 No hay contactos en el sistema")
    else:
        print(f"{'Nombre':<15}{'Teléfono':<15}{'Email':<15}")
        print(f"'-"*60)
        for nombre, datos in agenda.items():
            print(f"{nombre:<15}{datos[0]:<15}{datos[1]:<15}")
        print(f"'-"*60)

def buscar_contacto(agenda):
    borrarPantalla()
    print("🔍 Buscar contacto por el nombre")
    if not agenda:
        print("😔 No hay contactos disponibles")
    else:
        nombre = input("📛 Ingresa el nombre del contacto: ").upper().strip()
        if nombre in agenda:
            print(f"{'Nombre':<15}{'Teléfono':<15}{'Email':<15}")
            print(f"'-"*60)
            print(f"{nombre:<15}{agenda[nombre][0]:<15}{agenda[nombre][1]:<15}")
            print(f"'-"*60)
        else:
            print("😞 No existe el contacto")

def modificar_contacto(agenda):
    borrarPantalla()
    print("✏️ Modificar un contacto")
    if not agenda:
        print("😔 No hay contactos disponibles")
    else:
        nombre = input("📛 Ingresa el nombre del contacto: ").upper().strip()
        if nombre in agenda:
            print(f"{'Nombre':<15}{'Teléfono':<15}{'Email':<15}")
            print(f"'-"*60)
            print(f"{nombre:<15}{agenda[nombre][0]:<15}{agenda[nombre][1]:<15}")
            print(f"'-"*60)
            resp = input("❓ ¿Deseas modificar el contacto? (Si/No) ").lower().strip()
            if resp == "si":
                tel = input("📞 Ingresa el teléfono: ").strip()
                email = input("✉️ Ingresa el email: ").upper().strip()
                agenda[nombre] = [tel, email]
                print("✅ Acción realizada con éxito")
            else:
                print("🚫 Operación cancelada")
        else:
            print("😞 El contacto no existe")

def eliminar_contacto(agenda):
    borrarPantalla()
    print("🗑️ Eliminar contactos")
    if not agenda:
        print("😔 No hay contactos en la agenda")
    else:
        nombre = input("📛 Ingresa el nombre del contacto a eliminar: ").upper().strip()
        if nombre in agenda:
            print(f"{'Nombre':<15}{'Teléfono':<15}{'Email':<15}")
            print(f"'-"*60)
            print(f"{nombre:<15}{agenda[nombre][0]:<15}{agenda[nombre][1]:<15}")
            print(f"'-"*60)
            resp = input("❓ ¿Deseas eliminar el contacto? (Si/No) ").lower().strip()
            if resp == "si":
                agenda.pop(nombre)
                print("✅ Acción realizada con éxito")
            else:
                print("🚫 Operación cancelada")
        else:
            print("😞 Este contacto no existe")