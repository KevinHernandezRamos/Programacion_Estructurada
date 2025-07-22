import mysql.connector
from mysql.connector import Error

pelicula={}

def borrarPantalla():
    import os  
    os.system("cls")

def esperarTecla():
    input("\n\t\t... ⏎ Oprima cualquier tecla para continuar ...")  

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_peliculas"  
        )
        return conexion
    except Error as e:
        print(f"\n\t❌ El error que se presentó es: {e}")
        return None

def crearPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t🎬 .:: Crear Películas ::. 🎬 \n")
        pelicula["nombre"]=input("\t📝 Ingresa el nombre: ").strip()
        pelicula["categoria"]=input("\t📚 Ingresa la categoría: ").strip()
        pelicula["clasificacion"]=input("\t⭐ Ingresa la clasificación: ").strip()
        pelicula["genero"]=input("\t🎭 Ingresa el género: ").strip()
        pelicula["idioma"]=input("\t🌐 Ingresa el idioma: ").strip()
        
        cursor=conexionBD.cursor()
        sql="insert into peliculas (nombre,categoria,clasificacion,genero,idioma) value (%s,%s,%s,%s,%s)"
        val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"])
        cursor.execute(sql,val)
        conexionBD.commit()
        print("\n\t\t✅ ::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
        conexionBD.close()

def mostrarPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t📋 .:: Mostrar las Películas ::. 📋 \n")
        cursor=conexionBD.cursor()
        sql="select * from peliculas"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            print("\t🎥 Mostrar las Películas")
            print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
            print(f"-"*80)
            for pelis in registros:
                print(f"{pelis[0]:<10}{pelis[1]:<15}{pelis[2]:<15}{pelis[3]:<15}{pelis[4]:<15}{pelis[5]:<15}")
            print(f"-"*80)  
        else:
            print("\t❌ .:: No hay películas en el sistema ::..")   
        conexionBD.close()

def buscarPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t➕ .:: Buscar Películas ::. ➕ \n")
        nombre=input("\t🔍 Ingresa el nombre de la película a buscar: ").strip()
        cursor=conexionBD.cursor()
        sql="select * from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print("\t🎥 Mostrar las Películas")
            print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
            print(f"-"*80)
            for pelis in registros:
                print(f"{pelis[0]:<10}{pelis[1]:<15}{pelis[2]:<15}{pelis[3]:<15}{pelis[4]:<15}{pelis[5]:<15}")
            print(f"-"*80)  
        else:
            print("\t❌ .:: Películas no encontradas en el sistema ::..")
        conexionBD.close()

def borrarPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t🗑️ .:: Borrar Películas ::. 🗑️ \n")
        nombre=input("\t🔍 Ingresa el nombre de la película a borrar: ").strip()
        cursor=conexionBD.cursor()
        sql="select * from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print("\t🎥 Mostrar las Películas")
            print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
            print(f"-"*80)
            for pelis in registros:
                print(f"{pelis[0]:<10}{pelis[1]:<15}{pelis[2]:<15}{pelis[3]:<15}{pelis[4]:<15}{pelis[5]:<15}")
            print(f"-"*80) 
            resp=input(f"\t⚠️ ¿Deseas borrar la película {nombre}? (Si/No): ").lower().strip()
            if resp=="si":
                sql="delete from peliculas where nombre = %s"
                val=(nombre,)
                cursor.execute(sql,val)
                conexionBD.commit()
                print("\n\t\t✅ ::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
        else:
            print("\t❌ .:: Películas no encontradas en el sistema ::..")
        conexionBD.close()

def modificarPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t✏️ .:: Modificar Películas ::. ✏️ \n")
        nombre=input("\t🔍 Ingresa el nombre de la película a modificar: ").strip()
        cursor=conexionBD.cursor()
        sql="select * from peliculas where nombre=%s"
        val=(nombre,)
        cursor.execute(sql,val)
        registros=cursor.fetchall()
        if registros:
            print("\t✅ Película encontrada:")
            print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificacion':<15}{'Genero':<15}{'Idioma':<15}")
            print(f"-"*80)
            for pelis in registros:
                print(f"{pelis[0]:<10}{pelis[1]:<15}{pelis[2]:<15}{pelis[3]:<15}{pelis[4]:<15}{pelis[5]:<15}")
            print(f"-"*80)
            
            resp=input(f"\t⚠️ ¿Deseas modificar la película {nombre}? (Si/No): ").lower().strip()
            if resp=="si":
                pelicula["nombre"] = registros[0][1]
                pelicula["categoria"] = registros[0][2]
                pelicula["clasificacion"] = registros[0][3]
                pelicula["genero"] = registros[0][4]
                pelicula["idioma"] = registros[0][5]
                nuevo_nombre = input(f"\t📝 Ingresa el nuevo nombre ({pelicula['nombre']}): ").strip() or pelicula["nombre"]
                nueva_categoria = input(f"\t📚 Ingresa la nueva categoría ({pelicula['categoria']}): ").strip() or pelicula["categoria"]
                nueva_clasificacion = input(f"\t⭐ Ingresa la nueva clasificación ({pelicula['clasificacion']}): ").strip() or pelicula["clasificacion"]
                nuevo_genero = input(f"\t🎭 Ingresa el nuevo género ({pelicula['genero']}): ").strip() or pelicula["genero"]
                nuevo_idioma = input(f"\t🌐 Ingresa el nuevo idioma ({pelicula['idioma']}): ").strip() or pelicula["idioma"]
                
                pelicula["nombre"] = nuevo_nombre
                pelicula["categoria"] = nueva_categoria
                pelicula["clasificacion"] = nueva_clasificacion
                pelicula["genero"] = nuevo_genero
                pelicula["idioma"] = nuevo_idioma
                sql="update peliculas set nombre=%s, categoria=%s, clasificacion=%s, genero=%s, idioma=%s where nombre=%s"
                val=(pelicula["nombre"], pelicula["categoria"], pelicula["clasificacion"], pelicula["genero"], pelicula["idioma"], nombre)
                cursor.execute(sql,val)
                conexionBD.commit()
                print("\n\t\t✅ ::: ¡LA PELÍCULA SE MODIFICÓ CON ÉXITO! :::")
            else:
                print("\t❌ .:: Modificación cancelada ::..")
        else:
            print("\t❌ .:: Película no encontrada en el sistema ::..")
        conexionBD.close()