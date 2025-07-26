import mysql.connector
from mysql.connector import Error

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t...Presione cualquier tecla para continuar...")

def menu_principal():
    print("\t\t📋...:::Sistema de Gestión de Agenda de Contactos :::...📋\n\tSelecciona una opción:\n\n\t ➕ 1.- Agregar contacto\n\t 📋 2.- Mostrar contactos\n\t 🔎 3.- Buscar contacto\n\t 🔧 4.- Modificar contacto\n\t 🗑️ 5.- Eliminar contacto\n\t 🚪 6.- SALIR")
    op = input("\n👉 Selecciona una opción (1-6): ").upper().strip()
    return op

def conectar():
    try:
        conexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "bd_agenda"
        )
        return conexion
    except Error as e:
        print(f"Error de conexión: {e}")
        return None

def agregarContacto(agenda):
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD != None:
        print("\t\t✍️.:: Agregar Contacto ::.✍️")
        nombre = input("\nNombre: ").upper().strip()
        if nombre in agenda:
            print("\n🚫 Contacto ya registrado 🚫")
        else:
            telefono = input("Teléfono: ").strip()
            email = input("Email: ").lower().strip()
            agenda[nombre] = [telefono, email]
            cursor = conexionBD.cursor()
            sql = "INSERT INTO contacto (nombre, telefono, email) VALUES (%s, %s, %s)"
            val = (nombre, agenda[nombre][0], agenda[nombre][1])
            cursor.execute(sql, val)
            conexionBD.commit()
            print("\n✔️ :: Contacto agregado correctamente :: ✔️")
            cursor.close()

def mostrarContactos(agenda):
    conexionBD = conectar()
    if conexionBD != None:
        borrarPantalla()
        print("\t\t👥.:: Lista de Contactos ::.👥")
        cursor = conexionBD.cursor()
        sql = "SELECT * FROM contacto"
        cursor.execute(sql)
        contactos = cursor.fetchall()
        if contactos:
            print("\n\t ::Contactos::")
            print(f"\n{'ID':<15} {'Nombre':<15} {'Teléfono':<15} {'Email':<15}")
            print(f"-" * 60)
            for fila in contactos:
                print(f"{fila[0]:<15} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15}")
            print(f"-" * 60)
        else:
            print("🚫 No hay contactos registrados 🚫")
        cursor.close()

def buscarContacto(agenda):
    conexionBD = conectar()
    if conexionBD != None:
        borrarPantalla()
        print("\t\t🔎.:: Buscar Contacto ::.🔎")
        nombre = input("\n\tIngresa el nombre del contacto a buscar: ").upper().strip()
        cursor = conexionBD.cursor()
        sql = "SELECT * FROM contacto WHERE nombre = %s"
        val = (nombre,)
        cursor.execute(sql, val)
        contactos = cursor.fetchall()
        if contactos:
            print("\n\t ::Resultados::")
            print(f"\n{'ID':<15} {'Nombre':<15} {'Teléfono':<15} {'Email':<15}")
            print(f"-" * 60)
            for fila in contactos:
                print(f"{fila[0]:<15} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15}")
            print(f"-" * 60)
        else:
            print("\n\t🚫 Contacto no encontrado 🚫")
        cursor.close()

def modificarContacto(agenda):
    conexionBD = conectar()
    if conexionBD != None:
        borrarPantalla()
        print("\t\t🔧.:: Modificar Contacto ::.🔧")
        cursor = conexionBD.cursor()
        cursor.execute("SELECT id, nombre FROM contacto")
        contactos = cursor.fetchall()
        if contactos:
            print("\n\t ::Contactos Registrados::")
            print(f"\n{'ID':<15} {'Nombre':<15}")
            print(f"-" * 30)
            for fila in contactos:
                print(f"{fila[0]:<15} {fila[1]:<15}")
            print(f"-" * 30)
        else:
            print("🚫 No hay contactos registrados 🚫")
            return
        id = input("\n\tIngresa el ID del contacto a modificar: ").strip()
        cursor.execute("SELECT * FROM contacto WHERE id = %s", (id,))
        contacto = cursor.fetchone()
        if contacto:
            resp = input(f"¿Desea modificar el contacto {contacto[1]} con ID {id}? (Si/No): ").upper().strip()
            if resp == "SI":
                print("\nPresiona ENTER para mantener el valor actual.\n")
                nuevo_nombre = input(f"Nuevo Nombre [{contacto[1]}]: ").upper().strip()
                nuevo_telefono = input(f"Nuevo Teléfono [{contacto[2]}]: ").strip()
                nuevo_email = input(f"Nuevo Email [{contacto[3]}]: ").lower().strip()
                if nuevo_nombre == "":
                    nuevo_nombre = contacto[1]
                if nuevo_telefono == "":
                    nuevo_telefono = contacto[2]
                if nuevo_email == "":
                    nuevo_email = contacto[3]
                cursor.execute("UPDATE contacto SET nombre=%s, telefono=%s, email=%s WHERE id=%s", (nuevo_nombre, nuevo_telefono, nuevo_email, id))
                conexionBD.commit()
                print("\n✔️ :: Contacto modificado correctamente :: ✔️")
        else:
            print("\n\t🚫 :: ID no válido :: 🚫")
        cursor.close()

def eliminarContacto(agenda):
    conexionBD = conectar()
    if conexionBD != None:
        borrarPantalla()
        print("\t\t🗑️.:: Eliminar Contacto ::.🗑️")
        cursor = conexionBD.cursor()
        cursor.execute("SELECT id, nombre FROM contacto")
        contactos = cursor.fetchall()
        if contactos:
            print("\n\t ::Contactos Registrados::")
            print(f"\n{'ID':<15} {'Nombre':<15}")
            print(f"-" * 30)
            for fila in contactos:
                print(f"{fila[0]:<15} {fila[1]:<15}")
            print(f"-" * 30)
        else:
            print("🚫 No hay contactos registrados 🚫")
            return
        id = input("\n\tIngresa el ID del contacto a eliminar: ").strip()
        cursor.execute("SELECT * FROM contacto WHERE id = %s", (id,))
        contacto = cursor.fetchone()
        if contacto:
            resp = input(f"¿Desea eliminar el contacto {contacto[1]} con ID {id}? (Si/No): ").upper().strip()
            if resp == "SI":
                cursor.execute("DELETE FROM contacto WHERE id = %s", (id,))
                conexionBD.commit()
                print("\n✔️ :: Contacto eliminado correctamente :: ✔️")
        else:
            print("\n\t🚫 :: ID no válido :: 🚫")
        cursor.close()