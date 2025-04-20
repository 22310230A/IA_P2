# Salto Atrás Dirigido por Conflictos
# Grafo usado:
# Ciudades conectadas que no deben compartir el mismo color.
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Monterrey
#
# Salto atrás dirigido por conflictos: en lugar de retroceder solo un nivel,
# salta directamente hasta la ciudad que causó el conflicto.

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

def salto_atras(asignacion, ciudades_restantes, conflictos):
    if not ciudades_restantes:
        return asignacion

    ciudad = ciudades_restantes[0]

    for color in colores:
        if es_valido(asignacion, ciudad, color):
            asignacion[ciudad] = color
            conflictos[ciudad] = set()
            resultado = salto_atras(asignacion, ciudades_restantes[1:], conflictos)
            if resultado:
                return resultado
            del asignacion[ciudad]
        else:
            for vecino in vecinos[ciudad]:
                if vecino in asignacion and asignacion[vecino] == color:
                    conflictos.setdefault(ciudad, set()).add(vecino)

    if ciudad in conflictos and conflictos[ciudad]:
        for i, anterior in enumerate(ciudades_restantes):
            if anterior in conflictos[ciudad]:
                return salto_atras(asignacion, ciudades_restantes[i:], conflictos)

    return None

# Prueba
solucion = salto_atras({}, ciudades, {})
print(f"[Salto Atrás Dirigido por Conflictos] Solución: {solucion if solucion else 'No se encontró solución'}")
