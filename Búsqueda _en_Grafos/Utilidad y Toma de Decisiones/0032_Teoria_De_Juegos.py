# Teoría de Juegos usando nuestro grafo de ciudades:
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Guadalajara
#
# Dos jugadores deciden rutas para llegar a Guadalajara.
# Las rutas compiten: si ambos toman la misma, hay congestión y menor utilidad.

# Rutas posibles hacia Guadalajara
rutas = {
    'Ruta A': ['México', 'Querétaro', 'San Luis', 'Guadalajara'],
    'Ruta B': ['México', 'Puebla', 'Veracruz', 'Guadalajara']
}

# Pagos por cada combinación: (jugador 1, jugador 2)
# Si ambos eligen la misma ruta → congestión → menor utilidad
# Si eligen rutas distintas → recompensa total

pagos = {
    ('Ruta A', 'Ruta A'): (2, 2),
    ('Ruta B', 'Ruta B'): (2, 2),
    ('Ruta A', 'Ruta B'): (5, 5),
    ('Ruta B', 'Ruta A'): (5, 5)
}

jugadores = ['Jugador 1', 'Jugador 2']
estrategias = ['Ruta A', 'Ruta B']

# Mostrar pagos posibles
print("Matriz de pagos según elección de rutas:\n")
for a in estrategias:
    for b in estrategias:
        print(f"{jugadores[0]}={a} vs {jugadores[1]}={b} → Pago: {pagos[(a, b)]}")

print("\n Buscando equilibrios de Nash:\n")

# Evaluar posibles equilibrios de Nash
for e1 in estrategias:
    for e2 in estrategias:
        pago1, pago2 = pagos[(e1, e2)]

        # Alternativas
        otra_e1 = [alt for alt in estrategias if alt != e1][0]
        otra_e2 = [alt for alt in estrategias if alt != e2][0]

        # ¿Mejoraría alguno cambiando su decisión?
        mejor_e1 = pagos[(otra_e1, e2)][0]
        mejor_e2 = pagos[(e1, otra_e2)][1]

        if pago1 >= mejor_e1 and pago2 >= mejor_e2:
            print(f"Equilibrio de Nash: Jugador 1 = {e1}, Jugador 2 = {e2} → Pagos: {pago1, pago2}")

