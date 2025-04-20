# Algoritmos Genéticos
# Grafo usado:
# Red de ciudades conectadas por caminos posibles.
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Monterrey

# Algoritmos Genéticos: simulan evolución natural.
# Generan soluciones aleatorias (caminos), las cruzan y mutan para mejorar generación tras generación.

import random

grafo = {
    'México': [('Querétaro', 2), ('Puebla', 3)],
    'Querétaro': [('San Luis', 4)],
    'Puebla': [('Veracruz', 5)],
    'San Luis': [('Monterrey', 3)],
    'Veracruz': [('Monterrey', 2)],
    'Monterrey': []
}

objetivo = 'Monterrey'

def evaluar(camino):
    if camino[-1] != objetivo:
        return float('inf')
    return len(camino)

def generar_camino(inicio):
    camino = [inicio]
    actual = inicio
    while actual != objetivo and grafo[actual]:
        siguiente = random.choice(grafo[actual])[0]
        if siguiente not in camino:
            camino.append(siguiente)
            actual = siguiente
        else:
            break
    return camino

def cruzar(padre1, padre2):
    punto = random.randint(1, min(len(padre1), len(padre2)) - 1)
    hijo = padre1[:punto]
    for nodo in padre2:
        if nodo not in hijo:
            hijo.append(nodo)
    return hijo

def mutar(camino):
    if len(camino) > 2:
        i = random.randint(1, len(camino)-2)
        nodo_actual = camino[i-1]
        vecinos = [v for v, _ in grafo.get(nodo_actual, []) if v not in camino]
        if vecinos:
            camino[i] = random.choice(vecinos)
    return camino

def algoritmos_geneticos(inicio, poblacion_tam=6, generaciones=30):
    poblacion = [generar_camino(inicio) for _ in range(poblacion_tam)]

    for _ in range(generaciones):
        poblacion.sort(key=evaluar)
        nueva_poblacion = poblacion[:2]

        while len(nueva_poblacion) < poblacion_tam:
            padre1, padre2 = random.sample(poblacion[:4], 2)
            hijo = cruzar(padre1, padre2)
            hijo = mutar(hijo)
            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

    mejor = min(poblacion, key=evaluar)
    return mejor if mejor[-1] == objetivo else None

# Prueba
inicio = 'México'
camino = algoritmos_geneticos(inicio)

print(f"[Algoritmos Genéticos] Camino: {camino if camino else 'No se encontró una ruta'}")
