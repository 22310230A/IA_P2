# Comprobación Hacia Delante
# Grafo usado:
# Mapa de ciudades conectadas donde cada ciudad debe tener un color diferente a sus vecinas.
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Monterrey
#
# Comprobación hacia adelante: al asignar un color, elimina esa opción de los vecinos.
# Si algún vecino se queda sin colores posibles, retrocede de inmediato (evita perder tiempo).

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

def copiar_dominio(dominios):
    return {ciudad: list(colores) for ciudad, colores in dominios.items()}

def forward_checking(asignacion, ciudades_restantes, dominios):
    if not ciudades_restantes:
        return asignacion

    ciudad = ciudades_restantes[0]

    for color in dominios[ciudad]:
        if es_valido(asignacion, ciudad, color):
            asignacion[ciudad] = color

            # Copiamos dominios para no alterar globalmente
            nuevos_dominios = copiar_dominio(dominios)
            for vecino in vecinos[ciudad]:
                if vecino not in asignacion and color in nuevos_dominios[vecino]:
                    nuevos_dominios[vecino].remove(color)

                    # Si algún vecino se queda sin colores válidos → retroceder
                    if not nuevos_dominios[vecino]:
                        del asignacion[ciudad]
                        break
            else:
                resultado = forward_checking(asignacion, ciudades_restantes[1:], nuevos_dominios)
                if resultado:
                    return resultado

            del asignacion[ciudad]
    return None

def es_valido(asignacion, ciudad, color):
    for vecino in vecinos[ciudad]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True

# Inicialización
dominios_iniciales = {ciudad: list(colores) for ciudad in ciudades}
solucion = forward_checking({}, ciudades, dominios_iniciales)

print(f"[Comprobación hacia adelante] Solución: {solucion if solucion else 'No se encontró solución'}")
