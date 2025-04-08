# Grafo como diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs_limitado(grafo, nodo, objetivo, limite, camino=None):
    if camino is None:
        camino = [nodo]

    if nodo == objetivo:
        return camino

    if limite <= 0:
        return None

    for vecino in grafo.get(nodo, []):
        if vecino not in camino:
            resultado = dfs_limitado(grafo, vecino, objetivo, limite - 1, camino + [vecino])
            if resultado:
                return resultado

    return None

def busqueda_profundidad_iterativa(grafo, inicio, objetivo, limite_maximo):
    for limite in range(limite_maximo + 1):
        resultado = dfs_limitado(grafo, inicio, objetivo, limite)
        if resultado:
            return resultado
    return None

# Prueba del algoritmo
inicio = 'A'
objetivo = 'F'
limite_maximo = 5
camino = busqueda_profundidad_iterativa(grafo, inicio, objetivo, limite_maximo)

print(f"Camino encontrado desde {inicio} hasta {objetivo}: {camino}")
