print("Programa que calcula el salario neto de los trabajadores\n")
salario = float(input("Ingrese su salario mensual: "))

seguro_social = salario * 0.0514
seguro_educativo = salario * 0.02
prestamo = 50

pago =salario - seguro_social - seguro_educativo - prestamo

print("Su saldo a pagar de seguro social es de:", seguro_social)
print("Su saldo a pagar de seguro educativo es de:", seguro_educativo)
print("Su saldo a pagar de préstamo es de:", prestamo)
print("El salario a pagar es de:", round(pago, 2))
