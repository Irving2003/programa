def programa_perimetro_rectangulo():
    print("Programa que calcula el perímetro de un rectángulo\n")
    i1 = float(input("Escriba el valor de AB: "))
    i2 = float(input("Escriba el valor de BC: "))
    i3 = float(input("Escriba el valor de CD: "))
    i4 = float(input("Escriba el valor de DA: "))

    AB = i1
    BC = i2
    CD = i3
    DA = i4

    p = AB + BC + CD + DA
    PR = round(p, 2)
    print("El perímetro de un rectángulo es:", p, PR)
