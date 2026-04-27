nota = int(input("Ingresa tu nota del 1 al 100: "))

if nota >= 90 and nota <= 100:
    print("Excelente")
elif nota >= 70 and nota <= 89:
    print("Bueno")
elif nota >= 60 and nota <= 69:
    print("Regular")
elif nota >= 0 and nota < 60:
    print("Reprobado")
else:
    print("Nota no valida")