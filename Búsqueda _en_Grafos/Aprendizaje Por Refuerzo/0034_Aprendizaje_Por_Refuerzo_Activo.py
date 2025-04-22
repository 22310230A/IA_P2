# Aprendizaje por Refuerzo Activo
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
# A diferencia del aprendizaje pasivo, aquí el agente explora y aprende por sí mismo
# cuál es la mejor acción a tomar en cada estado para maximizar la recompensa total.

import random

# Estados del grafo (ciudades)
estados = ['México', 'Querétaro', 'Puebla', 'San Luis', 'Veracruz', 'Guadalajara']

# Acciones posibles desde cada ciudad
acciones = {
    'México': ['Querétaro', 'Puebla'],
    'Querétaro': ['San Luis'],
    'Puebla': ['Veracruz'],
    'San Luis': ['Guadalajara'],
    'Veracruz': ['Guadalajara'],
    'Guadalajara': []
}

# Recompensas inmediatas por moverse entre ciudades
recompensas = {
    ('México', 'Querétaro'): -2,
    ('México', 'Puebla'): -3,
    ('Querétaro', 'San Luis'): -4,
    ('Puebla', 'Veracruz'): -5,
    ('San Luis', 'Guadalajara'): 10,
    ('Veracruz', 'Guadalajara'): 10
}

# Inicialización de valores Q y conteo de visitas
Q = { (s, a): 0 for s in estados for a in acciones[s] }
visitas = { (s, a): 0 for s in estados for a in acciones[s] }
gamma = 0.9  # Factor de descuento
episodios = 20

# Algoritmo tipo exploración activa (tipo ε-greedy)
for _ in range(episodios):
    estado = 'México'
    trayectoria = []

    while estado != 'Guadalajara':
        # Elegimos una acción al azar para explorar (ε-greedy, con ε = 1.0)
        accion = random.choice(acciones[estado])
        recompensa = recompensas.get((estado, accion), 0)
        trayectoria.append((estado, accion, recompensa))
        estado = accion  # avanzar a la siguiente ciudad

    # Actualizar Q hacia atrás desde la última acción
    G = 0  # retorno acumulado
    for estado, accion, recompensa in reversed(trayectoria):
        G = recompensa + gamma * G
        visitas[(estado, accion)] += 1
        alpha = 1 / visitas[(estado, accion)]  # tasa de aprendizaje decreciente
        Q[(estado, accion)] += alpha * (G - Q[(estado, accion)])

# Derivar política óptima basada en Q
print("[Aprendizaje por Refuerzo Activo] Política aprendida:")
for estado in estados:
    if acciones[estado]:
        mejor_accion = max(acciones[estado], key=lambda a: Q[(estado, a)])
        print(f"{estado} → {mejor_accion}")
