# k-NN (k-Nearest Neighbors) y k-Medias (K-Means) - Clustering y Clasificación
#
# k-NN: Clasifica un nuevo punto basándose en los k puntos más cercanos del conjunto de entrenamiento.
# k-Medias: Agrupa datos sin etiquetas en clústeres.

import matplotlib
matplotlib.use('TkAgg')  # Para abrir gráficas en Ubuntu

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier

# Generamos datos simulados
np.random.seed(0)
grupo1 = np.random.randn(50, 2) + np.array([2, 2])
grupo2 = np.random.randn(50, 2) + np.array([-2, -2])
datos = np.vstack((grupo1, grupo2))
etiquetas = np.array([0] * 50 + [1] * 50)  # 0 para grupo1, 1 para grupo2

# --- K-MEANS ---
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(datos)
centroides = kmeans.cluster_centers_
predicciones_kmeans = kmeans.predict(datos)

# --- K-NN ---
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(datos, etiquetas)

# Clasificar un nuevo punto
nuevo_punto = np.array([[1, 1]])
prediccion_knn = knn.predict(nuevo_punto)

# --- Graficar ---
plt.figure(figsize=(10, 5))

# Gráfico K-Means
plt.subplot(1, 2, 1)
plt.scatter(datos[:, 0], datos[:, 1], c=predicciones_kmeans, cmap='viridis', label="Datos agrupados")
plt.scatter(centroides[:, 0], centroides[:, 1], c='red', marker='X', s=200, label="Centroides")
plt.title("K-Medias (Clustering)")
plt.legend()
plt.grid(True)

# Gráfico K-NN
plt.subplot(1, 2, 2)
plt.scatter(datos[:, 0], datos[:, 1], c=etiquetas, cmap='coolwarm', label="Datos etiquetados")
plt.scatter(nuevo_punto[:, 0], nuevo_punto[:, 1], c='black', marker='*', s=200, label=f"Nuevo punto (Clase {prediccion_knn[0]})")
plt.title("k-NN (Clasificación)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
