# Algoritmos de Búsqueda Local
#
# Simulamos un ejemplo básico de búsqueda local:
# encontrar el valor máximo de una función simple usando ascenso de colinas (hill climbing).

import random

# Función a optimizar
def funcion_objetivo(x):
    return -(x - 3) ** 2 + 9  # Parabola con máximo en x=3

# Algoritmo de ascenso de colinas
def hill_climbing(inicial, pasos, tam_paso):
    actual = inicial
    for _ in range(pasos):
        vecino = actual + random.choice([-tam_paso, tam_paso])
        if funcion_objetivo(vecino) > funcion_objetivo(actual):
            actual = vecino
    return actual, funcion_objetivo(actual)

# Ejecutar
inicio = random.uniform(0, 6)  # Empezar en un punto aleatorio entre 0 y 6
mejor_x, mejor_valor = hill_climbing(inicio, pasos=20, tam_paso=0.5)

# Mostrar resultados
print("[Algoritmos de Búsqueda Local]")
print(f"Punto inicial: {inicio:.2f}")
print(f"Mejor punto encontrado: {mejor_x:.2f}")
print(f"Valor de la función en ese punto: {mejor_valor:.2f}")
