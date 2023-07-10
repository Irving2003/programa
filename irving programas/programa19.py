print("Programa que clasifica triángulos\n")
A = int(input("Escriba el valor del lado A del triángulo: "))
B = int(input("Escriba el valor del lado B del triángulo: "))
C = int(input("Escriba el valor del lado C del triángulo: "))

if A == B == C:
    print("Es un triángulo equilátero")
elif A == B or B == C or A == C:
    print("Es un triángulo isósceles")
else:
    print("Es un triángulo escaleno")
print("Fin del programa")
