# Planificación Continua y Multiagente
#
# Simulamos un sistema donde múltiples agentes colaboran y ajustan
# sus planes en tiempo real ante cambios en el entorno.

# Definimos los agentes y sus planes iniciales
agentes = {
    'agente_1': {
        'objetivo': 'entregar_paquete',
        'plan': ['recoger_paquete', 'entregar_paquete']
    },
    'agente_2': {
        'objetivo': 'asistir_agente_1',
        'plan': ['verificar_estado_agente_1', 'proporcionar_ayuda']
    }
}

# Estado del entorno
entorno = {
    'paquete_disponible': True,
    'agente_1_disponible': True
}

# Función para ejecutar el plan de un agente
def ejecutar_plan(agente, entorno):
    print(f"\n[Ejecutando plan de {agente}]")
    plan = agentes[agente]['plan']
    for accion in plan:
        if accion == 'recoger_paquete':
            if entorno['paquete_disponible']:
                print(f"{agente} ha recogido el paquete.")
                entorno['paquete_disponible'] = False
            else:
                print(f"{agente} no puede recoger el paquete: no está disponible.")
                return False
        elif accion == 'entregar_paquete':
            if not entorno['paquete_disponible']:
                print(f"{agente} ha entregado el paquete.")
            else:
                print(f"{agente} no puede entregar el paquete: no lo ha recogido.")
                return False
        elif accion == 'verificar_estado_agente_1':
            if entorno['agente_1_disponible']:
                print(f"{agente} verifica que agente_1 está disponible.")
            else:
                print(f"{agente} detecta que agente_1 no está disponible.")
        elif accion == 'proporcionar_ayuda':
            if not entorno['agente_1_disponible']:
                print(f"{agente} proporciona ayuda a agente_1.")
                entorno['agente_1_disponible'] = True
            else:
                print(f"{agente} no necesita proporcionar ayuda: agente_1 está disponible.")
    return True

# Simulación de ejecución
print("[Planificación Continua y Multiagente]")
ejecutar_plan('agente_1', entorno)

# Simulamos un cambio en el entorno: agente_1 no está disponible
entorno['agente_1_disponible'] = False
print("\n[Cambio en el entorno: agente_1 no está disponible]")

# Agente 2 detecta el cambio y ajusta su plan
ejecutar_plan('agente_2', entorno)

# Agente 1 intenta continuar su plan después de recibir ayuda
ejecutar_plan('agente_1', entorno)
