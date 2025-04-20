# Problema: Asignación de colores a ciudades conectadas
#
# Ciudades:
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Monterrey
#
# Regla: ciudades conectadas no deben tener el mismo color

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

def resolver(asignacion, ciudades_restantes):
    if not ciudades_restantes:
        return asignacion

    ciudad = ciudades_restantes[0]
    for color in colores:
        if es_valido(asignacion, ciudad, color):
            asignacion[ciudad] = color
            resultado = resolver(asignacion, ciudades_restantes[1:])
            if resultado:
                return resultado
            del asignacion[ciudad]
    return None

# Prueba
solucion = resolver({}, ciudades)
print(f"[CSP] Asignación de colores válida: {solucion if solucion else 'No se encontró solución'}")
