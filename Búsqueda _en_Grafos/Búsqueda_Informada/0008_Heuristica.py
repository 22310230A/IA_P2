# Grafo

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

# Heurística: estimación de la distancia desde cada nodo hasta el objetivo 'G'
heuristica = {
    'S': 6,
    'A': 4,
    'B': 3,
    'C': 4,
    'D': 2,
    'E': 2,
    'F': 1,
    'G': 0  # El objetivo siempre tiene heurística 0
}

# Mostrar heurísticas de forma clara
print("Heurísticas hacia el nodo objetivo G:\n")
for nodo, h in heuristica.items():
    print(f"Nodo {nodo}: h(n) = {h}")
