def calcularPromedio(numMat):
    suma = 0
    for veces in range(1,numMat + 1):
        calif = int(input(f"Dime la calicacion de la materia {veces}: "))
        suma += calif
    promedio = suma / numMat
    return promedio

def main():
    print("Programa que calcula el promedio de tus calificaciones")
    cuantas = int(input("Dime cuantas materias llevas este semestre: "))
    prom = calcularPromedio(cuantas)
    print(f"El promedio de tus {cuantas} materias es de {prom}")
    

def creaLinea(ancho):
    st1 = "" #string vacio
    for num in range(ancho):
        st1 += "*"
    return st1

def main2():
    print("Programa que crea una linea del ancho deseado")
    wide = int(input("Dime el ancho de la linea: "))
    linea = creaLinea(wide)
    print(linea)
    
def rectangulo(ancho,alto):
    rect = ""
    for num in range(alto):
        rect += creaLinea(ancho) + "\n"
    return rect

def main3():
    print("Programa que crea un rectangulo del ancho y alto seleccionado")
    wide = int(input("Dime el ancho: "))
    height = int(input("Dime el alto: "))
    rec = rectangulo(wide,height)
    print(rec)

creaLinea(4)
        