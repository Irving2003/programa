print("Programa que calcula el costo de compra de gasolina\n")
litros = float(input("Valor de la cantidad de litros: "))

costo_total = (0.98 * litros) * 1.07

print("El costo total es:", round(costo_total, 2))
