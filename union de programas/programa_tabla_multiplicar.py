def tabla_multiplicar():
    print("Programa que muestra la tabla de multiplicar\n")
    for i in range(1, 13):
        print("Tabla de Multiplicar del", i)
        print("==========================")
        for j in range(1, 13):
            resultado = i * j
            print(i, "x", j, "=", resultado)
        print()
