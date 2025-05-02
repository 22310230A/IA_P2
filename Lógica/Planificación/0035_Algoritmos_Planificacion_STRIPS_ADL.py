# Algoritmos de Planificación: STRIPS y ADL
#
# Simulamos un plan estilo STRIPS: estado inicial, acciones con precondiciones y efectos,
# y estado objetivo. Modelamos un plan para viajar desde CDMX a Guadalajara.

# Estado inicial
estado = {
    'en(cdmx)': True,
    'tiene_boleto': False,
    'en_guadalajara': False
}

# Acciones STRIPS
acciones = {
    'comprar_boleto': {
        'precondiciones': ['en(cdmx)'],
        'agrega': ['tiene_boleto'],
        'elimina': []
    },
    'abordar_camion': {
        'precondiciones': ['en(cdmx)', 'tiene_boleto'],
        'agrega': ['en_guadalajara'],
        'elimina': ['en(cdmx)']
    }
}

# Aplicar acción
def aplicar_accion(estado, accion):
    if all(estado.get(cond, False) for cond in acciones[accion]['precondiciones']):
        nuevo_estado = estado.copy()
        for a in acciones[accion]['agrega']:
            nuevo_estado[a] = True
        for e in acciones[accion]['elimina']:
            nuevo_estado[e] = False
        return nuevo_estado
    return None

# Plan
plan = ['comprar_boleto', 'abordar_camion']

# Ejecutar plan paso a paso
print("[Planificación - STRIPS]\nEstado inicial:")
print(estado)
for paso in plan:
    nuevo = aplicar_accion(estado, paso)
    if nuevo:
        estado = nuevo
        print(f"\nDespués de '{paso}':")
        print(estado)
    else:
        print(f"\nNo se pudo aplicar '{paso}' por falta de precondiciones.")
