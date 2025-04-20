# Búsquedas A* y AO*
# Grafo usado:
# Representa ciudades conectadas con distintos costos de viaje entre ellas.
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Monterrey


import heapq
# Grafo con pesos
grafo = {
    'México': [('Querétaro', 2), ('Puebla', 3)],
    'Querétaro': [('San Luis', 4)],
    'Puebla': [('Veracruz', 5)],
    'San Luis': [('Monterrey', 3)],
    'Veracruz': [('Monterrey', 2)],
    'Monterrey': []
}

# Heurística estimada hacia 'Monterrey'
heuristica = {
    'México': 7,
    'Querétaro': 6,
    'Puebla': 5,
    'San Luis': 2,
    'Veracruz': 1,
    'Monterrey': 0
}

# --------------------- A* ---------------------
def busqueda_a_estrella(grafo, heuristica, inicio, objetivo):
    cola = [(heuristica[inicio], 0, [inicio])]  # (f, g, camino)
    visitados = set()

    while cola:
        f, g, camino = heapq.heappop(cola)
        actual = camino[-1]

        if actual == objetivo:
            return camino, g

        if actual in visitados:
            continue
        visitados.add(actual)

        for vecino, costo in grafo.get(actual, []):
            if vecino not in visitados:
                g_nuevo = g + costo
                f_nuevo = g_nuevo + heuristica[vecino]
                heapq.heappush(cola, (f_nuevo, g_nuevo, camino + [vecino]))

    return None, float('inf')

# --------------------- AO* (simplificado) ---------------------
def busqueda_ao_estrella(grafo, heuristica, inicio, objetivo):
    actual = inicio
    camino = [actual]

    while actual != objetivo:
        vecinos = grafo.get(actual, [])

        if not vecinos:
            return None

        mejor_vecino = min(vecinos, key=lambda x: x[1] + heuristica[x[0]])
        actual = mejor_vecino[0]
        camino.append(actual)

    return camino

# --------------------- Pruebas ---------------------
inicio = 'México'
objetivo = 'Monterrey'

camino_a, costo_a = busqueda_a_estrella(grafo, heuristica, inicio, objetivo)
print(f"[A*] Camino: {camino_a}, Costo total: {costo_a}")

camino_ao = busqueda_ao_estrella(grafo, heuristica, inicio, objetivo)
print(f"[AO*] Camino: {camino_ao}")
