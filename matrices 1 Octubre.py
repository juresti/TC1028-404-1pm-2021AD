def crearMatriz(numRen,numCol,valor):
    """Regresa una matriz del numRenXnumCol inicializada todos los valores en valor"""
    matriz = []
    for ren in range(numRen): #Añadir los renglones
        renglon = []
        for col in range(numCol): #Añadir los valores de las columnas
            renglon.append(valor)
        matriz.append(renglon)
    return matriz

def imprimirMatriz(matriz):
    """Imprime la matriz que recibe"""
    salida = ""
    for renglon in matriz: #Saca cada renglon de la matriz
        for valor in renglon: #Saca cada valor del renglon
            salida += str(valor) + " "
        salida += "\n"
    
    print(salida)

def esCuadrada(matriz):
    """Regresa True si la matriz es Cudadrada"""
    numRen = len(matriz)
    numCol = len(matriz[0])
    
    for ren in matriz:
        long = len(ren) #longitud del renglon actual
        if (long != numCol):
            return False
    
    if (numRen == numCol):
        return True
    else:
        return False
