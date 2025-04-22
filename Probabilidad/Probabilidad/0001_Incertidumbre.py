# Incertidumbre en Inteligencia Artificial
#
# En el mundo real, los agentes no siempre tienen información completa.
# La incertidumbre representa el desconocimiento o la falta de certeza
# sobre el estado del entorno, los datos o los resultados.

# Este ejemplo muestra cómo una decisión puede verse afectada
# por la falta de certeza del agente sobre su posición real.

# Grafo de ciudades (como en los otros temas):
#
#         México
#        /     \
#  Querétaro   Puebla
#      |         |
#  San Luis   Veracruz
#      \         /
#      Guadalajara

# Supongamos que el agente está en una ciudad, pero no sabe exactamente en cuál.
# Tiene una creencia (distribución) sobre su posible ubicación.

creencia = {
    'México': 0.3,
    'Querétaro': 0.1,
    'Puebla': 0.2,
    'San Luis': 0.1,
    'Veracruz': 0.2,
    'Guadalajara': 0.1
}

# El agente quiere moverse hacia Guadalajara, pero su incertidumbre lo obliga
# a tomar decisiones basadas en probabilidades.

# Si decide moverse desde "donde cree estar", ¿qué ciudad debería priorizar?

# Podemos simular una decisión basada en su creencia actual:
import random

# Seleccionamos una ciudad al azar según las probabilidades (simulación)
def muestreo_de_creencia(creencia):
    ciudades = list(creencia.keys())
    probabilidades = list(creencia.values())
    return random.choices(ciudades, weights=probabilidades, k=1)[0]

ciudad_asumida = muestreo_de_creencia(creencia)

print(f"[Incertidumbre] El agente asume que está en: {ciudad_asumida}")
print(f"→ Pero realmente no lo sabe con certeza.")

# En este escenario, el agente necesita métodos probabilísticos para:
# - Inferir su ubicación real
# - Tomar decisiones óptimas bajo incertidumbre
