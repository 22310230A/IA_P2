# Aprendizaje Profundo (Deep Learning) - Perceptrón Multicapa básico
#
# Simulamos un modelo simple de red neuronal para clasificación
# usando un Perceptrón Multicapa (MLP).

import matplotlib
matplotlib.use('TkAgg')  # Para asegurarnos que se puede mostrar la gráfica en Ubuntu

import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPClassifier

# Generamos datos de ejemplo
np.random.seed(1)
X = np.r_[np.random.randn(100, 2) - [2, 2], np.random.randn(100, 2) + [2, 2]]
Y = [0] * 100 + [1] * 100  # Etiquetas: 0 y 1

# Entrenar un Perceptrón Multicapa
modelo = MLPClassifier(hidden_layer_sizes=(5,), activation='relu', max_iter=1000, random_state=1)
modelo.fit(X, Y)

# Crear una malla para graficar la frontera de decisión
xx, yy = np.meshgrid(np.linspace(-6, 6, 200), np.linspace(-6, 6, 200))
Z = modelo.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Gráfico
plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap='coolwarm', edgecolors='k')
plt.title("Aprendizaje Profundo - Perceptrón Multicapa")
plt.xlabel("X1")
plt.ylabel("X2")
plt.grid(True)
plt.show()
