# Redes de Hamming, Hopfield, Hebb y Boltzmann (resumen práctico)
#
# Estas redes funcionan principalmente como memorias asociativas
# o como modelos de energía en sistemas neuronales.

import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt

# --- Red de Hopfield (memoria asociativa clásica) ---

# Definimos patrones a memorizar (binarios)
patrones = np.array([
    [1, -1, 1, -1],
    [-1, 1, -1, 1]
])

# Peso de la red: Regla de Hebb
W = np.zeros((4, 4))
for p in patrones:
    W += np.outer(p, p)

np.fill_diagonal(W, 0)  # No autoconexiones

# Función para actualizar estado (sincrónico)
def actualizar_hopfield(estado_inicial, pesos, pasos=5):
    estado = np.copy(estado_inicial)
    for _ in range(pasos):
        estado = np.sign(pesos @ estado)
        estado[estado == 0] = 1  # En caso de cero, lo forzamos a 1
    return estado

# Patrón inicial ruidoso
estado_inicial = np.array([1, -1, -1, -1])

# Recuperar patrón
estado_final = actualizar_hopfield(estado_inicial, W)

# Mostrar resultados
print("[Redes de Hamming, Hopfield, Hebb y Boltzmann]")
print(f"Estado inicial ruidoso: {estado_inicial}")
print(f"Estado recuperado: {estado_final}")

# --- Visualización ---
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
axes[0].imshow(estado_inicial.reshape(1, -1), cmap='gray', aspect='auto')
axes[0].set_title('Estado Inicial')

axes[1].imshow(estado_final.reshape(1, -1), cmap='gray', aspect='auto')
axes[1].set_title('Estado Recuperado')

for ax in axes:
    ax.axis('off')

plt.suptitle("Red de Hopfield - Recuperación de Patrones")
plt.show()
