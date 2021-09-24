lA = [3,8.8,[True,"Adios",4,["a",9],13],"Ya fin",8]
print(lA[2][3][0])

def listaP(numPer):
    lPer = []
    for num in range(numPer):
        nombre = input(f"{num +1}. Dime el nombre: ")
        lPer.append(nombre)
    return lPer
