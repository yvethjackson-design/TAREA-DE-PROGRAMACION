import matplotlib.pyplot as plt
 
productos=["laptop","mause","teclado","tablet","audifonos"]
ventas=[15,30,20,10,25]


plt.bar(productos,ventas)
plt.title("ventas de productos")
plt.xlabel("productos")
plt.ylabel("cantidad vendida")


plt.get_current_fig_manager().set_window_title ("ejercicio 1")


plt.show()
