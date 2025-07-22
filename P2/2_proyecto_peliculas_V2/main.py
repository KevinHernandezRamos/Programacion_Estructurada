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