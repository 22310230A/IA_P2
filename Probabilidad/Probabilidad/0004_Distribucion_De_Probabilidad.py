# Distribución de Probabilidad
#
# Una distribución de probabilidad asigna una probabilidad a cada posible estado
# en un conjunto de valores. Aquí, usamos las ciudades del grafo como estados.

# Grafo visual (referencia):
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Guadalajara

# Supongamos que tenemos una distribución sobre la ubicación del agente
P_estado = {
    'México': 0.15,
    'Querétaro': 0.25,
    'Puebla': 0.1,
    'San Luis': 0.2,
    'Veracruz': 0.1,
    'Guadalajara': 0.2
}

# Verificación: debe sumar 1
suma = sum(P_estado.values())

print("[Distribución de Probabilidad]")
print("Probabilidad de estar en cada ciudad:\n")
for ciudad, prob in P_estado.items():
    print(f"{ciudad}: {prob:.2f}")

print(f"\n¿Suma de la distribución?: {suma:.2f}")
if abs(suma - 1.0) < 0.01:
    print("Distribución válida.")
else:
    print("Error: la suma no es igual a 1.")

# Aplicaciones:
# - Definir creencias en redes bayesianas
# - Modelar estados ocultos
# - Filtrado y predicción en percepción
