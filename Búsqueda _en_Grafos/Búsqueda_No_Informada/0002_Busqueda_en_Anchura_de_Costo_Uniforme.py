import heapq  # Cola de prioridad

# Grafo con costos en formato: 'nodo': [(vecino, costo), ...]
grafo = {
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5), ('E', 3)],
    'C': [('F', 4)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

def busqueda_costo_uniforme(grafo, inicio, objetivo):
    # Cola de prioridad: (costo total, camino hasta ahora)
    cola = [(0, [inicio])]
    visitados = set()

    while cola:
        costo_actual, camino = heapq.heappop(cola)
        nodo = camino[-1]

        if nodo in visitados:
            continue

        visitados.add(nodo)

        # Si llegamos al objetivo, regresamos el camino y su costo
        if nodo == objetivo:
            return camino, costo_actual

        for vecino, costo in grafo.get(nodo, []):
            if vecino not in visitados:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                heapq.heappush(cola, (costo_actual + costo, nuevo_camino))

    return None, float('inf')

# Prueba del algoritmo
inicio = 'A'
objetivo = 'F'
camino, costo = busqueda_costo_uniforme(grafo, inicio, objetivo)

print(f"Camino de menor costo desde {inicio} hasta {objetivo}: {camino} con costo {costo}")
