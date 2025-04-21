# Redes de Decisión
# Grafo usado:
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Monterrey
#
# El agente está en México y debe elegir una ruta.
# Cada ruta tiene un costo (esfuerzo) y una utilidad esperada en el destino.

# Opciones disponibles desde México
rutas = {
    'Querétaro': {
        'costo': 2,
        'probabilidad_exito': 0.9,
        'utilidad_ciudad': 70
    },
    'Puebla': {
        'costo': 3,
        'probabilidad_exito': 0.8,
        'utilidad_ciudad': 100
    }
}

def utilidad_esperada(prob, utilidad, costo):
    return (prob * utilidad) - costo

# Evaluar las rutas disponibles
for destino, datos in rutas.items():
    utilidad = utilidad_esperada(
        prob=datos['probabilidad_exito'],
        utilidad=datos['utilidad_ciudad'],
        costo=datos['costo']
    )
    print(f"Ruta a {destino}: utilidad esperada = {utilidad:.2f}")
