import matplotlib.pyplot as plt

productos = ['Cereal', 'Cafe', 'Anticongelante']
ventas = [100, 150, 200]

# Crear gráfico de barras

plt.bar(productos, ventas)
plt.title('Ventas por Producto')
plt.show()


