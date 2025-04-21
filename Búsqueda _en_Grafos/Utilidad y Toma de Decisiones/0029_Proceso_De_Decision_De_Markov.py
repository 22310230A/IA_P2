# Proceso de Decisión de Markov (MDP)
#  Modelo de un MDP:
#
#         CDMX
#        /    \
#    León     Morelia
#     |         |
#  Aguascalientes   Tepatitlán
#         \       /
#         Guadalajara
#
# Objetivo: modelar los estados, acciones, transiciones y recompensas de forma completa

import random

estados = ['CDMX', 'León', 'Morelia', 'Aguascalientes', 'Tepatitlán', 'Guadalajara']
acciones = ['ir_a']

# Transiciones probabilísticas: estado → [(acción, destino, probabilidad, recompensa)]
transiciones = {
    'CDMX': [('ir_a', 'León', 0.8, -2), ('ir_a', 'Morelia', 0.9, -3)],
    'León': [('ir_a', 'Aguascalientes', 1.0, -4)],
    'Morelia': [('ir_a', 'Tepatitlán', 1.0, -4)],
    'Aguascalientes': [('ir_a', 'Guadalajara', 1.0, 10)],
    'Tepatitlán': [('ir_a', 'Guadalajara', 1.0, 10)],
    'Guadalajara': []
}

# Inicialización de valores
valores = {estado: 0 for estado in estados}
politica = {estado: None for estado in estados}

# Parámetros
gamma = 0.9
umbral = 0.01

def mdp():
    global valores, politica
    cambio = float('inf')

    while cambio > umbral:
        nuevo_valores = valores.copy()
        cambio = 0

        for estado in estados:
            if not transiciones[estado]:
                continue

            mejor_valor = float('-inf')
            mejor_accion = None

            for accion, destino, prob, recompensa in transiciones[estado]:
                utilidad = prob * (recompensa + gamma * valores[destino])
                if utilidad > mejor_valor:
                    mejor_valor = utilidad
                    mejor_accion = destino

            nuevo_valores[estado] = mejor_valor
            politica[estado] = mejor_accion
            cambio = max(cambio, abs(valores[estado] - mejor_valor))

        valores = nuevo_valores

# Ejecutar
mdp()

# Mostrar resultados
print("[MDP] Política óptima y valores estimados:")
for estado in estados:
    print(f"{estado}: → {politica[estado]}, Valor: {valores[estado]:.2f}")
