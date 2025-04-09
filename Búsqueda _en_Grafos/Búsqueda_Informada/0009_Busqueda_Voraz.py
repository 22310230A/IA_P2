# Grafo con conexiones
grafo = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': [],
    'E': [],
    'F': ['G'],
    'G': []
}

# Heurística (entre más bajo, más cerca del objetivo)
heuristica = {
    'S': 6,
    'A': 4,
    'B': 3,
    'C': 4,
    'D': 2,
    'E': 2,
    'F': 1,
    'G': 0
}

def busqueda_voraz(grafo, heuristica, inicio, objetivo):
    visitados = set()
    camino = [inicio]

    actual = inicio
    while actual != objetivo:
        visitados.add(actual)

        vecinos = grafo.get(actual, [])
        # Filtramos vecinos no visitados
        vecinos_no_visitados = [n for n in vecinos if n not in visitados]

        if not vecinos_no_visitados:
            return None  # No hay a dónde ir

        # Elegimos el vecino con menor heurística
        actual = min(vecinos_no_visitados, key=lambda n: heuristica[n])
        camino.append(actual)

    return camino

# Prueba
inicio = 'S'
objetivo = 'G'
camino = busqueda_voraz(grafo, heuristica, inicio, objetivo)

print(f"Camino encontrado desde {inicio} hasta {objetivo}: {camino}")
