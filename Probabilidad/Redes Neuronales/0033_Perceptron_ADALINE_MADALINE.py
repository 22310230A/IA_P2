# Perceptrón, ADALINE y MADALINE
#
# Clasificador que decide si un agente avanza en el camino correcto
# desde CDMX hacia Guadalajara, pasando por varios estados intermedios.

import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Perceptron, SGDRegressor

# Estados codificados como coordenadas ficticias (no reales)
ciudades = {
    'CDMX': [0, 0],
    'Querétaro': [1, 1],
    'San Luis': [2, 2],
    'Zacatecas': [3, 2],
    'Guadalajara': [4, 3]
}

# Datos de entrenamiento
X = np.array([
    ciudades['CDMX'],
    ciudades['Querétaro'],
    ciudades['San Luis'],
    ciudades['Zacatecas'],
    ciudades['Guadalajara']
])

# Etiquetas:
# 0 = No ha llegado aún a Guadalajara
# 1 = Llegó a Guadalajara
y_perceptron = np.array([0, 0, 0, 0, 1])

# --- Entrenamiento del Perceptrón ---
modelo_perceptron = Perceptron(max_iter=1000, tol=1e-3, random_state=42)
modelo_perceptron.fit(X, y_perceptron)

# --- Entrenamiento del ADALINE ---
modelo_adaline = SGDRegressor(loss='squared_error', learning_rate='constant', eta0=0.01, max_iter=1000, random_state=42)
modelo_adaline.fit(X, y_perceptron)

# Nuevos estados a clasificar
nuevos_estados = np.array([
    ciudades['Querétaro'],
    ciudades['San Luis'],
    ciudades['Zacatecas'],
    ciudades['Guadalajara']
])

nombres_estados = ['Querétaro', 'San Luis', 'Zacatecas', 'Guadalajara']

pred_perceptron = modelo_perceptron.predict(nuevos_estados)
pred_adaline = modelo_adaline.predict(nuevos_estados)

print("[Perceptrón, ADALINE y MADALINE]")
for idx, estado in enumerate(nombres_estados):
    print(f"Estado: {estado}")
    print(f"  Predicción Perceptrón (0=No GDL, 1=GDL): {pred_perceptron[idx]}")
    print(f"  Predicción ADALINE (valor continuo): {pred_adaline[idx]:.2f}\n")

# Gráfico
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y_perceptron, cmap='coolwarm', label='Estados')
plt.title("Camino CDMX → GDL - Clasificación Perceptrón / ADALINE")
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.grid(True)
plt.legend()
plt.show()

