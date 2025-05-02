# Sistemas Expertos
#
# Simulamos un sistema experto básico que recomienda una acción
# según condiciones como clima, tráfico y horario.

# Hechos conocidos
hechos = {
    'llueve': True,
    'hay_trafico': True,
    'es_hora_pico': False
}

# Base de reglas del sistema experto
def motor_inferencia(hechos):
    recomendaciones = []

    # Regla 1
    if hechos['llueve'] and hechos['hay_trafico']:
        recomendaciones.append("Salir más temprano o posponer el viaje.")

    # Regla 2
    if not hechos['llueve'] and not hechos['hay_trafico']:
        recomendaciones.append("Es buen momento para salir.")

    # Regla 3
    if hechos['es_hora_pico']:
        recomendaciones.append("Usar transporte público si es posible.")

    # Regla 4
    if hechos['llueve'] and not hechos['es_hora_pico']:
        recomendaciones.append("Llevar paraguas y salir con precaución.")

    return recomendaciones

# Ejecutar el sistema experto
resultado = motor_inferencia(hechos)

# Mostrar resultados
print("[Sistemas Expertos - Recomendaciones del sistema]\n")
for r in resultado:
    print(f"- {r}")
