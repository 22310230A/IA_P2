from collections import deque

# Grafo con ciclos posibles
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def busqueda_en_grafo(grafo, inicio, objetivo):
    # Cola para mantener los caminos a explorar (tipo BFS)
    cola = deque([[inicio]])

    # Conjunto para registrar los nodos ya visitados
    visitados = set()

    while cola:
        # Tomamos el primer camino de la cola
        camino = cola.popleft()
        nodo = camino[-1]

        # Si ya lo visitamos, lo saltamos
        if nodo in visitados:
            continue

        # Marcamos como visitado
        visitados.add(nodo)

        # Si es el objetivo, regresamos el camino encontrado
        if nodo == objetivo:
            return camino

        # Agregamos a la cola todos los vecinos no visitados
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)

    return None  # Si no se encuentra ningún camino

# Prueba del algoritmo
inicio = 'A'
objetivo = 'F'
camino = busqueda_en_grafo(grafo, inicio, objetivo)

print(f"Camino encontrado desde {inicio} hasta {objetivo}: {camino}")
