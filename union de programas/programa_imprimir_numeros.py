def imprimir_numeros():
    print("Programa que imprime los números del 0 al 15\n")
    numero = 0
    while numero <= 15:
        print(numero)
        if numero % 2 == 0:
            print("El número es par")
        else:
            print("El número es impar")
        numero += 1
