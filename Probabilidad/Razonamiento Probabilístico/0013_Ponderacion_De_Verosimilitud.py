# Ponderación de Verosimilitud
#
# Es un método de muestreo donde no se rechazan muestras,
# sino que cada muestra se pondera (pesa) según la probabilidad
# de haber observado la evidencia.

import random

# Red simplificada:
# México → Querétaro → San Luis → Guadalajara

# Probabilidades condicionales simuladas
P_México = 0.3
P_Querétaro_dado_México = {True: 0.8, False: 0.2}
P_SanLuis_dado_Querétaro = {True: 0.9, False: 0.3}
P_Guadalajara_dado_SanLuis = {True: 0.95, False: 0.1}

# Observación fija (evidencia)
# Queremos estimar P(San Luis = True | Guadalajara = True)

def generar_muestra_ponderada(evidencia):
    peso = 1.0

    # Generar México
    mexico = random.random() < P_México

    # Querétaro
    queretaro = random.random() < P_Querétaro_dado_México[mexico]

    # San Luis
    san_luis = random.random() < P_SanLuis_dado_Querétaro[queretaro]

    # Guadalajara (evidencia conocida)
    if evidencia['Guadalajara'] is True:
        peso *= P_Guadalajara_dado_SanLuis[san_luis]
    else:
        peso *= 1 - P_Guadalajara_dado_SanLuis[san_luis]

    return {
        'México': mexico,
        'Querétaro': queretaro,
        'San Luis': san_luis,
        'Guadalajara': evidencia['Guadalajara'],
        'peso': peso
    }

# Muestreo con ponderación
def muestreo_ponderado(n, evidencia):
    suma_pesos = 0
    suma_pesos_SL_true = 0

    for _ in range(n):
        muestra = generar_muestra_ponderada(evidencia)
        peso = muestra['peso']
        suma_pesos += peso

        if muestra['San Luis']:
            suma_pesos_SL_true += peso

    return suma_pesos_SL_true / suma_pesos if suma_pesos > 0 else 0

# Ejecutar
evidencia = {'Guadalajara': True}
N = 10000

print("Ponderación de Verosimilitud")
print(f"Aproximación de P(San Luis | Guadalajara=True): {muestreo_ponderado(N, evidencia):.4f}")
