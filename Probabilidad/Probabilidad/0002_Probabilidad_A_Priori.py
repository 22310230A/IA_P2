# Probabilidad a Priori
#
# La probabilidad a priori representa el conocimiento inicial que tiene un agente
# sobre un evento o estado antes de observar alguna evidencia.
#
# En este caso, se representa como la distribución de creencias iniciales
# sobre la posible ubicación del agente en el grafo de ciudades.

# Grafo usado (ciudades):
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Guadalajara

# Distribución a priori sobre dónde puede estar el agente
P_a_priori = {
    'México': 0.3,
    'Querétaro': 0.1,
    'Puebla': 0.2,
    'San Luis': 0.1,
    'Veracruz': 0.2,
    'Guadalajara': 0.1
}

# Comprobamos que es una distribución válida (suma = 1)
suma = sum(P_a_priori.values())
print("[Probabilidad a Priori] Distribución de creencia inicial:")
for ciudad, prob in P_a_priori.items():
    print(f"{ciudad}: {prob:.2f}")

print(f"\n¿Distribución válida? Suma = {suma:.2f}")
if abs(suma - 1.0) < 0.01:
    print("Sí, es una distribución de probabilidad válida.")
else:
    print("No, hay un error en las probabilidades.")
