def leerAsistencia():
    with open("Asistencia.txt","r") as miArchivo:
        datosS = miArchivo.readlines()
    #print(datosS)
    
    listaFinal = []
    for persona in datosS:
        datoSB = persona.rstrip()
        listaFinal.append(datoSB.split(","))
    
    listaSalida = []
    for persona in listaFinal:
        nombre = persona[0]
        numAsist = int(persona[1])
        listaSalida.append([nombre,numAsist])
        
    return listaSalida

def actualizaAsistencia(listaAsist,nombre):
    """Recibe una lista de listas que contiene la información de cuantas veces a venido una persona.
        Tambien recibe un nombre para actualizar la asistencia de esa persona.
        Regresa la lista con la asistencia actualizada"""
    
    cont = 0
    encontro = False
    for persona in listaAsist:
        if nombre in persona:
            listaAsist[cont][1] += 1
            encontro = True
        cont += 1
        
    if not encontro:
        listaAsist.append([nombre,1])
    
    return listaAsist
  
def guardaAsistencia(listaAsistencia):
    """Recibe una lista de listas con la información de la asistencia.
        Guarda la información en el archivo con el formato del archivo"""
    listaParaDisco = []
    for persona in listaAsistencia:
        salida = persona[0] + ","
        salida += str(persona[1]) + "\n"
        listaParaDisco.append(salida)
    #print(listaParaDisco)
    
    with open("Asistencia.txt","w") as miArchivo:
        miArchivo.writelines(listaParaDisco)
        print("Archivo actualizado en el disco")
        
    
  
def main():
    listaAsistencia = leerAsistencia()
    #print(listaAsistencia)
    nombre = input("Dime a quien le quieres poner asistencia: ")
    listaAsistencia = actualizaAsistencia(listaAsistencia,nombre)
    #print(listaAsistencia)
    guardaAsistencia(listaAsistencia)
    
