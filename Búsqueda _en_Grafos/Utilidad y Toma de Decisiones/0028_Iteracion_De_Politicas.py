# Iteración de Políticas
# Grafo usado (como MDP):
#
#            CDMX
#        /        \
#    León        Morelia
#     |             |
#  Aguascalientes   Tepatitlán
#         \       /
#         Guadalajara
#
# La política indica qué acción tomar en cada ciudad para maximizar la utilidad esperada.

estados = ['CDMX', 'León', 'Morelia', 'Aguascalientes', 'Tepatitlán', 'Guadalajara']

transiciones = {
    'CDMX': [('León', -2), ('Morelia', -3)],
    'León': [('Aguascalientes', -4)],
    'Morelia': [('Tepatitlán', -4)],
    'Aguascalientes': [('Guadalajara', 10)],
    'Tepatitlán': [('Guadalajara', 10)],
    'Guadalajara': []
}

# Inicialización de política arbitraria
politica = {estado: (transiciones[estado][0][0] if transiciones[estado] else None) for estado in estados}
valores = {estado: 0 for estado in estados}

# Parámetros
gamma = 0.9
umbral = 0.01

def iteracion_de_politicas():
    global politica, valores
    estable = False

    while not estable:
        # Evaluación de la política
        while True:
            delta = 0
            nuevo_valores = valores.copy()
            for estado in estados:
                accion = politica[estado]
                if accion is None:
                    continue
                recompensa = next(r for s, r in transiciones[estado] if s == accion)
                nuevo_valores[estado] = recompensa + gamma * valores[accion]
                delta = max(delta, abs(nuevo_valores[estado] - valores[estado]))
            valores = nuevo_valores
            if delta < umbral:
                break

        # Mejora de política
        estable = True
        for estado in estados:
            if not transiciones[estado]:
                continue
            mejor_accion = max(
                transiciones[estado],
                key=lambda t: t[1] + gamma * valores[t[0]]
            )[0]
            if politica[estado] != mejor_accion:
                politica[estado] = mejor_accion
                estable = False

# Ejecutar algoritmo
iteracion_de_politicas()

# Mostrar política óptima y valores finales
print("[Iteración de Políticas] Política óptima:")
for estado in estados:
    print(f"{estado} → {politica[estado]}")

print("\nValores estimados:")
for estado in estados:
    print(f"{estado}: {valores[estado]:.2f}")
