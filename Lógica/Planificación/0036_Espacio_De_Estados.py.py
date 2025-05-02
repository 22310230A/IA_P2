# Espacio de Estados
#
# Simulamos un espacio de estados como un grafo, donde cada nodo
# representa una ubicación y cada arista una posible acción de viaje.

# Definimos el espacio como un diccionario de transiciones posibles
espacio_de_estados = {
    'cdmx': ['queretaro', 'puebla'],
    'queretaro': ['san_luis'],
    'puebla': ['veracruz'],
    'san_luis': ['guadalajara'],
    'veracruz': ['guadalajara'],
    'guadalajara': []
}

# Búsqueda de rutas posibles con DFS
def buscar_rutas(origen, destino, visitados=None, camino=None):
    if visitados is None:
        visitados = set()
    if camino is None:
        camino = []

    camino = camino + [origen]
    visitados.add(origen)

    if origen == destino:
        return [camino]

    rutas = []
    for vecino in espacio_de_estados.get(origen, []):
        if vecino not in visitados:
            nuevas_rutas = buscar_rutas(vecino, destino, visitados.copy(), camino)
            rutas.extend(nuevas_rutas)

    return rutas

# Consultar rutas desde CDMX a Guadalajara
rutas_encontradas = buscar_rutas('cdmx', 'guadalajara')

# Mostrar resultados
print("[Espacio de Estados - Rutas posibles]")
for i, ruta in enumerate(rutas_encontradas, 1):
    print(f"Ruta {i}: {' → '.join(ruta)}")
