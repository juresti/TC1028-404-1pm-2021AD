"""
Puedo poner un comentario
Y lo va a ver
Pero como no asigno el string, no pasa nada
"""

# Este es un comentario y no lo ve Python
# Otro # para que no vea esta linea
# tampoco la ve

def pares(lista):
    cont = 0
    for num in lista:
        if (num % 2) == 0:
            cont += 1
    return cont

def capturaLista(num):
    lista = []
    for num in range(num):
        elem = input(f"Dime el elemento {num + 1} de la lista: ")
        lista.append(elem)
    return lista

def main():
    print("Ejercicio 1")
    numElem = int(input("Dime cuantos elementos en tu lista: "))
    lista = capturaLista(numElem)
    
    listaInt = []
    for elem in lista:
        listaInt.append(int(elem))
        
    cuantos = pares(listaInt)
    print(f"En la lista {listaInt}, tenemos {cuantos} pares")
    

def primo(num):
    for dato in range(2,num):
        if (num % dato) == 0:
            return False
    return True

def menor(cuantos):
    menor = int(input("Dime un numero: "))
    for num in range(cuantos - 1):
        dato = int(input("Dime un numero: "))
        if (dato < menor):
            menor = dato
        print(f"El menor hasta el momento es {menor}")
    return menor

def menorWhile(cuantos):
    menor = 99999999999
    cont = 0
    while (cont < cuantos):
        dato = int(input("Dime un numero: "))
        cont += 1
        if (dato < menor):
            menor = dato
        print(f"El menor hasta el momento es {menor}")
    return menor


def lineaSolida(ancho):
    salida = ""
    for num in range(ancho):
        salida += "*"
    return salida

def lineaVacia(ancho):
    salida = "*"
    for num in range(ancho - 2):
        salida += " "
    salida += "*"
    return salida

def rectSolido(alto,ancho):
    salida = ""
    for num in range(alto):
        salida += lineaSolida(ancho) + "\n"
    return salida

def rectVacio(alto,ancho):
    salida = lineaSolida(ancho) + "\n"
    for numn in range(alto - 2):
        salida += lineaVacia(ancho) + "\n"
    salida += lineaSolida(ancho) + "\n"
    return salida

