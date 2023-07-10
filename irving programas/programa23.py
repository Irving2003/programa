print("Programa que muestra los números del 1 al 10\n")
numero = 1
while numero <= 10:
    if numero > 5:
        print("Mayor a 5")
    elif numero < 5:
        print("Menor a 5")
    else:
        print("Igual a 5")
    if numero == 9:
        break
    numero += 1
print("Fin del programa")
