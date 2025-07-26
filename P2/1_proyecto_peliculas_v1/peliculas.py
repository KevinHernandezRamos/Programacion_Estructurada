peliculas = []

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    print("\n\t\t... Oprima cualquier tecla para continuar... ⏎")
    input()

def agregarPeliculas():
    borrarPantalla()
    print("\n\t🎬 .:: Agregar Películas ::. 🎬 \n")
    peliculas.append(input("📽️ Ingresa el nombre: ").upper().strip())
    print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! ✅ :::")

def consultarPeliculas():
    borrarPantalla()
    print("\n\t📋 .:: Consultar o Mostrar las Películas ::. 📋 \n")
    if len(peliculas) > 0:
        for i in range(0, len(peliculas)):
            print(f"\t{i+1}: {peliculas[i]} 🎞️")
    else:
        print("\n\t .:: No hay películas en el sistema en este momento ::. 😔")

def vaciarPeliculas():
    borrarPantalla()
    print("\n\t🗑️ .:: Vaciar Todas las Películas ::. 🗑️ \n")
    resp = input("¿Deseas quitar TODAS las Películas del sistema? (Si/No): ").lower().strip()
    if resp == "si":
        peliculas.clear()
        print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! ✅ :::")

def buscarPeliculas():
    borrarPantalla()
    print("\n\t🔍 .:: Buscar Películas ::. 🔍 \n")
    pelicula_buscar = input("📽️ Ingresa el nombre de la película a buscar: ").upper().strip()
    encontro = 0
    if not (pelicula_buscar in peliculas):
        print("\n\t\t No se encontró la película 😔")
    else:
        for i in range(0, len(peliculas)):
            if pelicula_buscar == peliculas[i]:
                print(f"\nLa película {pelicula_buscar} sí la tenemos y está en la casilla {i+1} 🎞️")
                encontro += 1
        print(f"\nTenemos {encontro} películas con este título 📊")
        print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! ✅ :::")

def eliminarPeliculas():
    borrarPantalla()
    print("\n\t🗑️ .:: Borrar Películas ::. 🗑️ \n")
    pelicula_buscar = input("📽️ Ingresa el nombre de la película a eliminar: ").upper().strip()
    encontro = 0
    if not (pelicula_buscar in peliculas):
        print("\n\t\t No se encontró la película 😔")
    else:
        resp = "si"
        while pelicula_buscar in peliculas and resp == "si":
            resp = input("¿Deseas borrar la película del sistema? (Si/No): ").lower().strip()
            if resp == "si":
                posicion = peliculas.index(pelicula_buscar)
                print(f"\nLa película que se borró {pelicula_buscar} estaba en la casilla {posicion+1} 🎞️")
                peliculas.remove(pelicula_buscar)
                encontro += 1
                print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! ✅ :::")
        print(f"\n\tSe borraron {encontro} películas con este título 📊")

def actualizarPeliculas():
    borrarPantalla()
    print("\n\t✏️ .:: Actualizar Películas ::. ✏️ \n")
    pelicula_buscar = input("📽️ Ingresa el nombre de la película a actualizar: ").upper().strip()
    if not (pelicula_buscar in peliculas):
        print("\n\t\t No se encontró la película 😔")
    else:
        resp = input(f"¿Deseas actualizar la película '{pelicula_buscar}'? (Si/No): ").lower().strip()
        if resp == "si":
            nuevo_nombre = input("📝 Ingresa el nuevo nombre de la película: ").upper().strip()
            posicion = peliculas.index(pelicula_buscar)
            peliculas[posicion] = nuevo_nombre
            print(f"\nLa película '{pelicula_buscar}' fue actualizada a '{nuevo_nombre}' en la casilla {posicion+1} 🎞️")
            print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! ✅ :::")