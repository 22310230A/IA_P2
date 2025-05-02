# Planificación Condicional
#
# Simulamos un plan que se adapta según condiciones del entorno,
# como si hay tráfico o si está lloviendo.

# Estado del entorno
entorno = {
    'llueve': False,
    'hay_trafico': True
}

# Plan condicional basado en el entorno
def planificar(entorno):
    plan = []

    if entorno['llueve']:
        plan.append("llevar paraguas")
    else:
        plan.append("ropa ligera")

    if entorno['hay_trafico']:
        plan.append("salir más temprano")
        plan.append("usar transporte público")
    else:
        plan.append("usar auto personal")

    plan.append("llegar a terminal")
    plan.append("abordar camión")

    return plan

# Generar plan
plan_final = planificar(entorno)

# Mostrar resultados
print("[Planificación Condicional]")
print(f"Condiciones del entorno: {entorno}")
print("Plan generado:")
for i, paso in enumerate(plan_final, 1):
    print(f"{i}. {paso.capitalize()}")
