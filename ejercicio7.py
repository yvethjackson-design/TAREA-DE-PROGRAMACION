lado1 = float(input("Ingresa el lado 1: "))
lado2 = float(input("Ingresa el lado 2: "))
lado3 = float(input("Ingresa el lado 3: "))

if lado1 == lado2 and lado2 == lado3:
    print("Equilatero - todos iguales")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Isosceles - 2 iguales")
else:
    print("Escaleno - todos diferentes")