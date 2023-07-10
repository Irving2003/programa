print("Programa que verifica si un número es primo\n")
numero = int(input("Ingrese un número: "))

es_primo = True
if numero < 2:
    es_primo = False
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print("El número", numero, "es primo")
else:
    print("El número", numero, "no es primo")
