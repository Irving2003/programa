print("Programa que calcula el volumen de un prisma rectangular\n")
i1 = float(input("Escriba el valor de el largo: "))
i2 = float(input("Escriba el valor de el ancho: "))
i3 = float(input("Escriba el valor de la altura: "))

Largo = i1
Ancho = i2
Altura = i3

V = Largo * Ancho * Altura
VR = round(V, 4)

print("El volumen de un prisma rectangular es:", VR)
