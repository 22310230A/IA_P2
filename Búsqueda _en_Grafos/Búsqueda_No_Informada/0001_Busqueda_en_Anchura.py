from collections import deque

# Definimos un grafo simple usando un diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def busqueda_en_anchura(grafo, inicio, objetivo):
    # Cola para recorrer el grafo
    cola = deque([[inicio]])
    
    # Conjunto para guardar los nodos visitados
    visitados = set()

    while cola:
        # Sacamos el primer camino de la cola
        camino = cola.popleft()
        nodo = camino[-1]

        # Si el nodo no ha sido visitado
        if nodo not in visitados:
            visitados.add(nodo)

            # Verificamos si hemos llegado al objetivo
            if nodo == objetivo:
                return camino

            # Agregamos los vecinos del nodo a la cola
            for vecino in grafo.get(nodo, []):
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)

    return None

# Prueba del algoritmo
inicio = 'A'
objetivo = 'F'
camino = busqueda_en_anchura(grafo, inicio, objetivo)

print(f"Camino desde {inicio} hasta {objetivo}: {camino}")
