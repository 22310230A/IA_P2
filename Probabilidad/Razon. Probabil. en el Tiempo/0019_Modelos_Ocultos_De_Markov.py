# Modelos Ocultos de Markov (Hidden Markov Models - HMM)
#
# En un HMM:
# - El estado real del sistema es oculto (no observable directamente).
# - Solo podemos observar señales relacionadas con ese estado.
#
# Aquí, el agente se mueve entre ciudades, pero solo recibe observaciones ruidosas
# que le dan pistas sobre su ubicación.

import random

# Estados ocultos
estados = ['Querétaro', 'San Luis', 'Guadalajara']

# Observaciones posibles
observaciones_posibles = ['industrial', 'rural', 'urbano']

# Matriz de transición entre estados ocultos
transiciones = {
    'Querétaro': {'Querétaro': 0.1, 'San Luis': 0.9},
    'San Luis': {'San Luis': 0.3, 'Guadalajara': 0.7},
    'Guadalajara': {'Guadalajara': 1.0}
}

# P(observación | estado)
P_obs = {
    'Querétaro': {'industrial': 0.8, 'rural': 0.1, 'urbano': 0.1},
    'San Luis': {'industrial': 0.2, 'rural': 0.7, 'urbano': 0.1},
    'Guadalajara': {'industrial': 0.1, 'rural': 0.2, 'urbano': 0.7}
}

# Generar una secuencia oculta de estados y observaciones
def generar_hmm(pasos):
    secuencia_estados = []
    secuencia_obs = []

    estado = 'Querétaro'
    for _ in range(pasos):
        secuencia_estados.append(estado)
        obs = random.choices(
            population=list(P_obs[estado].keys()),
            weights=list(P_obs[estado].values())
        )[0]
        secuencia_obs.append(obs)

        opciones, probs = zip(*transiciones[estado].items())
        estado = random.choices(opciones, weights=probs)[0]

    return secuencia_estados, secuencia_obs

# Ejecutar simulación
pasos = 8
estados_generados, observaciones = generar_hmm(pasos)

# Mostrar resultados
print("[Modelos Ocultos de Markov]")
print("Observaciones:")
print(" → ".join(observaciones))
print("\nEstados reales (ocultos):")
print(" → ".join(estados_generados))
