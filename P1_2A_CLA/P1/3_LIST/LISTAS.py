
#EJEMPLO 1 CREAR UNA LISTA DE NUMEROS E IMPRIMIR EL CONTENIDO

NUMEROS=[50,100,150,200,250]

#1ERA FORMA  LOS IMPRIME TODOS EN LINEA

print(NUMEROS)

#2DA FORMA TRABAJA CON EL VALOR - LOS IMPRIME TODOS HACIA ABAJO

for i in NUMEROS:
    print(i)

#3RA FORMA TRABAJA CON LOS INDICES

for i in range(0,len(NUMEROS)):
    print(NUMEROS[i])


#CREAR UNA LISTA DE PALABRAS Y POSTERIORMENTE BUSCAR LA COINCIDENCIA DE UNA PALABRA

PALABRAS=["CORVETTE","PORSCHE","PORSCHE","LAMBO"]

"PORSCHE" in PALABRAS

print("PORSCHE" in PALABRAS)

#2DO ESCENARIO

PALABRAS=["CORVETTE","PORSCHE","PORSCHE","LAMBO"]
PALABRA_BUSCAR=input("DIME LA PALABRA A BUSCAR: ")

if PALABRA_BUSCAR in PALABRAS:
    print("SI SE ENCONTRO LA PALABRA:")
else:
    print("NO SE ENCONTRO LA PALABRA")


#3RA FORMA
ENCONTRO=False
for i in PALABRAS:
       if i==PALABRA_BUSCAR:
           ENCONTRO=True
if ENCONTRO==True:
     print("SI SE ENCONTRO LA PALABRA:")
else:
     print("NO SE ENCONTRO LA PALABRA")


#4TA FORMA
ENCONTRO=False
for i in range(0,len(NUMEROS)):
       if PALABRAS[i]==PALABRA_BUSCAR:
           ENCONTRO=True
if ENCONTRO:
     print("SI SE ENCONTRO LA PALABRA:")
else:
     print("NO SE ENCONTRO LA PALABRA")

#EJEMPLO 3 AÑADIR ELEMENTO A LA LISTA
NUMEROS=[]
OPC="si"
while OPC == "si":
     NUMEROS=float(input("DAME UN NUMERO ENTERO O DECIMAL: "))
     NUMEROS.append(NUMEROS)
     OPC = input("¿DESEAS SOLICITAR OTRO NUMERO? SI / NO ").lower()
     print(NUMEROS)

#4TA FORMA

#EJEMPLO 3 AÑADIR ELEMENTO A LA LISTA
NUMEROS=[]
OPC="si"
while OPC == "si":
     NUMEROS=float(input("DAME UN NUMERO ENTERO O DECIMAL: "))
     NUMEROS.appendf(float(input("DAME UN NUMERO ENTERO O DECIMAL: ")))
     OPC = input("¿DESEAS SOLICITAR OTRO NUMERO? SI / NO ").lower()
     print(NUMEROS)


#CREAR UNA LISTA MULTIDIMENSIONAL (MATRIZ) QUE ALMACENE EL NOMBRE Y TELEFONO DE 4 PERSONAS

agenda=[
        ["Carlos","6181234567"],
        ["Alberto","6181478525"],
        ["Martin","6183215487"]
       ]

print(agenda)

for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])    

cadena=""
for r in range(0,3):
    for c in range(0,2):
      cadena+=f"{agenda[r][c]}, "
    cadena+="\n"     
print(cadena) 