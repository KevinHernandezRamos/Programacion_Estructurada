agenda_contactos = {
                    "RUBEN":["6181234567","ruben@gmail.com"],
                    "DANIEL":["6181234568","daniel@gmail.com"],
                    "XIMENA":["6181234569","xime@gmail.com"],
                   }


def borrarPantalla():  
    import os
    os.system("cls")

def esperarTecla():  
    input("Oprima cualquier tecla para continuar ⏎ ")

def menu_principal():  
    print("📝..::: Sistema de Gestión de Agenda de Contactos :::... 📝\n")
    print("1️\tAgregar contacto ")
    print("2️\tMostrar todos los contactos ")
    print("3️\tBuscar contacto por nombre ")
    print("4️\tSALIR \n")
    opcion = input("😎 Elige una opción (1-4): ")
    return opcion