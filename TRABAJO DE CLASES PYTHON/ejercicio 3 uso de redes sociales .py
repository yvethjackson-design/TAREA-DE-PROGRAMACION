import matplotlib.pyplot as plt
redes= ["tiktok","instagram","facebook","youtube","whatsapp"]
horas= [4,3,2,5,6]

plt.pie(horas , labels=redes ,autopct='%1.1f%%')
plt.title("Promedio de Estudiantes") 
plt.xlabel("Estudiantes")
plt.ylabel("promedio")


plt.title("uso de redes sociales")
plt.show()
