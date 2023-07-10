print("Programa que calcula el interés de un préstamo\n")
prestamo = int(input("Ingrese la cantidad del préstamo: "))
tasa_mensual = float(input("Ingrese la tasa mensual: "))
plazo = int(input("Ingrese la cantidad de meses para pagar el préstamo: "))

porcentaje_tasa = tasa_mensual * 100
tasa_mensual = porcentaje_tasa / 12

cuota = prestamo * (tasa_mensual / (1 - (1 + tasa_mensual) ** (-plazo)))
interes_mensual = prestamo * tasa_mensual
capital_mensual = cuota - interes_mensual

print("La cuota a pagar por mes es de:", round(cuota, 2))
print("El interés mensual es de:", round(interes_mensual, 2))
print("El capital mensual es de:", round(capital_mensual, 2))
