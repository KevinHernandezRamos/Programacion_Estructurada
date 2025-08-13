import os
import getpass

def borrarPantalla():
    os.system('cls')

def esperarTecla():
    input("\n🔘 Presiona Enter para continuar...")

def mostrar_titulo(titulo):
    print(f"\n{'='*50}")
    print(f"🌟 {titulo.upper()} 🌟")
    print(f"{'='*50}\n")

def menu_inicial():
    borrarPantalla()
    mostrar_titulo("Bienvenido al Sistema de Gestión de Videojuegos")
    print("1) 👑 Modo Administrador")
    print("2) 👤 Modo Cliente")
    print("3) 🚪 Salir")
    opcion = input("\n🔹 Elige una opción (1-3): ")
    return opcion.upper()

def menu_administrador():
    borrarPantalla()
    mostrar_titulo("Menú Administrador")
    print("1) 🎮 Registrar videojuego")
    print("2) 📋 Mostrar inventario completo")
    print("3) 💵 Vender videojuego")
    print("4) ⏱️ Rentar videojuego")
    print("5) 📊 Reporte de Transacciones")
    print("6) ↩️ Volver al menú inicial")
    return input("\n🔹 Elige una opción (1-6): ")

def menu_cliente_principal():
    borrarPantalla()
    mostrar_titulo("Modo Cliente")
    print("1) 🔑 Iniciar Sesión")
    print("2) 📝 Registrarse")
    print("3) ↩️ Volver al menú inicial")
    return input("\n🔹 Elige una opción (1-3): ")

def menu_cliente_secundario(nombre_usuario):
    borrarPantalla()
    mostrar_titulo(f"Tienda de Videojuegos --- Bienvenido {nombre_usuario}")
    print("1) 🕹️ Ver catálogo completo")
    print("2) 💰 Comprar videojuego")
    print("3) ⏳ Rentar videojuego")
    print("4) 🏠 Salir de la tienda")
    return input("\n🔹 ¿Qué deseas hacer? (1-4): ")

def formatear_lista_juegos(juegos, tipo=None):
    if not juegos:
        print("📭 No hay videojuegos disponibles ❌" + 
              (f" para {tipo}" if tipo else "") + ".")
        return
    
    encabezado = f"{'ID':<5}{'Nombre':<30}{'Precio':<10}{'Stock':<10}"
    if not tipo:
        encabezado = f"{'ID':<5}{'Nombre':<30}{'Tipo':<10}{'Precio':<10}{'Stock':<10}"
    
    print(encabezado)
    print("-"*(55 if tipo else 65))
    
    for juego in juegos:
        if tipo:
            print(f"{juego['id']:<5}{juego['nombre']:<30}${juego['precio']:<9}{juego['stock']:<10}")
        else:
            tipo_emoji = "💰" if juego["tipo"] == "venta" else "⏳"
            print(f"{juego['id']:<5}{juego['nombre']:<30}{tipo_emoji + ' ' + juego['tipo']:<10}${juego['precio']:<9}{juego['stock']:<10}")

def formatear_transacciones(transacciones):
    if not transacciones:
        print("📭 No hay transacciones registradas ❌")
        return
    
    print(f"{'ID':<5}{'Usuario':<20}{'Videojuego':<25}{'Tipo':<10}{'Fecha':<20}")
    print("-"*80)
    
    for trans in transacciones:
        tipo_emoji = "💰" if trans[3] == "venta" else "⏳"
        print(f"{trans[0]:<5}{trans[1] if trans[1] else 'Admin':<20}{trans[2]:<25}{tipo_emoji + ' ' + trans[3]:<10}{trans[4].strftime('%Y-%m-%d %H:%M'):<20}")