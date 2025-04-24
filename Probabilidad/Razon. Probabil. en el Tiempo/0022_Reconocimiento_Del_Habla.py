# Reconocimiento del Habla (usando un modelo oculto de Markov)
#
# Simulamos una cadena oculta de fonemas y una secuencia observada de sonidos.
# El objetivo es inferir qué secuencia de estados (fonemas) es la más probable
# que haya generado la señal observada.

import random

# Estados ocultos (fonemas)
fonemas = ['s', 't', 'k']

# Observaciones posibles (sonidos)
observaciones_posibles = ['z', 'tʰ', 'x']

# Matriz de transición entre fonemas
transiciones = {
    's': {'s': 0.5, 't': 0.3, 'k': 0.2},
    't': {'s': 0.2, 't': 0.6, 'k': 0.2},
    'k': {'s': 0.1, 't': 0.3, 'k': 0.6}
}

# P(sonido | fonema)
P_obs = {
    's': {'z': 0.9, 'tʰ': 0.05, 'x': 0.05},
    't': {'z': 0.1, 'tʰ': 0.8, 'x': 0.1},
    'k': {'z': 0.05, 'tʰ': 0.1, 'x': 0.85}
}

# Secuencia observada de sonidos (ruidosa)
sonidos = ['z', 'tʰ', 'x']

# Algoritmo de Viterbi (para encontrar la secuencia más probable de fonemas)
def viterbi(observaciones, estados, transiciones, emisiones):
    V = [{}]
    path = {}

    # Inicialización
    for estado in estados:
        V[0][estado] = 1.0 / len(estados) * emisiones[estado][observaciones[0]]
        path[estado] = [estado]

    # Iteración
    for t in range(1, len(observaciones)):
        V.append({})
        nuevo_path = {}

        for estado in estados:
            (prob, estado_prev) = max(
                (V[t - 1][e_prev] * transiciones[e_prev][estado] * emisiones[estado][observaciones[t]], e_prev)
                for e_prev in estados
            )
            V[t][estado] = prob
            nuevo_path[estado] = path[estado_prev] + [estado]
        path = nuevo_path

    # Resultado
    n = len(observaciones) - 1
    (prob_max, estado_final) = max((V[n][estado], estado) for estado in estados)
    return path[estado_final], prob_max

# Ejecutar
secuencia, probabilidad = viterbi(sonidos, fonemas, transiciones, P_obs)

# Mostrar resultados
print("[Reconocimiento del Habla]")
print(f"Sonidos observados: {sonidos}")
print(f"Secuencia fonética más probable: {secuencia}")
print(f"Probabilidad: {probabilidad:.6f}")
