import mysql.connector
from mysql.connector import Error

def borrarPantalla():
    import os
    os.system("cls") 

def esperarTecla():
    input("Oprima cualquier tecla para continuar ⏎")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_calificaciones"
        )
        return conexion 
    except Error as e:
        print(f"Error al conectar a la BD: {e} 🚫")
        return None

def menu_principal():
    print("...:::Sistema de Gestión de Calificaciones 📚 :::...\n\t\t1. Agregar Calificaciones ➕\n\t\t2. Mostrar Calificaciones 📋\n\t\t3. Calcular el promedio 📊\n\t\t4. Buscar Alumno 🔍\n\t\t5. SALIR 🚪")
    opcion = input("\n\t\tElige una opción (1-5): ")
    return opcion

def agregar_calificaciones():
    borrarPantalla()
    conexion = conectar()
    if conexion != None:
        print("\n\t\tAgregar Calificaciones 📝")
        nombre = input("Ingresa el nombre del alumno: ").upper().strip()
        calificaciones = []
        for i in range(1, 4):
            while True:
                try:
                    cal = float(input(f"Ingresa la calificación {i} 🎓: "))
                    if 0 <= cal <= 10:
                        calificaciones.append(cal)
                        break
                    else:
                        print("⚠️ Ingresa un valor entre 1-10 ⚠️")
                except ValueError:
                    print(" ❌ Ingresa un valor numérico ❌")
        cursor = conexion.cursor()
        sql = "INSERT INTO alumnos (nombre, cal1, cal2, cal3) VALUES (%s, %s, %s, %s)"
        val = (nombre, calificaciones[0], calificaciones[1], calificaciones[2])
        cursor.execute(sql, val)
        conexion.commit()
        print("::: Acción realizada con éxito ::: 🎉")

def mostrar_calificaciones():
    borrarPantalla()
    conexion = conectar()
    if conexion != None:
        cursor = conexion.cursor()
        sql = "SELECT * FROM alumnos"
        cursor.execute(sql)
        registros = cursor.fetchall()
        if registros:
            print(f"{'Nombre':<15}{'CALIF 1':<10}{'CALIF 2':<10}{'CALIF 3':<10}")
            print("-" * 50)
            for fila in registros:
                print(f"{fila[1]:<15}{fila[2]:<10}{fila[3]:<10}{fila[4]:<10}")
            print("-" * 50)
            print(f"Son {len(registros)} alumnos registrados ✔")
        else:
            print("❌ No hay calificaciones en el sistema ❌")

def calcular_promedios():
    borrarPantalla()
    conexion = conectar()
    if conexion != None:
        cursor = conexion.cursor()
        sql = "SELECT nombre, cal1, cal2, cal3 FROM alumnos"
        cursor.execute(sql)
        regis = cursor.fetchall()
        if regis:
            print(f"{'Nombre':<15}{'Promedio':<10}")
            print("-" * 30)
            total = 0
            for fila in regis:
                promedio = (fila[1] + fila[2] + fila[3]) / 3
                print(f"{fila[0]:<15}{promedio:<10.2f}")
                total += promedio
            grupo = total / len(regis)
            print("-" * 30)
            print(f"El promedio del grupo es: {grupo:.2f} 📈")
        else:
            print("❌ No hay calificaciones en el sistema ❌")


def buscar_alumno():
    borrarPantalla()
    conexion = conectar()
    if conexion != None:
        cursor = conexion.cursor()
        sql = "SELECT nombre FROM alumnos"
        cursor.execute(sql)
        registros = cursor.fetchall()
        if registros:
            print("📋 Alumnos registrados:")
            print(f"{'Nombre':<15}")
            print("-" * 20)
            for fila in registros:
                print(f"{fila[0]:<15}")
            print("-" * 20)
            print(f"Son {len(registros)} alumnos registrados 😎")
        else:
            print("❌ No hay alumnos registrados en el sistema ❌")

        print("\n Buscar a un alumno por nombre 🔍")
        nombre = input("Ingresa el nombre del alumno a buscar 🔎: ").upper().strip()
        sql = "SELECT * FROM alumnos WHERE nombre = %s"
        val = (nombre,)
        cursor.execute(sql, val)
        buscar = cursor.fetchone()
        if buscar:
            print(f"\n Información de {nombre}📋:")
            print(f"{'Nombre':<15}{'CALIF 1':<10}{'CALIF 2':<10}{'CALIF 3':<10}")
            print("-" * 50)
            print(f"{buscar[1]:<15}{buscar[2]:<10}{buscar[3]:<10}{buscar[4]:<10}")
            print("-" * 50)
        else:
            print(f"❌ No se encontró al alumno {nombre}, inténtalo de nuevo ❌")