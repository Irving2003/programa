def programa_area_triangulo():
    print("Programa que calcula el área de un triángulo\n")
    base = float(input("Escriba la base: "))
    altura = float(input("Escriba la altura: "))

    area = (base * altura) / 2
    DR = round(area, 2)

    print("Imprimir:", DR)
