edad = int(input("Ingresa tu edad: "))
if edad < 5:
    print("Gratis")
elif edad >= 5 and edad <= 18:
    print("Precio a pagar: L 10")
elif edad >= 19 and edad <= 60:
    print("Precio a pagar: L 25")
elif edad > 60:
    print("Precio a pagar: L 15")
else:
    print("Edad no valida")