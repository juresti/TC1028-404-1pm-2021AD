def listaP(numPer):
    lPer = []
    for num in range(numPer):
        nombre = input(f"{num +1}. Dime el nombre: ")
        lPer.append(nombre)
    return lPer

def impPer(listaP):
    "Recibe una lista de personas y las imprime en consola"
    if (listaP):
        for persona in listaP:
            print(persona)
    else:
        print("Tu lista está vacia. Selecciona captura personas")
        
def menuPer():
    print("\nBienvenido al sistema de control de personas")
    print("1) Captura personas")
    print("2) Imprime personas")
    print("3) Salir")
    op = int(input("Dime tu opcion: "))
    return op

def controlPersonas():
    selec = 0
    listaPer = []
    while (selec != 3):
        selec = menuPer()
        if (selec == 1):
            numP = int(input("Dime cuantas personas capturaras: "))
            listaPer = listaP(numP)
        elif (selec == 2):
            impPer(listaPer)
        elif (selec == 3):
            print("Hasta luego \n")
        else:
            print("Error. Valores validos del 1 al 3")

#controlPersonas()

def listaEdades(datosP):
    edades = []
    for datoPersona in datosP:
        edades.append(datoPersona[1])
    return edades

def promedioEdades(lista):
    suma = 0
    for edad in lista:
        suma += edad
    promedio = suma / len(lista)
    return promedio
