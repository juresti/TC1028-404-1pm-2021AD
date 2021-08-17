import math

print("Ejercicio 1")
radio = float(input("Dime el radio: "))
area = 4 * math.pi * radio ** 2
print(f"El area con el radio {radio} es de {area}")

print("\nEjercicio 2")
a = float(input("Dime el lado a: "))
b = float(input("Dime el lado b: "))
c = float(input("Dime el lado c: "))
s = (a + b + c) / 2
area = math.sqrt(s * (s-a) * (s-b) * (s-c))
print(f"El area es {area}")
