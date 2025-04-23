# Filtrado, Predicción, Suavizado y Explicación
#
# Simulamos cómo evoluciona la creencia del agente en el tiempo, y cómo se puede:
# - Filtrar (saber dónde está ahora)
# - Predecir (dónde estará)
# - Suavizar (dónde estuvo)
# - Explicar (qué estados pasados explican la evidencia actual)

# Estados posibles
estados = ['Querétaro', 'San Luis', 'Guadalajara']

# Matriz de transición estacionaria
transiciones = {
    'Querétaro': {'Querétaro': 0.1, 'San Luis': 0.9},
    'San Luis': {'San Luis': 0.3, 'Guadalajara': 0.7},
    'Guadalajara': {'Guadalajara': 1.0}
}

# Evidencias observadas en el tiempo
# Cada evidencia es una observación parcial (ruidosa)
observaciones = ['industrial', 'rural', 'urbano']

# Probabilidad de observación por estado
# P(observación | estado)
P_obs = {
    'Querétaro': {'industrial': 0.8, 'rural': 0.1, 'urbano': 0.1},
    'San Luis': {'industrial': 0.2, 'rural': 0.7, 'urbano': 0.1},
    'Guadalajara': {'industrial': 0.1, 'rural': 0.2, 'urbano': 0.7}
}

# Creencia inicial
creencia = {'Querétaro': 1.0, 'San Luis': 0.0, 'Guadalajara': 0.0}

# Filtrado paso a paso (Forward algorithm)
historial_creencias = []

for obs in observaciones:
    nueva = {estado: 0.0 for estado in estados}

    # Predicción
    for estado_prev in estados:
        for estado_actual in estados:
            trans = transiciones[estado_prev].get(estado_actual, 0)
            nueva[estado_actual] += creencia[estado_prev] * trans

    # Actualización con evidencia (filtrado)
    for estado in estados:
        nueva[estado] *= P_obs[estado][obs]

    # Normalización
    total = sum(nueva.values())
    for estado in estados:
        nueva[estado] /= total if total > 0 else 1

    creencia = nueva
    historial_creencias.append(creencia.copy())

# Mostrar resultados
print("[Filtrado, Predicción, Suavizado y Explicación]")
for t, paso in enumerate(historial_creencias):
    print(f"Paso {t + 1} (observación: {observaciones[t]}):")
    for estado in estados:
        print(f"  {estado}: {paso[estado]:.4f}")
    print()
