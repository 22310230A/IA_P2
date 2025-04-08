# Grafo representado como diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def busqueda_profundidad_limitada(grafo, nodo, objetivo, limite, camino=None):
    if camino is None:
        camino = [nodo]

    if nodo == objetivo:
        return camino

    if limite <= 0:
        return None

    for vecino in grafo.get(nodo, []):
        if vecino not in camino:
            nuevo_camino = busqueda_profundidad_limitada(grafo, vecino, objetivo, limite - 1, camino + [vecino])
            if nuevo_camino:
                return nuevo_camino

    return None

# Prueba del algoritmo
inicio = 'A'
objetivo = 'F'
limite = 3
camino = busqueda_profundidad_limitada(grafo, inicio, objetivo, limite)

print(f"Camino encontrado (límite {limite}) desde {inicio} hasta {objetivo}: {camino}")
