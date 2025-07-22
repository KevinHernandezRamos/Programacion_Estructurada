#PROYECTO 1
#Crear un proyecto que permita gestionar (administrar peliculas; colocar un menu de opciones para
#agregar, borrar, modificar, consultar, buscar y vaciar peliculas)

# NOTAS:
# 1.- Utilizar funciones y mandar llamar desde otro archivo.
# 2.- Utilizar una lista para almacenar el nombre de las películas.
# 7 opciones: agregar, borrar (quitar la película de la lista), consultar (consultar todas las películas), modificar, buscar (y si existe le puedes modificar el nombre)
# Utilizar un Match
# Menú de opciones con un si no existe volver a mostrar el menú

import peliculas

opcion = True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t🎥 ..::: CINEPOLIS CLON :::... 🎥 \n\t\t📽️ ..::: Sistema de Gestión de Películas :::... 📽️\n\t\t 1.- Agregar 🎬 \n\t\t 2.- Eliminar 🗑️ \n\t\t 3.- Actualizar ✏️ \n\t\t 4.- Consultar 📋 \n\t\t 5.- Buscar 🔍 \n\t\t 6.- Vaciar 🗑️ \n\t\t 7.- SALIR 🚪")
    opcion = input("\t🎯 Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.eliminarPeliculas()
            peliculas.esperarTecla()
        case "3":
            peliculas.actualizarPeliculas()
            peliculas.esperarTecla()
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
            opcion = False
            peliculas.esperarTecla()
            print("\n\t👋 Terminaste la ejecución del SW")
        case _:
            input("\n\t❌ Opción inválida, vuelve a intentarlo ... por favor ⏎")
