# Procesos Estacionarios
#
# Un proceso estocástico es estacionario si las reglas de transición
# (probabilidades) no cambian con el tiempo.

# Usamos una pequeña cadena de ciudades:
# Querétaro → San Luis → Guadalajara
# con la posibilidad de permanecer en cada ciudad.

# Estados del sistema
estados = ['Querétaro', 'San Luis', 'Guadalajara']

# Matriz de transición fija (estacionaria): P(siguiente | actual)
transiciones = {
    'Querétaro': {'Querétaro': 0.1, 'San Luis': 0.9},
    'San Luis': {'San Luis': 0.3, 'Guadalajara': 0.7},
    'Guadalajara': {'Guadalajara': 1.0}  # estado terminal absorbente
}

# Distribución inicial: el agente comienza 100% en Querétaro
estado_actual = {
    'Querétaro': 1.0,
    'San Luis': 0.0,
    'Guadalajara': 0.0
}

# Simulación de evolución del sistema en el tiempo
pasos = 6
print("[Proceso Estacionario] Evolución de la creencia en el tiempo:\n")

for t in range(1, pasos + 1):
    nuevo_estado = {estado: 0.0 for estado in estados}

    # Aplicar la matriz de transición
    for estado in estados:
        for destino in transiciones[estado]:
            prob = estado_actual[estado] * transiciones[estado][destino]
            nuevo_estado[destino] += prob

    estado_actual = nuevo_estado

    print(f"Paso {t}:")
    for ciudad, prob in estado_actual.items():
        print(f"  {ciudad}: {prob:.4f}")
    print()
