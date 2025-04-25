# Retropropagación del Error
#
# La retropropagación es el algoritmo que permite a una red neuronal ajustar sus pesos
# automáticamente mediante el cálculo del gradiente del error.

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPClassifier

# Datos de ejemplo: XOR (no linealmente separable)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 1, 1, 0])  # Etiquetas para XOR

# Red neuronal con retropropagación
modelo = MLPClassifier(hidden_layer_sizes=(5,), activation='tanh', solver='sgd', learning_rate_init=0.1, max_iter=10000, random_state=42)
modelo.fit(X, y)

# Crear malla para graficar frontera de decisión
xx, yy = np.meshgrid(np.linspace(-0.5, 1.5, 300),
                     np.linspace(-0.5, 1.5, 300))
Z = modelo.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Graficar resultados
plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, cmap='coolwarm', alpha=0.6)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolors='k')
plt.title("Retropropagación del Error - Solución XOR")
plt.xlabel("X1")
plt.ylabel("X2")
plt.grid(True)
plt.show()
