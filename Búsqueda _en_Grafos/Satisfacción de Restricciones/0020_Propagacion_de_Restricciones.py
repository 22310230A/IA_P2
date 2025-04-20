# Propagación de Restricciones
# Grafo usado:
# Mapa de ciudades donde se deben asignar colores sin repetir entre vecinos.
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Monterrey
#
# Propagación de restricciones: elimina colores inválidos en los vecinos,
# y también en los vecinos de los vecinos, en cadena.

from collections import deque

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

def ac3(dominios):
    cola = deque([(x, y) for x in ciudades for y in vecinos[x]])

    while cola:
        x, y = cola.popleft()
        if reducir(x, y, dominios):
            if not dominios[x]:
                return False
            for z in vecinos[x]:
                if z != y:
                    cola.append((z, x))
    return True

def reducir(x, y, dominios):
    reducido = False
    for valor in dominios[x][:]:
        if all(valor == val for val in dominios[y]):
            dominios[x].remove(valor)
            reducido = True
    return reducido

def backtracking_prop_restricciones(asignacion, ciudades_restantes, dominios):
    if not ciudades_restantes:
        return asignacion

    ciudad = ciudades_restantes[0]
    for color in dominios[ciudad]:
        if es_valido(asignacion, ciudad, color):
            asignacion[ciudad] = color

            nuevos_dominios = {c: list(d) for c, d in dominios.items()}
            nuevos_dominios[ciudad] = [color]

            if ac3(nuevos_dominios):
                resultado = backtracking_prop_restricciones(asignacion, ciudades_restantes[1:], nuevos_dominios)
                if resultado:
                    return resultado

            del asignacion[ciudad]
    return None

def es_valido(asignacion, ciudad, color):
    for vecino in vecinos[ciudad]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True

# Prueba
dominios_iniciales = {ciudad: list(colores) for ciudad in ciudades}
solucion = backtracking_prop_restricciones({}, ciudades, dominios_iniciales)

print(f"[Propagación de restricciones] Solución: {solucion if solucion else 'No se encontró solución'}")
