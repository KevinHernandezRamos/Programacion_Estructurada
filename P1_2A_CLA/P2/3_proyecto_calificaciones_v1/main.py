#proyecto 3 
# Crear un proyecto que permita Gestionar (Administrar) calificaciones, colocar un menu de opciones para agregar, mostrar, calcular promedio calificaciones de un estudiante. 

#Notas: 
# 1.- Utilizar funciones y mandar llamar desde otro archivo (modulos)
# 2.- Utilizar list (bidimensional) para almacenar el nombre del alumno, asi como sus tres calificaciones

import calificaciones

def main():
    datos = []  

    opcion=True
    while opcion:
     calificaciones.borrarPantalla()
     opcion=calificaciones.menu_principal()

     match opcion:
        case "1":  
            calificaciones.agregar_calificaciones(datos)
            calificaciones.esperarTecla()
        case "2":
            calificaciones.mostrar_calificaciones(datos)
            calificaciones.esperarTecla() 
        case "3":
            calificaciones.calcular_promedios(datos)
            calificaciones.esperarTecla()   
        case "4":
            opcion=False    
            calificaciones.borrarPantalla()
            print(" Terminaste la ejecucion del SW")
        case _:
            opcion=True 
            print("Opción invalida vuelva a intentarlo") 
            calificaciones.esperarTecla()

if __name__ == "__main__":
    main()