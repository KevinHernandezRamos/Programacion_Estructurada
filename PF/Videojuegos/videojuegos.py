from conexionBD import *

def registrar(nombre, tipo, precio, stock):
    try:
        sql = "insert into videojuegos(nombre, tipo, precio, stock) values (%s, %s, %s, %s)"
        val = (nombre, tipo, precio, stock)
        cursor.execute(sql, val)
        conexion.commit()
        return {"id": cursor.lastrowid, "nombre": nombre, "tipo": tipo, "precio": precio, "stock": stock}
    except:
        return None

def mostrar():
    try:
        sql = "select * from videojuegos"
        cursor.execute(sql)
        registros = cursor.fetchall()
        return [{"id": row[0], "nombre": row[1], "tipo": row[2], "precio": row[3], "stock": row[4]} for row in registros]
    except:
        return []

def mostrar_renta():
    try:
        sql = "select * from videojuegos where tipo = 'renta' and stock > 0"
        cursor.execute(sql)
        registros = cursor.fetchall()
        return [{"id": row[0], "nombre": row[1], "tipo": row[2], "precio": row[3], "stock": row[4]} for row in registros]
    except:
        return []

def buscar(nombre):
    try:
        sql = "select * from videojuegos where nombre = %s"
        val = (nombre,)
        cursor.execute(sql, val)
        registro = cursor.fetchone()
        if registro:
            return {"id": registro[0], "nombre": registro[1], "tipo": registro[2], "precio": registro[3], "stock": registro[4]}
        return None
    except:
        return None

def actualizar_stock(id, nuevo_stock):
    try:
        sql = "update videojuegos set stock = %s where id = %s"
        val = (nuevo_stock, id)
        cursor.execute(sql, val)
        conexion.commit()
        return cursor.rowcount > 0
    except:
        return False