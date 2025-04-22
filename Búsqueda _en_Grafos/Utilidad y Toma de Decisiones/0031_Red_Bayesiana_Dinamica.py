# Red Bayesiana Dinámica (DBN)
#
# Representa cómo evoluciona un sistema en el tiempo mediante una red bayesiana conectada en pasos temporales.
# Usamos como ejemplo la evolución de estados de clima (Soleado o Lluvia) y cómo eso afecta las decisiones de moverse.

# Estados posibles del clima
estados = ['Soleado', 'Lluvia']

# Probabilidades iniciales
P_inicial = {
    'Soleado': 0.7,
    'Lluvia': 0.3
}

# Probabilidades de transición: P(estado_t+1 | estado_t)
P_transicion = {
    'Soleado': {
        'Soleado': 0.8,
        'Lluvia': 0.2
    },
    'Lluvia': {
        'Soleado': 0.4,
        'Lluvia': 0.6
    }
}

# Probabilidades de observación: P(observación | estado)
P_observacion = {
    'Soleado': {
        'Cielo despejado': 0.9,
        'Nublado': 0.1
    },
    'Lluvia': {
        'Cielo despejado': 0.2,
        'Nublado': 0.8
    }
}

# Sucesión de observaciones en el tiempo
observaciones = ['Cielo despejado', 'Nublado', 'Nublado']

# Creencia inicial (copiamos P_inicial)
creencia = P_inicial.copy()

# Actualización usando filtrado bayesiano
def actualizar_creencia(creencia_anterior, observacion_actual):
    nueva_creencia = {}

    for estado_actual in estados:
        # 1. Predicción: suma ponderada de todas las posibles transiciones
        predicho = sum(
            creencia_anterior[estado_previo] * P_transicion[estado_previo][estado_actual]
            for estado_previo in estados
        )

        # 2. Observación: multiplicamos por la probabilidad de la observación actual
        observado = P_observacion[estado_actual][observacion_actual]
        nueva_creencia[estado_actual] = predicho * observado

    # Normalización
    total = sum(nueva_creencia.values())
    for estado in nueva_creencia:
        nueva_creencia[estado] /= total

    return nueva_creencia

# Ejecutar la actualización paso a paso
for t, observacion in enumerate(observaciones):
    creencia = actualizar_creencia(creencia, observacion)
    print(f"[Paso {t+1}] Observación: {observacion}")
    for estado, prob in creencia.items():
        print(f"  - {estado}: {prob:.4f}")
