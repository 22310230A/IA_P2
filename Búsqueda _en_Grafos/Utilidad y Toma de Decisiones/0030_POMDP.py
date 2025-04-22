# POMDP (Proceso de Decisión de Markov Parcialmente Observable)
#
#         CDMX
#        /    \
#    León     Morelia
#     |         |
#  Aguascalientes   Tepatitlán
#         \       /
#        Guadalajara
#
# En un POMDP el agente no sabe con certeza en qué estado está,
# pero mantiene una creencia (probabilidad) sobre su ubicación.

# Estados posibles
estados = ['CDMX', 'León', 'Morelia', 'Aguascalientes', 'Tepatitlán', 'Guadalajara']

# Acciones disponibles desde cada estado
acciones = {
    'CDMX': ['ir_a_León', 'ir_a_Morelia'],
    'León': ['ir_a_Aguascalientes'],
    'Morelia': ['ir_a_Tepatitlán'],
    'Aguascalientes': ['ir_a_Guadalajara'],
    'Tepatitlán': ['ir_a_Guadalajara'],
    'Guadalajara': []
}

# Modelo de transición: acción → (destino, recompensa)
modelo = {
    'ir_a_León': ('León', -2),
    'ir_a_Morelia': ('Morelia', -3),
    'ir_a_Aguascalientes': ('Aguascalientes', -4),
    'ir_a_Tepatitlán': ('Tepatitlán', -4),
    'ir_a_Guadalajara': ('Guadalajara', 10)
}

# Creencia inicial del agente (probabilidad de estar en cada estado)
creencia = {
    'CDMX': 0.6,
    'León': 0.2,
    'Morelia': 0.2,
    'Aguascalientes': 0.0,
    'Tepatitlán': 0.0,
    'Guadalajara': 0.0
}

gamma = 0.9  # factor de descuento

def utilidad_esperada(creencia, accion):
    """Calcula la utilidad esperada de una acción, dada la creencia actual."""
    destino, recompensa = modelo[accion]
    utilidad = 0
    for estado, prob in creencia.items():
        if accion in acciones[estado]:
            utilidad += prob * (recompensa + gamma * 0)  # No se propaga utilidad, ejemplo simple
    return utilidad

# Evaluar todas las acciones posibles dadas las creencias
acciones_posibles = set()
for acts in acciones.values():
    acciones_posibles.update(acts)

mejor_accion = None
mejor_utilidad = float('-inf')

for accion in acciones_posibles:
    util = utilidad_esperada(creencia, accion)
    if util > mejor_utilidad:
        mejor_utilidad = util
        mejor_accion = accion

# Mostrar resultado
print(f"[POMDP] Mejor acción según creencia: {mejor_accion}")
print(f"Utilidad esperada: {mejor_utilidad:.2f}")
