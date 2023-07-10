print("Programa que calcula el impuesto del 7% para 5 artículos")

i = 0
while i < 5:
    valor = float(input("Escribe el valor del artículo: "))
    impuesto = valor * 0.07
    print("El impuesto del artículo con valor", valor, "es:", impuesto)
    i += 1
