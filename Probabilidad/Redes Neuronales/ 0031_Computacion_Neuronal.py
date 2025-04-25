# Computación Neuronal
#
# Las redes neuronales artificiales se inspiran en el funcionamiento
# de las neuronas biológicas, simulando cómo los impulsos se transmiten y procesan.

import numpy as np
import matplotlib
matplotlib.use('TkAgg')  

import matplotlib.pyplot as plt

# Simulación de una neurona artificial simple
def neurona_simple(entradas, pesos, sesgo):
    suma_ponderada = np.dot(entradas, pesos) + sesgo
    salida = 1 if suma_ponderada >= 0 else 0  # Función de activación escalón
    return salida

# Entradas y pesos de ejemplo
entradas = np.array([0.5, -0.6, 0.3])
pesos = np.array([0.4, 0.7, -0.5])
sesgo = 0.2

# Calcular la salida de la neurona
salida = neurona_simple(entradas, pesos, sesgo)

print("[Computación Neuronal]")
print(f"Entradas: {entradas}")
print(f"Pesos: {pesos}")
print(f"Sesgo: {sesgo}")
print(f"Salida de la neurona: {salida}")

# Visualización: Entrada vs. Salida (para una sola entrada)
x = np.linspace(-1, 1, 100)
y = [1 if (w * xi + sesgo) >= 0 else 0 for xi, w in zip(x, [pesos[0]] * len(x))]

plt.figure(figsize=(8, 5))
plt.plot(x, y)
plt.title("Simulación de Computación Neuronal (Función Escalón)")
plt.xlabel("Entrada")
plt.ylabel("Salida")
plt.grid(True)
plt.show()
