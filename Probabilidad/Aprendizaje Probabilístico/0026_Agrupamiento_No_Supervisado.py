# Agrupamiento No Supervisado (K-Means básico)
#
# En el agrupamiento no supervisado, el modelo organiza los datos en grupos
# sin necesidad de etiquetas conocidas previamente.

import matplotlib
matplotlib.use('TkAgg')  # Forzamos backend interactivo para mostrar la gráfica

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# Generamos datos simulados (dos grupos)
np.random.seed(0)
grupo1 = np.random.randn(50, 2) + np.array([2, 2])
grupo2 = np.random.randn(50, 2) + np.array([-2, -2])
datos = np.vstack((grupo1, grupo2))

# Algoritmo K-Means
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(datos)

# Resultados
centroides = kmeans.cluster_centers_
etiquetas = kmeans.labels_

# Graficar resultados
plt.figure(figsize=(8, 6))
plt.scatter(datos[:, 0], datos[:, 1], c=etiquetas, cmap='viridis', label='Datos')
plt.scatter(centroides[:, 0], centroides[:, 1], c='red', s=200, alpha=0.7, marker='X', label='Centroides')
plt.title("Agrupamiento No Supervisado (K-Means)")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()
