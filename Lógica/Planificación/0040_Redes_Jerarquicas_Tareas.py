# Redes Jerárquicas de Tareas
#
# Simulamos una planificación jerárquica (HTN), donde tareas
# complejas se dividen en subtareas simples.

# Tarea principal
tarea_principal = 'viajar_cdmx_guadalajara'

# Jerarquía de tareas
tareas = {
    'viajar_cdmx_guadalajara': ['prepararse_para_viaje', 'comprar_boleto', 'abordar_camion'],
    'prepararse_para_viaje': ['empacar_maleta', 'verificar_documentos']
}

# Lista de tareas atómicas que se pueden ejecutar directamente
tareas_atomicas = ['empacar_maleta', 'verificar_documentos', 'comprar_boleto', 'abordar_camion']

# Función para descomponer tareas jerárquicas
def descomponer(tarea, tareas, tareas_atomicas):
    if tarea in tareas_atomicas:
        return [tarea]
    subtareas = tareas.get(tarea, [])
    plan = []
    for sub in subtareas:
        plan.extend(descomponer(sub, tareas, tareas_atomicas))
    return plan

# Generar el plan completo
plan_final = descomponer(tarea_principal, tareas, tareas_atomicas)

# Mostrar resultado
print("[Redes Jerárquicas de Tareas - HTN]")
print(f"Tarea principal: {tarea_principal}")
print("Plan descompuesto en subtareas atómicas:")
for i, paso in enumerate(plan_final, 1):
    print(f"{i}. {paso.replace('_', ' ').capitalize()}")
