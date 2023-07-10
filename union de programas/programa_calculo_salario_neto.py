def programa_calculo_salario_neto():
    print("Programa que calcula el salario neto de un empleado\n")
    salario_bruto = int(input("Ingrese su salario bruto: "))

    seguro_social = salario_bruto * 0.08
    seguro_educativo = salario_bruto * 0.02
    impuesto = salario_bruto * 0.15
    prestamo = 100

    salario_neto = salario_bruto - seguro_social - seguro_educativo - impuesto - prestamo

    print("La cantidad a pagar de su seguro social es de:", seguro_social)
    print("La cantidad a pagar de su seguro educativo es de:", seguro_educativo)
    print("La cantidad a pagar de su impuesto es de:", impuesto)
    print("La cantidad a pagar de su préstamo es de:", prestamo)
    print("El salario neto es de:", salario_neto)
