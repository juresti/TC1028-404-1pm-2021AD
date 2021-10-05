import os
print(os.getcwd())
os.chdir("/Users/dr.jorge/Desktop")
print(os.getcwd())

def escribeLinea(nombreArch,linea):
    miArchivo = open(nombreArch + ".txt","w")
    miArchivo.write(linea)
    miArchivo.close()

def leeArchivo(nombreArch):
    miArchivo = open(nombreArch + ".txt","r")
    datos = miArchivo.readlines()
    miArchivo.close()
    return datos

def quitaBackSlash(listaSucia):
    listaLimpia = []
    for linea in listaSucia:
        quitaBS = linea.rstrip()
        listaLimpia.append(quitaBS)
    return listaLimpia

def reporteVendedores(nomArch):
    """Recibe el nombre del archivo con los datos de los vendedores e
        imprime todos los datos de un vendedor en una sola linea"""
    datosSucios = leeArchivo(nomArch)
    #print(datosSucios)
    datos = quitaBackSlash(datosSucios)
    #print(datos)
    
    print("Reporte de los vendedores")
    print("Nombre\t\tID\tSueldo")
    print("-------------------------------------")
    for num in range(0,len(datos),3):
        nombre = datos[num]
        idVend = datos[num + 1]
        sueldo = datos[num + 2]
        print(f"{nombre}\t\t{idVend}\t{sueldo}")
        
def agregaArchivoVendedor(nomArch,nombre,idV,sueldo):
    archivo = open(nomArch + ".txt","a")
    archivo.write(nombre + "\n")
    archivo.write(idV + "\n")
    archivo.write(sueldo + "\n")
    archivo.close()
        
    