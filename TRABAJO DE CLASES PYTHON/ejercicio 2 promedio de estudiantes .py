import matplotlib.pyplot as plt
estudiantes= ["Jose","Maria","Carlos","Ana","Luis"]
promedios= [85,92,70,98,80]

plt.plot(estudiantes,promedios,marker='o')
plt.title("Promedio de Estudiantes") 
plt.xlabel("Estudiantes")
plt.ylabel("promedio")


plt.grid()
plt.show()
