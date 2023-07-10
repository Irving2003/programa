def programa_calculo_factorial():
    print("Programa que calcula el factorial de un número\n")
    n = int(input("Ingrese un número: "))

    factorial = 1

    if n < 0:
        print("El factorial no está definido para números negativos")
    elif n == 0:
        print("El factorial de 0 es 1")
    else:
        for i in range(1, n + 1):
            factorial *= i
        print("El factorial de", n, "es", factorial)
