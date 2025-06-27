#Dict u objeto para almacenar los atributos (Nombre, Categoria, Clasificacion, Genero, Idioma) y sus valores



pelicula = {
    "nombre": "",
    "categoría": "",
    "clasificación": "",
    "género": "",
    "idioma": ""
}

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t\t... Oprima cualquier tecla para continuar... ⏎")

def crearPeliculas():
    borrarPantalla()
    print("\n\t🎬 .:: Alta de Películas ::. 🎬 \n")
    pelicula.update({"nombre": input("📽️ Ingresa el nombre: ").upper().strip()})
    pelicula.update({"categoría": input("📂 Ingresa la categoría: ").upper().strip()})
    pelicula.update({"clasificación": input("⭐ Ingresa la clasificación: ").upper().strip()})
    pelicula.update({"género": input("🎭 Ingresa el género: ").upper().strip()})
    pelicula.update({"idioma": input("🌐 Ingresa el idioma: ").upper().strip()})
    print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! ✅ :::")

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t📋 .:: Consultar o Mostrar la Película ::. 📋 \n")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t{i.capitalize()}: {pelicula[i]} 🎞️")
    else:
        print("\n\t .:: No hay películas en el sistema ::. 😔")

def borrarPeliculas():
    borrarPantalla()
    print("\n\t🗑️ .:: Borrar o Quitar Todas las Películas ::. 🗑️ \n")
    resp = input("¿Deseas borrar o quitar todas las películas del sistema? (Si/No): ").lower().strip()
    if resp == "si":
        pelicula.clear()
        print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! ✅ :::")

def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t➕ .:: Agregar Características a Películas ::. ➕ \n")
    atributo = input("📝 Ingresa la nueva característica de la película: ").lower().strip()
    valor = input(f"💡 Ingresa el valor de la característica '{atributo}': ").lower().strip()
    pelicula[atributo] = valor
    print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! ✅ :::")

def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t✏️ .:: Modificar Características de Películas ::. ✏️ \n")
    if len(pelicula) > 0:
        print("\n\tValores actuales: 📋")
        for i in pelicula:
            print(f"\t{i.capitalize()}: {pelicula[i]} 🎞️")
        for i in pelicula:
            resp = input(f"\t¿Deseas cambiar el valor de '{i}'? (Si/No): ").lower().strip()
            if resp == "si":
                pelicula.update({i: input(f"\t🔄 Ingresa el nuevo valor para '{i}': ").upper().strip()})
                print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! ✅ :::")
    else:
        print("\n\t .:: No hay películas en el sistema ::. 😔")
        esperarTecla()

def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t❌ .:: Borrar Características de una Película ::. ❌ \n")
    if len(pelicula) == 0:
        print("\n\t .:: No hay películas en el sistema ::. 😔")
        esperarTecla()
    else:
        print("\n\tCaracterísticas disponibles en la película: 📋")
        for caracteristica in pelicula:
            print(f"\t- {caracteristica.capitalize()} 🎞️")
        opcion = input("\n\t¿Deseas borrar una característica de la película? (Si/No): ").lower().strip()
        if opcion == "si":
            atributo = input("\n\t🔍 Ingresa la característica a eliminar: ").lower().strip()
            if atributo in pelicula:
                confirmacion = input(f"\n\t¿Estás seguro de que deseas eliminar la característica '{atributo}'? (Si/No): ").lower().strip()
                if confirmacion == "si":
                    del pelicula[atributo]
                    print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! ✅ :::")
                else:
                    print("\n\t\t::: Operación cancelada por el usuario. 🚫 :::")
            else:
                print(f"\n\t .:: La característica '{atributo}' no fue encontrada en la película ::. 😔")
        else:
            print("\n\t .:: Operación cancelada ::. 🚫")
        esperarTecla()