from conexionBD import *
import datetime

def registrar_transaccion(usuario_id, videojuego_id, tipo_transaccion):
    try:
        fecha = datetime.datetime.now()
        sql = "INSERT INTO transacciones (usuario_id, videojuego_id, tipo_transaccion, fecha) VALUES (%s, %s, %s, %s)"
        val = (usuario_id, videojuego_id, tipo_transaccion, fecha)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al registrar transacción: {e}")
        return False

def obtener_todas():
    try:
        sql = "SELECT * FROM transacciones"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener transacciones: {e}")
        return []