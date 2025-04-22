# Q-Learning usando el grafo de ciudades:
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Guadalajara
#
# El agente explora el grafo y actualiza los valores Q(s, a) directamente.
# No necesita conocer las transiciones ni recompensas por adelantado.

import random

# Estados del grafo
estados = ['México', 'Querétaro', 'Puebla', 'San Luis', 'Veracruz', 'Guadalajara']

# Acciones posibles desde cada estado
acciones = {
    'México': ['Querétaro', 'Puebla'],
    'Querétaro': ['San Luis'],
    'Puebla': ['Veracruz'],
    'San Luis': ['Guadalajara'],
    'Veracruz': ['Guadalajara'],
    'Guadalajara': []
}

# Recompensas por transición (desconocidas para el agente)
recompensas = {
    ('México', 'Querétaro'): -2,
    ('México', 'Puebla'): -3,
    ('Querétaro', 'San Luis'): -4,
    ('Puebla', 'Veracruz'): -5,
    ('San Luis', 'Guadalajara'): 10,
    ('Veracruz', 'Guadalajara'): 10
}

# Inicializamos Q(s, a) con 0
Q = { (s, a): 0 for s in estados for a in acciones[s] }

# Parámetros de aprendizaje
alpha = 0.5       # tasa de aprendizaje
gamma = 0.9       # factor de descuento
epsilon = 0.2     # probabilidad de explorar (ε-greedy)
episodios = 50

for _ in range(episodios):
    estado = 'México'

    while estado != 'Guadalajara':
        # Política ε-greedy
        if random.random() < epsilon:
            accion = random.choice(acciones[estado])  # explorar
        else:
            accion = max(acciones[estado], key=lambda a: Q[(estado, a)])  # explotar

        recompensa = recompensas.get((estado, accion), 0)
        siguiente = accion

        # Valor máximo de la siguiente acción
        if acciones[siguiente]:
            max_Q_sig = max(Q[(siguiente, a)] for a in acciones[siguiente])
        else:
            max_Q_sig = 0

        # Actualización Q-learning
        Q[(estado, accion)] += alpha * (recompensa + gamma * max_Q_sig - Q[(estado, accion)])

        estado = siguiente  # avanzar al siguiente estado

# Mostrar la política aprendida
print("[Q-Learning] Política óptima aprendida:")
for estado in estados:
    if acciones[estado]:
        mejor_accion = max(acciones[estado], key=lambda a: Q[(estado, a)])
        print(f"{estado} → {mejor_accion}")
