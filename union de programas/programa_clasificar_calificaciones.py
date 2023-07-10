def programa_clasificar_calificaciones():
    print("Programa que clasifica calificaciones\n")
    valor = float(input("Escriba el valor: "))

    if valor >= 90:
        print("Es A")
    elif valor >= 80:
        print("Es B")
    elif valor >= 70:
        print("Es C")
    elif valor >= 60:
        print("Es D")
    else:
        print("Es F")
    print("Fin del programa")
