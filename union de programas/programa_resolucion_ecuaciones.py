def programa_resolucion_ecuaciones():
    print("Programa que resuelve ecuaciones\n")
    a1 = float(input("Escriba el valor de a: "))
    b2 = float(input("Escriba el valor de b: "))
    c3 = float(input("Escriba el valor de c: "))

    a = a1
    b = b2
    c = c3

    c1 = (4 * a) + (3 * b)
    c2 = (21 * a) - 18 + (8 * b) - 5
    c3 = (4 * a) + (3 * b) + 7
    c4 = (2 * a) + (3 * b) - (c ** 5)
    c5 = (2 * a) + (3 * b) - (c ** 2)

    print("El valor de c1 es:", round(c1, 2))
    print("El valor de c2 es:", round(c2, 2))
    print("El valor de c3 es:", round(c3, 2))
    print("El valor de c4 es:", round(c4, 2))
    print("El valor de c5 es:", round(c5, 2))
