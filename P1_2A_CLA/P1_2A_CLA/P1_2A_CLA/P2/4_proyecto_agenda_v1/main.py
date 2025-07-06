import agenda

def main():
    agenda_contactos = {} 

    opcion=True
    while opcion:
     agenda.borrarPantalla()
     opcion=agenda.menu_principal()
     match opcion:
        case "1":  
            agenda.agregar_contacto(agenda_contactos)
            agenda.esperarTecla()
        case "2":
            agenda.mostrar_contacto(agenda_contactos)
            agenda.esperarTecla() 
        case "3":
            agenda.buscar_contacto(agenda_contactos)
            agenda.esperarTecla()   
        case "4":
            opcion=False    
            agenda.borrarPantalla()
            print(" Terminaste la ejecucion del SW")
        case _:
            opcion=True 
            print("Opción invalida vuelva a intentarlo") 
            agenda.esperarTecla()
if __name__ == "__main__":
    main()