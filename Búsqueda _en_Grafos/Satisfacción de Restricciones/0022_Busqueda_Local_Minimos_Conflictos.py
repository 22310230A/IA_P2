# Búsqueda Local: Mínimos-Conflictos
# Grafo usado:
# Ciudades conectadas que deben tener colores diferentes entre ellas.
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Monterrey
#
# Mínimos conflictos: comienza con una asignación aleatoria,
# luego cambia los colores de ciudades conflictivas hasta resolver todo (si es posible).

import random

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

def conflictos(ciudad, color, asignacion):
    return sum(1 for vecino in vecinos[ciudad] if asignacion.get(vecino) == color)

def minimos_conflictos(ciudades, max_intentos=1000):
    asignacion = {ciudad: random.choice(colores) for ciudad in ciudades}

    for _ in range(max_intentos):
        conflictuadas = [c for c in ciudades if conflictos(c, asignacion[c], asignacion) > 0]

        if not conflictuadas:
            return asignacion

        ciudad = random.choice(conflictuadas)
        mejor_color = min(colores, key=lambda color: conflictos(ciudad, color, asignacion))
        asignacion[ciudad] = mejor_color

    return None

# Prueba
solucion = minimos_conflictos(ciudades)
print(f"[Mínimos Conflictos] Solución: {solucion if solucion else 'No se encontró solución'}")
