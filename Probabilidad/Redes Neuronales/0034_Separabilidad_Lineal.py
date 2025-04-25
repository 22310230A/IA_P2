# Separabilidad Lineal
#
# La separabilidad lineal ocurre cuando dos clases pueden ser
# separadas por una sola línea recta (o un plano en espacios mayores).

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

# Creamos dos grupos de puntos que son separables linealmente
np.random.seed(0)
grupo1 = np.random.randn(50, 2) + np.array([-2, -2])
grupo2 = np.random.randn(50, 2) + np.array([2, 2])

# Concatenamos los datos
X = np.vstack((grupo1, grupo2))
y = np.array([0]*50 + [1]*50)  # Etiquetas

# Graficamos
plt.figure(figsize=(8, 6))
plt.scatter(X[:50, 0], X[:50, 1], color='red', label='Clase 0')
plt.scatter(X[50:, 0], X[50:, 1], color='blue', label='Clase 1')

# Dibujar línea de separación manual
x_linea = np.linspace(-5, 5, 100)
y_linea = x_linea  # Línea: y = x
plt.plot(x_linea, y_linea, 'k--', label='Posible frontera lineal')

plt.title("Separabilidad Lineal")
plt.xlabel("X1")
plt.ylabel("X2")
plt.legend()
plt.grid(True)
plt.show()
