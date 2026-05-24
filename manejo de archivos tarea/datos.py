producto1="Arroz"
producto2="Leche"
producto3="Pan"

cantidad1=3
cantidad2=5
cantidad3=2

precio1=45
precio2=38
precio3=20

total1=precio1*cantidad1
total2=precio2*cantidad2
total3=precio3*cantidad3

totalfinal=total1+total2+total3

archivo=open("datos.txt","w")
archivo.write(producto1+" "+str(cantidad1)+" x "+str(precio1)+" = "+str(total1)+"\n")
archivo.write(producto2+" "+str(cantidad2)+" x "+str(precio2)+" = "+str(total2)+"\n")
archivo.write(producto3+" "+str(cantidad3)+" x "+str(precio3)+" = "+str(total3)+"\n")
archivo.write("TOTAL FINAL = "+str(totalfinal))
archivo.close()






estudiante="Karen"

materia1="Matematicas"
materia2="Programacion"
materia3="Ingles"

nota1=85
nota2=70
nota3=90

promedio=(nota1+nota2+nota3)/3

if promedio>=70:
    estado="Aprobo"
else:
    estado="Reprobo"

archivo=open("reporte.txt","w")

archivo.write(estudiante+"\n")
archivo.write(materia1+" = "+str(nota1)+"\n")
archivo.write(materia2+" = "+str(nota2)+"\n")
archivo.write(materia3+" = "+str(nota3)+"\n")
archivo.write("Promedio = "+str(promedio)+"\n")
archivo.write(estado)

archivo.close()






alumno="Luis"

asistidas=18
faltadas=2

totalclases=asistidas+faltadas

porcentaje=(asistidas/totalclases)*100

archivo=open("asistencia.txt","w")

archivo.write("Alumno: "+alumno+"\n")
archivo.write("Asistidas: "+str(asistidas)+"\n")
archivo.write("Faltadas: "+str(faltadas)+"\n")
archivo.write("Porcentaje: "+str(porcentaje)+"%")

archivo.close()



empleado="Carlos"

horas=40
pagohora=120

salariobruto=horas*pagohora

deduccion=salariobruto*0.10

salariofinal=salariobruto-deduccion

archivo=open("salario.txt","w")

archivo.write("Empleado: "+empleado+"\n")
archivo.write("Salario Bruto: "+str(salariobruto)+"\n")
archivo.write("Deduccion: "+str(deduccion)+"\n")
archivo.write("Salario Final: "+str(salariofinal))

archivo.close()


marca1="Toyota"
modelo1="Corolla"
año1=2020

marca2="Honda"
modelo2="Civic"
año2=2021

marca3="Ford"
modelo3="Focus"
año3=2019

archivo=open("vehiculos.txt","w")

archivo.write("Vehiculo 1\n")
archivo.write("Marca: "+marca1+"\n")
archivo.write("Modelo: "+modelo1+"\n")
archivo.write("Año: "+str(año1)+"\n\n")

archivo.write("Vehiculo 2\n")
archivo.write("Marca: "+marca2+"\n")
archivo.write("Modelo: "+modelo2+"\n")
archivo.write("Año: "+str(año2)+"\n\n")

archivo.write("Vehiculo 3\n")
archivo.write("Marca: "+marca3+"\n")
archivo.write("Modelo: "+modelo3+"\n")
archivo.write("Año: "+str(año3))

archivo.close()



producto1="Arroz"
stock1=5

producto2="Leche"
stock2=20

producto3="Azucar"
stock3=8

producto4="Cafe"
stock4=15

producto5="Pan"
stock5=4

archivo=open("inventario.txt","w")

archivo.write(producto1+" Stock: "+str(stock1)+"\n")
archivo.write(producto2+" Stock: "+str(stock2)+"\n")
archivo.write(producto3+" Stock: "+str(stock3)+"\n")
archivo.write(producto4+" Stock: "+str(stock4)+"\n")
archivo.write(producto5+" Stock: "+str(stock5)+"\n\n")

archivo.write("Productos con menos de 10 unidades\n")

if stock1<10:
    archivo.write(producto1+"\n")

if stock2<10:
    archivo.write(producto2+"\n")

if stock3<10:
    archivo.write(producto3+"\n")

if stock4<10:
    archivo.write(producto4+"\n")

if stock5<10:
    archivo.write(producto5+"\n")

archivo.close()




celsius=30

fahrenheit=(celsius*9/5)+32
archivo=open("temperaturas.txt","w")
archivo.write("Celsius: "+str(celsius)+"\n")
archivo.write("Fahrenheit: "+str(fahrenheit))
archivo.close()



pelicula="shrek2"

boletos=6
precio=120

total=boletos*precio

descuento=0

if boletos>5:
    descuento=total*0.10

totalpagar=total-descuento

archivo=open("cine.txt","w")

archivo.write("Pelicula: "+pelicula+"\n")
archivo.write("Boletos: "+str(boletos)+"\n")
archivo.write("Precio: "+str(precio)+"\n")
archivo.write("Descuento: "+str(descuento)+"\n")
archivo.write("Total a pagar: "+str(totalpagar))

archivo.close()


libro="Don Quijote"
autor="Cervantes"
paginas=500
estado="Disponible"

archivo=open("biblioteca.txt","w")

archivo.write("Libro: "+libro+"\n")
archivo.write("Autor: "+autor+"\n")
archivo.write("Paginas: "+str(paginas)+"\n")
archivo.write("Estado: "+estado)

archivo.close()





comida=500
transporte=300
entretenimiento=700

gastototal=comida+transporte+entretenimiento

mayor=comida
categoria="Comida"

if transporte>mayor:
    mayor=transporte
    categoria="Transporte"

if entretenimiento>mayor:
    mayor=entretenimiento
    categoria="Entretenimiento"

archivo=open("gastos.txt","w")

archivo.write("Comida: "+str(comida)+"\n")
archivo.write("Transporte: "+str(transporte)+"\n")
archivo.write("Entretenimiento: "+str(entretenimiento)+"\n")
archivo.write("Gasto Total: "+str(gastototal)+"\n")
archivo.write("Mayor gasto: "+categoria)

archivo.close()