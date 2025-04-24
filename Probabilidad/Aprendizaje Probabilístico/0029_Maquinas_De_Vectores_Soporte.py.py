# Máquinas de Vectores de Soporte (SVM) con Núcleo Lineal
#
# Las SVM son clasificadores que encuentran el hiperplano óptimo que separa las clases.
# Pueden usar "núcleos" para crear fronteras no lineales.

import matplotlib
matplotlib.use('TkAgg')  # Asegura que se muestre la ventana en Ubuntu

import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm

# Generamos datos de ejemplo
np.random.seed(1)
X = np.r_[np.random.randn(20, 2) - [2, 2], np.random.randn(20, 2) + [2, 2]]
Y = [0] * 20 + [1] * 20  # Etiquetas: 0 y 1

# Entrenar un SVM con núcleo lineal
modelo = svm.SVC(kernel='linear', C=1.0)
modelo.fit(X, Y)

# Obtener los vectores de soporte
vectores_soporte = modelo.support_vectors_

# Gráfico de los datos
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap='coolwarm', label='Datos')
plt.scatter(vectores_soporte[:, 0], vectores_soporte[:, 1], edgecolors='k', facecolors='none', s=120, label='Vectores de soporte')

# Dibujar la frontera de decisión
w = modelo.coef_[0]
b = modelo.intercept_[0]
x_linea = np.linspace(-5, 5)
y_linea = -(w[0] * x_linea + b) / w[1]

# Márgenes
margen = 1 / np.linalg.norm(w)
y_mas = y_linea + margen
y_menos = y_linea - margen

plt.plot(x_linea, y_linea, 'k-', label='Frontera')
plt.plot(x_linea, y_mas, 'k--', linewidth=0.8)
plt.plot(x_linea, y_menos, 'k--', linewidth=0.8)

plt.title("Máquina de Vectores de Soporte (SVM)")
plt.xlabel("X1")
plt.ylabel("X2")
plt.legend()
plt.grid(True)
plt.show()
