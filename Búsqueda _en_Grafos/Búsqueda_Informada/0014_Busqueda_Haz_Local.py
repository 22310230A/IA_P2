# Buzqueda haz local
# Grafo usado:
# Red de ciudades conectadas por caminos posibles.
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Monterrey

# Haz Local: explora múltiples caminos a la vez (haz), pero solo se queda con los mejores para la siguiente ronda.
# Es una búsqueda más amplia que la de ascensión de colinas.

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

def haz_local(grafo, heuristica, inicio, objetivo, k=2):
    haz_actual = [[inicio]]

    while haz_actual:
        nuevos_haces = []

        for camino in haz_actual:
            ultimo = camino[-1]
            if ultimo == objetivo:
                return camino

            for vecino, _ in grafo.get(ultimo, []):
                if vecino not in camino:
                    nuevos_haces.append(camino + [vecino])

        # Ordenamos por heurística del último nodo del camino
        nuevos_haces.sort(key=lambda camino: heuristica[camino[-1]])

        # Seleccionamos los k mejores haces para la siguiente ronda
        haz_actual = nuevos_haces[:k]

    return None

# Prueba
inicio = 'México'
objetivo = 'Monterrey'
camino = haz_local(grafo, heuristica, inicio, objetivo)

print(f"[Haz Local] Camino: {camino if camino else 'No se encontró una ruta'}")
