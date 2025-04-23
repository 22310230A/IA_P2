# Filtros de Kalman (versión 1D simplificada)
#
# Se usa para estimar el estado de un sistema dinámico (posición, velocidad, etc.)
# a partir de mediciones ruidosas y un modelo de predicción.

# Supongamos que queremos rastrear la posición de un objeto
# que se mueve con velocidad constante, pero nuestras mediciones tienen ruido.

import random

# Parámetros del sistema
posicion_real = 0.0
velocidad_real = 1.0

# Ruido en el sistema
ruido_movimiento = 0.1
ruido_medicion = 0.5

# Estimación inicial
posicion_estim = 0.0
incertidumbre_estim = 1.0

# Matriz de covarianza y ruido
R = ruido_medicion**2  # incertidumbre de la medición
Q = ruido_movimiento**2  # incertidumbre del modelo

# Pasos de simulación
pasos = 10

print("[Filtro de Kalman 1D - Posición]")

for t in range(1, pasos + 1):
    # Movimiento real del objeto
    posicion_real += velocidad_real + random.gauss(0, ruido_movimiento)

    # Medición con ruido
    medicion = posicion_real + random.gauss(0, ruido_medicion)

    # PREDICCIÓN
    posicion_predicha = posicion_estim + velocidad_real
    incertidumbre_predicha = incertidumbre_estim + Q

    # ACTUALIZACIÓN (Kalman Gain)
    K = incertidumbre_predicha / (incertidumbre_predicha + R)
    posicion_estim = posicion_predicha + K * (medicion - posicion_predicha)
    incertidumbre_estim = (1 - K) * incertidumbre_predicha

    print(f"Paso {t}:")
    print(f"  Real      : {posicion_real:.2f}")
    print(f"  Medición  : {medicion:.2f}")
    print(f"  Estimado  : {posicion_estim:.2f}")
    print(f"  Incertidumbre: {incertidumbre_estim:.4f}\n")
