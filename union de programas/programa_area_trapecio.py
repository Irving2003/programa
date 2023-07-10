def programa_area_trapecio():
    print("Programa que calcula el área de un trapecio\n")
    i1 = float(input("Escriba el valor de base 1: "))
    i2 = float(input("Escriba el valor de base 2: "))
    i3 = float(input("Escriba el valor de la Altura: "))

    Base1 = i1
    Base2 = i2
    Altura = i3

    A = ((Base1 + Base2) * Altura) / 2
    AR = round(A, 2)

    print("El área de un trapecio es:", AR)
