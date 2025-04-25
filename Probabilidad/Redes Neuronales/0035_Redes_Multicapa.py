# Redes Multicapa (Multilayer Perceptron - MLP)
#
# Las redes multicapa superan las limitaciones del perceptrón simple,
# permitiendo resolver problemas no linealmente separables.

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPClassifier

# Creamos un conjunto de datos no linealmente separable (anillos concéntricos)
from sklearn.datasets import make_moons

# Generar datos
X, y = make_moons(n_samples=200, noise=0.2, random_state=42)

# Entrenar un Perceptrón Multicapa
modelo = MLPClassifier(hidden_layer_sizes=(10, 5), activation='relu', max_iter=2000, random_state=42)
modelo.fit(X, y)

# Crear malla para graficar frontera de decisión
xx, yy = np.meshgrid(np.linspace(X[:,0].min()-0.5, X[:,0].max()+0.5, 300),
                     np.linspace(X[:,1].min()-0.5, X[:,1].max()+0.5, 300))
Z = modelo.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Graficar resultados
plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, cmap='coolwarm', alpha=0.6)
plt.scatter(X[:,0], X[:,1], c=y, cmap='coolwarm', edgecolors='k')
plt.title("Red Multicapa (MLP) - Clasificación")
plt.xlabel("X1")
plt.ylabel("X2")
plt.grid(True)
plt.show()
