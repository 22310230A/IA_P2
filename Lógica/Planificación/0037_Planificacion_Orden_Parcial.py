# Planificación de Orden Parcial
#
# Simulamos un plan donde algunas acciones tienen orden obligatorio,
# pero otras pueden ejecutarse en cualquier secuencia válida.

# Acciones del plan y sus dependencias parciales
acciones = {
    'comprar_boleto': [],
    'empacar': [],
    'abordar_camion': ['comprar_boleto'],
    'llegar_guadalajara': ['abordar_camion']
}

# Función para encontrar orden válido respetando restricciones
def planificar_parcial(acciones):
    plan = []
    pendientes = acciones.copy()

    while pendientes:
        ejecutadas_en_paso = []
        for accion, pre in pendientes.items():
            if all(p in plan for p in pre):
                plan.append(accion)
                ejecutadas_en_paso.append(accion)
        if not ejecutadas_en_paso:
            raise Exception("Dependencias cíclicas o sin solución.")
        for ejecutada in ejecutadas_en_paso:
            pendientes.pop(ejecutada)
    return plan

# Ejecutar planificación
plan_generado = planificar_parcial(acciones)

# Mostrar resultado
print("[Planificación de Orden Parcial]")
print("Secuencia válida de acciones:")
for i, paso in enumerate(plan_generado, 1):
    print(f"{i}. {paso.replace('_', ' ').capitalize()}")
