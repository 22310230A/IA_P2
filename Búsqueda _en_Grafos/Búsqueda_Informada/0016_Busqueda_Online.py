# Búsqueda Online
# Grafo usado:
# Representa ciudades conectadas. El agente no conoce el grafo completo desde el inicio.
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Monterrey

# Búsqueda Online: el agente solo ve los vecinos del nodo actual en tiempo real.
# Aprende el grafo paso a paso mientras se mueve, sin saber todo desde el inicio.

grafo = {
    'México': [('Querétaro', 2), ('Puebla', 3)],
    'Querétaro': [('San Luis', 4)],
    'Puebla': [('Veracruz', 5)],
    'San Luis': [('Monterrey', 3)],
    'Veracruz': [('Monterrey', 2)],
    'Monterrey': []
}

# Simula la obtención dinámica de vecinos, como si se revelaran en tiempo real
def obtener_vecinos(nodo):
    return grafo.get(nodo, [])

def busqueda_online(inicio, objetivo):
    actual = inicio
    camino = [actual]
    visitados = set()

    while actual != objetivo:
        visitados.add(actual)
        vecinos = obtener_vecinos(actual)
        vecinos_no_visitados = [v for v, _ in vecinos if v not in visitados]

        if not vecinos_no_visitados:
            return None  # No hay a dónde ir

        siguiente = vecinos_no_visitados[0]  # Elige el primero que vea
        camino.append(siguiente)
        actual = siguiente

    return camino

# Prueba
inicio = 'México'
objetivo = 'Monterrey'
camino = busqueda_online(inicio, objetivo)

print(f"[Búsqueda Online] Camino: {camino if camino else 'No se encontró una ruta'}")
