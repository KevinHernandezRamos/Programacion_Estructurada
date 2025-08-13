import mysql.connector

try:
    conexion=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_gestionjuegos"
    )
    cursor=conexion.cursor(buffered=True)
except:
    print(f"Error al conectarse a la base de datos vuelve a intentarlo de nuevo mas tarde") 