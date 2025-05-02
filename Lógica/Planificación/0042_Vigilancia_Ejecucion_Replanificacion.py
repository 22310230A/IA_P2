# Vigilancia de Ejecución y Replanificación
#
# Simulamos la ejecución paso a paso de un plan con monitoreo.
# Si algo falla en el camino, se replanifica automáticamente.

# Plan original
plan = [
    'comprar_boleto',
    'abordar_camion',
    'llegar_guadalajara'
]

# Simulación del entorno dinámico
eventos_inesperados = {
    'abordar_camion': 'retraso del transporte'  # evento que impide continuar normalmente
}

# Función de ejecución con monitoreo
def ejecutar_plan(plan, eventos):
    print("[Vigilancia de Ejecución y Replanificación]")
    for paso in plan:
        if paso in eventos:
            print(f" Fallo en '{paso}': {eventos[paso]}")
            print("Replanificando...")
            return replanificar(paso)
        else:
            print(f" Ejecutando: {paso}")
    print("Plan completado con éxito.")

# Función de replanificación
def replanificar(fallo):
    if fallo == 'abordar_camion':
        nuevo_plan = ['esperar siguiente camión', 'abordar_camion', 'llegar_guadalajara']
    else:
        nuevo_plan = ['consultar agente de viajes']
    print(" Nuevo plan sugerido:")
    for paso in nuevo_plan:
        print(f"- {paso.capitalize()}")
    return nuevo_plan

# Ejecutar plan con vigilancia
ejecutar_plan(plan, eventos_inesperados)
