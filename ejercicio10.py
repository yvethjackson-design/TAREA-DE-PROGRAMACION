nota1 = float(input("Ingresa la nota 1: "))
nota2 = float(input("Ingresa la nota 2: "))
nota3 = float(input("Ingresa la nota 3: "))

promedio = (nota1 + nota2 + nota3) / 3
print(f"Promedio: {promedio}")

if promedio >= 90:
    print("Excelente")
elif promedio >= 70 and promedio <= 89:
    print("Bueno")
elif promedio >= 60 and promedio <= 69:
    print("Regular")
else:
    print("Reprobado")

if promedio < 60:
    print("Debe repetir la materia")