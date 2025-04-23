# Algoritmo Hacia Adelante-Atrás (Forward-Backward)
#
# Usado para realizar "suavizado" en procesos temporales:
# Permite estimar la probabilidad de haber estado en un estado pasado
# usando todas las observaciones (pasadas y futuras).

# Estados
estados = ['Querétaro', 'San Luis', 'Guadalajara']

# Transiciones estacionarias P(estado_t+1 | estado_t)
transiciones = {
    'Querétaro': {'Querétaro': 0.1, 'San Luis': 0.9},
    'San Luis': {'San Luis': 0.3, 'Guadalajara': 0.7},
    'Guadalajara': {'Guadalajara': 1.0}
}

# P(observación | estado)
P_obs = {
    'Querétaro': {'industrial': 0.8, 'rural': 0.1, 'urbano': 0.1},
    'San Luis': {'industrial': 0.2, 'rural': 0.7, 'urbano': 0.1},
    'Guadalajara': {'industrial': 0.1, 'rural': 0.2, 'urbano': 0.7}
}

# Observaciones en el tiempo
observaciones = ['industrial', 'rural', 'urbano']

# Paso 1: Forward (filtrado)
alpha = []
creencia = {'Querétaro': 1.0, 'San Luis': 0.0, 'Guadalajara': 0.0}

for obs in observaciones:
    nueva = {estado: 0.0 for estado in estados}

    # Predicción y actualización
    for prev in estados:
        for actual in estados:
            trans = transiciones[prev].get(actual, 0)
            nueva[actual] += creencia[prev] * trans

    for estado in estados:
        nueva[estado] *= P_obs[estado][obs]

    # Normalizar
    total = sum(nueva.values())
    for estado in estados:
        nueva[estado] /= total if total > 0 else 1

    alpha.append(nueva.copy())
    creencia = nueva

# Paso 2: Backward
beta = [{estado: 1.0 for estado in estados}]
for t in reversed(range(len(observaciones) - 1)):
    beta_t = {}
    for estado in estados:
        suma = 0
        for sig in estados:
            trans = transiciones[estado].get(sig, 0)
            obs_prob = P_obs[sig][observaciones[t + 1]]
            suma += trans * obs_prob * beta[0][sig]
        beta_t[estado] = suma
    # Normalizar
    total = sum(beta_t.values())
    for estado in estados:
        beta_t[estado] /= total if total > 0 else 1
    beta.insert(0, beta_t)

# Paso 3: Suavizado: gamma[t](estado) = alpha[t](estado) * beta[t](estado)
print("[Algoritmo Hacia Adelante-Atrás]")
for t in range(len(observaciones)):
    print(f"Paso {t + 1} (obs: {observaciones[t]})")
    for estado in estados:
        gamma = alpha[t][estado] * beta[t][estado]
        print(f"  {estado}: {gamma:.4f}")
    print()
