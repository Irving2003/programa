print("Programa que calcula el área de un triángulo")

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

base = float(input("Escriba la base: "))
altura = float(input("Escriba la altura: "))

area = calcular_area_triangulo(base, altura)

print("El área del triángulo es:", area)

print("Fin del Programa")
