# Hipótesis de Markov: Procesos de Markov
#
# Un proceso de Markov cumple con la hipótesis de que:
# El estado actual contiene toda la información relevante del pasado.
# Es decir, P(X_t | X_{t−1}, ..., X_0) = P(X_t | X_{t−1})

import random

# Estados (ciudades)
estados = ['Querétaro', 'San Luis', 'Guadalajara']

# Transiciones entre estados (cadena de Markov)
transiciones = {
    'Querétaro': ['San Luis', 'Querétaro'],
    'San Luis': ['San Luis', 'Guadalajara'],
    'Guadalajara': ['Guadalajara']
}

# Probabilidades asociadas
probabilidades = {
    'Querétaro': [0.9, 0.1],
    'San Luis': [0.7, 0.3],
    'Guadalajara': [1.0]
}

# Simulación de una trayectoria usando solo el estado actual (Markov)
def simular_markov(inicio, pasos):
    trayectoria = [inicio]
    actual = inicio
    for _ in range(pasos):
        opciones = transiciones[actual]
        probs = probabilidades[actual]
        actual = random.choices(opciones, weights=probs)[0]
        trayectoria.append(actual)
    return trayectoria

# Ejecutar la simulación
inicio = 'Querétaro'
pasos = 10
trayectoria = simular_markov(inicio, pasos)

print("[Hipótesis de Markov: Proceso de Markov]")
print(f"Trayectoria simulada desde {inicio} (pasos = {pasos}):")
print(" → ".join(trayectoria))
