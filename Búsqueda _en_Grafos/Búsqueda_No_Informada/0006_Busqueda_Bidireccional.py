from collections import deque

# Definimos un grafo en forma de diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

def bidireccional(grafo, inicio, objetivo):
    if inicio == objetivo:
        return [inicio]  # Si inicio y objetivo son iguales

    # Colas para almacenar caminos desde ambos lados
    cola_inicio = deque([[inicio]])     # Desde el inicio
    cola_objetivo = deque([[objetivo]]) # Desde el objetivo

    # Diccionarios para registrar nodos visitados y sus caminos
    visitados_inicio = {inicio: [inicio]}
    visitados_objetivo = {objetivo: [objetivo]}

    while cola_inicio and cola_objetivo:
        # ---------- Expansión desde el lado del inicio ----------
        camino_inicio = cola_inicio.popleft()
        nodo_inicio = camino_inicio[-1]

        for vecino in grafo.get(nodo_inicio, []):
            if vecino not in visitados_inicio:
                nuevo_camino = camino_inicio + [vecino]
                visitados_inicio[vecino] = nuevo_camino
                cola_inicio.append(nuevo_camino)

                # Si el nodo también fue visitado desde el otro lado, encontramos el camino
                if vecino in visitados_objetivo:
                    # Unimos los dos caminos encontrados
                    return nuevo_camino[:-1] + visitados_objetivo[vecino][::-1]

        # ---------- Expansión desde el lado del objetivo ----------
        camino_objetivo = cola_objetivo.popleft()
        nodo_objetivo = camino_objetivo[-1]

        for padre in grafo:
            if nodo_objetivo in grafo[padre]:  # Buscar nodos que apuntan al actual
                if padre not in visitados_objetivo:
                    nuevo_camino = [padre] + camino_objetivo
                    visitados_objetivo[padre] = nuevo_camino
                    cola_objetivo.append(nuevo_camino)

                    # Si también fue visitado desde el inicio, conectamos caminos
                    if padre in visitados_inicio:
                        return visitados_inicio[padre][:-1] + nuevo_camino

    return None  # Si no se encuentra ningún camino

# Prueba del algoritmo
inicio = 'A'
objetivo = 'F'
camino = bidireccional(grafo, inicio, objetivo)

print(f"Camino encontrado desde {inicio} hasta {objetivo}: {camino}")
