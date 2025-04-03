# Grafo simple como diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def busqueda_en_profundidad(grafo, inicio, objetivo, visitados=None, camino=None):
    if visitados is None:
        visitados = set()
    if camino is None:
        camino = [inicio]

    visitados.add(inicio)

    if inicio == objetivo:
        return camino

    for vecino in grafo.get(inicio, []):
        if vecino not in visitados:
            nuevo_camino = busqueda_en_profundidad(grafo, vecino, objetivo, visitados, camino + [vecino])
            if nuevo_camino:
                return nuevo_camino

    return None

# Prueba del algoritmo
inicio = 'A'
objetivo = 'F'
camino = busqueda_en_profundidad(grafo, inicio, objetivo)

print(f"Camino encontrado desde {inicio} hasta {objetivo}: {camino}")
