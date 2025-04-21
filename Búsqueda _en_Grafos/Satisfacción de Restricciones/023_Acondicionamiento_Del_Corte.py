# Acondicionamiento del Corte
# Grafo usado:
# Mapa de ciudades conectadas con restricciones de color.
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Monterrey
#
# Acondicionamiento del corte: se eliminan temporalmente variables y restricciones
# para resolver por partes, y luego se integran las soluciones.

ciudades = ['México', 'Querétaro', 'Puebla', 'San Luis', 'Veracruz', 'Monterrey']

vecinos_originales = {
    'México': ['Querétaro', 'Puebla'],
    'Querétaro': ['México', 'San Luis'],
    'Puebla': ['México', 'Veracruz'],
    'San Luis': ['Querétaro', 'Monterrey'],
    'Veracruz': ['Puebla', 'Monterrey'],
    'Monterrey': ['San Luis', 'Veracruz']
}

colores = ['Rojo', 'Verde', 'Azul']

def es_valido(asignacion, ciudad, color, vecinos):
    for vecino in vecinos[ciudad]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True

def backtracking(asignacion, ciudades_restantes, vecinos):
    if not ciudades_restantes:
        return asignacion

    ciudad = ciudades_restantes[0]
    for color in colores:
        if es_valido(asignacion, ciudad, color, vecinos):
            asignacion[ciudad] = color
            resultado = backtracking(asignacion, ciudades_restantes[1:], vecinos)
            if resultado:
                return resultado
            del asignacion[ciudad]
    return None

def acondicionamiento_del_corte():
    # Paso 1: eliminamos temporalmente Monterrey del grafo
    ciudades_reducidas = [c for c in ciudades if c != 'Monterrey']
    vecinos_reducidos = {c: [v for v in vecinos if v != 'Monterrey'] for c, vecinos in vecinos_originales.items() if c != 'Monterrey'}

    # Paso 2: resolvemos el subproblema sin Monterrey
    asignacion_parcial = backtracking({}, ciudades_reducidas, vecinos_reducidos)

    if not asignacion_parcial:
        return None

    # Paso 3: agregamos Monterrey y lo conectamos nuevamente
    vecinos_completos = dict(vecinos_originales)
    for ciudad in ciudades:
        if ciudad not in asignacion_parcial:
            continue
        if ciudad in vecinos_completos['Monterrey']:
            if asignacion_parcial[ciudad] in colores:
                # Eliminamos color en conflicto para Monterrey
                colores_validos = [c for c in colores if c != asignacion_parcial[ciudad]]
                for color in colores_validos:
                    if es_valido(asignacion_parcial, 'Monterrey', color, vecinos_completos):
                        asignacion_parcial['Monterrey'] = color
                        return asignacion_parcial
                return None

    return None

# Prueba
solucion = acondicionamiento_del_corte()
print(f"[Acondicionamiento del Corte] Solución: {solucion if solucion else 'No se encontró solución'}")
