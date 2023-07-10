def programa_determinar_impuestos():
    print("Programa que determina si una persona paga impuestos\n")
    salario = float(input("Escriba el salario: "))

    if salario < 3000:
        impuesto = salario * 1.07
        print("Esta persona debe abonar impuestos:", impuesto)
    else:
        print("No debe abonar impuestos")
    print("Fin del programa")
