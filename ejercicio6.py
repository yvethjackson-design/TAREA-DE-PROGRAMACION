num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
operacion = input("Ingresa la operacion (+, -, *, /): ")

if operacion == "+":
    resultado = num1 + num2
    print(f"Resultado: {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"Resultado: {resultado}")
elif operacion == "*":
    resultado = num1 * num2
    print(f"Resultado: {resultado}")
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {resultado}")
    else:
        print("Error: No se puede dividir entre cero")
else:
    print("Operacion no valida")