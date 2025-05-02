# Planificación Lógica Proposicional: SATPLAN (simplificado)
#
# Simulamos la representación de un problema de planificación
# como proposiciones booleanas y verificamos si un plan cumple con el objetivo.

# Representación de acciones como proposiciones booleanas
acciones = {
    'comprar_boleto': {
        'precondiciones': ['en(cdmx)', 'sin_boleto'],
        'efectos': ['con_boleto', '¬sin_boleto']
    },
    'abordar_camion': {
        'precondiciones': ['en(cdmx)', 'con_boleto'],
        'efectos': ['en(guadalajara)', '¬en(cdmx)']
    }
}

# Estado inicial
estado = {
    'en(cdmx)': True,
    'sin_boleto': True,
    'con_boleto': False,
    'en(guadalajara)': False
}

# Objetivo
objetivo = {'en(guadalajara)'}

# Función para verificar si se puede aplicar una acción
def puede_aplicarse(accion, estado):
    return all(estado.get(p, False) for p in acciones[accion]['precondiciones'])

# Función para aplicar una acción (simulando evaluación proposicional)
def aplicar(accion, estado):
    nuevo_estado = estado.copy()
    for efecto in acciones[accion]['efectos']:
        if efecto.startswith('¬'):
            nuevo_estado[efecto[1:]] = False
        else:
            nuevo_estado[efecto] = True
    return nuevo_estado

# Generar plan como conjunto de proposiciones
plan = ['comprar_boleto', 'abordar_camion']

# Ejecutar el plan paso a paso
print("[SATPLAN - Planificación lógica proposicional]\nEstado inicial:")
print(estado)

for paso in plan:
    if puede_aplicarse(paso, estado):
        estado = aplicar(paso, estado)
        print(f"\nDespués de '{paso}':")
        print(estado)
    else:
        print(f"\nNo se puede aplicar '{paso}' (precondiciones no satisfechas).")

# Verificar si se alcanzó el objetivo
exito = all(estado.get(o, False) for o in objetivo)
print(f"\n¿Objetivo alcanzado? {'Sí' if exito else 'No'}")
