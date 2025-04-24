# Modelos de Markov Ocultos (HMM)
#
# Simulamos un caso donde el agente se mueve entre ciudades (estados ocultos),
# pero solo recibe observaciones ruidosas sobre su estado.

import matplotlib
matplotlib.use('TkAgg')  

import matplotlib.pyplot as plt
import numpy as np
from hmmlearn import hmm

# Estados ocultos
estados = ['Querétaro', 'San Luis', 'Guadalajara']

# Codificación de estados
estado_codificado = {'Querétaro': 0, 'San Luis': 1, 'Guadalajara': 2}

# Modelo HMM
modelo = hmm.MultinomialHMM(n_components=3, random_state=42)

# IMPORTANTE: definir n_trials
modelo.n_trials = 1

# Definir matriz de transiciones
modelo.startprob_ = np.array([1.0, 0.0, 0.0])
modelo.transmat_ = np.array([
    [0.1, 0.9, 0.0],
    [0.0, 0.3, 0.7],
    [0.0, 0.0, 1.0]
])

# Probabilidades de emisión
modelo.emissionprob_ = np.array([
    [0.8, 0.1, 0.1],
    [0.2, 0.7, 0.1],
    [0.1, 0.2, 0.7]
])

# Generar muestras
X, Z = modelo.sample(10)


# Mostrar resultados
print("[Modelos de Markov Ocultos]")
print(f"Observaciones generadas: {X.ravel()}")
print(f"Estados ocultos generados: {[estados[z] for z in Z]}")

# Opcional: Graficar
plt.figure(figsize=(8, 4))
plt.plot(X.ravel(), marker='o', linestyle='-', label="Observaciones")
plt.title("Secuencia de Observaciones - HMM")
plt.xlabel("Tiempo")
plt.ylabel("Observación codificada")
plt.grid(True)
plt.legend()
plt.show()
