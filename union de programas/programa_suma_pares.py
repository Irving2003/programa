print("Programa que suma los números pares")

def sumar_numeros_pares(feg):
    suma = 0
    for i in range(1, feg + 1):
        if i % 2 == 0:
            suma += i
    return suma

if __name__ == '__main__':
    solucion = sumar_numeros_pares(20)
    print(solucion)

    print("Final del Programa")
