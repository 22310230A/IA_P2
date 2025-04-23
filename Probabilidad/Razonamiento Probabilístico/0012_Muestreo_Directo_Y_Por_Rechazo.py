# Muestreo Directo y Por Rechazo
#
# En redes bayesianas grandes, calcular inferencia exacta puede ser costoso.
# Por eso usamos métodos de muestreo:
# - Directo: generamos muestras completas usando las probabilidades condicionales.
# - Por rechazo: descartamos muestras que no coinciden con la evidencia.

import random

# Red Bayesiana simplificada:
# México → Querétaro → San Luis → Guadalajara

# Probabilidades condicionales (simuladas)
P_México = 0.3
P_Querétaro_dado_México = {True: 0.8, False: 0.2}
P_SanLuis_dado_Querétaro = {True: 0.9, False: 0.3}
P_Guadalajara_dado_SanLuis = {True: 0.95, False: 0.1}

# Generar una muestra completa del mundo (muestreo directo)
def generar_muestra():
    mexico = random.random() < P_México
    queretaro = random.random() < P_Querétaro_dado_México[mexico]
    san_luis = random.random() < P_SanLuis_dado_Querétaro[queretaro]
    guadalajara = random.random() < P_Guadalajara_dado_SanLuis[san_luis]

    return {
        'México': mexico,
        'Querétaro': queretaro,
        'San Luis': san_luis,
        'Guadalajara': guadalajara
    }

# Muestreo directo: generamos muchas muestras sin condiciones
def muestreo_directo(n):
    cuenta = 0
    for _ in range(n):
        muestra = generar_muestra()
        if muestra['Guadalajara']:  # Queremos P(San Luis | Guadalajara = True)
            if muestra['San Luis']:
                cuenta += 1
    return cuenta / n

# Muestreo por rechazo: solo contamos muestras donde Guadalajara = True
def muestreo_por_rechazo(n):
    aceptadas = 0
    cuenta = 0
    for _ in range(n):
        muestra = generar_muestra()
        if muestra['Guadalajara']:
            aceptadas += 1
            if muestra['San Luis']:
                cuenta += 1
    return cuenta / aceptadas if aceptadas > 0 else 0

# Ejecutar ambos métodos
N = 10000
print("[Muestreo Directo]")
print(f"Aproximación de P(San Luis | Guadalajara=True): {muestreo_directo(N):.4f}")

print("\n[Muestreo por Rechazo]")
print(f"Aproximación de P(San Luis | Guadalajara=True): {muestreo_por_rechazo(N):.4f}")
