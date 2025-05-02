# Grafos de Planificación: GRAPHPLAN (simplificado)
#
# Simulamos niveles de acciones y estados en un grafo de planificación
# para alcanzar un objetivo desde un estado inicial.

# Estado inicial
estado_inicial = {'en(cdmx)', 'sin_boleto'}

# Objetivo
objetivo = {'en(guadalajara)'}

# Acciones definidas por sus precondiciones y efectos
acciones = {
    'comprar_boleto': {
        'precondiciones': {'en(cdmx)', 'sin_boleto'},
        'agrega': {'con_boleto'},
        'elimina': {'sin_boleto'}
    },
    'abordar_camion': {
        'precondiciones': {'en(cdmx)', 'con_boleto'},
        'agrega': {'en(guadalajara)'},
        'elimina': {'en(cdmx)'}
    }
}

# Simulación por niveles
def graphplan(estado_inicial, acciones, objetivo, max_niveles=5):
    niveles = [estado_inicial.copy()]

    for nivel in range(max_niveles):
        nivel_actual = niveles[-1]
        nuevo_estado = nivel_actual.copy()

        for accion, datos in acciones.items():
            if datos['precondiciones'].issubset(nivel_actual):
                nuevo_estado.update(datos['agrega'])
                nuevo_estado.difference_update(datos['elimina'])

        if objetivo.issubset(nuevo_estado):
            niveles.append(nuevo_estado)
            return niveles

        if nuevo_estado == nivel_actual:
            break  # sin cambios, no hay avance

        niveles.append(nuevo_estado)

    return None

# Ejecutar GRAPHPLAN
resultado = graphplan(estado_inicial, acciones, objetivo)

# Mostrar resultados
print("[GraphPlan - Grafo de planificación por niveles]\n")
if resultado:
    for i, nivel in enumerate(resultado):
        print(f"Nivel {i}: {nivel}")
    print("\n→ Objetivo alcanzado.")
else:
    print("No se pudo alcanzar el objetivo con las acciones dadas.")
