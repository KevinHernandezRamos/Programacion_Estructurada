#PROYECTO 2
#Crear un proyecto que permita gestionar (administrar peliculas; colocar un menu de opciones para
#agregar, borrar, modificar, consultar, buscar y vaciar peliculas)

#NOTAS
#1.- Utilizar funciones y mandar llamar desde otro archivo
#2.- Utilizar una dict para almacenar los atrinutos y caracterizticas de las peliculas (nombre, categoria, clasificacion, genero, idioma) de las peliculas
# 7 opciones: agregar, borrar (quitar la película de la lista), consultar (consultar todas las películas), modificar, buscar (y si existe le puedes modificar el nombre)
# Utilizar un Match
# Menú de opciones con un si no existe volver a mostrar el menú


import peliculas

opcion = True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t🎥 ..::: CINEPOLIS CLON :::... 🎥 \n\t\t📽️ ..::: Sistema de Gestión de Películas :::... 📽️\n\t\t 1.- Crear 🎬 \n\t\t 2.- Borrar 🗑️ \n\t\t 3.- Mostrar 📋 \n\t\t 4.- Agregar Característica ➕ \n\t\t 5.- Modificar Característica ✏️ \n\t\t 6.- Borrar Característica ❌ \n\t\t 7.- SALIR 🚪")
    opcion = input("\t🎯 Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.crearPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.esperarTecla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.agregarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "5":
            peliculas.modificarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "6":
            peliculas.borrarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion = False
            peliculas.esperarTecla()
            print("\n\t👋 Terminaste la ejecución del SW")
        case _:
            input("\n\t❌ Opción inválida, vuelve a intentarlo ... por favor ⏎")






















# def mostrar_menu():
#     """Muestra el menú de opciones para gestionar películas"""
#     print("\n PELICULOLANDIA ")
#     print("1. Agregar película")
#     print("2. Borrar película")
#     print("3. Consultar todas las películas")
#     print("4. Modificar película")
#     print("5. Buscar película")
#     print("6. Vaciar lista de películas")
#     print("7. Salir")
#     return input("Seleccione una opción ( 1-7 ): ")

# def main():
#     peliculas = []  # Lista para almacenar los nombres de las peliculas
#     while True:
#         opcion = mostrar_menu()
#         match opcion:
#             case "1":
#                 nombre = input("Ingrese el nombre de la pelicula: ")
#                 peliculas.append(nombre)
#                 print(f"Pelicula '{nombre}' agregada correctamente")
            
#             case "2":
#                 nombre = input("Ingrese el nombre de la pelicula a borrar: ")
#                 if nombre in peliculas:
#                     peliculas.remove(nombre)
#                     print(f"Pelicula '{nombre}' borrada correctamente")
#                 else:
#                     print("Pelicula no existe")
            
#             case "3":
#                 if peliculas:
#                     print("\nLista de peliculas:")
#                     for i, pelicula in enumerate(peliculas, 1):
#                         print(f"{i}. {pelicula}")
#                 else:
#                     print("No hay peliculas en la lista")
            
#             case "4":
#                 nombre = input("Ingrese el nombre de la película a modificar: ")
#                 if nombre in peliculas:
#                     nuevo_nombre = input("Ingrese el nuevo nombre: ")
#                     indice = peliculas.index(nombre)
#                     peliculas[indice] = nuevo_nombre
#                     print(f"Pelicula modificada a '{nuevo_nombre}'.")
#                 else:
#                     print("La Pelicula no fue encontrada")
            
#             case "5":
#                 nombre = input("Ingrese el nombre de la película a buscar: ")
#                 if nombre in peliculas:
#                     print(f"Pelicula '{nombre}' encontrada en la lista.")
#                 else:
#                     print("Pelicula no encontrada.")
            
#             case "6":
#                 peliculas.clear()
#                 print("Lista de películas vaciada.")
            
#             case "7":
#                 print("Estas saliendo del software")
#                 break
            
#             case _:
#                 print("Opción no es valida por favor selecciona una opción entre (1 - 7)")
        
#         # Preguntar si desea continuar
#         continuar = input("\n¿Deseas regresar al menu? (s/n): ").lower()
#         if continuar != 's':
#             print("Saliendo del software")
#             break

# if __name__ == "__main__":
#     main()
