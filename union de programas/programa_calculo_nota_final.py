def programa_calculo_nota_final():
    print("Programa que calcula la nota final\n")
    n1 = float(input("Ingrese la primera evaluación: "))
    n2 = float(input("Ingrese la segunda evaluación: "))
    n3 = float(input("Ingrese la tercera evaluación: "))
    n4 = float(input("Ingrese la cuarta evaluación: "))
    n5 = float(input("Ingrese la quinta evaluación: "))

    nota_final = (n1 + n2 + n3 + n4 + n5) / 100

    print("Su nota final es:", round(nota_final, 2))
