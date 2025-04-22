# Exploración vs. Explotación con el grafo de ciudades:
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Guadalajara
#
# El agente elige entre explorar (tomar caminos al azar)
# o explotar (seguir la mejor ruta aprendida según Q-values)

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

# Recompensas por transición
recompensas = {
    ('México', 'Querétaro'): -2,
    ('México', 'Puebla'): -3,
    ('Querétaro', 'San Luis'): -4,
    ('Puebla', 'Veracruz'): -5,
    ('San Luis', 'Guadalajara'): 10,
    ('Veracruz', 'Guadalajara'): 10
}

# Inicializar Q(s, a)
Q = { (s, a): 0 for s in estados for a in acciones[s] }

# Parámetros
alpha = 0.5
gamma = 0.9
episodios = 50
epsilon_explora = 1.0  # solo explora
epsilon_explota = 0.0  # solo explota

def entrenar_Q(epsilon):
    """Entrena una política Q con cierto nivel de exploración"""
    Q_local = Q.copy()

    for _ in range(episodios):
        estado = 'México'

        while estado != 'Guadalajara':
            if random.random() < epsilon:
                accion = random.choice(acciones[estado])
            else:
                accion = max(acciones[estado], key=lambda a: Q_local[(estado, a)])

            recompensa = recompensas.get((estado, accion), 0)
            siguiente = accion

            if acciones[siguiente]:
                max_Q_sig = max(Q_local[(siguiente, a)] for a in acciones[siguiente])
            else:
                max_Q_sig = 0

            Q_local[(estado, accion)] += alpha * (recompensa + gamma * max_Q_sig - Q_local[(estado, accion)])
            estado = siguiente

    return Q_local

# Entrenamos dos políticas: una exploradora y una explotadora
Q_explora = entrenar_Q(epsilon_explora)
Q_explota = entrenar_Q(epsilon_explota)

# Mostrar comparación
print("[Exploración] Política:")
for estado in estados:
    if acciones[estado]:
        mejor_accion = max(acciones[estado], key=lambda a: Q_explora[(estado, a)])
        print(f"{estado} → {mejor_accion}")

print("\n[Explotación] Política:")
for estado in estados:
    if acciones[estado]:
        mejor_accion = max(acciones[estado], key=lambda a: Q_explota[(estado, a)])
        print(f"{estado} → {mejor_accion}")
