def programa_suma_numeros_pares():
    print("Programa que calcula la suma de los números pares\n")
    suma = 0
    for i in range(2, 101, 2):
        suma += i
    print("La suma de los números pares del 1 al 100 es:", suma)
