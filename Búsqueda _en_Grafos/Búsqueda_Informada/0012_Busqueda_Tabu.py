# Busqueda tabu
# Grafo usado:
# Representa ciudades conectadas con caminos posibles y sus heurísticas.
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Monterrey

# En esta búsqueda se permite moverse a soluciones no óptimas, pero evita volver a lugares ya visitados recientemente (lista tabú).
# Esto ayuda a escapar de soluciones locales y buscar otras mejores.

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

def busqueda_tabu(grafo, heuristica, inicio, objetivo, tamaño_tabu=2):
    actual = inicio
    camino = [actual]
    lista_tabu = [actual]

    while actual != objetivo:
        vecinos = grafo.get(actual, [])
        candidatos = [nodo for nodo, _ in vecinos if nodo not in lista_tabu]

        if not candidatos:
            return None  # No hay opciones válidas

        # Selecciona el vecino con menor heurística, sin importar si empeora
        siguiente = min(candidatos, key=lambda x: heuristica[x])
        camino.append(siguiente)

        # Actualiza nodo actual y la lista tabú
        actual = siguiente
        lista_tabu.append(actual)
        if len(lista_tabu) > tamaño_tabu:
            lista_tabu.pop(0)

    return camino

# Prueba
inicio = 'México'
objetivo = 'Monterrey'
camino = busqueda_tabu(grafo, heuristica, inicio, objetivo)

print(f"[Búsqueda Tabú] Camino: {camino if camino else 'No se encontró una ruta'}")
