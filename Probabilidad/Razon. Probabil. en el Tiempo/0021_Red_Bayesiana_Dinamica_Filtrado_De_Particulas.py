# Red Bayesiana Dinámica: Filtrado de Partículas
#
# El filtrado de partículas mantiene una población de partículas
# (posibles estados del sistema) que se actualiza con transición y observación.

import random

# Estados posibles
estados = ['Querétaro', 'San Luis', 'Guadalajara']

# Transiciones entre estados
transiciones = {
    'Querétaro': ['San Luis'],
    'San Luis': ['San Luis', 'Guadalajara'],
    'Guadalajara': ['Guadalajara']
}

# P(observación | estado)
P_obs = {
    'Querétaro': {'industrial': 0.8, 'rural': 0.1, 'urbano': 0.1},
    'San Luis': {'industrial': 0.2, 'rural': 0.7, 'urbano': 0.1},
    'Guadalajara': {'industrial': 0.1, 'rural': 0.2, 'urbano': 0.7}
}

# Observaciones recibidas en el tiempo
observaciones = ['industrial', 'rural', 'urbano', 'urbano']

# Número de partículas
N = 1000

# Inicialización: todas las partículas en Querétaro
particulas = ['Querétaro'] * N

print("[Filtrado de Partículas]")

# Ciclo sobre cada observación
for t, obs in enumerate(observaciones):
    # Paso 1: transición de cada partícula
    nuevas = []
    for p in particulas:
        siguientes = transiciones[p]
        nuevas.append(random.choice(siguientes))
    particulas = nuevas

    # Paso 2: ponderación por verosimilitud
    pesos = []
    for p in particulas:
        pesos.append(P_obs[p][obs])

    # Paso 3: remuestreo según los pesos
    total = sum(w for w in pesos)
    if total == 0:
        pesos = [1] * N
        total = N

    normalizados = [w / total for w in pesos]
    particulas = random.choices(particulas, weights=normalizados, k=N)

    # Estimación actual: frecuencia de cada estado
    conteo = {estado: particulas.count(estado) / N for estado in estados}
    print(f"Paso {t + 1} (observación: {obs}):")
    for estado in estados:
        print(f"  {estado}: {conteo[estado]:.4f}")
    print()
