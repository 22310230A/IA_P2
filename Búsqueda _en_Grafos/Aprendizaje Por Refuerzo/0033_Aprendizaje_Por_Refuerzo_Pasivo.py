# Aprendizaje por Refuerzo Pasivo
#
# Grafo de ciudades:
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Guadalajara
#
# El agente ya tiene una política fija, y aprende los valores de los estados
# observando múltiples trayectorias sin explorar por sí mismo.

estados = ['México', 'Querétaro', 'Puebla', 'San Luis', 'Veracruz', 'Guadalajara']

# Política fija (qué acción tomar en cada estado)
politica_fija = {
    'México': 'Querétaro',
    'Querétaro': 'San Luis',
    'San Luis': 'Guadalajara',
    'Puebla': 'Veracruz',
    'Veracruz': 'Guadalajara',
    'Guadalajara': None  # estado final
}

# Recompensas inmediatas por transición
recompensas = {
    ('México', 'Querétaro'): -2,
    ('Querétaro', 'San Luis'): -4,
    ('San Luis', 'Guadalajara'): 10,
    ('México', 'Puebla'): -3,
    ('Puebla', 'Veracruz'): -5,
    ('Veracruz', 'Guadalajara'): 10
}

# Inicialización de valores
valores = {estado: 0 for estado in estados}
cuentas = {estado: 0 for estado in estados}
gamma = 0.9

# Simulamos múltiples episodios siguiendo la política
episodios = 10

for _ in range(episodios):
    estado = 'México'
    historia = []

    # Recorre la ruta siguiendo la política
    while politica_fija[estado]:
        siguiente = politica_fija[estado]
        recompensa = recompensas.get((estado, siguiente), 0)
        historia.append((estado, recompensa))
        estado = siguiente

    historia.append(('Guadalajara', 0))  # estado final

    # Estimación hacia atrás
    G = 0
    for estado, recompensa in reversed(historia):
        G = recompensa + gamma * G
        cuentas[estado] += 1
        valores[estado] += (G - valores[estado]) / cuentas[estado]

# Mostrar valores aprendidos
print("[Aprendizaje por Refuerzo Pasivo] Valores estimados por estado:")
for estado in estados:
    print(f"{estado}: {valores[estado]:.2f}")
