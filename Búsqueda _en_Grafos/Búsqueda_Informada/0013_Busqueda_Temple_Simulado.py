# Busqueda Temple Simulado
#  Grafo usado:
# Red de ciudades conectadas con diferentes caminos y costos.
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Monterrey

# Temple Simulado acepta caminos peores al inicio para evitar atascos.
# A medida que "se enfría", se vuelve más exigente. Simula el proceso físico de enfriamiento controlado.

import math
import random

grafo = {
    'México': [('Querétaro', 2), ('Puebla', 3)],
    'Querétaro': [('San Luis', 4)],
    'Puebla': [('Veracruz', 5)],
    'San Luis': [('Monterrey', 3)],
    'Veracruz': [('Monterrey', 2)],
    'Monterrey': []
}

heuristica = {
    'México': 7,
    'Querétaro': 6,
    'Puebla': 5,
    'San Luis': 2,
    'Veracruz': 1,
    'Monterrey': 0
}

def temple_simulado(grafo, heuristica, inicio, objetivo, temperatura_inicial=10, enfriamiento=0.95):
    actual = inicio
    camino = [actual]
    temperatura = temperatura_inicial

    while actual != objetivo and temperatura > 0.1:
        vecinos = grafo.get(actual, [])
        if not vecinos:
            return None  # No hay más caminos posibles

        siguiente, _ = random.choice(vecinos)

        delta = heuristica[actual] - heuristica[siguiente]
        probabilidad = math.exp(delta / temperatura) if delta < 0 else 1

        if random.random() < probabilidad:
            actual = siguiente
            camino.append(actual)

        temperatura *= enfriamiento

    return camino if actual == objetivo else None

# Prueba
inicio = 'México'
objetivo = 'Monterrey'
camino = temple_simulado(grafo, heuristica, inicio, objetivo)

print(f"[Temple Simulado] Camino: {camino if camino else 'No se encontró una ruta'}")
