
import mysql.connector

conexion = mysql.connector.connect(user="root", password="" ,
                                   host = "localhost" ,
                                   database = "bd_peliculas" ,
                                   port = "3306")

print("CONEXION ESTABLECIDA CORRECTAMENTE" ,conexion)

# cursor = conexion.cursor()
# cursor.execute("CREATE DATABASE bd_peliculas")
# # cursor.execute("SHOW DATABASES")

# # for bd in cursor:
# #     print(bd)

# conexion.close()