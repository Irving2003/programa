def programa_serie_fibonacci():
    print("Programa que muestra la serie de Fibonacci\n")
    n = int(input("Ingrese un número: "))

    a, b = 0, 1
    fibonacci = [a, b]

    for i in range(2, n):
        a, b = b, a + b
        fibonacci.append(b)

    print("La serie de Fibonacci hasta el", n, "es:", fibonacci)
