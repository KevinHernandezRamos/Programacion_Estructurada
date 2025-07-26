lista = []
def almacenar():
    resp = "si"
    while resp == "si":
        try:
            numero = float(input("Ingresa Numero: ").strip())
            lista.append(numero)
            resp = input("¿Deseas ingresar otro numero? (Si/No): ").lower().strip()
        except ValueError:
            print("Por favor, ingresa un número válido")
            continue

def buscar():
    try:
        numero = float(input("Ingresa un numero: ").strip())
        if numero in lista:
            for i in range(len(lista)):
                if numero == lista[i]:
                    print(f"El numero {numero} se encuentra en la posición: {i}")
        else:
            print("El numero no está en la lista")
    except ValueError:
        print("Por favor, ingresa un número válido")

almacenar()
buscar()