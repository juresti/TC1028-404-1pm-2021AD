def leerArchivo(nombre):
    with open(nombre + ".txt","r") as miArchivo:
        datosSucios = miArchivo.readlines()
    return datosSucios

def quitarBS(listaSucia):
    listaLimpia = []
    for infoProd in listaSucia:
        listaLimpia.append(infoProd.rstrip())
    return listaLimpia
    
def separarEnListas(lista):
    """Recibe una lista con strings que tienen un separador
        Regresa una lista de listas en donde cada sublista tiene la informacion del producto"""
    listaSeparada = []
    for datosArt in lista:
        listaSeparada.append(datosArt.split("\t"))
    return listaSeparada

def convierteDatosInv(lista):
    listaConvertida = []
    for datosProd in lista:
        idProd = int(datosProd[0])
        desc = datosProd[1]
        cant = int(datosProd[2])
        precio = float(datosProd[3])
        listaConvertida.append([idProd,desc,cant,precio])
    return listaConvertida

def cargarInventario():
    """Carga el archivo .txt con el inventario y regresa una lista de listas en donde
        cada sublista es un producto con su información"""
    datosS = leerArchivo("Inventario")
    #print(datosS)
    datosSinBS = quitarBS(datosS)
    #print(datosSinBS)
    datosSeparados = separarEnListas(datosSinBS)
    #print(datosSeparados)
    datosFinales = convierteDatosInv(datosSeparados[1:])
    #print(datosFinales)
    return datosFinales
    
def hayEnInventario(inventario,idProd):
    """Regresa True si el idProd se encuentra en el inventario"""
    for producto in inventario:
        if idProd in producto:
            return True
    return False

def ventaProducto(inventario):
    idProd = 11 #SeleccionaProducto
    if hayEnInventario(inventario,idProd):
        print("Si tenemos, lo quiere?")
    else:
        print("Mala suerte! Creo que el de enfrente tiene.")

def main():
    inventario = cargarInventario()
    ventaProducto(inventario)
    