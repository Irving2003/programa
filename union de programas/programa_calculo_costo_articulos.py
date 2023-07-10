def programa_calculo_costo_articulos():
    print("Programa que calcula el costo de compra de los artículos\n")
    p1 = float(input("Ingrese el costo del primer artículo: "))
    p2 = float(input("Ingrese el costo del segundo artículo: "))
    p3 = float(input("Ingrese el costo del tercer artículo: "))

    costo_total = (p1 + p2 + p3) * 1.07

    print("El costo total de la compra es de:", round(costo_total, 3))
