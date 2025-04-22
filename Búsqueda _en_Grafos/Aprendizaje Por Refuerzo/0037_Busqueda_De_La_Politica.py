# Búsqueda de la Política usando el grafo de ciudades:
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Guadalajara
#
# El agente comienza con una política aleatoria y mejora su decisión
# en cada estado evaluando los valores estimados hasta que encuentra la mejor ruta.

# Estados y acciones posibles
estados = ['México', 'Querétaro', 'Puebla', 'San Luis', 'Veracruz', 'Guadalajara']
acciones = {
    'México': ['Querétaro', 'Puebla'],
    'Querétaro': ['San Luis'],
    'Puebla': ['Veracruz'],
    'San Luis': ['Guadalajara'],
    'Veracruz': ['Guadalajara'],
    'Guadalajara': []
}

# Recompensas conocidas
recompensas = {
    ('México', 'Querétaro'): -2,
    ('México', 'Puebla'): -3,
    ('Querétaro', 'San Luis'): -4,
    ('Puebla', 'Veracruz'): -5,
    ('San Luis', 'Guadalajara'): 10,
    ('Veracruz', 'Guadalajara'): 10
}

# Inicialización de política arbitraria (primer acción disponible)
politica = { estado: (acciones[estado][0] if acciones[estado] else None) for estado in estados }

# Valores estimados
valores = { estado: 0 for estado in estados }

# Parámetros
gamma = 0.9
umbral = 0.01
estable = False

while not estable:
    # Evaluación de política
    while True:
        cambio = 0
        nuevos_valores = valores.copy()

        for estado in estados:
            accion = politica[estado]
            if accion is None:
                continue

            recompensa = recompensas.get((estado, accion), 0)
            nuevos_valores[estado] = recompensa + gamma * valores.get(accion, 0)
            cambio = max(cambio, abs(nuevos_valores[estado] - valores[estado]))

        valores = nuevos_valores
        if cambio < umbral:
            break

    # Mejora de política
    estable = True
    for estado in estados:
        if not acciones[estado]:
            continue

        # Elegimos la mejor acción según los valores actuales
        mejor_accion = max(
            acciones[estado],
            key=lambda a: recompensas.get((estado, a), 0) + gamma * valores.get(a, 0)
        )

        if politica[estado] != mejor_accion:
            politica[estado] = mejor_accion
            estable = False

# Mostrar resultados
print("[Búsqueda de la Política] Política óptima encontrada:")
for estado in estados:
    if politica[estado]:
        print(f"{estado} → {politica[estado]}")
