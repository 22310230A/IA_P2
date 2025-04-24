# Aprendizaje Bayesiano
#
# En el aprendizaje bayesiano, el modelo mantiene una distribución de probabilidad
# sobre los posibles valores de sus parámetros, y la actualiza conforme observa datos nuevos.

# Simulamos el caso de un agente que quiere estimar la probabilidad de éxito de una acción (p),
# y actualiza su creencia usando la regla de Bayes a medida que observa resultados.

# Distribución Beta: Beta(α, β) es la distribución conjugada para una Bernoulli
# α = éxitos + 1, β = fracasos + 1

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta

# Parámetros iniciales (creencia a priori)
alpha = 1  # éxitos + 1
beta_val = 1  # fracasos + 1

# Resultados observados (1 = éxito, 0 = fracaso)
datos = [1, 0, 1, 1, 0, 1, 1, 1, 0]

# Paso a paso: actualizar la distribución con cada dato
x = np.linspace(0, 1, 100)

plt.figure(figsize=(10, 6))
for i, resultado in enumerate(datos):
    if resultado == 1:
        alpha += 1
    else:
        beta_val += 1

    y = beta.pdf(x, alpha, beta_val)
    plt.plot(x, y, label=f"Después de {i+1} observaciones")

plt.title("Evolución de la creencia sobre la probabilidad de éxito (Aprendizaje Bayesiano)")
plt.xlabel("Probabilidad de éxito")
plt.ylabel("Densidad")
plt.legend()
plt.grid(True)
plt.show()
