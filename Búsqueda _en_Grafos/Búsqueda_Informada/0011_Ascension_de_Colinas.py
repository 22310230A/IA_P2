# Búsqueda de Ascensión de Colinas
# Grafo usado:
# Representa ciudades conectadas con distintos costos estimados.
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Monterrey

# Esta búsqueda siempre se mueve al vecino con la heurística más baja (subida directa a la colina).
# No retrocede si se equivoca. Puede quedarse atrapada en un punto que "parece bueno", pero no lleva al objetivo.

grafo = {
    'México': [('Querétaro', 2), ('Puebla', 3)],
    'Querétaro': [('San Luis', 4)],
    'Puebla': [('Veracruz', 5)],
    'San Luis': [('Monterrey', 3)],
    'Veracruz': [('Monterrey', 2)],
    'Monterrey': []
}

heuristica = {
    'México': 7,
    'Querétaro': 6,
    'Puebla': 5,
    'San Luis': 2,
    'Veracruz': 1,
    'Monterrey': 0
}

def ascension_de_colinas(grafo, heuristica, inicio, objetivo):
    actual = inicio
    camino = [actual]

    while actual != objetivo:
        vecinos = grafo.get(actual, [])

        # Filtra vecinos que no llevan a nada
        vecinos_validos = [nodo for nodo, _ in vecinos]
        if not vecinos_validos:
            return None  # Se quedó atrapado

        # Selecciona el vecino con menor heurística
        siguiente = min(vecinos_validos, key=lambda x: heuristica[x])

        # Si no es mejor que el actual, se queda atrapado
        if heuristica[siguiente] >= heuristica[actual]:
            return None

        actual = siguiente
        camino.append(actual)

    return camino

# Prueba
inicio = 'México'
objetivo = 'Monterrey'
camino = ascension_de_colinas(grafo, heuristica, inicio, objetivo)

print(f"[Ascensión de Colinas] Camino: {camino if camino else 'No se encontró una ruta óptima'}")
