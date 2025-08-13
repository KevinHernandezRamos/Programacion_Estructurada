from funciones import (
    borrarPantalla, esperarTecla, mostrar_titulo,
    menu_inicial, menu_administrador, menu_cliente_principal, menu_cliente_secundario,
    formatear_lista_juegos, formatear_transacciones
)
from Usuarios import usuarios
from Videojuegos import videojuegos
from Transacciones import transacciones
import getpass

def exportar_a_excel_inventario():
    import pandas as pd
    datos = videojuegos.mostrar()
    if datos:
        df = pd.DataFrame(datos)
        df.to_excel("inventario.xlsx", index=False)
        print("\n✅ Inventario exportado a 'inventario.xlsx'")
    else:
        print("\n⚠ No hay datos para exportar.")

def exportar_a_excel_transacciones():
    import pandas as pd
    datos = transacciones.obtener_todas()
    if datos:
        df = pd.DataFrame(datos)
        df.to_excel("transacciones.xlsx", index=False)
        print("\n✅ Transacciones exportadas a 'transacciones.xlsx'")
    else:
        print("\n⚠ No hay datos para exportar.")


def ejecutar_modo_administrador():
    while True:
        opcion = menu_administrador()
        
        if opcion == "1":
            registrar_videojuego()
            esperarTecla()
        elif opcion == "2":
            mostrar_inventario(True)  
        elif opcion == "3":
            procesar_venta(es_admin=True)
            esperarTecla()
        elif opcion == "4":
            procesar_renta(es_admin=True)
            esperarTecla()
        elif opcion == "5":
            mostrar_transacciones(True) 
        elif opcion == "6":
            break
        else:
            print("\n❌ Opción inválida, vuelve a intentarlo. ❌")
            esperarTecla()

def ejecutar_modo_cliente():
    usuario = None
    while True:
        opcion = menu_cliente_principal()
        
        if opcion == "1":
            usuario = login_cliente()
            if usuario:
                ejecutar_menu_cliente_secundario(usuario)
        elif opcion == "2":
            if registrar_cliente():
                usuario = login_cliente()
                if usuario:
                    ejecutar_menu_cliente_secundario(usuario)
        elif opcion == "3":
            break
        else:
            print("\n❌ Opción inválida, por favor elige una opción válida.❌")
            esperarTecla()

def ejecutar_menu_cliente_secundario(usuario):
    while True:
        opcion = menu_cliente_secundario(usuario[1])
        
        if opcion == "1":
            mostrar_inventario(False)  
        elif opcion == "2":
            procesar_venta(usuario_id=usuario[0])
            esperarTecla()
        elif opcion == "3":
            procesar_renta(usuario_id=usuario[0])
            esperarTecla()
        elif opcion == "4":
            print("\n👋 Gracias por visitar nuestra tienda Vuelve pronto")
            break
        else:
            print("\n❌ Opción inválida, por favor elige una opción válida ❌")
            esperarTecla()


def registrar_cliente():
    borrarPantalla()
    mostrar_titulo("Registro de Cliente")
    
    nombre = input("👤 Nombre: ").strip().title()
    apellidos = input("👥 Apellido: ").strip().title()
    
    while True:
        email = input("📧 Gmail: ").strip().lower()
        if '@' in email and '.' in email:
            break
        print("❌ Por favor, ingresa un correo válido ❌")
    
    contrasena = getpass.getpass("🔒 Contraseña: ").strip()
    
    if usuarios.registrar(nombre, apellidos, email, contrasena):
        print(f"\n🎉 ¡Registro exitoso! Bienvenido, {nombre}.")
        return True
    print("\n❌ Error al registrar. El correo ya está en uso intenta de nuevo")
    return False

def login_cliente():
    borrarPantalla()
    mostrar_titulo("Inicio de Sesión")
    
    email = input("📧 Gmail: ").strip().lower()
    contrasena = getpass.getpass("🔒 Contraseña: ").strip()
    
    usuario = usuarios.inicio_sesion(email, contrasena)
    if usuario:
        print(f"\n🎮 Bienvenido de nuevo {usuario[1]}!")
        return usuario
    print("\n❌ Correo o contraseña incorrectos")
    return None

def registrar_videojuego():
    borrarPantalla()
    mostrar_titulo("Registro de Videojuego")
    
    nombre = input("🎮 Nombre del videojuego: ").strip().title()
    
    while True:
        tipo = input("🔘 Tipo (venta/renta): ").lower()
        if tipo in ["venta", "renta"]:
            break
        print("❌ Tipo inválido ingresa solamente 'venta' o 'renta'")
    
    while True:
        try:
            precio = float(input("💲 Precio: "))
            if precio > 0: break
            print("❌ El precio debe ser mayor a 0")
        except ValueError:
            print("❌ Por favor, ingresa un número válido")
    
    while True:
        try:
            stock = int(input("📦 Cantidad disponible: "))
            if stock >= 0: break
            print("❌ El stock no puede ser negativo")
        except ValueError:
            print("❌ Por favor, ingresa un número entero válido")
    
    if videojuegos.registrar(nombre, tipo, precio, stock):
        print(f"\n✅ {nombre} registrado correctamente")
    else:
        print("\n❌ No se pudo registrar el videojuego")

def mostrar_inventario(es_admin=False):
    borrarPantalla()
    mostrar_titulo("Catálogo de Videojuegos")
    formatear_lista_juegos(videojuegos.mostrar())
    
    opcion = input("\n📂 ¿Desea exportar a Excel? (S/N): ").strip().lower()
    if opcion == "s":
        exportar_a_excel_inventario()
        esperarTecla()
    else:
        esperarTecla()

def mostrar_transacciones(es_admin=False):
    borrarPantalla()
    mostrar_titulo("Historial de Transacciones")
    formatear_transacciones(transacciones.obtener_todas())
    
    opcion = input("\n📂 ¿Desea exportar a Excel? (S/N): ").strip().lower()
    if opcion == "s":
        exportar_a_excel_transacciones()
        esperarTecla()
    else:
        esperarTecla()

def procesar_venta(es_admin=False, usuario_id=None):
    borrarPantalla()
    mostrar_titulo("Venta de Videojuego" if es_admin else "Compra de Videojuego")
    
    formatear_lista_juegos([j for j in videojuegos.mostrar() if j["tipo"] == "venta"], "venta")
    
    nombre = input("\n🎮 Nombre del videojuego: ").strip()
    juego = videojuegos.buscar(nombre)
    
    if not juego:
        print("\n❌ Videojuego no encontrado ❌")
        return
    
    if juego["stock"] <= 0:
        print("\n❌ No hay stock disponible ❌")
        return
    
    if not es_admin and juego["tipo"] != "venta":
        print("\n❌ Este videojuego no está disponible para compra ❌")
        return
    
    print(f"\n💲 Precio: ${juego['precio']}")
    
    try:
        pago = float(input("💰 Ingresa el monto a pagar: $"))
        if pago < juego["precio"]:
            print("\n❌ Monto insuficiente ❌")
            return
        
        if videojuegos.actualizar_stock(juego["id"], juego["stock"] - 1):
            if not es_admin and usuario_id is not None:
                transacciones.registrar_transaccion(usuario_id, juego["id"], "venta")
            print(f"\n✅ {'Venta' if es_admin else 'Compra'} exitosa de {juego['nombre']}!")
            
            if pago > juego["precio"]:
                print(f"🔄 Cambio: ${pago - juego['precio']:.2f}.")
            
            print(f"📦 Stock restante: {juego['stock'] - 1}")
        else:
            print("\n❌ Error al actualizar el stock ❌")
    except ValueError:
        print("\n❌ Por favor, ingresa un monto válido ❌")

def procesar_renta(es_admin=False, usuario_id=None):
    borrarPantalla()
    mostrar_titulo("Renta de Videojuego")
    
    formatear_lista_juegos([j for j in videojuegos.mostrar() if j["tipo"] == "renta"], "renta")
    
    nombre = input("\n🎮 Nombre del videojuego: ").strip()
    juego = videojuegos.buscar(nombre)
    
    if not juego:
        print("\n❌ Videojuego no encontrado❌ ")
        return
    
    if juego["stock"] <= 0:
        print("\n❌ No hay stock disponible ❌")
        return
    
    if not es_admin and juego["tipo"] != "renta":
        print("\n❌ Este videojuego no está disponible para renta ❌")
        return
    
    print(f"\n💲 Precio de renta: ${juego['precio']}")
    
    try:
        pago = float(input("💰 Ingresa el monto a pagar: $"))
        if pago < juego["precio"]:
            print("\n❌ Monto insuficiente ❌")
            return
        
        if videojuegos.actualizar_stock(juego["id"], juego["stock"] - 1):
            if not es_admin and usuario_id is not None:
                transacciones.registrar_transaccion(usuario_id, juego["id"], "renta")
            print(f"\n✅ Renta exitosa de {juego['nombre']}!")
            
            if pago > juego["precio"]:
                print(f"🔄 Cambio: ${pago - juego['precio']:.2f}")
            
            print(f"📦 Stock restante: {juego['stock'] - 1}")
        else:
            print("\n❌ Error al actualizar el stock ❌")
    except ValueError:
        print("\n❌ Por favor, ingresa un monto válido ❌")

def main():
    while True:
        opcion = menu_inicial()
        
        if opcion == "1":
            borrarPantalla()
            contraseña = getpass.getpass("🔒 Ingresa la contraseña del administrador: ")
            if usuarios.verificar_admin(contraseña):
                ejecutar_modo_administrador()
            else:
                print("\n❌ Contraseña incorrecta Acceso denegado ❌")
                esperarTecla()
        elif opcion == "2":
            ejecutar_modo_cliente()
        elif opcion == "3":
            print("\n👋 Terminó la ejecución del SW")
            break
        else:
            print("\n❌ Opción no válida, intenta de nuevo❌")
            esperarTecla()

if __name__ == "__main__":
    main()
