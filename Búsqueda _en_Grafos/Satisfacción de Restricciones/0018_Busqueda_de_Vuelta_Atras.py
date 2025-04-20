# Búsqueda de Vuelta Atrás
# Grafo usado:
# Representa ciudades conectadas que no deben compartir el mismo color.
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Monterrey
#
# Backtracking: intenta asignar colores uno por uno.
# Si se queda sin opciones válidas, retrocede y cambia decisiones anteriores.

ciudades = ['México', 'Querétaro', 'Puebla', 'San Luis', 'Veracruz', 'Monterrey']

vecinos = {
    'México': ['Querétaro', 'Puebla'],
    'Querétaro': ['México', 'San Luis'],
    'Puebla': ['México', 'Veracruz'],
    'San Luis': ['Querétaro', 'Monterrey'],
    'Veracruz': ['Puebla', 'Monterrey'],
    'Monterrey': ['San Luis', 'Veracruz']
}

colores = ['Rojo', 'Verde', 'Azul']

def es_valido(asignacion, ciudad, color):
    for vecino in vecinos[ciudad]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True

def backtracking(asignacion, ciudades_restantes):
    if not ciudades_restantes:
        return asignacion

    ciudad = ciudades_restantes[0]
    for color in colores:
        if es_valido(asignacion, ciudad, color):
            asignacion[ciudad] = color
            resultado = backtracking(asignacion, ciudades_restantes[1:])
            if resultado:
                return resultado
            del asignacion[ciudad]  # Vuelta atrás
    return None

# Prueba
solucion = backtracking({}, ciudades)
print(f"[Backtracking] Asignación de colores válida: {solucion if solucion else 'No se encontró solución'}")
