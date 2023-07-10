print("Programa que muestra los números del 1 al 10")

for a in range(1, 11):
    if a > 5:
        print("Mayor a 5")
    elif a < 5:
        print("Menor a 5")
    else:
        print("Igual a 5")
    if a == 9:
        break

print("Final del Programa")
