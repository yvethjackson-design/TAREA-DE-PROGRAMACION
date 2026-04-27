total = float(input("Ingresa el total de la compra: "))

if total > 1000:
    descuento = total * 0.20
    total_pagar = total - descuento
    print(f"Descuento del 20%: L {descuento}")
    print(f"Total a pagar: L {total_pagar}")
elif total >= 500 and total <= 1000:
    descuento = total * 0.10
    total_pagar = total - descuento
    print(f"Descuento del 10%: L {descuento}")
    print(f"Total a pagar: L {total_pagar}")
else:
    print("Sin descuento")
    print(f"Total a pagar: L {total}")