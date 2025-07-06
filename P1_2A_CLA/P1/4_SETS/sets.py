"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
#import os
# os.system("clear")


# paises=["Mexico","Brasil","España","Canada"]
# print(paises)
# print(paises[1])

# paises={"Mexico","Brasil","España","Canada"}
# print(paises)

#FUNCIONES O OPERACIONES



#PROGRAMA QUE SOLICITE LOS EMAIL DE LOS ALUMNOS DE LA UTD 
#ALMACENAR UNA LISTA Y POSTERIORMENTE MOSTRAR EN PANTALLA LOS EMAIL SIN DUPLICADOS

emails=[]
resp="si"

while resp=="si":
    emails.append(input("INGRESA UN EMAIL: "))
    resp=input("¿DESEAS AGREGAR OTRO EMAIL? ").lower()

emails_set=set(emails)
emails=list(emails_set)
print(emails)