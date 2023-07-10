def programa_calculo_compra_articulos():
    print("Programa que calcula la compra de 5 artículos\n")
    precio1 = float(input("Precio del artículo 1: "))
    precio2 = float(input("Precio del artículo 2: "))
    precio3 = float(input("Precio del artículo 3: "))
    precio4 = float(input("Precio del artículo 4: "))
    precio5 = float(input("Precio del artículo 5: "))

    total_sin_impuesto = precio1 + precio2 + precio3 + precio4 + precio5
    DR = round(total_sin_impuesto, 2)
    print("El total sin impuesto es:", DR)

    total_con_impuesto = total_sin_impuesto * 1.07
    DR = round(total_con_impuesto, 2)
    print("El total con impuesto es:", DR)

    promedio_de_compra = total_sin_impuesto / 5
    DR = round(promedio_de_compra, 2)
    print("El promedio de compra es:", DR)
