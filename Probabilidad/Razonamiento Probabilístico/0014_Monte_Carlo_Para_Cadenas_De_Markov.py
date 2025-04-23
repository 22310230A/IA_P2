# Monte Carlo para Cadenas de Markov
#
# Simulamos trayectorias aleatorias a través de una cadena de Markov
# para estimar el valor esperado (utilidad) de cada estado.

import random

# Estados del sistema (ciudades)
estados = ['Querétaro', 'San Luis', 'Guadalajara']

# Transiciones entre estados (cadena de Markov)
transiciones = {
    'Querétaro': {'San Luis': 0.9, 'Querétaro': 0.1},
    'San Luis': {'Guadalajara': 0.8, 'San Luis': 0.2},
    'Guadalajara': {'Guadalajara': 1.0}  # estado absorbente
}

# Recompensas por llegar a un estado
recompensas = {
    'Querétaro': 0,
    'San Luis': -1,
    'Guadalajara': 10
}

# Número de simulaciones
simulaciones = 10000
gamma = 0.9

# Valor estimado acumulado para cada estado
valores = {estado: 0 for estado in estados}
conteos = {estado: 0 for estado in estados}

# Simulación Monte Carlo
for _ in range(simulaciones):
    estado = 'Querétaro'
    G = 0
    factor = 1.0
    recorrido = []

    # Simular un episodio completo
    while estado != 'Guadalajara':
        recorrido.append(estado)
        recompensa = recompensas[estado]
        G += factor * recompensa
        factor *= gamma
        opciones = list(transiciones[estado].items())
        estados_siguientes, probs = zip(*opciones)
        estado = random.choices(estados_siguientes, weights=probs)[0]

    # Agregar última recompensa de Guadalajara
    G += factor * recompensas['Guadalajara']
    recorrido.append('Guadalajara')

    # Actualizar estimaciones para cada estado en la trayectoria
    for estado_en_trayectoria in set(recorrido):
        valores[estado_en_trayectoria] += G
        conteos[estado_en_trayectoria] += 1

# Calcular promedios
for estado in estados:
    if conteos[estado] > 0:
        valores[estado] /= conteos[estado]

# Mostrar resultados
print("[Monte Carlo para Cadenas de Markov]")
for estado in estados:
    print(f"Valor estimado de {estado}: {valores[estado]:.4f}")
