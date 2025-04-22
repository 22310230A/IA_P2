# Probabilidad Condicionada y Normalización
#
# Un agente cree estar en alguna ciudad (a priori),
# pero ahora recibe una observación parcial ("zona industrial").
# Se actualiza la creencia usando probabilidad condicionada y se normaliza.

# Grafo de ciudades (contexto visual):
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Guadalajara

# Distribución a priori (antes de observar)
P_a_priori = {
    'México': 0.3,
    'Querétaro': 0.1,
    'Puebla': 0.2,
    'San Luis': 0.1,
    'Veracruz': 0.2,
    'Guadalajara': 0.1
}

# Probabilidades de observación P(evidencia | ciudad)
# Suponemos que el agente percibe una "zona industrial"
P_evidencia_dado_ciudad = {
    'México': 0.2,
    'Querétaro': 0.9,
    'Puebla': 0.1,
    'San Luis': 0.8,
    'Veracruz': 0.2,
    'Guadalajara': 0.1
}

# Paso 1: Calcular la probabilidad conjunta: P(ciudad ∩ evidencia)
prob_conjunta = {}
for ciudad in P_a_priori:
    prob_conjunta[ciudad] = P_evidencia_dado_ciudad[ciudad] * P_a_priori[ciudad]

# Paso 2: Normalización (para obtener una distribución válida)
Z = sum(prob_conjunta.values())  # constante de normalización

P_posterior = {ciudad: prob_conjunta[ciudad] / Z for ciudad in prob_conjunta}

# Mostrar resultados
print("[Probabilidad Condicionada y Normalización]")
print("Distribución posterior (P(ciudad | evidencia = 'zona industrial')):\n")
for ciudad, prob in P_posterior.items():
    print(f"{ciudad}: {prob:.4f}")

print(f"\nVerificación (suma): {sum(P_posterior.values()):.4f}")
